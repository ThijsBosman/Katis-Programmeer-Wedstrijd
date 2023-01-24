
def is_doubles(dice0, dice1):
	if(dice0 == dice1 and (dice0 != '*' or dice1 != '*')): return True
	return False

def chance_doubles(dice0, dice1):
	if(dice0 == '*' or dice1 == '*'): return (1, 6)
	return (1, 1)

def is_mia(dice0, dice1):
	if((dice0 == '1' and dice1 == '2') or (dice0 == '1' and dice1 == '2')): return True
	return False

def chance_mia(dice0, dice1):
	if(is_mia(dice0, dice1)): return (1,1)

	if(dice0 == '*' or dice1 == '*'):
		if(dice0 == '*' and dice1 == '*'):
			return (1, 18)

	return (0, 1)



while(1):
	dice_rolls = input()
	if(dice_rolls == '0 0 0 0'): break
	
	dice_rolls = dice_rolls.split(" ")

	
