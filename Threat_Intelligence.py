import requests
import json
import re

# Set up API endpoint URL and authentication credentials
url = "https://api.threatintelligenceplatform.com/v1/indicator"
username = "your_username"
password = "your_password"

# Define function to retrieve threat intelligence for a given IP address
def get_ip_threat_intel(ip_address):
    # Make API request with provided credentials and IP address
    response = requests.get(url + "/" + ip_address, auth=(username, password))
    
    # Check if response is successful (HTTP status code 200)
    if response.status_code == 200:
        # Extract relevant threat intelligence information from response
        threat_intel = {}
        data = json.loads(response.content)
        if 'geo' in data:
            threat_intel['country'] = data['geo']['country_name']
            threat_intel['latitude'] = data['geo']['latitude']
            threat_intel['longitude'] = data['geo']['longitude']
        if 'threat' in data:
            threat_intel['severity'] = data['threat']['severity']
            threat_intel['classification'] = data['threat']['classification']
        if 'reputation' in data:
            threat_intel['reputation'] = data['reputation']['overall_score']
        
        # Return extracted threat intelligence information
        return threat_intel
    
    # If response is unsuccessful, return None
    else:
        return None

# Define function to parse log files and identify IP addresses
def parse_log_file(log_file_path):
    # Read log file contents into memory
    with open(log_file_path, 'r') as f:
        log_data = f.read()
    
    # Use regular expressions to identify IP addresses in log data
    ip_regex = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ip_addresses = re.findall(ip_regex, log_data)
    
    # Return identified IP addresses
    return ip_addresses

# Main program logic
if __name__ == "__main__":
    # Define path to log file
    log_file_path = "/var/log/auth.log"
    
    # Parse log file and extract identified IP addresses
    ip_addresses = parse_log_file(log_file_path)
    
    # Loop through identified IP addresses and retrieve threat intelligence information
    for ip_address in ip_addresses:
        threat_intel = get_ip_threat_intel(ip_address)
        
        # Print retrieved threat intelligence information
        if threat_intel is not None:
            print("IP address:", ip_address)
            for key, value in threat_intel.items():
                print(key + ":", value)
            print()
        else:
            print("Unable to retrieve threat intelligence for IP address:", ip_address)
