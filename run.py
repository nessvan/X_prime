#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 12:33:15 2017

@author: ness
"""
import sys
# To include the application's path in the Python search path
sys.path.append("app_main")

"""(run.py) Start Flask built-in development web server"""
from geocoding_app import app  # from package app_main's __init__.py import app

if __name__ == '__main__':
   # for local loopback only, on dev machine
   app.run(host='127.0.0.1', port=5000, debug=True)

   # listening on all IPs, on server
   #app.run(host='0.0.0.0', port=8080, debug=True)