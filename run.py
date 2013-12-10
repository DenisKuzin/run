#!/usr/bin/python
u'''
Automation module
Run actions by simple command
Usage: run <command>
'''

from sys import argv
import sh

def miredo():
    u'''
    Miredo client
    '''
    result = sh.miredo()
    print(result.ran)
    print(result)

def revert():
    u'''
    Hg revert all changes without backup
    '''
    result = sh.hg.revert(C=True, all=True)
    print(result.ran)
    print(result)

def unknown_command():
    u'''
    Command with this name not found
    '''
    print('What is "%s"?' % argv[1])

if __name__ == '__main__':
    if len(argv) != 2:
        print 'Usage: run <command>'
    else:
        globals().get(argv[1], unknown_command)()