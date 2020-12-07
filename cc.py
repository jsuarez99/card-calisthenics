from Deck import Deck
from datetime import datetime
import math

#----------------------------------------------
#For simplicity, this "e"xercise toggle is True for squats, false for pushups
eToggle = True

#Dictionary for counts of each exercise
exCounts = { 'sit-ups' : 0,
	'squats' : 0,
	'push-ups' : 0,
	'burpees' : 0
	}

def getExercise(card):
	global exCounts
	cardNumVal = card.getFaceNum()

	if card.getFace() in ['Joker', 'Ace']:
		print('25 sit-ups...GO!')
		exCounts['sit-ups'] += 25
		
	elif card.getFaceNum() > 5:
		global eToggle
		exName = "squats" if eToggle else "push-ups"
		print(f'{cardNumVal} {exName}...GO!')
		exCounts[exName] += cardNumVal
		eToggle = not eToggle
		
	elif cardNumVal >= 2 and cardNumVal <=5:
		print(f'{cardNumVal} burpees...GO!')
		exCounts['burpees'] += cardNumVal

#---------------------------------------------
# Get a brand new shuffled deck with jokers
deck = Deck(jokers=True)

#---------------------------------------------
# Begin the workout
print("Welcome to Card Deck Calisthenics!")
print("The card deck is shuffled and ready to go!")
print("Your first card is:")
startTime = 0
endTime = 0

while not deck.isEmpty():
	c = deck.drawCard()
	print(f'{c}, card {len(deck.drawn)} of {deck.deckSize}')
	getExercise(c)
	
	if startTime == 0:
		startTime = datetime.today()

	if not deck.isEmpty():
		usrInput = input('Press enter to get the next card:')
	else:
		usrInput = input('Last one! Press enter end workout:')
		endTime = datetime.today()
		totalTimeSec = (endTime-startTime).total_seconds()
		
		minutes = totalTimeSec // 60
		totalTimeSec %= 60
		
		print( f'{math.trunc(minutes)}:{math.trunc(totalTimeSec)}' )
		print('Workout complete! Good job!')
		for k,v in exCounts.items():
			print(k, ': ', v)