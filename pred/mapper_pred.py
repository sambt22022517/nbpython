#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re

for line in sys.stdin:
    line = line.split('\t')[-1]
    line = re.sub(r'http\S+', '', line)
    line = re.sub(r"[-()\"#/@;%&$:<>{}`+=~|.!?,]", "", line)
    line = line.lower()
    line = re.sub("\d+", "",line)
    line = re.sub('@en', '', line) 
    line = re.sub('<br /><br />', ' ', line) 
    line = re.sub('[^a-zA-Z]', ' ', line)  
    line = re.sub('\s+', ' ', line)  
    line = line.strip()  
          
    print(line)                    

