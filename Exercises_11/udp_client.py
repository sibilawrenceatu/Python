#UDP Client program
"""
UDPClient by: JOR
Send UDP packets to a particular address and port.
Alpha: 13FEB22
"""
#Improting libraries socket, time, datetime and settings
import socket
import time
from datetime import datetime
import settings.udp as settings
UDP_IP = settings.UDP["SERVER_UDP_IPv4"]
UDP_PORT = settings.UDP["SERVER_PORT"]
print(f'This is the UDP client, it will try to connect to a server at {UDP_IP}:{UDP_PORT} in the settings file.')
print('This script has no error handling, by design')
while True:
 with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
  s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
  message_text = f"ATU {datetime.now()}"
  message = message_text.encode('utf-8')
  s.sendto(message, (UDP_IP, UDP_PORT))
  print(f'Sent {message_text}')
  time.sleep(1)
 