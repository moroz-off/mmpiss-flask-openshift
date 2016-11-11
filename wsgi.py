#!/usr/bin/env python
import os
from flask_openshift_template import app as application


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server(os.getenv('MMPISS_HOST') if os.getenv('MMPISS_HOST') else 'localhost', int(os.getenv('MMPISS_PORT')) if os.getenv('MMPISS_PORT') else 8051, application)
    httpd.serve_forever()
