class Card:
	suiteNames = {'C' : 'Clubs' , 
		'S' : 'Spades', 
		'D' : 'Diamonds', 
		'H' : 'Hearts'}
	valMap = { 1 : 'Ace',
		11 : 'Jack',
		12 : 'Queen',
		13 : 'King' }

	def __init__(self, suite, numValue = None):	
		self.suite = suite
		
		if suite == 'Joker':
			self.numValue = 0
		else:
			self.numValue = numValue
		
	def getFace(self):
		if self.suite == 'Joker':
			return self.suite
		else:
			return self.valMap[self.numValue] \
				if self.numValue in self.valMap.keys() \
				else self.numValue
			
	def getFaceNum(self):
		return self.numValue
			
	def getSuite(self):
		if self.suite != 'Joker':
			return self.suiteNames[self.suite]
		else:
			return self.suite
		
	def __str__(self):
		suiteName = self.getSuite()
		faceVal = self.getFace()
		
		if suiteName == 'Joker':
			return 'Joker'
		else:
			return f'{faceVal} of {suiteName}'