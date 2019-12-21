ps | grep python | awk '{print $1}' | xargs kill -9

nohup python -u zmq_run_server.py & 
nohup python -u bottle_server.py &
nohup python -u bottle_server2.py &