player1 = input('Player 1 Pick rock/paper/scissors: ')
player2 = input('Player 2 Also pick rock/paper/scissors: ')

def compare(p1,p2):
	if p1 == p2:
		return("It's a tie")
	elif p1 == 'rock':
		if p2 == 'scissors':
			return('rock wins')
		else:
			return('paper wins')
	elif p1 == 'scissors':
		if p2 == 'paper':
			return('scissors wins')
		else:
			return('rock wins')
	elif p1 == 'paper':
		if p2 == 'rock':
			return('paper wins')
		else:
			return('scissors wins')
	else: 
		return('Invalid input')
	
print(compare(player1, player2))
