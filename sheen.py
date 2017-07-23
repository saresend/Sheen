import re
import os
import sys

def parseFile(file_path):
    foundTodo = False
    f = open(file_path, 'r')
    todoReg = re.compile(r'(.*)(TODO.+)')
    count = 0
    try:
        for line in f:
            match = todoReg.match(line)
            if match != None:
                foundTodo = True
                print('\tLine ' + str(count) + ': ' + match.group(2))
            count += 1
    except UnicodeDecodeError as e:
        pass

    if foundTodo == False:
        print("No TODOs Found")


def scan_directory(dirName):
    try:
        directory = os.scandir(dirName)
        for fileObj in directory:
            if fileObj.is_dir():
                scan_directory(fileObj.path)
            elif fileObj.is_file():
                print(fileObj.path)
                parseFile(fileObj.path)

    except NotADirectoryError as e:
        parseFile(dirName)
    

if len(sys.argv) < 2:
    print("Please enter file or directory name")
    exit()
else: 
    scan_directory(sys.argv[1])

