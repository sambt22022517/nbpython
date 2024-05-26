#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    if(line.split('\t')[1]=='='):
        continue 
    
    line = line.strip()
    # split the line into words
    print(line)