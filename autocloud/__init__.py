# -*- coding: utf-8 -*-

import ConfigParser
import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__name__))

config = ConfigParser.RawConfigParser()
name = "{PROJECT_ROOT}/config/autocloud.cfg".format(
        PROJECT_ROOT=PROJECT_ROOT)

if not os.path.exists(name):
    name = '/etc/autocloud/autocloud.cfg'

config.read(name)

KOJI_SERVER_URL = config.get('autocloud', 'koji_server_url')
BASE_KOJI_TASK_URL = config.get('autocloud', 'base_koji_task_url')


HOST = config.get('autocloud', 'host') or '127.0.0.1'
PORT = int(config.get('autocloud', 'port')) or 5000
DEBUG = config.getboolean('autocloud', 'debug')

SQLALCHEMY_URI = config.get('sqlalchemy', 'uri')

VIRTUALBOX = config.get('autocloud', 'virtualbox')
