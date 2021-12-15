#!./venv/bin/python
import argparse
import os
import shutil


def dir_path(string):
    # Checks if the string is correct
    if os.path.isdir(string):
        return string
    elif os.path.isfile(string):
        print(f'install.py: {string}: It is a file')
        return None
    else:
        return None


def main():
    """This script adds all the scripts to a PATH variable, to simply execute them.
    Most likely you want to run this script without any arguments to add the scripts from the current directory"""
    parser = argparse.ArgumentParser('Adds all the scripts to a PATH variable')
    parser.add_argument('indir', help='The path where the scripts are located', type=str, nargs='?', default='.')
    args = parser.parse_args()
    folder = dir_path(args.indir)
    if not folder:
        return 0
    scripts = []
    path_var = os.environ['PATH'].split(os.pathsep)[0]
    for file in os.listdir(folder):
        if file.endswith('.py'):
            scripts.append(file)
            shutil.copy(os.path.abspath(file), path_var)
    print('The following scripts were added to PATH variable, and now can be executed as it is named: ')
    for script in scripts:
        print(script)


if __name__ == '__main__':
    main()
