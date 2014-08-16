#-*- coding: utf-8 -*-

import os, sys, cgi
from http.server import HTTPServer, CGIHTTPRequestHandler

folder = os.getcwd()

webdir = '%s' % folder
port = 8006

print('Server started...')
print('Check http://localhost:%s' % port)


os.chdir(webdir)
serveraddres = ('localhost', port)
serverobject = HTTPServer(serveraddres, CGIHTTPRequestHandler)
serverobject.serve_forever()
