#!/usr/bin/env python

try:
    # Python 2.x
    from SocketServer import ThreadingMixIn
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from BaseHTTPServer import HTTPServer
    import thread
    import threading
    import SocketServer, time
    import multiprocessing
#    import dataQueueServer
except ImportError:
    # Python 3.x
    import thread
    import threading
    from socketserver import ThreadingMixIn
    from http.server import SimpleHTTPRequestHandler, HTTPServer
    import SocketServer, time
    import multiprocessing 
#    import dataQueueServer

class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024)
        cur_thread = threading.current_thread()
        response = "{}: {}".format(cur_thread.name, data)
#        videoPool.add(data)
        print "Output! %s" % data
        self.request.sendall(response)

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass



import sys
import os

if sys.argv[1:]:
    address = sys.argv[1]
    if (':' in address):
        interface = address.split(':')[0]
        port = int(address.split(':')[1])
    else:
        interface = '0.0.0.0'
        port = int(address)
else:
    port = 8000
    interface = '0.0.0.0'

if sys.argv[2:]:
    os.chdir(sys.argv[2])

print('Started HTTP server on ' +  interface + ':' + str(port))

def start_server(interface, port, ThreadedTCPRequestHandler):



#    videoPool = QueueServer()
    print (interface)
    print (port)
#    server = ThreadingSimpleServer((interface, port), SimpleHTTPRequestHandler)
    server = ThreadedTCPServer((interface, port), ThreadedTCPRequestHandler)
    server.serve_forever()

thread.start_new_thread(start_server (interface, port, ThreadedTCPRequestHandler),())

#try:
#    while 1:
#        sys.stdout.flush()
#        server.handle_request()
#except KeyboardInterrupt:
#    print('Finished.')

print('The server is running but my script is still executing!')
