import os
import csv
import sys
import shutil
import zipfile

path = sys.argv[1]

print(f'File: {path}')


def read_file(path):
    """
    Print out the lines from a file
    """
    if not path:
        raise Exception('Path cannot be empty')
    print(f'Process {path}')
    with open(path, 'r') as FILE:
        lines = FILE.readlines()
        for line in lines:
            print(line)


def read_csv(path):
    """
    Print out the objects of a CSV
    """
    if not path:
        raise Exception('Path cannot be empty')
    print(f'Process {path}')
    with open(path, 'r') as FILE:
        lines = csv.reader(FILE)
        for line in lines:
            print(line)


def read_csv_as_dict(path):
    """
    Print out the objects of a CSV
    """
    if not path:
        raise Exception('Path cannot be empty')
    print(f'Process {path}')
    with open(path, 'r') as FILE:
        lines = csv.DictReader(FILE)
        for line in lines:
            print(line)


def write_csv(path):
    with open(path, 'w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
        writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
        writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


def remove_file(path):
    print(f'Remove {path}')
    try:
        os.remove(path)
        return True
    except:
        return False


def remove_directory(path):
    print(f'Remove directory at {path}')
    try:
        shutil.rmtree(path)
        return True
    except:
        return False


def zip_directory(path, archive_name):
    shutil.make_archive(archive_name, 'zip', path)


def unzip_directory(path):
    z = zipfile.ZipFile(path)
    for f in z.namelist():
        print(f)
        if f.endswith('/'):
            os.makedirs(f)

# zip_directory('files', 'new_archive')
unzip_directory('new_archive.zip')