'''
Created on Dec 26, 2019

@author: marcoshung
'''
import os
import shutil
from os import path
from pathlib import Path
from posix import getcwd
directories = {"Documents" : [".pdf", ".txt",".doc", ".xlsx", ".docx"],
               "Images" : [".jpg", ".jpeg", ".png"],
               "Videos" : [".mp4", ".mov", ".flv"],
               "DO NOT CHANGE" : [".py", ".java"],
               }

def getDirectory(string):
    for category, suffixes in directories.items():
        for suffix in suffixes:
            if(suffix == string):
                return category
            
    return "MISC"
def organizeDirectory():
    for item in os.scandir():
        filePath = Path(item)
        if(filePath.is_dir()):
            continue
        fileType = filePath.suffix.lower()
        directory = getDirectory(fileType)
        if(directory == "DO NOT CHANGE"):
            continue
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))
    
def organizeDocuments():
    os.chdir('Documents')
    for item in os.scandir():
        filePath = Path(item)
        if(filePath.is_dir()):
            continue
        directory = ""
        if(filePath.name.lower().__contains__("cover letter")):
            directory += "Job Apps/Cover Letter"
        elif(filePath.name.lower().__contains__("resume")):
            directory += "Job Apps/Resume"
        else:
            directory += "Misc."
        directoryPath = Path(directory) 
        futureDirPAth = str(directoryPath) + "/" + str(filePath)
        if(path.exists(futureDirPAth)):
            print("bad")
        else:
            shutil.move(os.path.abspath(filePath), os.path.abspath(directoryPath))
        #shutil.move(item,directoryPath)

if __name__ == "__main__":
    organizeDirectory()
    organizeDocuments()