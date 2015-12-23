#!/usr/bin/python

import sys
from DictionaryServices import *

def main():
    try:
        infile = sys.argv[1].decode('utf-8')
    except IndexError:
        errmsg = 'You did not enter any terms to look up in the Dictionary.'
        print errmsg
        sys.exit()
    try:
        with open(infile) as f:
            for line in f:
                lookup(line.decode('utf-8'))
                raw_input("Press Enter to continue...")
                print ""
    except IOError:
        print "Problem reading file " + infile

def lookup(searchword):
    wordrange = (0, len(searchword))
    dictresult = DCSCopyTextDefinition(None, searchword, wordrange)
    if not dictresult:
        errmsg = "'%s' not found in Dictionary." % (searchword)
        print errmsg.encode('utf-8')
    else:
        print dictresult.encode('utf-8')

if __name__ == '__main__':
    main()
