"""Trie."""
import time
from trie import Trie, Node, setup, save_trie, load_trie
import sys

trie = Trie()
setup(trie, "./nounList.txt")

# Runs until user exit
while True:
	"""Welcome to the kontakt helper"""
	print()
	action = input("What do you want to do? Enter 'help' for more: ")

	if action == "\q":
		sys.exit()
	elif action == "isNoun":
		inputLetters = input("Enter a word to check: ")

		# Makes sure input is in lower case
		inputLetters = inputLetters.lower()

		if trie.hasWord(inputLetters):
			print("Yes")
		else:
			print("No")
	elif action == "whatsNext":
		prefixLetters = input("Enter prefix (in order): ").lower()
		start = time.time()
		wordList = trie.prefix(prefixLetters)
		for i in range(len(wordList)):
			if i < 5:
				print("Prefix:", wordList[i][0], ", Number of words:", wordList[i][1])
		end = time.time()
		print("Completed search in", end - start, 'seconds')

	elif action == "help":
		print("")
		print("=== Kontakt word game help ===")
		print("")
		print("\q			-	Exit Kontakt helpers")
		print("isNoun			-	Returns Yes if a given word is a noun")
		print("whatsNext		-	Returns the top 5 word prefixes when given a shorter prefix")
		print("")
	else:
		print("Input not recognised")
