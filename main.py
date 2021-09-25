from os import system as sys
import Miner
import Farmer
import Forager
import Trans
 
shut = False

def AutoDaily():

	print("Welcome to the MS2 auto-mining bot.")
	print("Warning! This program is imperfect.")
	print("To use this program you must run it from your house in MS2.")
	print("Would you like to shutdown the computer after the bot is done?")
	while True:
		global shut
		shutDown = input()
		shutDown = str.lower(shutDown)

		if shutDown == 'yes':
			shut = True
			break
		elif shutDown == 'no':
			break
		else:
			print("You didn't say yes or no")

	print("The bot will start 3 seconds after you type \"start\"")
	
	while True:
		isStart = input()
		isStart = str.lower(isStart)
		if isStart == 'start':
			break
		else:
			print("You didn't type START")

	Miner.Mine()
	Trans.Transition1()
	Forager.Forage()
	Trans.Transition2()
	Farmer.Farm()

if __name__ == '__main__':
	AutoDaily()
	if shut == True:
		sys("shutdown -s -f -t 00")
	