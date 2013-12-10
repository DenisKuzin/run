#!/usr/bin/python
u'''
Automation module
Run actions by simple command
Usage: run <command>
'''

from sys import argv
from os import path
import sh
import settings

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

def django():
    u'''
    Django development server
    '''
    manage_py = sh.python.bake('-t', path.join(settings.trbd_home, 'manage.py'))
    for message in manage_py('runserver', '0.0.0.0:8080', _iter=True):
        print(message)

def test():
    u'''
    Unit tests on trbd project
    '''
    manage_py = sh.python.bake('-t', path.join(settings.trbd_home, 'manage.py'))
    for message in manage_py('test', '-v', '3', 'documents.FunctionalTests', _iter=True):
        print(message)

def celery():
    u'''
    Celery message queue
    '''
    result = sh.rm(path.join(settings.trbd_home, 'celery.log'), f=True)
    print(result.ran)
    print(result)
    manage_py = sh.python.bake('-t', path.join(settings.trbd_home, 'manage.py'))
    for message in manage_py('celeryd', verbosity=3, settings='settings', concurrency=1, pool='solo', discard=True, logfile=path.join(settings.trbd_home, 'celery.log'), loglevel='DEBUG', traceback=True, hostname='test_worker', _iter=True):
        print(message)

def office():
    u'''
    OpenOffice server
    '''
    for message in sh.Command('/opt/openoffice.org3/program/soffice "-accept=socket,host=localhost,port=8100;urp;StarOffice.ServiceManager" -nologo -headless -nofirststartwizard')(_iter=True):
        print(message)

def rabbit():
    u'''
    RabbitMQ Broker
    '''
    for message in sh.rabbitmq-server(_iter=True):
        print(message)

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
