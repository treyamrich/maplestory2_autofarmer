import Keys as Key 

def Farm():
#From the your house
	Key.Wait(3)
	Key.upLeft(0.225)
	Key.upRight(0.6)
#First row
	for i in range(11):
		
		if i == 0:
			for j in range(100):
				Key.Spacebar(0.75)
		else:
			for j in range(20):
				Key.Spacebar(0.75)

		Key.upRight(0.825)
#End of the row
	for i in range(20):
		Key.Spacebar(0.75)
#To next row
	Key.upLeft(0.825)
#Second row
	for i in range(6):
		for j in range(25):
			Key.Spacebar(0.75)

		Key.downLeft(0.825)
#End of second row
	for i in range(25):
		Key.Spacebar(0.75)