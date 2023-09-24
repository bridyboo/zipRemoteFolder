# Import the os module for path manipulation
import os
import fileArchive

class SharedPathArchive:

    def __init__(self, path):
        self.path = path
    # Define the network path to the shared drive
    # network_path = r"\\fsrv_01\H\mun0466test\test.txt"

    def archive(self, prefix):
        archive = fileArchive.FileArchive(self.path, self.path,os.path.join(self.path + '.zip'), prefix)
        # Check if the file exists
        if os.path.exists(self.path):
            try:
                archive.prefixZip()

            except Exception as e:
                print(f"Error: {e}")
        else:
            print("File does not exist.")