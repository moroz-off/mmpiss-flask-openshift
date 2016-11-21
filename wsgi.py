#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask_openshift_template import app as application


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    from logging.handlers import RotatingFileHandler
    import logging
    handler = RotatingFileHandler('sys.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.ERROR)
    application.logger.addHandler(handler)
    host = os.getenv('MMPISS_HOST') if os.getenv('MMPISS_HOST') else 'localhost'
    port = int(os.getenv('MMPISS_PORT')) if os.getenv('MMPISS_PORT') else 8051
    httpd = make_server(host, port, application)
    print("Started server", host, port, sep=":")
    httpd.serve_forever()
