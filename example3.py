"""
Simple program to demonstrate Pylint
Count all files in a folder.
"""
import sys
import os
from glob import glob

def countFiles(folder):
    count = 0
    folderContents = glob(os.path.join(folder, '*'))
    for item in folderContents:
        if os.path.isdir(item):
            count += countFiles(item)
        else:
            count += 1
    return count

def main():
    if len(sys.argv) < 2:
        print 'USAGE: example3.py <folder path> [<folder path>]*'

    folders = sys.argv[1:]

    fileCount = 0
    for folder in folders:
        fileCount += countFiles(folder)

    print 'Found a total of {} items.'.format(fileCount)


if __name__ == '__main__':
    main()
