
import zipfile
import os

def unzip(filePath, folder):
    zip_file = zipfile.ZipFile(filePath)
    if os.path.isdir(folder):
        pass
    else:
        os.mkdir(folder)
    #get all files in the compressed package
    for name in zip_file.namelist():
        #unzip each file in the certain folder
        zip_file.extract(name, folder)
    zip_file.close()

def main():
    file_path = "updateFile.zip"
    dir = "C:/Users/jesse/Downloads/MA/workSpace/download/"
    unzip(file_path, dir)
    print("File is decompressed!")

if __name__ ==  "__main__":
    main()
