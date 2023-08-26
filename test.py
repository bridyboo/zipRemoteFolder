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

# Define a PowerShell command to execute remotely
ps_script = 'Write-Host "Hello, from Python via WinRM"'

# Execute the PowerShell command
result = session.run_ps(ps_script)

# Print the command's standard output
print(result.std_out.decode())