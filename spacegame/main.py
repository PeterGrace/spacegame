"""The primary module for this skeleton application."""
import click
import logging
import sys
from spacegame.Server import Server


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
    # TODO: bring up Universe

    print "Enter any input to quit."
    server = Server.MUDServer(port=5281)
    server.run()


if __name__ == '__main__':
    main()
