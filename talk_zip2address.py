#!/usr/bin/env python
# -*- coding:utf-8 -*-

import shlex
import subprocess

import urllib2
import json
import sys

CMD_SAY = 'jsay'

def main(zip1, zip2):
    say_zip(zip1, zip2)
    say_address(zip1, zip2)
    return

def say_zip(zip1, zip2):
    text = u'郵便番号、%s%s、は' % (zip1, zip2)
    text = CMD_SAY + ' ' + text
    text = text.encode('utf-8')
    print text
    proc = subprocess.Popen(shlex.split(text))
    proc.communicate()
    return

def say_address(zip1, zip2):
    json_url = 'http://api.thni.net/jzip/X0401/JSON/'

    try:
        r = urllib2.urlopen('%s%s/%s.js' % (json_url , zip1, zip2))
        obj = json.loads(r.read())

        state_name = obj['stateName']
        city = obj['city']
        street = obj['street']

        # SAY
        address_str = u'%s、%s、%s、です。' % (state_name, city, street)
        address_str = address_str.encode('utf-8')

        text = '%s %s'  % (CMD_SAY, address_str)
        print text
        proc = subprocess.Popen(shlex.split(text))
        proc.communicate()
    finally:
        r.close()

    return

### Execute
if __name__ == "__main__":
    zip1 = sys.argv[1]
    zip2 = sys.argv[2]
    main(zip1, zip2)
