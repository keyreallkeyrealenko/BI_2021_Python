#!./venv/bin/python
import argparse
import os
import shutil


def dir_path(string):
    # tuple with 0 when string is a dir, with 1 when string is a file
    if os.path.isdir(string):
        return string, 0
    elif os.path.isfile(string):
        return string, 1
    else:
        print(f'{string}: No such file or directory')


def main():
    """Here we implemented sort UNIX-command. As original one it takes input as a path to a file or to a directory.
    If you want to delete a folder add '-r' flag."""
    parser = argparse.ArgumentParser('Remove files/directories')
    parser.add_argument('infile', nargs='?', type=dir_path, default='.')
    parser.add_argument('-r', help='Attempt to remove the file hierarchy rooted in each file argument',
                        action='store_true')
    args = parser.parse_args()
    # 0/1 - indicate folder or file respectively
    if args.infile[1] == 0 and not args.r:
        print(f'rm: {args.infile[0]}: is a directory')
        return 0
    elif args.infile[1] == 0 and args.r:
        shutil.rmtree(args.infile[0])
        return 0
    else:
        os.remove(args.infile[0])
        return 0


if __name__ == '__main__':
    main()
