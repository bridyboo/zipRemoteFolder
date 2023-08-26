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

# Define the file path you want to write to remotely
file_path = r'\\fsrv_01\H\mun0466test\test.txt'  # Replace with the actual file path

# Define the content you want to write to the file
content_to_write = 'hello'

# Define a PowerShell script to write the content to the file
ps_script = f'Set-Content -Path "{file_path}" -Value "{content_to_write}"'

# Execute the PowerShell script
result = session.run_ps(ps_script)

# Print the command's standard output
print(result.std_out.decode())