import os
import sys
import time
import logging
import subprocess

logging.basicConfig(filename='intrusion_detection.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# define variables
ip_addr = '192.168.1.1'
blocked_ip_list = []

def check_iptables():
    global blocked_ip_list
    # check the iptables for blocked IP addresses
    try:
        blocked_ip_list = subprocess.check_output(['iptables', '-L', '-n', '--line-numbers']).decode('utf-8').split('\n')
    except Exception as e:
        logging.error(f'Error while checking iptables: {e}')
        sys.exit(1)

def block_ip(ip):
    global blocked_ip_list
    # block the IP address using iptables
    try:
        subprocess.call(['iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP'])
        logging.info(f'{ip} has been blocked')
        # update the list of blocked IP addresses
        check_iptables()
    except Exception as e:
        logging.error(f'Error while blocking IP {ip}: {e}')

def unblock_ip(ip):
    global blocked_ip_list
    # unblock the IP address using iptables
    try:
        line_num = None
        # find the line number of the blocked IP address
        for line in blocked_ip_list:
            if ip in line:
                line_num = line.split()[0]
                break
        if line_num:
            subprocess.call(['iptables', '-D', 'INPUT', line_num])
            logging.info(f'{ip} has been unblocked')
            # update the list of blocked IP addresses
            check_iptables()
        else:
            logging.warning(f'{ip} is not blocked')
    except Exception as e:
        logging.error(f'Error while unblocking IP {ip}: {e}')

def read_logs():
    # read the log file and look for signs of intrusion
    try:
        with open('/var/log/auth.log') as f:
            log_lines = f.readlines()
        for line in log_lines:
            if 'Failed password' in line and ip_addr in line:
                # found a sign of intrusion
                logging.warning(f'Possible intrusion attempt from {ip_addr}')
                # block the IP address
                block_ip(ip_addr)
    except Exception as e:
        logging.error(f'Error while reading logs: {e}')

if __name__ == '__main__':
    while True:
        # check the iptables for blocked IP addresses
        check_iptables()
        # read the logs for signs of intrusion
        read_logs()
        # sleep for 10 seconds
        time.sleep(10)
