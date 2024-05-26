#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

for line in sys.stdin:    
    
    try:
        label, _, count = line.split('\t')
    except ValueError:
        continue
    
    # convert count (currently a string) to int
    try:        
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    
    
    print('%s\t%s' % (label, count))