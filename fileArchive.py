import shutil
import os


# This class focuses on manipulating folder and file structures
class FileArchive:

    def __init__(self, source, destination, target):
        self.source = source
        self.destination = destination
        self.target = target
        self.POSTFIX = r'5.txt'

    # This function is a wrapper for the shutil.make_archive function
    def make_archive(self):
        if not os.path.exists(self.destination):
            os.makedirs(self.destination)
        base = os.path.basename(self.target)
        name = base.split('.')[0]
        format = base.split('.')[1]
        archive_from = os.path.dirname(self.source)
        archive_to = os.path.basename(self.source.strip(os.sep))
        print(self.source, self.target, archive_from, archive_to)
        shutil.make_archive(name, format, archive_from, archive_to)
        shutil.move('%s.%s' % (name, format), self.target)

    # This function walks through the path queried and zips all the files in the folder into an archive folder
    # This will trigger when there's a file that ends with a specific 'postfix' i.e. testfile999 <<
    def zipFolder(self):
        for root, dirs, files in os.walk(self.source, topdown=False):
            for file in files:
                if file.endswith(self.POSTFIX):  # modifies end with postfix
                    self.make_archive()
                    # os.remove(base + file) ? don't know if this will work

    # This function trims the dirname & basename to create unique .zip files for each folder in the 'filepath' file
    def trimPathName(self):
        root = os.path.dirname(self.source)
        basename = os.path.basename(self.source)
        destination = os.path.join(root, 'archives', 'archive_' + basename + '.zip')
        return destination