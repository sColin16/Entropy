import sys

from wordgen import make_model_dict, save_dict

def capture_args():
	"""Captures the command line input arguments"""

	# TODO: validate, and give directions

	input = sys.argv[1]
	output = sys.argv[2]
	order = int(sys.argv[3])

	return (input, output, order)

def main():
	"""Handles primary functions of analyzing"""

	# TODO: validate that input file exists
	# TODO: confirm an overwrite of output file (wordgen?)

	input, output, order = capture_args()

	file = open(input)

	model = make_model_dict(file, order)

	save_dict(model, output)

if __name__ == '__main__':
	main()
