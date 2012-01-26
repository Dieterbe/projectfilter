#!/usr/bin/env python2
import argparse
from lib import backend
from filters.authorfilter import AuthorFilter
from filters.fnamefilter import FnameFilter
from filters.remotefilter import RemoteFilter

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Project filter')
    parser.add_argument('--fname', help='Filter on given filename (glob)')
    parser.add_argument('--author', help='Filter on author in git (regex)')
    parser.add_argument('--remote', help='Filter on git remote (regex)')
    parser.add_argument('--debug', action='store_true', default=False, help='Debug messages')
    parser.add_argument('directory', nargs='+', help='Directory/ies holding project directories')
    args = parser.parse_args()

    backend.debug_enabled = args.debug
    ret = backend.list_projectdirs(args.directory)
    if args.remote:
        ret = RemoteFilter(ret, args.remote)
    if args.author:
        ret = AuthorFilter(ret, args.author)
    if args.fname:
        ret = FnameFilter(ret, args.fname)
    for projectdir in ret:
        print projectdir
