#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Author: Massimiliano Torromeo <massimiliano.torromeo@gmail.com>
# License: BSD

name = "dephp"
description = "Unofficial CLI application that decodes files through unphp.net web service"
version = "0.1.0"
url = "http://github.com/mtorromeo/dephp"

import os
import sys


def main():
    import ConfigParser
    import argparse

    try:
        import setproctitle
        setproctitle.setproctitle(name)
    except ImportError:
        pass

    parser = argparse.ArgumentParser(prog=name, description=description)

    parser.add_argument('-V', '--version', action='version', version="%(prog)s " + version)
    parser.add_argument('-m', '--metadata', action="store_true", help='Print response metadata')
    parser.add_argument('-a', '--apikey', action="store", help='Unphp.net API key')
    parser.add_argument('-o', '--output', help="Write the result to OUTPUT. If not specified it will be printed to STDOUT")
    parser.add_argument('file', nargs='?', help='The file to read. If not specified it will be read from STDIN')

    args = parser.parse_args()


    config = ConfigParser.SafeConfigParser(defaults=dict(
        entrypoint="http://www.unphp.net/api/v2/post",
        apikey=args.apikey
    ))
    try:
        config.read(["/etc/{}.conf".format(name), os.path.expanduser("~/.{}.conf".format(name))])
    except ConfigParser.Error as e:
        sys.exit(e.message)

    del args.apikey
    apikey = config.get('DEFAULT', 'apikey')
    if not apikey:
        sys.exit('You must specify a valid unphp API key. You can request on here at http://www.unphp.net/api/request/')


    run(apikey, config.get('DEFAULT', 'entrypoint'), **vars(args))


def run(apikey, entrypoint="http://www.unphp.net/api/v2/post", file=False, metadata=False, output=False):
    import requests

    script = open(file, 'rb') if file else sys.stdin

    r = requests.post(entrypoint, files={"file": script}, data={"api_key": apikey})
    r = r.json()

    if metadata:
        for k,v in r.items():
            print "{: >16} {}".format(k, v)
        print


    if r['result'] == 'success':
        r = requests.get(r['output'])
        if output:
            with open(output, 'wb') as f:
                f.write(r.text[28:])
        else:
            print r.text


if __name__ == '__main__':
    main()