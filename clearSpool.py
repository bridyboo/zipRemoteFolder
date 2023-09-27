import sharedPathArchive
import remoteArchive
import pwinput


path = input("please add path for spool directory: ")
choice = input("archive all (a) or prefix (b)? ")
input("\n\n")

if choice == 'a':
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

else:
    if not path.startswith(r'\\'):
        username = input("please provide username: ")
        password = pwinput.pwinput()
        server = input("please provide server address: ")
        remote = remoteArchive.RemoteArchive(server, username, password)
        remote.archiveAll()
        input()

    else:
        sharedArchive = sharedPathArchive.SharedPathArchive(path)
        sharedArchive.archiveAll()
        input()