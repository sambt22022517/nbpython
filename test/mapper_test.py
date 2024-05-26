#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re

count = 0
for line in sys.stdin:
    if count>=0:
        labels = line.split('\t')[0] 
        line = line.split('\t')[1]
        line = re.sub(r'http\S+', '', line)
        line = re.sub(r"[-()\"#/@;%&$:<>{}`+=~|.!?,]", "", line)
        line = line.lower()
        line = re.sub("\d+", "",line)
        line = re.sub('@en', '', line)
        line = re.sub('<br /><br />', ' ', line) 
        line = re.sub('[^a-zA-Z]', ' ', line)  
        line = re.sub('\s+', ' ', line)  
        line = line.strip()  
          
        print(labels+'\t'+line)                    
                            
    count+=1  
