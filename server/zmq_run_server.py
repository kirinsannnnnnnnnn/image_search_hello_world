import zmq, time

def start_server():
  context = zmq.Context()
  socket = context.socket(zmq.REP)
  socket.bind('tcp://*:5556')
  print('ZMQ: server startup')

  while True:
    message = socket.recv_string()
    print('ZMQ: received message = {}'.format(message))
    print('now waiting...')
    time.sleep(5)
    print('ZMQ: replying message = {}'.format(message*2))
    socket.send_string('reply: {}'.format(message*2))

  socket.close()
  context.destroy()

if __name__=='__main__':
  start_server()
