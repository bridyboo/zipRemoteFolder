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
        # Create an 'archive' folder one level above the 'path'
        archive_folder = os.path.join(os.path.dirname(self.path), 'archive')
        if not os.path.exists(archive_folder):
            os.makedirs(archive_folder)

        target = os.path.join(self.path + date() + '.zip')
        archive = fileArchive.FileArchive(self.path, archive_folder, target, prefix)
        # Check if the file exists
        if os.path.exists(self.path):
            try:
                archive.prefixZip()
                final_spot = archive.moveFile(target)
                print(f'Successfully zipped files with prefix "{prefix}" to "{final_spot}"')

            except Exception as e:
                print(f"Error: {e}")
        else:
            print("File does not exist.")

    # Archive/zip everything in a folder
    def archiveAll(self):
        # Create an 'archive' folder one level above the 'path'
        archive_folder = os.path.join(os.path.dirname(self.path), 'archive')
        if not os.path.exists(archive_folder):
            os.makedirs(archive_folder)

        target = os.path.join(self.path + date() + '.zip')
        archive = fileArchive.FileArchive(self.path, archive_folder, target)
        if os.path.exists(self.path):
            try:
                archive.zipFolder()
                final_spot = archive.moveFile(target)
                print(f'Successfully zipped files to "{final_spot}"')

            except Exception as e:
                print(f"Error: {e}")
        else:
            print("File does not exist.")