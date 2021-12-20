#!./venv/bin/python
import argparse
import os


def dir_path(string, out):
    if os.path.exists(string):
        return string
    else:
        print(f'mv.py rename {string} to {out}: No such file or directory')
        return None


def main():
    """Here we implemented mv UNIX-command. As original one it takes input as a file or a folder,
    output as a path where to save a file or a folder."""
    parser = argparse.ArgumentParser('Moves files or folders, often uses to rename files or folders')
    parser.add_argument('infile', type=str)
    parser.add_argument('outfile', type=str, default=None, nargs='?')
    args = parser.parse_args()
    file = dir_path(args.infile, args.outfile)
    if not file:
        return 0
    os.rename(file, args.outfile)
    return 0


if __name__ == '__main__':
    main()
