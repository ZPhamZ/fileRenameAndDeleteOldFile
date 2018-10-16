import os
import time

def fileNameChange():
    filePath = "//networkorserver/folder1/folder2/folder3/"
    ##Changes from current pyscript directory to filePath directory
    os.chdir(filePath)
    fileList = os.listdir(filePath)
    print(fileList)
    ##Splits the file name on the '.' delimiter
    ##Sets the first part of the filename into filePrefix variable
    ##Sets the second part of the filename into fileExtension
    filePrefix, fileExtension = fileList[0].split('.')
    print(filePrefix)
    print(fileExtension)
    ##Removes last 8 characters from filePrefix value
    fileNoDate = filePrefix[:-8]
    ##Setting up new file name by concatenation
    newFileName = 'old.' + fileNoDate + '.' + fileExtension
    ##Changes the file name from the returned list in os.listdir to newFileName
    os.rename(fileList[0], newFileName)

def deleteFile():
    oldFilePath = '//networkorserver/folder1/folder2/folder3/file.log'
##    time.sleep(5)
    try:
        os.remove(oldFilePath)
    except OSError:
        pass

def main():
    fileNameChange()
    deleteFile()

main()
