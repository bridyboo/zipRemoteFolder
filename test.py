import winrm

# Define the WinRM connection parameters
hostname = 'YVWTNMUN19CI12.datacenter.asp'  # Replace with the target hostname or IP address
username = 'datacenter\matthew.darmadi'   # Replace with your username
password = 'Ohshitcent6'   # Replace with your password

# Create a session
session = winrm.Session(
    hostname,
    auth=(username, password),
    transport='ntlm',  # Use 'ntlm' for NTLM authentication, or 'kerberos' for Kerberos authentication
    server_cert_validation='ignore'  # You can change this based on your certificate validation requirements
)

# Define the folder path you want to open remotely
folder_path = r'\\fsrv_01\H\mun0466test\spool_0466test - Copy'  # Replace with the actual folder path

# Define a PowerShell command to open the folder using Invoke-Item
ps_script = f'Invoke-Item -Path "{folder_path}"'

# Execute the PowerShell command
result = session.run_ps(ps_script)

# Print the command's standard output
print(result.std_out.decode())