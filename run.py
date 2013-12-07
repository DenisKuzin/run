#!/usr/bin/python

from sys import argv
from sh import miredo

def main():
    if len(argv) != 2:
        print 'Usage: run <command>'
        return
    command = argv[1]
    if command == 'miredo':
        miredo()
    else:
        print 'What is "%s"?' % command

if __name__ == '__main__':
    main()
