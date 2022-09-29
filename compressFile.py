import os
import shutil
from zipfile import ZipFile
from os import path
from shutil import make_archive

def main():
    #check if the file exists
    if path.exists("updateFile.py"):
        src = path.realpath("updateFile.py");
    #put things into a ZIP file
    with ZipFile("updateFile.zip", "w") as newZip:
        newZip.write("updateFile.py")
        newZip.write("Signature.txt")

if __name__== "__main__":
    main()
