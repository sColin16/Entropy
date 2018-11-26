import pandas as pd
import numpy as np
import sys
import pickle

from tqdm import tqdm

#mode = 'analyze'  # Studies an input file and outputs model
#mode = 'create'	   # Outputs words based an a previously created model
mode = 'test'

file_name = 'words3.txt'  # File containing all the words to study
model_name = 'full5.p'    # File where the model is to be/was saved
order = 5		  # The number of previus characters used

words = 100		  # The number of words that the model outputs

# TODO: create two seperate files, accept cml args
# TODO: organize models into folders

# His first word was 'mpasideranllytoprmetionondatongmames'
# hiverd
# telve
# ffrophy
# puaste

# These are order two words
# rocardionate
# supirrustisidente
# inguannetighai

def test():
	print(sys.argv)

def tokenize(word):
	"""Splits a word into it component tokens (mostly letter).
	A 'START' token begins the word 'END' ends the word."""

	tokens = list(word[:-1])  # Strip the \n at the end
	tokens.insert(0, 'START')
	tokens.append('END')

	return tokens

def get_previous(tokenized, index, order):
	"""Returns a string of the previous tokens that come before a
	certain letter in a tokenized word. Used for both making the
	model and generating words"""

	start = max(0, index - order)
	previous_tokens = tokenized[start:index]

	previous_string = ''.join(previous_tokens)

	return previous_string

def make_model_dict(file, order):
	"""Builds a dictionary-based probability model. Significantly
	faster than using a pandas DataFrame"""

	dict = {}

	for line in tqdm(file):
		tokenized = tokenize(line)

		for i in range(len(tokenized) - 1):
			previous = get_previous(tokenized, i + 1, order)
			token = tokenized[i+1]

			if previous not in dict:
				dict[previous] = {}

			if token not in dict[previous]:
				dict[previous][token] = 1

			else:
				dict[previous][token] += 1

	return dict

def save_dict(model, name):
	"""Wrapper to easily save the dictionary model"""

	pickle.dump(model, open(name, 'wb'))

def load_dict(name):
	"""Wrapper to easily retrieve the saved model"""

	return pickle.load(open(name))

def pick_letter(model, previous):
	"""Picks a letter based off the probability distribution"""

	s = pd.Series(model[previous])	# Raw series values
	p = s/s.sum()			# Probability Distribution

	return np.random.choice(p.keys(), p = p.values)

def generate_word(model, order):
	"""Generates an entire word by picking letters until the 'END'
	token is chosen"""

	tokens = ['START']

	while True:
		previous = get_previous(tokens, len(tokens), order)
		letter = pick_letter(model, previous)

		tokens.append(letter)

		if letter == 'END':
			break

	word = ''.join(tokens[1:-1])

	return word

def analyze(input, output, order):
	"""Handles analyzing the input file from the name, and saving it,
	all in a single step"""

	file = open(input)

	model = make_model_dict(file, order)

	save_dict(model, output)

"""Use sys.argv to accept input and output files, order"""
"""Create new program to generate word to output file"""

def create():
	model = load_dict(model_name)

	for i in range(words):
		print(generate_word(model, order))

def main():
	if mode == 'analyze':
		analyze()
	elif mode == 'create':
		create()
	else:
		test()

if __name__ == '__main__':
	main()
