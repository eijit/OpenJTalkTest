#!/usr/bin/env python
# -*- coding:utf-8 -*-

import shlex
import subprocess

import urllib2
import json
import sys

CMD_SAY = 'jsay'

def main(apikey):
    say_nhk_now_on_air('270', 'e1', apikey)
    return

def say_nhk_now_on_air(area, service, apikey):
    json_url = 'http://api.nhk.or.jp/v2/pg/now/%s/%s.json' % (area, service)

    try:
        r = urllib2.urlopen('%s?key=%s' % (json_url , apikey))
        obj = json.loads(unicode(r.read()))
        nowonair_list = obj['nowonair_list']
        attr = {'previous': u'前', 'present': u'今', 'following': u'次'}
        for key in attr:
            program = nowonair_list[service][key]
            title = program['title'].encode('utf-8')
            period = attr[key].encode('utf-8')
            text = '''%s '%sの番組は、%s、です。' ''' % (CMD_SAY, period, title)
            print text

            proc = subprocess.Popen(shlex.split(text))
            proc.communicate()
    finally:
        r.close()

    return

### Execute
if __name__ == "__main__":
    apikey = sys.argv[1]
    main(apikey)
