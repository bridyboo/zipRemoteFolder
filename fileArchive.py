import os
import zipfile
from tqdm import tqdm
import time


# This class focuses on manipulating folder and file structures
class FileArchive:
    def __init__(self, source, destination, target, prefix=None):
        if prefix is None:
            self.source = source
            self.destination = destination
            self.target = target  # this will have datetime for its zip file
        else:
            self.source = source
            self.destination = destination
            self.target = target  # this will have datetime for its zip file
            self.prefix = prefix

    def zipFolder(self):
        all_file = [file for file in os.listdir(self.source)]

        with zipfile.ZipFile(self.target, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in tqdm(all_file, desc="Zipping Files"):
                file_path = os.path.join(self.source, file)
                zipf.write(file_path, file)
                os.remove(file_path)

    # This function is for zipping with a prefix
    def prefixZip(self):
        # Create a list of files in the folder that match the prefix
        matching_files = [file for file in os.listdir(self.source) if file.startswith(self.prefix)]

        # Create the ZIP archive and add the matching files to it
        with zipfile.ZipFile(self.target, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in tqdm(matching_files, desc="zipping Files"):
                file_path = os.path.join(self.source, file)
                zipf.write(file_path, file)
                os.remove(file_path)

    # This function trims the dirname & basename to create unique .zip files for each folder in the 'filepath' file
    def trimPathName(self):
        root = os.path.dirname(self.source)
        basename = os.path.basename(self.source)
        destination = os.path.join(root, 'archives', 'archive_' + basename + '.zip')
        return destination
