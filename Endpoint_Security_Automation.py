import win32com.client

def enable_real_time_protection():
    # Create instance of Windows Defender Antivirus API
    defender = win32com.client.Dispatch("Microsoft.WindowsDefender")

    # Check if real-time protection is currently enabled
    if defender.RealTimeProtectionEnabled:
        print("Real-time protection is already enabled.")
        return

    # Enable real-time protection
    defender.RealTimeProtectionEnabled = True
    print("Real-time protection has been enabled.")

def scan_file(file_path):
    # Create instance of Windows Defender Antivirus API
    defender = win32com.client.Dispatch("Microsoft.WindowsDefender")

    # Scan file for threats
    result = defender.ScanFile(file_path)

    # Check if threats were found
    if result["IsMalware"]:
        print("Threats were found in the file: ")
        for threat in result["Threats"]:
            print(threat["Name"])
    else:
        print("No threats were found in the file.")

def update_definitions():
    # Create instance of Windows Defender Antivirus API
    defender = win32com.client.Dispatch("Microsoft.WindowsDefender")

    # Update virus and spyware definitions
    defender.UpdateNow()
    print("Virus and spyware definitions have been updated.")

# Example usage
enable_real_time_protection()
scan_file("C:\\Users\\User\\Downloads\\test_file.exe")
update_definitions()
