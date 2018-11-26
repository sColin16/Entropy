from wordgen import load_dict
from math import log

import pandas as pd
from tqdm import tqdm

from sys import argv

dict = load_dict(argv[1])

df = pd.DataFrame(dict)
df = df.fillna(0)

total = df.sum().sum()

entropy = 0

for key in tqdm(df.keys()):
	row_entropy = 0
	p = df[key]
	p = p/p.sum()

	for value in p.values:
		if value != 0:
			row_entropy -= value * log(value, 2)

	entropy += (df[key].sum()/total) * row_entropy

print(entropy)
