from Card import Card
import random

class Deck:	
	def __init__(self, jokers = False):
		self.deck = []
		self.drawn = []  #cards drawn will go here
		for i in range(1,14):
			for s in ['C','S','H','D']:
				self.deck.append(Card(s,i))
				
		if jokers:
			self.deck.append(Card('Joker'))
			self.deck.append(Card('Joker'))

		self.shuffle(10)
	
	
	def drawCard(self, number = 1):
		if len(self.deck) > 0:
			currentCard = self.deck.pop()
			self.drawn.append(currentCard)
			return currentCard
		else:
			return None


	def isEmpty(self):
		return len(self.deck) == 0


	def shuffle(self, num = 1):
		for i in range(0,num):
			random.shuffle(self.deck)