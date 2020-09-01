# https://github.com/JackFurby/trie/blob/master/trie.py
import glob
import errno
import pickle


class Node:
	"""Node object for trie."""

	# children contains links to other nodes
	# data contains word if node is the end of a word
	# end indicates if the current node is the end of a word
	def __init__(self, end=False, data=None):
		"""Initilise the node."""
		self.end = end
		self.data = data
		self.children = dict()
		self.wordNum = 0


class Trie:
	"""Trie data structure."""

	def __init__(self):
		"""Initilise the trie."""
		self.head = Node()

	def addWord(self, word):
		"""Add a word to the trie."""
		currentNode = self.head

		for i in range(len(word)):
			# if letter already exists in children move to the node
			if word[i] in currentNode.children:
				currentNode = currentNode.children[word[i]]
				currentNode.wordNum += 1
				# if letter is then end of word being added update node to show this
				if i == len(word) - 1:
					currentNode.end = True
			# if letter is not in children add it
			else:
				if i < len(word) - 1:
					currentNode.children[word[i]] = Node(False, word[0:i + 1])
				else:
					currentNode.children[word[i]] = Node(True, word)
				currentNode = currentNode.children[word[i]]
			currentNode.wordNum += 1

	def hasWord(self, word):
		"""If the trie has the word being searched for return true."""
		if word == '' or word is None:
			return False

		currentNode = self.head
		for letter in word:
			if letter in currentNode.children:
				currentNode = currentNode.children[letter]
			else:
				return False

		# if final node marks the end of a word return true
		if currentNode.end is False:
			return False
		else:
			return True

	def getChildWordNums(self, node=None):
		"""Given a node this will return all child nodes with word counts"""
		allChildren = []
		for i in node.children:
			nextNode = node.children.get(i)
			allChildren.append([nextNode.data, nextNode.wordNum])
		allChildren.sort(key=lambda x: -x[1])
		return allChildren

	def prefix(self, prefix, currentNode=None):
		"""Given a list of letters find all words that can be made begining with a string."""
		if currentNode is None:
			currentNode = self.head

		# Apply prefix to search
		for char in prefix:
			currentNode = currentNode.children[char]

		# move over to regular wordSearch (with prefix in place)
		return self.getChildWordNums(currentNode)


def setup(trie, path):
	"""Add each word from a txt file to trie data structure."""
	files = glob.glob(path)
	for name in files:
		try:
			f = open(name, "r").read().splitlines()
			lines = list(f)
			print(len(lines), 'total words')
			for word in lines:
				# make sure word is in lowercase
				word = word.lower()
				trie.addWord(word)
		except IOError as exc:
			if exc.errno != errno.EISDIR:
				raise


def save_trie(trie, name):
	"""Save a trie to a file."""
	with open('./words/' + name + '.pkl', 'wb') as f:
		pickle.dump(trie, f, pickle.HIGHEST_PROTOCOL)


def load_trie(name):
	"""Load a trie from a file."""
	with open('./words/' + name + '.pkl', 'rb') as f:
		return pickle.load(f)
