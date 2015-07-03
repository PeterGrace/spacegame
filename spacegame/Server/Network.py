'''Telnet-related server stuffs for connectivity.'''

import select
import socket
import threading
import logging


class Server(threading.Thread):
    def __init__(self, logger=None, *args, **kwargs):
        self._host = kwargs.get('host', '0.0.0.0')
        self._port = kwargs.get('port', 5280)
        self._backlog = kwargs.get('backlog', 5)

        self._threads = []
        self._size = 1024
        self._server = None
        self._threads = []

        self.running = False
        self.logger = logging.getLogger('main.%s' % (self.__class__.__name__,))

    def bind_socket(self):
        try:
            self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._server.bind((self._host, self._port))
            self._server.listen(self._backlog)
        except socket.error, (value, message):
            if self._server:
                self._server.close()
            self.logger.critical("Could not open server socket: %s", message)
            raise

    def run(self):
        self.bind_socket()
        self.running = True
        while self.running:
            inputready, outputready, exceptready = select.select([self._server],
                                                                 [], [])
            for s in inputready:
                if s == self._server:
                    # accept connection and spawn off player thread
                    clientid = len(self._threads) + 1

                    c = Client(self._server.accept(), clientid)
                    self.logger.info('Client %d connected: %s:%s', clientid,
                                     c.address[0], c.address[1])
                    c.start()
                    self._threads.append(c)

            # thread cleanup
            for c in self._threads:
                if not c.isAlive():
                    # TODO: future results (if any) needed from client cleanup
                    c.cleanup = True

            self._threads = [t for t in self._threads if not t.cleanup]

        # close all threads
        self._server.close()
        for c in self._threads:
            c.join()


class Client(threading.Thread):
    def __init__(self, (client, address), clientid):
        threading.Thread.__init__(self)
        self.client = client
        self.address = address
        self.size = 1024
        self.playerid = None
        self.clientid = clientid
        self.running = True
        self.cleanup = False

        self.logger = logging.getLogger('main.%s.%d' % (self.__class__.__name__,
                                                        self.clientid))

    def join(self, timeout=None):
        self.client.send("Connection is terminating.\n")
        self.running = False
        super(Client, self).join(timeout)

    def run(self):
        self.running = True
        while self.running:
            try:
                data = self.client.recv(self.size)
            except IOError:
                self.logger.info('Client %d disconnected.', self.clientid)
                self.running = False
                continue

            if data:
                self.client.send(data)
            else:
                self.client.close()
                running = False