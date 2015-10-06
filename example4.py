"""
Simple program to demonstrate Pylint
Count all files in a folder.
"""
import sys
import os
from glob import glob

def count_files(folder):
    """Count all files in folder and recurse into other foldes."""
    count = 0
    folder_contents = glob(os.path.join(folder, '*'))
    for item in folder_contents:
        if os.path.isdir(item):
            count += count_files(item)
        else:
            count += 1
    return count

def main():
    """Gather args and call count_files."""
    if len(sys.argv) < 2:
        print 'USAGE: example3.py <folder path> [<folder path>]*'

    folders = sys.argv[1:]

    file_count = 0
    for folder in folders:
        file_count += count_files(folder)

    print 'Found a total of {} items.'.format(file_count)


if __name__ == '__main__':
    main()
