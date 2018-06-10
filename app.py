# -*- coding: utf-8 -*-
"""
----------------------------------------------------
    File Name:      app
    Description:
    Author:         潘晓华
    date:           2018/6/10
----------------------------------------------------
"""

import os
import mod_wsgi.server

mod_wsgi.server.start(
  '--log-to-terminal',
  '--port', '8080',
  '--trust-proxy-header', 'X-Forwarded-For',
  '--trust-proxy-header', 'X-Forwarded-Port',
  '--trust-proxy-header', 'X-Forwarded-Proto',
  '--processes', os.environ.get('MOD_WSGI_PROCESSES', '1'),
  '--threads', os.environ.get('MOD_WSGI_THREADS', '5'),
  '--application-type', 'module',
  '--entry-point', 'run'
)