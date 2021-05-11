# Author Style Transfer

The method learns to perform style transfer between two non-parallel corpora. For example, given positive and negative reviews as two corpora, the model can learn to reverse the sentiment of a sentence.

## Dependencies
Python 2.7, TensorFlow 1.3.0, ipdb, ntlk

## Quick Start
baldwin.txt contains baldin corpus  
transferred\_to\_harte contains results of transferring baldwin.txt to Harte's style.  
  
To create dataset, "cd data"  
Use "python onevone.py [indexa] [indexb]" to create one vs one dataset.  
ex: "python onevone.py 8 26" Baldwin vs Harte  
Use "python query\_author.py" to lookup author indices.  
Use "python onevmany.py [indexa]" to create one vs many author dataset.  
ex: "python onevmany.py 8" Baldwin vs Many  
  
To train model, create some temporary directory "mkdir temp"  
Move to code directory, "cd code"  
Use "python train.py [data\_dir] [temp\_dir\_path]" ie "python train.py 8-26 temp"  
Some dev.epoch files should contain transferred content in temp dir as the model continually trains.  
  
## Note on Usage
Computational resources used: 128g GPU w/ 4 Cuda Threads.
Many thanks to Tufts HPC for providing the computational resources required.
Training required ~14 hours per model.

## References
This repo contains the code and data of the following paper:

<i> "Style Transfer from Non-Parallel Text by Cross-Alignment". Tianxiao Shen, Tao Lei, Regina Barzilay, and Tommi Jaakkola. NIPS 2017. [arXiv](https://arxiv.org/abs/1705.09655)</i>

This repo makes use of the victorian authorship dataset from the following:

<i> Gungor, A. (2018). Fifty Victorian Era Novelists Authorship Attribution Data. Purdue Universitym Master Thesis. http://dx.doi.org/10.7912/D2N65J</i>

