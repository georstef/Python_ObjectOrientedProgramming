import sys
import os
import zipfile

class ZipReplace:
    def __init__(self, filename,  search_string, replace_string):
        self.filename = filename
        self.txtfilename = filename.replace('zip', 'txt')
        self.search_string = search_string
        self.replace_string = replace_string
        self.directory = os.path.split(filename)[0]
        self.extension = os.path.split(filename)[1]

    def _full_filename(self, filename):
        return filename #os.path.join(self.temp_directory, filename)
        
    def zip_find_replace(self):
        self.unzip_files()
        self.find_replace()
        self.zip_files()

    def unzip_files(self):
        zip = zipfile.ZipFile(self.filename)
        try:
            zip.extractall(self.directory)
        finally:
            zip.close()
            
    def find_replace(self):
        for filename in os.listdir(self.directory):
            #print(filename, self.txtfilename)
            if filename == os.path.split(self.txtfilename)[1]:
                with open(self.txtfilename) as file:
                    contents = file.read()
                contents = contents.replace(self.search_string, self.replace_string)
                with open(self.txtfilename, "w") as file:
                    file.write(contents)
                
    def zip_files(self):
        file = zipfile.ZipFile(self.filename, 'w')
        for filename in os.listdir(self.directory):
            if filename == os.path.split(self.txtfilename)[1]:
                file.write(self.txtfilename, filename)

if __name__ == "__main__":
    ZipReplace('E:/Python33/apps/OOP/chapter5/something.zip', 'self', 'selfi').zip_find_replace()
