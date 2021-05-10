import os
import sys

code = """python style_transfer.py --test ../data/data_dir/data_ext.test --output ../temp_dir/data_ext.dev --vocab ../temp_dir/data_dir.vocab --model ../temp_dir/model --load_model true --beam 8"""

assert len(sys.argv) == 3, "Usage: Python train.py [authorpair] [tmpdir]" ;
assert os.path.exists('../data/' + sys.argv[1]), 'Invalid data_dir';
assert os.path.exists('../' + sys.argv[2]), 'Invalid tmp dir';

pair = sys.argv[1]

data_dir = pair
data_ext = pair
temp_dir = sys.argv[2]


with open('.temp.sh','w') as f:
    body = code.replace('temp_dir',temp_dir).replace('data_dir',data_dir).replace('data_ext',data_ext)
    f.write(body)

os.system('bash .temp.sh')
os.system('rm .temp.sh')
