import Keys as Key 

def Mine():

	def mineLoop():
		pass
		for i in range(15):
			Key.Spacebar(0.75)

	def Copper():
		Key.upLeft(0.8)
		Key.upRight(4.3)
		Key.downRight(0.2)
		mineLoop()

	def Tin():
		Copper()
		Key.upLeft(0.6)
		Key.upRight(2.1)
		Key.downRight(0.2)
		mineLoop()

	def Zinc():
		Tin()
		Key.upLeft(0.2)
		Key.upRight(2.4)
		Key.downRight(1)
		Key.upRight(1.7)
		mineLoop()

	def Silver():
		Zinc()
		Key.Down(0.6)
		Key.downRight(0.4)
		Key.upRight(1.7)
		Key.upLeft(3.3)
		Key.upRight(1.6)
		mineLoop()

	def Iron():
		Silver()
		Key.downLeft(1.2)
		Key.upLeft(3.4)
		Key.upRight(1.6)
		mineLoop()

	def Lead():
		Iron()
		Key.downLeft(0.2)
		Key.upLeft(2)
		Key.jumpUpLeft(0.2)
		Key.upLeft(1.6)
		Key.downLeft(0.2)
		mineLoop()

	def Ravensteel():
		Lead()
		Key.upRight(0.2)
		Key.upLeft(1.5)
		Key.upRight(1.4)
		Key.jumpUpRight(0.2)
		Key.upRight(1)
		Key.jumpUpRight(0.2)
		Key.upRight(0.4)
		Key.downRight(0.6)
		mineLoop()

	def Nickel():
		Ravensteel()
		Key.downLeft(0.2)
		Key.upLeft(0.6)
		Key.downLeft(3.4)
		Key.jumpDownLeft(0.2)
		Key.downLeft(0.4)
		Key.downRight(0.4)
		Key.Down(1)
		Key.downLeft(0.6)
		mineLoop()

	def Tungsten():
		Nickel()
		Key.Down(0.4)
		Key.downLeft(1.2)
		Key.upLeft(4.2)
		Key.upRight(0.6)
		#mineLoop()Uncomment when you are level 9

	def Gold():
		Tungsten()
		Key.upLeft(1.2)
		Key.jumpUpLeft(0.2)
		Key.upLeft(1.2)
		Key.upRight(0.4)
		#mineLoop() Uncomment when you are level 10

	def Platinum():
		Gold()
		Key.Up(2)
		Key.upRight(0.6)
		Key.jumpUpRight(0.2)
		Key.upRight(5.4)
		Key.downRight(0.2)
		#mineLoop() Uncomment when you are level 11

	def Cobalt():
		Platinum()
		Key.downRight(2.9)
		Key.upRight(0.9)
		#mineLoop() Uncomment when you are level 12

	def Palladium():
		Cobalt()
		Key.downRight(2.5)
		Key.upRight(1)
		Key.downRight(1.2)
		Key.downLeft(0.2)
		#mineLoop() Uncomment when you are level 13

	def backToPortal():

		Key.upRight(0.2)
		Key.upLeft(1.2)
		Key.downLeft(1.8)
		Key.upLeft(5.7)
		Key.downLeft(4.6)
		Key.downRight(2.4)
		Key.downLeft(4)
		Key.downRight(7.6)
		Key.Down(2)
		Key.downRight(3.5)
		Key.Down(2)
		Key.downLeft(2.1)
		Key.Down(0.9)
		Key.downLeft(3.6)
		Key.downRight(1.6)
		Key.downLeft(0.4)

#From Berg Island
	Key.Wait(3)
	Key.Up(0.6)
	Palladium()
	backToPortal()