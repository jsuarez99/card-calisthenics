from Deck import Deck

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

while not deck.isEmpty():
	c = deck.drawCard()
	print(c)
	getExercise(c)

	if not deck.isEmpty():
		usrInput = input('Press enter to get the next card:')
	else:
		print('Workout complete! Good job!')
		for k,v in exCounts.items():
			print(k, ': ', v)