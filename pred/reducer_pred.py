#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re
import math
vocabSet = set()
likelihood = {}
prior = {}


f = open('conditional')
for line in f.readlines():
    count = line.split('\t')[1]
    try:
        word, label = line.split('\t')[0]
    except ValueError:
        continue
        
    if word not in vocabSet:
        likelihood[word]={}
        vocabSet.add(word)
    likelihood[word][label] = count   
     
   
f1 =open('prior')
for line in f1.readlines():        
    try:
        label, prob = line.split('\t')
    except ValueError:
        continue
    prior[label] = float(prob)
    
   
 
Posterior = {}
j = 0
texts = []
for line in sys.stdin: 
    try:
        text = line
        texts.append(text)
    except ValueError:
        continue
    
    Posterior[j] = {}   
    words = re.split(' ', text)
    
    
    for lab in prior.keys(): 
        
        Posterior[j][lab] = prior[lab]
        
        for word in words:
            try:
                Posterior[j][lab] += float(likelihood[word][lab])                              
            except KeyError:
                Posterior[j][lab] += math.log(1/100000)
    j += 1
pred_labels=[]    
for k,v in Posterior.items():
    pro = list(v.values())
    l = list(v.keys())
    pred_labels.append(l[pro.index(max(pro))])   

for i in range(len(pred_labels)):
    print(f'{pred_labels[i]}\t{texts[i]}')
