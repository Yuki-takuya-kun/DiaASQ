import json
from attrdict import AttrDict
import yaml
from pprint import pprint
# from src.preprocess import Preprocessor
from transformers import BertTokenizer
data_path = 'data/dataset/jsons_zh/train.json'
with open(data_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

lengths = []
for i, elem in enumerate(data):
    pprint(elem['sentences'],width=150)
    
    pprint(elem['triplets'])
    print('-'*50+'\n')
    pprint(elem['replies'])
    pprint(elem['speakers'])
    #print(list(elem.keys()))
    input()
    print('\n' + '='*100 + '\n')
    #lengths.append((el#print(max(lengths, key = lambda x:x[1]))




