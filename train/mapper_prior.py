#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

# input from hdfs
for line in sys.stdin:
    labels = line.split('\t')[0]
    
    for lab in labels.split(','):
        print('%s\t%s' % (lab, 1))
    
