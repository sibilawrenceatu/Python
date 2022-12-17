#Main program for device classes 
#Importing Firewall,Switch and loadbalancer modules
from devices import Firewall,Switch,Loadbalance

# Create a firewall instance
firewall27 = Firewall("firewall27")
# Configure it
firewall27.configure_firewall()
# Create a firewall instance
firewall28 = Firewall("firewall28")
# Verify a CRC
firewall28.calculate_crc("dummy data for firewall")

# Create a switch instance
switch1 = Switch("switch1")
# Configure it
switch1.configure_switch()
# Create a switch instance
switch2 = Switch("switch2")
# Verify a CRC
switch2.calculate_crc("dummy data for switch")

# Create a load balancer instance
lb1 = Loadbalance("Loadbalancer1")
# Configure it
lb1.configure_load()
# Create a load balancer  instance
switch2 = Loadbalance("Loadbalancer2")
# Verify a CRC
switch2.calculate_crc("dummy data for loadbalancer")