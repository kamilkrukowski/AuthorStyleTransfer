import os
import sys
import numpy as np
from random import shuffle

assert len(sys.argv) == 3, "Usage: Python util.py [index authora] [index authorb]" ;

def process(a, b):
    global author
    a = str(a)
    aout = open(a + '.out','w')
    aout.write(author[int(a)] + '\n')
    b = str(b)
    bout = open(b + '.out','w')
    bout.write(author[int(b)] + '\n')
    step = 15
    start = int(step/2)
    stop = 1000 - 3*start
    with open('data.csv','r') as f:
        data = f.readline()
        data = f.readline().strip().split(',')
        while data != ['']:
            if data[1] == a:
                data = data[0].split(' ')
                for i in np.arange(start, stop, step):
                    aout.write(''.join([j + ' ' for j in data[i:i+step]]) + '\n')
            elif data[1] == b:
                data = data[0].split(' ')
                for i in np.arange(start, stop, step):
                    bout.write(''.join([j + ' ' for j in data[i:i+step]]) + '\n')
            data = f.readline().strip().split(',')


def split(name, a,is0, train=0.9, dev=0.05, test=0.05):
    assert train + dev + test == 1.0, "Split does not add up to 1.0";
    assert is0 == 0 or is0 == 1, "Need bool";
    a = str(a)
    adata = open(a + '.out','r').read().strip().split('\n')
    shuffle(adata)
    total = len(adata)
    train = int(total*train)
    total -= train
    dev = int(total*(dev/(dev+test)))
    test = total - dev
    print("Test {} Dev {} Train {}".format(test,dev,train))
    with open(name + '.train' + '.' + str(is0), 'w') as f:
        for i in range(train):
            f.write(adata[i] + '\n')
    with open(name + '.dev' + '.' + str(is0), 'w') as f:
        for i in range(dev):
            f.write(adata[train+i] + '\n')
    with open(name + '.test' + '.' + str(is0), 'w') as f:
        for i in range(test):
            f.write(adata[train+dev+i] + '\n')

a = 37
b = 39

process(a,b)
name = str(a) + '-' + str(b)
split(name,a,0,train=0.7,test=0.2,dev=0.1)
split(name,b,1,train=0.7,test=0.2,dev=0.1)
#process(13,16)
