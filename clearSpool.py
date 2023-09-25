import sharedPathArchive
import remoteArchive
import pwinput

#######################################################################################################################
POSTFIX = r'5.txt'
base = r'B:\ForWatchdogProject\testFiles'  # so this shit works, because it's a static path
################################################################################################


path = input("please add path for spool directory: ")
prefix = input("what prefix are you looking to archive? ")

if not path.startswith(r'\\'):
    username = input("please provide username: ")
    password = pwinput.pwinput()
    server = input("please provide server address: ")
    remote = remoteArchive.RemoteArchive(server, username, password)
    remote.archive(prefix)
    input()

else:
    sharedArchive = sharedPathArchive.SharedPathArchive(path)
    sharedArchive.archive(prefix)
    input()
