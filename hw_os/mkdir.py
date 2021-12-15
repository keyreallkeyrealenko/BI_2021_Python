#!./venv/bin/python
import argparse
import os


def main():
    """Here we implemented mkdir UNIX-command. As original one
    it takes input as a path to new created directory."""
    parser = argparse.ArgumentParser('Creates the directories named as operands')
    parser.add_argument('-p', help='Create intermediate directories as required', action='store_true')
    parser.add_argument('infile', type=str)
    args = parser.parse_args()
    if args.p:
        os.makedirs(args.infile)
        return 0
    else:
        try:
            os.mkdir(args.infile)
        except FileNotFoundError:
            print(f'mkdir: {args.infile}: No such file or directory')
        return 0


if __name__ == '__main__':
    main()
