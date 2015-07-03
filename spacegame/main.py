"""The primary module for this skeleton application."""
import click
import logging
import sys
import time
from spacegame.Network import Server
from spacegame.Parser import Parser


@click.command()
def main():
    '''Skeleton App made by pymkcli'''

    # TODO: get configuration from command line

    # TODO: read log level from configuration
    logger = logging.getLogger('main')
    logger.setLevel(logging.DEBUG)
    log_hdlr = logging.StreamHandler(sys.stdout)
    log_hdlr.setFormatter(logging.Formatter('%(asctime)s %(levelname)-8s %(message)s'))
    logger.addHandler(log_hdlr)

    # TODO: database?

    logger.info('Bringing up command parser...')
    MainParser = Parser()

    # TODO: bring up Universe

    logger.info('Bringing up TCPServer...')
    TCPServer = Network.Server(port=5281)
    TCPServer.run()

    # main game loop
    running = True
    logger.info('And the universe sprang forth with life and legend!')
    while running:
        # not trying to kill the cpu during this part of the dev process
        time.sleep(0.25)

    logger.info('The universe is currently collapsing...')
    # TODO: shutdown nicely

if __name__ == '__main__':
    main()
