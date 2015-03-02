#!/usr/bin/env python

DESCRIPTION = 'Joey Script "Interpretor.'

import argparse
import os.path
import sys
import time

sys.path.append(os.path.join(os.path.split(__file__)[0], '..'))

import mippy


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description=DESCRIPTION)
    mippy.add_arguments(parser)

    args = parser.parse_args()


    hosts = {}

    if True:	
        d = os.path.join(os.path.expanduser('~/.mippy'))

        if not os.path.exists(d):
            os.mkdir(d)

        hosts_path = os.path.join(d, 'hosts')
        if not os.path.exists(hosts_path):
            f = open(hosts_path, 'w+')
            f.write('# Resolves MIP addresses to names.')
            f.close()

        f = open(hosts_path)
        for line in f.readlines():
            if line.strip()[0] == '#':
                continue
            address, name = line.split()
            hosts[name] = address

        f.close()

    if ':' not in args.device:
        if hosts.has_key(args.device):
            args.device = hosts[args.device]

    gt = mippy.GattTool(args.adaptor, args.device)

    mip = mippy.Mip(gt)
    mip.playSound(0x4d)

    turtle = mippy.Turtle(mip)

    while True:
        line = sys.stdin.readline()
        if line == None:
            sys.exit()
        if len(line.strip()) == 0:
            print 'Huh?'
        for char in line:
            if char == 'f':
                mip.distanceDrive(0.25)
            elif char == 'b':
                mip.distanceDrive(-0.25)
            elif char == 'l':
                mip.turnByAngle(-100)
            elif char == 'r':
                mip.turnByAngle(100)
            elif char == 'o':
                mip.turnByAngle(450)
            elif char == 'm':
                mip.playSound(47)
            elif char == 's':
                mip.playSound(35)
            time.sleep(1)

