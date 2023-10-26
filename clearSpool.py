import sharedPathArchive
import remoteArchive
import pwinput
import os
import readline

# Quality of Life for CLI
os.system('mode con: cols=150 lines=30')  # window size
readline.parse_and_bind("control-v: paste")  # this allows ctrl+v for paste in older windows

path = input("please add path for spool directory: ")
choice = input("archive all (a) or prefix (b)? ")

username = os.getlogin()
if choice == 'a':
    if not path.startswith(r'\\'):  # If path doesn't start with '\\' we need to remote to a different server
        print("This is your username datacenter\\" + username)
        password = pwinput.pwinput()
        server = input("please provide server address: ")
        remote = remoteArchive.RemoteArchive(server, username, password, path)
        remote.archiveAll()
        input()

    else:
        sharedArchive = sharedPathArchive.SharedPathArchive(path)
        sharedArchive.archiveAll()
        input()


else:
    prefix = input("what prefix are you looking to archive? ")

    if not path.startswith(r'\\'):
        print("This is your username datacenter\\" + username)
        password = pwinput.pwinput()
        server = input("please provide server address: ")
        remote = remoteArchive.RemoteArchive(server, username, password, path)
        remote.archive(prefix)
        input()

    else:
        sharedArchive = sharedPathArchive.SharedPathArchive(path)
        sharedArchive.archive(prefix)
        input()
