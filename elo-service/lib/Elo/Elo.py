from __future__ import division
from elo import rate_1vs1
		

class Elo:
	"""docstring for Elo"""
	def __init__(self, player, word, win):
		self.player = player
		self.word = word
		self.win = win

	def elo(self):
		if self.win == 1:
			print 'one'
			print rate_1vs1(self.player, self.word)
			return rate_1vs1(self.player, self.word)
		elif self.win == 0:
			print 'zero'
			print rate_1vs1(self.word, self.player)
			return rate_1vs1(self.word, self.player)
