# SecurePy

SecurePy: Python Scripts for Network Security and Vulnerability Management
SecurePy is a collection of Python scripts designed to help security engineers and IT professionals automate network security and vulnerability management tasks. These scripts are intended to be used as part of a larger security program, and can be customized to fit the needs of your organization.

Network Scanner
network_scanner.py is a Python script that uses the nmap library to perform a port scan on a specified target IP address. It scans for open ports, services running on those ports, and the operating system running on the target.

To use the script, simply run:
python network_scanner.py
You will be prompted to enter the target IP address.

Password Strength Checker
password_strength_checker.py is a Python script that checks the strength of a password based on its length, complexity, and uniqueness. It checks if the password meets the minimum length requirement and contains at least one lowercase character, uppercase character, number, and special character.

To use the script, simply run:
python password_strength_checker.py
You will be prompted to enter the password you want to check.

Log File Analysis
log_file_analysis.py is a Python script that reads a log file (in the Apache access log format) and extracts relevant information such as the IP address, date, HTTP request, status code, size, referrer, and user agent. You can add custom logic to analyze the log data and identify any suspicious or malicious activity.
To use the script, simply run:
python log_file_analysis.py
The script will read the log file access.log in the same directory.

Vulnerability Scanner
vulnerability_scanner.py is a Python script that performs a vulnerability scan on a specified target IP address using the OpenVAS vulnerability scanner. It runs the openvas-nasl command to execute the plugins in the /usr/share/openvas/plugins/ directory and reports any vulnerabilities found.

To use the script, simply run:
python vulnerability_scanner.py
You will be prompted to enter the target IP address.

File Integrity Checker
file_integrity_checker.py is a Python script that calculates the hash value of a file and checks it against the last calculated hash value. This can be used to detect changes to a file and ensure its integrity.

To use the script, simply run:
python file_integrity_checker.py <filename>
Replace <filename> with the name of the file you want to check.

License
SecurePy is released under the MIT License. Feel free to use, modify, and distribute the scripts as you see fit. If you find any bugs or have suggestions for improvements, please create an issue on the GitHub repository.
