from wordgen import load_dict
from math import log

import pandas as pd

d = load_dict('full0.p')

p = pd.Series(d[''])

p = p/p.sum()

entropy = 0

for value in p.values:
	entropy -= value * log(value, 2)

print(entropy)
