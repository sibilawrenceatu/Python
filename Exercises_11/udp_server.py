#UDP server program
"""
UDPServer by: JOR
Listens for packets on a particular address and port.
Alpha: 13FEB22
"""
#Importing socket and settings libraries 
import socket
import settings.udp as settings
UDP_IP = settings.UDP["SERVER_UDP_IPv4"]
UDP_PORT = settings.UDP["SERVER_PORT"]
BUFFER_SIZE = 1024
print(f'This is the UDP server, it will open a port at {UDP_IP}:{UDP_PORT} and being listening')
print(f'Make sure the actual server IP address matches {UDP_IP} in the settings file')
print('This script has no error handling, by design')
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
 s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
 s.bind( (UDP_IP, UDP_PORT) )
 print('Listening on', UDP_IP)
 while True:
  data, addr = s.recvfrom(BUFFER_SIZE)
  data = data.decode()
  print(addr, data)