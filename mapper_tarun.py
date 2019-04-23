#!/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""
import sys
import csv

def main(divider='\t'):
    info = get_input(sys.stdin)
    for term in info:
        temp=term[-5:]
        for terms in temp:
            if terms.strip():
                print '%s%s%d' % (terms.strip(), divider, 1)
            else:
                continue

def get_input(document):
    readip = csv.reader(document)
    readip.next()
    for rule in readip:
        yield rule

if __name__ == "__main__":
    main()
