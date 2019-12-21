import json, sys
import numpy as np
import zmq
from bottle import (post, run, request, 
  response, route)

htttp_port = 8889

@route('/check_alive_bottle')
def check_alive():
  return "Bottle is alive!!!!!!"

@route('/check_zmq/<message>', method='GET')
def check_zmq(message):
  port = '5556'
  context = zmq.Context()
  socket = context.socket(zmq.REQ)
  socket.connect('tcp://localhost:{0}'.format(port))

  print('Bottle: sending message: ' + message)
  socket.send_string(message)

  recv_message = socket.recv_string()
  print('Bottle: received message = {}'.format(recv_message))

  return 'OK'

def get_socket():
  port = '5556'
  context = zmq.Context()
  socket = context.socket(zmq.REQ)
  socket.connect('tcp://localhost:{0}'.format(port))

  return socket

@route('/post', method='POST')
def post():
  socket = get_socket()
  print(socket)

  content_type = request.get_header('Content-Type')
  if not content_type=='application/json':
    raise Exception('invalid Content-Type: {}'.format(content_type))

  data = request.json

  socket.send_string(message)

  recv_message = socket.recv_string()
  print('Bottle: received message = {}'.format(recv_message))

  return 'OK'


if __name__=='__main__':
  run(host='localhost', port=htttp_port, debug=True)
