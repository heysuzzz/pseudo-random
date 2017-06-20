#! /usr/bin/env python3

from collections import Counter
import random
import argparse

class TextCreator(object):
	def __init__(self, text):

		self.text = text
		self.word_indexes = [(i, word) for i, word in enumerate(text)]
		self.unique_words = []
		for word in text:
			if word not in self.unique_words:
				self.unique_words.append(word)

	def get_following_word(self, target_word):
		# gets the indexes of all words following the target word
		following_indexes = []
		for i, word in self.word_indexes:
			if word == target_word:
				following_indexes.append(i + 1)

		# gets words associated with the indexes
		following_words = []		
		for (i, word) in self.word_indexes:
			if i in following_indexes:
				following_words.append(word)

		# returns a random word, following the actual distribution of following words
		return random.choice(following_words)

	def get_random_string(self, seed, length=100):
		count = 0
		words = []
		while count < length:
			new_word = self.get_following_word(seed)
			seed = new_word
			words.append(new_word)
			count += 1

		return words


if __name__ == '__main__':
	
	parser = argparse.ArgumentParser(description='generate pseudo-random text')
	parser.add_argument('-i', '--input', help='input text file',type=str, required=True)
	parser.add_argument('-o', '--output', help='output text file', type=str, required=True)
	args = parser.parse_args()

	# reads the text file from the terminal
	in_list = []
	with open(args.input) as f:
		for line in f:
			for word in line.split():
				in_list.append(word)

	my_text = TextCreator(in_list)

	new_list = my_text.get_random_string('city', length=250)

	# writes to the provided text file
	with open(args.output, 'w') as o:
		for word in new_list:
			o.write(word)
			o.write(' ')