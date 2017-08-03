#!/usr/bin/env python
 
from http.server import BaseHTTPRequestHandler, HTTPServer
 
# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
 
  # GET
  def do_GET(self):
        print('path: ',self.path)
        if self.path == '/':
          self.getIndex()
        elif self.path == '/picture/fountain.jpg':
          self.getImage()
        elif self.path == '/css/mystyle.css':
          self.getCss()
        return


  def getIndex(self):
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
 
        # Send message back to client
        message = open('./../res/html/index.html','r')

        # Write content as  utf-8 data
        self.wfile.write(bytes(message.read(), "utf-16"))
        return

  def getCss(self):
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','text/css')
        self.end_headers()
 
        # Send message back to client
        message = open('./../res/css/mystyle.css','r')

        # Write content as  utf-8 data
        self.wfile.write(bytes(message.read(), "utf-16"))
        return
 
  def getImage(self):
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','image/jpeg')
        self.end_headers()
 
        # Send message back to client
        message = open('./../res/picture/fountain.jpg','rb')

        # Write content as  utf-8 data
        self.wfile.write(bytearray(message.read()))
        return

def run():
  print('starting server...')
 
  # Server settings
  # Choose port 8080, for port 80, which is nor mally used for a http server, you need root access
  server_address = ('127.0.0.1', 8081)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()
 
 
run()