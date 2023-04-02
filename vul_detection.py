import socket
import argparse


# Define command line arguments
parser = argparse.ArgumentParser(description='Vulnerability Scanner')
parser.add_argument('--host',metavar='host',type=str, required=True, help='Target host IP address')
parser.add_argument('--port', metavar='port', type=str, required=True, help='Target host port')

args = parser.parse_args()

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set a timeoutp
sock.settimeout(5)

# Connect to the target
result = sock.connect_ex((args.host, int(args.port)))

# Check if the port is open
if result == 0:
    print(f"Port {args.port} is open")
else:
    print(f"Port {args.port} is closed")
    
# Check for known vulnerabilities on the target
vulnerabilities = {
    '21': 'FTP vulnerability',
    '22': 'SSH vulnerability',
    '80': 'HTTP vulnerability',
    '443': 'HTTPS vulnerability'
}

if str(args.port) in vulnerabilities:
    print(f"{vulnerabilities[str(args.port)]} detected on port {args.port}")
