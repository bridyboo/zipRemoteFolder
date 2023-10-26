import winrm
import datetime
from tqdm import tqdm
import time
import os


# This static method is a helper function for the zip file's datetime
def date():
    curr_date = datetime.datetime.now()
    return curr_date.strftime("%Y-%m-%d_%H%M%S")  # yyyyMMdd_hms


# This class is to archive all files on a remote server with a specific prefix
class RemoteArchive:

    def __init__(self, hostname, username, password, path):
        self.hostname = hostname
        self.username = "datacenter\\" + username
        self.password = password
        self.path = path

    def archive(self, prefix):
        # Define the path to the .txt file you want to edit on the remote server
        remote_file_path = self.path  # this works
        file_prefix = prefix  # prefix for the spool type
        archive_path = os.path.join(os.path.dirname(self.path), 'archive')
        output_zip_file = remote_file_path + date()  # zip folder name will have datetime

        # Initialize a WinRM session with administrative credentials
        session = winrm.Session(
            self.hostname,
            auth=(self.username, self.password),
            transport='ntlm'
        )

        # Define the PowerShell command to zip files with a prefix
        powershell_command = f"""
        if (-not (Test-Path -Path "{archive_path}" -PathType Container)) {{
            New-Item -Path "{archive_path}" -ItemType Directory
        }}
        Compress-Archive -Path "{remote_file_path}\\{file_prefix}*" -DestinationPath "{output_zip_file}" -Force
        Move-Item -Path "{output_zip_file}.zip" -Destination "{archive_path}" -Force
        """

        # Define the PowerShell command to delete files with a prefix
        powershell_delete_command = (
            f'Remove-Item -Path "{remote_file_path}\\{file_prefix}*" -Force'
        )

        # Execute the PowerShell script remotely
        with tqdm(total=2, desc="Processing") as pbar:  # wacky woohoo solution for this not elegant
            result = session.run_ps(powershell_command)
            pbar.update(1)
            time.sleep(0.3)
            session.run_ps(powershell_delete_command)
            pbar.update(2)

        # Check the execution result
        if result.status_code == 0:
            print(
                f'Successfully zipped files with prefix "{file_prefix}" to "{archive_path}"')
        else:
            print(f'Error: {result.std_err.decode()}')

    def archiveAll(self):
        # Define the path to the .txt file you want to edit on the remote server
        remote_file_path = self.path  # this works
        archive_path = os.path.join(os.path.dirname(self.path), 'archive')
        output_zip_file = remote_file_path + date()  # zip folder name will have datetime

        # Initialize a WinRM session with administrative credentials
        session = winrm.Session(
            self.hostname,
            auth=(self.username, self.password),
            transport='ntlm'
        )

        # Define the PowerShell command to zip files with a prefix
        powershell_command = f"""
        if (-not (Test-Path -Path "{archive_path}" -PathType Container)) {{
            New-Item -Path "{archive_path}" -ItemType Directory
        }}
        Compress-Archive -Path "{remote_file_path}\\*" -DestinationPath "{output_zip_file}" -Force
        Move-Item -Path "{output_zip_file}.zip" -Destination "{archive_path}" -Force
        """

        # Define the PowerShell command to delete files with a prefix
        powershell_delete_command = (
            f'Remove-Item -Path "{remote_file_path}\\*" -Force'
        )

        # Execute the PowerShell script remotely
        with tqdm(total=2, desc="Processing") as pbar:  # wacky woohoo solution for this not elegant
            result = session.run_ps(powershell_command)
            pbar.update(1)
            time.sleep(0.3)
            session.run_ps(powershell_delete_command)
            pbar.update(2)

        # Check the execution result
        if result.status_code == 0:
            print(
                f'Successfully zipped files to "{archive_path}"')
        else:
            print(f'Error: {result.std_err.decode()}')
