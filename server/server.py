#!/usr/bin/env python
 
from http.server import BaseHTTPRequestHandler, HTTPServer
 
# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):


  def getFileFromPath(a):
    if a == '/picture/Cat.jpg':
     # b = print.a.find(".jpg")
      a = a[8:-4]
      print(a)
    # self.getImage('./../res'+ a )
    # if self.path == '*'.jpg:

    print ("TEEEEEEEEEEEEEEEEEEEEEEEEEEEST")
    print (self.getImage('./../res/'+a))

    return a
  
  # GET
  def do_GET(self):
        print('path: ',self.path)
        if self.path == '/':
          self.getIndex()
          getFileFromPath(a) 
          #Bilder müssen über die Funktion aufgerufen werden
        elif self.path == '/css/mystyle.css':
          self.getCss()  
        # self.path == .jpg
        #     '/picture/Cat.jpg' --> './../res/picture/Cat.jpg'
        #     '/picture/dogs.jpeg' --> './../res/picture/dogs.jpeg'
        # ...
        #     '/picture/***.jpg' --> './../res/picture/***.jpg'
        """
        elif self.path == '/picture/Cat.jpg':
          self.getImage('./../res/picture/Cat.jpg')
        elif self.path == '/picture/dogs.jpeg':
          self.getImage('./../res/picture/dogs.jpeg')
        elif self.path == '/picture/fountain.jpg':
          self.getImage('./../res/picture/fountain.jpg')
        elif self.path == '/picture/tiger.jpg':
          self.getImage('./../res/picture/tiger.jpg')
          """
        
        
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
 
  def getImage(self, mypath):
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','image/jpeg')
        self.end_headers()
        print('mypath: ' + mypath)
 
        message = open(mypath, 'rb')
        # Send message back to client
        """
        if self.path == '/picture/fountain.jpg':
          message = open('./../res/picture/fountain.jpg','rb')
        elif self.path == '/picture/Cat.jpg':
          message = open('./../res/picture/Cat.jpg','rb')
        elif self.path == '/picture/dogs.jpeg':
          message = open('./../res/picture/dogs.jpeg','rb')
        elif self.path == '/picture/tiger.jpg':
          message = open('./../res/picture/tiger.jpg','rb')
        """
        
     #   message = open('./../res/picture/fountain.jpg','rb')
        # Write content as  utf-8 data
        self.wfile.write(bytearray(message.read()))
        return

def run2():
  print('starting server...')
 
  # Server settings
  # Choose port 8080, for port 80, which is nor mally used for a http server, you need root access
  server_address = ('127.0.0.1', 8081)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()
 
 
run2()