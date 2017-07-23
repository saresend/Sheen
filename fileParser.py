import re
import os

def parseFile(file_path):
    f = open(file_path, 'r')
    todoReg = re.compile(r'(.*)(TODO.+)')
    count = 0
    for line in f:
        match = todoReg.match(line)
        if match != None:
            print('\tLine ' + str(count) + ': ' + match.group(2))
        count += 1


def scan_directory(dirName):
    directory = os.scandir(dirName)
    for fileObj in directory:
        print(fileObj.path)
        parseFile(fileObj.path)
    
if __name__ == "__main__":
    # parseFile('TwitterAgent.py')
    scan_directory('testDir')
            
    
