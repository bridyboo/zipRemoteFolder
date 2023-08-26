import fileArchive
import paramiko
import os

#######################################################################################################################
POSTFIX = r'5.txt'
base = r'B:\ForWatchdogProject\testFiles'  # so this shit works, because it's a static path
################################################################################################
#dest = r'B:\ForWatchdogProject\archives\archive'  #for testing

# destination = input("enter destination for zip")
# target = os.path.join(destination + '.zip')


hostname = input("Input your server hostname here: ")
port = 22
username = input("input username:")
password = input("your password: ")

path = input("input spool folder location :")
# Create an SSH Client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the server
    ssh.connect(hostname, port, username, password)

    # Run commands on the remote server
    try:
        archiver = fileArchive.FileArchive(path, os.path.dirname(path), os.path.join(path + '.zip'))
        archiver.trimPathName()
        archiver.make_archive()
    except FileNotFoundError:
        print("The file does not exist.")

    # Print the output of the command
    print("archive complete")

finally:
    # Close the SSH connection
    ssh.close()
