import Keys as Key 

def Forage():

	def forageLoop():
		pass
		for i in range(15):
			Key.Spacebar(0.75)

	def Marjorjam():

		Key.upLeft(1.6)
		Key.upRight(5.1)
		Key.downRight(1)
		forageLoop()

	def Lavender():

		Marjorjam()
		Key.upLeft(1.8)
		Key.upRight(5.3)
		Key.upLeft(0.2)
		forageLoop()

	def Rosemary():

		Lavender()
		Key.downLeft(1)
		Key.upLeft(2.1)
		Key.upRight(1.4)
		forageLoop()

	def Mandarin():

		Rosemary()
		Key.Left(2.3)
		Key.downLeft(1.6)
		forageLoop()

	def lemonBalm():

		Mandarin()
		Key.Up(3)
		Key.upLeft(1.2)
		forageLoop()
	
	def Jasmine():

		lemonBalm()
		Key.Down(1.15)
		Key.downLeft(6.15)
		forageLoop()

	def teaTree():

		Jasmine()
		Key.upRight(1.2)
		Key.upLeft(2)
		Key.upRight(1.2)
		forageLoop()

	def cherrySage():

		teaTree()
		Key.Down(0.6)
		Key.Left(2.3)
		Key.downLeft(1.2)
		forageLoop()

	def Patchouli():

		cherrySage()
		Key.upRight(2)
		Key.upLeft(2.4)
		Key.Up(0.6)
		#forageLoop()

	def Oregano():

		Patchouli()
		Key.upLeft(1.8)
		Key.jumpUpLeft(0.2)
		Key.upLeft(0.8)
		Key.Up(0.6)
		#forageLoop()

	def Yarrow():

		Oregano()
		Key.Up(0.6)
		Key.Right(3.5)
		Key.downRight(0.4)
		#forageLoop()

	def Basil():

		Yarrow()
		Key.upRight(4.1)
		Key.Up(0.6)
		#forageLoop()

	def Bergamot():

		Basil()
		Key.Left(0.6)
		Key.downLeft(2.9)
		Key.upLeft(2.5)
		Key.jumpUpLeft(0.2)
		Key.upLeft(0.8)
		Key.downLeft(0.4)
		#forageLoop()

	Bergamot()
