import os
import fileArchive

# This class is to archive all files with a prefix on a shared network
class SharedPathArchive:
    def __init__(self, path):
        self.path = path

    def archive(self, prefix):
        archive = fileArchive.FileArchive(self.path, self.path, os.path.join(self.path + '.zip'), prefix)
        # Check if the file exists
        if os.path.exists(self.path):
            try:
                archive.prefixZip()
                print(f'Successfully zipped files with prefix "{prefix}" to "{self.path}.zip"')

            except Exception as e:
                print(f"Error: {e}")
        else:
            print("File does not exist.")