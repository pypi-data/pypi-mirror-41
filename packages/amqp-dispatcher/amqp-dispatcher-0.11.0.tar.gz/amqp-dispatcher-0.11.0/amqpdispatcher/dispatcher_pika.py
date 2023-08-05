#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
import pika
import socket
import sys

from six.moves.urllib.parse import urlparse, urlunparse

from amqpdispatcher.dispatcher_common import setup
from pika import BlockingConnection as RabbitConnection


def connection_params(user, password, host, port, vhost, heartbeat):
    netloc = None
    if user and password:
        netloc = '{0}:{1}'.format(user, password)
    elif user:
        netloc = user

    if netloc is None:
        netloc = host
    else:
        netloc = '{0}@{1}'.format(netloc, host)
    if port:
        netloc = '{0}:{1}'.format(netloc, port)

    query = 'heartbeat={0}'.format(heartbeat)

    url = urlunparse(('amqp', netloc, vhost, '', query, ''))
    params = pika.URLParameters(url)
    params.socket_timeout = 5
    return params


def connect_to_hosts(connector, hosts, port, user, password, vhost, heartbeat, **kwargs):
    logger = logging.getLogger('amqp-dispatcher')

    for host in hosts:
        logger.info('Trying to connect to host: {0}'.format(host))
        try:
            return connector(connection_params(
                user,
                password,
                host,
                port,
                vhost,
                heartbeat))
        except socket.error:
            logger.info('Error connecting to {0}'.format(host))
    logger.error('Could not connect to any hosts')


def main():
    greenlet = setup('pika',
                     RabbitConnection,
                     connect_to_hosts)
    if greenlet is not None:
        greenlet.start()
        greenlet.join()
        sys.exit(greenlet.get())


if __name__ == '__main__':
    main()
