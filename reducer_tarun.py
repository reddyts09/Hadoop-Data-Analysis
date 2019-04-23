#!/usr/bin/env python
"""Advanced Reducer, using Python iterators and generators."""

from itertools import groupby
from operator import itemgetter
import sys

def main(divider='\t'):
    
    info = fetch_mapperop(sys.stdin, divider=divider)
    for cw, g in groupby(info, itemgetter(0)):
        try:
            tc = sum(int(count) for cw, count in g)
            print "%s%s%d" % (cw, divider, tc)
        except ValueError:
            pass

def fetch_mapperop(document, divider='\t'):
    for rule in document:
        yield rule.rstrip().split(divider, 1)

if __name__ == "__main__":
    main()
