import os
import zipfile
import shutil

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

    # This function is a wrapper for the shutil.make_archive function
    def _make_archive(self):
        if not os.path.exists(self.destination):
            os.makedirs(self.destination)
        base = os.path.basename(self.target)
        name = base.split('.')[0]
        format = base.split('.')[1]
        archive_from = os.path.dirname(self.source)
        archive_to = os.path.basename(self.source.strip(os.sep))
        shutil.make_archive(name, format, archive_from, archive_to)
        shutil.move('%s.%s' % (name, format), self.target)

    # This function walks through the path queried and zips all the files in the folder into an archive folder
    # This will trigger when there's a file that ends with a specific 'postfix' i.e. testfile999 <<
    def zipFolder(self):
        self._make_archive()

        # Use shutil.rmtree to delete all files in the folder
        shutil.rmtree(self.source)

        os.mkdir(self.source)  # recreate folder

    # This function is for zipping with a prefix
    def prefixZip(self):
        # Create a list of files in the folder that match the prefix
        matching_files = [file for file in os.listdir(self.source) if file.startswith(self.prefix)]

        # Create the ZIP archive and add the matching files to it
        with zipfile.ZipFile(self.target, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in matching_files:
                file_path = os.path.join(self.source, file)
                zipf.write(file_path, file)
                os.remove(file_path)

    # This function trims the dirname & basename to create unique .zip files for each folder in the 'filepath' file
    def trimPathName(self):
        root = os.path.dirname(self.source)
        basename = os.path.basename(self.source)
        destination = os.path.join(root, 'archives', 'archive_' + basename + '.zip')
        return destination
