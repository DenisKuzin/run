#!/usr/bin/python

from sys import argv
import sh

def main():
    if len(argv) != 2:
        print 'Usage: run <command>'
        return
    command = argv[1]
    if command == 'miredo':
        sh.miredo()
    elif command == 'revert':
        sh.hg.revert("-C", "--all")
    else:
        print 'What is "%s"?' % command

if __name__ == '__main__':
    main()
