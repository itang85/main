#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import configparser


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

    # set listen port of dev server
    config = configparser.ConfigParser()
    config.read('./uwsgi.ini')
    localAddr = '0.0.0.0' + config['uwsgi']['socket']
    if sys.argv[1] == 'runserver' and len(sys.argv) == 2:
        sys.argv.append(localAddr)
        print('localAddr is: http://127.0.0.1' + config['uwsgi']['socket'])

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
