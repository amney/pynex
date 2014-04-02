#!/bin/env python

from utilities import RollBack, saves, saves_improved
import cisco

@saves
def set_hostname(hostname):
    cisco.cli('conf t')
    cisco.cli('hostname %s' % hostname)


@saves_improved(vdc_all=True)
def set_hostname_improved(hostname):
    cisco.cli('conf t')
    cisco.cli('hostname %s' % hostname)


def critical_code():
    with RollBack('critical'):
        cisco.cli('conf t')
        cisco.cli('int po 1337')
        raise cisco.cli_execution_error
        cisco.cli('ip add 1.1.1.1/24')


def main():
    set_hostname('saves')
    print cisco.cli('show start | grep hostname')
    set_hostname_improved('saves-improved')
    print cisco.cli('show start | grep hostname')

    critical_code()


if __name__ == '__main__':
    main()
