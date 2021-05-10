from nltk import translate
import sys

assert len(sys.argv) == 3, "Usage: python get_bleu.py [target corpus] [transferred data]";


ref1 = sys.argv[1]
trans1 = sys.argv[2]

ref1 = open(ref1,'r').read().strip().split('\n')
for i in range(len(ref1)):
    ref1[i] = ref1[i].split(' ')

trans1 = open(trans1,'r').read().strip().split('\n')
for i in range(len(trans1)):
    trans1[i] = trans1[i].split(' ')

ref = ref1
trans = trans1
bleu = translate.bleu_score.corpus_bleu(ref, trans, weights=(0.5,0.3,0.2,0), smoothing_function=translate.bleu_score.SmoothingFunction().method4)
#Sparsity of 4-grams requires smoothing and shifted weighing
print("BLEU {}".format(bleu))
