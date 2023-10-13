import os
import fileArchive
import datetime


# This static method is a helper function for the zip file's datetime
def date():
    curr_date = datetime.datetime.now()
    return curr_date.strftime("%Y-%m-%d_%H%M%S")


# This class is to archive all files with a prefix on a shared network
class SharedPathArchive:
    def __init__(self, path):
        self.path = path

    # Archive/zip files with a prefix
    def archive(self, prefix):
        target = os.path.join(self.path + date() + '.zip')
        archive = fileArchive.FileArchive(self.path, self.path, target, prefix)
        # Check if the file exists
        if os.path.exists(self.path):
            try:
                archive.prefixZip()
                print(f'Successfully zipped files with prefix "{prefix}" to "{target}"')

            except Exception as e:
                print(f"Error: {e}")
        else:
            print("File does not exist.")

    # Archive/zip everything in a folder
    def archiveAll(self):
        target = os.path.join(self.path + date() + '.zip')
        archive = fileArchive.FileArchive(self.path, self.path, target)
        if os.path.exists(self.path):
            try:
                archive.zipFolder()
                print(f'Successfully zipped files "{target}"')

            except Exception as e:
                print(f"Error: {e}")
        else:
            print("File does not exist.")
