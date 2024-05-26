#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
 
for line in sys.stdin:
    
    try:
        label, count = line.split('\t')
    except ValueError:
        continue
    
    try:        
        count = int(count)
    except ValueError:
        continue
    
    print('%s\t%s' % (label, count))
    
    