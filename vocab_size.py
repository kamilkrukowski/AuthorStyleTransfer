import sys

assert len(sys.argv) > 1, "Usage: python vocab_size.py [path]";

path = sys.argv[1]
words = open(path,'r').read().replace('\n',' ')
vocab = set(words.split(' '))

if len(sys.argv) == 1:
    print(len(vocab))
else:
    path = sys.argv[2]
    words = open(path,'r').read().replace('\n',' ')
    vocab2 = set(words.split(' '))

    print(len(set(list(vocab) + list(vocab2))))
