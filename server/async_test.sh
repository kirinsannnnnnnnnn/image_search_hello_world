nohup curl localhost:8888/check_zmq/111 > log1.out &
sleep 1
nohup curl localhost:8889/check_zmq/2222 > log2.out &
