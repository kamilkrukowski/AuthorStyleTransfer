import os
import sys
import numpy as np

"List to query author names from author index"
author = []
with open('authorlist.txt','r') as f:
    data = f.read().strip().split('\n')
    for i in data:
        author.append(i)

"First we have bookkeeping that counts how often each index author occurs"
author1 = 0
author2 = 0
total = 0
huh = []
for i in range(51):
    huh.append(0)

line = ''
with open('data.csv','r') as f:
    data = f.readline()
    data = f.readline().strip().split(',')
    line = data
    while data != ['']:
        huh[int(data[1])] += 1
        data = f.readline()
        data = data.strip().split(',')

print("Author sample counts by index")
huh = huh[1:]

print(huh)
print("Usage: [index] of author to query, range 1-50, or 'q' to quit")

data = input()
while data != 'q':
    try:
        i = int(data)
        print("{} at index {} has {} recorded samples".format(author[i-1], i, huh[i-1]))
    except:
        print("Usage: [index] of author to query, range 1-50, or 'q' to quit")
    data = input()
