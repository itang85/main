# !/usr/bin/python
# encoding=utf-8
import sys
import pexpect

from django.core.management.base import BaseCommand, CommandError
from app.common.models import *


class SshController:
    def __init__(self):
        self.connection = {}

    def connect(self, name, ip, user, passwd):
        ssh = pexpect.spawn('ssh {user}@{ip}'.format(user=user, ip=ip))
        try:
            r = ssh.read()
            print(r)
            i = ssh.expect(['password:', 'continue connecting(yes/no)?'], timeout=5)
            if i == 0:
                ssh.sendline(passwd)
            elif i == 1:
                ssh.sendline('yes\n')
                ssh.expect('password:')
                ssh.sendline(passwd)
            ssh.sendline('ls /')
            r = ssh.read()
            print(r)
        except pexpect.EOF:
            print("EOF")
        except pexpect.TIMEOUT:
            print("TIMEOUT")
        finally:

            if name not in self.connection:
                self.connection[name] = []
            self.connection[name].append(ssh)

        return ssh

    def execute(self, name, cmd):
        for connection in self.connection[name]:
            connection.sendline(cmd)
            r = connection.read()
            print(r)

    def close(self, name=None):
        if name is not None:
            for connection in self.connection[name]:
                connection.close()
            del self.connection[name]
        else:
            for name in self.connection:
                for connection in self.connection[name]:
                    connection.close()
            self.connection = None


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        # parser.add_argument('sysArgs', nargs='+', type=int)
        pass

    def handle(self, *args, **options):
        ssh = SshController()
        ssh.connect('test', '127.0.0.1', 'ubuntu', '123456')
        ssh.execute('test', 'ls -l /')
        ssh.close()
        self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % options['sysArgs']))


