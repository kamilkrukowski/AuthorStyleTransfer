#!/bin/bash
A="2-11"
python style_transfer.py --train ../data/$A/2-11.train --dev ../data/$A/2-11.dev --output ../tmp2/2-11.dev --vocab ../tmp2/2-11.vocab --model ../tmp2/model
