import winrm


class RemoteArchive:

    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = "datacenter\\" + username
        self.password = password

    # Define the server details
    # hostname = "YVWTNMUN19CI12.datacenter.asp"
    # username = "datacenter\\matthew.darmadi"  # Use double backslashes to escape
    # password = "Ohshitcent6"

    def archive(self, prefix):
        # Define the path to the .txt file you want to edit on the remote server
        remote_file_path = r'E:\temp\testFolder'  # this works
        file_prefix = prefix  # prefix for the spool type
        output_zip_file = remote_file_path

        # Initialize a WinRM session with administrative credentials
        session = winrm.Session(
            self.hostname,
            auth=(self.username, self.password),
            transport='ntlm'
        )

        # Define the PowerShell command to zip files with a prefix
        powershell_command = (
            f'Compress-Archive -Path "{remote_file_path}\\{file_prefix}*" -DestinationPath "{output_zip_file}" -Force'
        )

        # Define the PowerShell command to delete files with a prefix
        powershell_delete_command = (
            f'Remove-Item -Path "{remote_file_path}\\{file_prefix}*" -Force'
        )

        # Execute the PowerShell script remotely
        result = session.run_ps(powershell_command)
        session.run_ps(powershell_delete_command)

        # Check the execution result
        if result.status_code == 0:
            print(
                f'Successfully zipped files with prefix "{file_prefix}" to "{output_zip_file}.zip"')
        else:
            print(f'Error: {result.std_err.decode()}')
