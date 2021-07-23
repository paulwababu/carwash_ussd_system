#!/usr/bin/python3
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FlaskApp/")

from FlaskApp import app as application
application.secret_key = 'jango-insecure-bxzsxr-_@9n_mk+ul_4$p5(1+$o8^1kocbx(#4rw%m%0i)7lwv'
