import sys
import socket
import time
import threading

usage="python3 practise.py ip start_port end_port"
print("-"*70)
print("python simple port scanner")
print("-"*70)

if len(sys.argv) != 4:
    print(usage)
    sys.exit()
start_time=time.time()
try:
   target= socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("name resolution error")
    sys.exit()

start_port=int(sys.argv[2])
end_port=int(sys.argv[3])
def port_scanner(port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    conn=s.connect_ex((target,port,))
    s.settimeout(1)
    if (not conn):
        print("port {} is open".format(port))
        s.close()

for port in range(start_port, end_port +1): # +1 to include last port.
    thread= threading.Thread(target=port_scanner,args=(port,))
    thread.start()    

end_time=time.time()
total_time=end_time-start_time
print("results in", total_time)
