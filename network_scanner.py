import argparse
from scapy.all import ARP, Ether, srp

def scan_network(target_ip, timeout):
    # Create an ARP request packet
    arp = ARP(pdst=target_ip)
    # Create an Ethernet frame around the ARP request packet
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    # Combine the Ethernet frame and the ARP request packet
    packet = ether/arp

    # Use Scapy's srp() function to send the packet and receive a response
    result = srp(packet, timeout=timeout, verbose=False)[0]

    # Extract the IP and MAC addresses from the response
    clients = []
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})

    return clients

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scan a network for connected devices.')
    parser.add_argument('target_ip', help='The IP address of the network to scan (e.g. 192.168.0.0/24).')
    parser.add_argument('-t', '--timeout', type=float, default=2, help='The timeout (in seconds) for the ARP requests (default: 2 seconds).')
    args = parser.parse_args()

    print(f'Scanning network {args.target_ip}...')
    clients = scan_network(args.target_ip, args.timeout)
    print('Connected devices:')
    for client in clients:
        print(f'IP: {client["ip"]}\tMAC: {client["mac"]}')
