import sys
import socket
import threading
import time


usage=("python3 paractise.py IP START_PORT END_PORT")
print("-"*70)
print("simple port scanner")
print("-"*70)

if len(sys.argv)!=4:
    print(usage)
    sys.exit()
start_time= time.time()
try:
    target=socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Ip resolution failed")
    sys.exit()

start_port=int(sys.argv[2])
end_port=int(sys.argv[3])

def port_scan(port):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn= s.connect_ex((target,port,))
    s.settimeout(1)
    if (not conn):
        print("port number {} is open".format(port))
    s.close()

for port in range(start_port, end_port +1):
    thread=threading.Thread(target=port_scan,args=(port,))
    thread.start()
end_time=time.time()
total_time=end_time-start_time

print("total time",total_time)
