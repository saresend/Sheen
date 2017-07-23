import re
import os
import sys

def parseFile(file_path, endDict):
    foundTodo = False
    f = open(file_path, 'r')
    todoReg = re.compile(r'(.*)(TODO.+)')
    count = 0
    try:
        for line in f:
            match = todoReg.match(line)
            if match != None:
                foundTodo = True
                if file_path not in endDict:
                    endDict[file_path] = []
                endDict[file_path].append('\tLine ' + str(count) + ': ' + match.group(2))
            count += 1
    except UnicodeDecodeError as e:
        pass

    if foundTodo == False:
        print("No TODOs Found")


def scan_directory(dirName, endDict):
   
    try:
        directory = os.scandir(dirName)
        for fileObj in directory:
            if fileObj.is_dir():
                scan_directory(fileObj.path, endDict)
            elif fileObj.is_file():
                parseFile(fileObj.path, endDict)

    except NotADirectoryError as e:
        parseFile(dirName, endDict)

    
    

if len(sys.argv) < 2:
    print("Please enter file or directory name")
    exit()
else: 
    endDict = {}
    scan_directory(sys.argv[1], endDict)
    for k, v in endDict.items():
        print(k)
        for line in v:
            print(line)

