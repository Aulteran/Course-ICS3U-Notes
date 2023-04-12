'''
cursor parking lot [  ][  ][  ][  ]
'''

from random import randint
from typing import List

lines = "----------------------------------"
print ("\n**%s**"%lines)
print ("**       POKEMON: TEXT MANIAC       **")
print ("**%s**\n"%lines)
inventory = ['']
starter_pokemon = [
    'pikachu', 'charmander', 'bulbasaur', 'squirtle'
]
pokeball_count = 5

#setting up the pokemon properties
abilities = {
  'pikachu': {
    'Static': 3, 
		'Volt Tackle':5,
		'Catastropika': 6
  },
  'charmander': {
		'Blaze': 4,
		'Solar Power': 7
  },
  'bulbasaur': {
    'Overgrow': 4,
		'Chlorophyll': 7
  },
  'squirtle': {
    'Torrent': 4,
		'Rain Dish': 6
  },
	'nidoking': {
		'Poison Point': 4,
		'Rivalry': 7
	},
	'vulpix': {
		'Flash Fire': 4,
		'Drought': 6
	},
	'sandshrew': {
		'Sand Veil': 5,
		'Sand Rush': 7
	},
	'graveler': {
		'Rock Head': 4,
		'Sturdy': 6
	},
	'onix': {
		'Rock Head': 6,
		'Sturdy': 8
	},
	'electrode': {
		'soundproof': 4,
		'static': 6
	}
}
evolutions = {
 'pikachu': {
    'Stage1': 'Raichu'
  },
  'charmander': {
    'Stage1': 'Charmeleon',
    'Stage2': 'Charizard'
  },
  'bulbasaur': {
    'Stage1': 'Ivysaur',
    'Stage2': 'Venusaur'
  },
  'squirtle': {
    'Stage1': 'Warturtle',
    'Stage2': 'Blastoise'
  }
}

#input handler experimentation
def getInput(promptMsg: str, errorMsg: str, values: List[str]):
	response = input(promptMsg).lower()
	for value in values:
		if response == value:
			return response
	print(errorMsg)
	return getInput(promptMsg, errorMsg, values)

'''
#abilities testing atm
def abilities(poke):
	for item in abilities[poke]:
		print ("  - %s : %s Damage"%(item, abilities[inventory[1].lower()][item]))
'''
randpoke = ''

def monsterfight():
	print ("There's a monster right there!")
	print ("You can choose to fight it or run past it.\nKeep in mind, running only has a 40% success rate.")
	fightq1 = getInput(
		"Do you choose to FIGHT it, or RUN?\n", "Your response was not valid, please try again", ["fight", "run"]
	)
	if (fightq1 == "run"):
		surv_chance = randint(1,11)
		if (surv_chance == (1 or 2 or 3 or 4)):
			print("You managed to run past the monster alive, your luck is incredible")
			survch1 = True
		else:
			print("You died, next time, try to think it through.")
			survch1 = False
	elif (fightq1 == "fight"):
		fight1poke = getInput("which pokemon do you want to use for this battle?\n", "Your response was not valid, please try again", [inventory[1].lower(), inventory[2].lower(), inventory[3].lower()])
		print (inventory)
		if fight1poke == inventory[1]:
			inventory.pop(1)
		elif fight1poke == inventory[2]:
			inventory.pop(2)
		elif fight1poke == inventory[3]:
			inventory.pop(3)

def prep2():
	print ("\n%s\nWelcome to Preparation Level 2"%lines)
	global randpoke
	rand = randint(0,3)
	if (rand == 1):
		randpoke = "Nidoking"
	elif (rand == 2):
		randpoke = "Sandshrew"
	elif (rand == 3):
		randpoke = "Vulpix"
	# grammar and vowels am i right
	if (
		randpoke[0] == "A" or randpoke[0] == "E" or randpoke[0] == "I" or randpoke[0] == "O" or randpoke[0] == "U"
		):
		print ("Woah! It's an %s."%randpoke)
	else:
		print ("Woah! It's a %s."%randpoke)
	throwball = getInput("Type T to throw a pokeball\n", "You didn't Throw, try again", ["t"])
	if (throwball.lower() == "t"):
		print ("Throwing Pokeball!")
		def prepthrow1():
			rand2 = randint(0,2)
			if (rand2 == 1):
				global pokeball_count
				print ("You caught %s!"%randpoke)
				inventory.append(randpoke)
				pokeball_count -= 1
			else:
				print ("You missed, try again")
				throwball = input("Type T to throw a pokeball\n")
				rand2 = ''
				prepthrow1()
		prepthrow1()
		print ("You've finished all available preparation levels. You are now being moved to the monster fight")

def prep1():
	global randpoke
	rand = randint(0,3)
	if (rand == 1):
		randpoke = "Graveler"
	elif (rand == 2):
		randpoke = "Onix"
	elif (rand == 3):
		randpoke = "Electrode"
	# grammar and vowels am i right
	if (
		randpoke[0] == "A" or randpoke[0] == "E" or randpoke[0] == "I" or randpoke[0] == "O" or randpoke[0] == "U"
		):
		print ("Woah! It's an %s."%randpoke)
	else:
		print ("Woah! It's a %s."%randpoke)
	throwball = getInput("Type T to throw a pokeball\n", "You didn't Throw, try again", ["t"])
	if (throwball.lower() == "t"):
		print ("Throwing Pokeball!")
		def prepthrow1():
			rand3 = randint(0,2)
			if (rand3 == 1):
				global pokeball_count
				print ("You caught %s!"%randpoke)
				inventory.append(randpoke)
				pokeball_count -= 1
			else:
				print ("You missed, try again")
				throwball = input("Type T to throw a pokeball\n")
				rand3 = ''
				prepthrow1()
		prepthrow1()

# check your inventory
def inventory_check():
	print ("\n%s\nYour inventory has:"%lines)
	for item in inventory:
		print (item)

# choose starter pokemon
def choose_starter():
	global pokeball_count
	starter = getInput(
		"What pokemon do you want to begin with?\nYour options are:\n Pikachu\n Charmander\n Bulbasaur\n Squirtle\n", "Your response was not valid, please try again\n\n%s"%lines, ["pikachu", "charmander", "bulbasaur", "squirtle"]
	)
	starter = starter.lower()
	if (starter == 'pikachu'):
		inventory.append("Pikachu")
	elif (starter == 'charmander'):
		inventory.append("Charmander")
	elif (starter == 'bulbasaur'):
		inventory.append('Bulbasaur')
	elif (starter == 'squirtle'):
		inventory.append('Squirtle')
	else:
		print (
			"Your response was not valid, please try again\n\n%s"%lines
		)
		starter = ''
		choose_starter()
	
# starting the game
def bootgame():
	global pokeball_count
	global randpoke
	print (
		"\n%s\nAlright! Lets choose your starter pokemon!\n"%lines
	)
	choose_starter()
	inventory[0] = 'Pokeball - %s'%pokeball_count
	pokeball_count -= 1 
	print ("\nOkay!, you've chosen %s as your starter pokemon."%inventory[1])
	print ("                         -x-                         ")
	print ("%s is equipped with the following abilites:"%inventory[1])
	for item in abilities[inventory[1].lower()]:
		print ("  - %s : %s Damage"%(item, abilities[inventory[1].lower()][item]))
	print ("Make sure to remember these, you can't come back to them later.")
	print ("%s\n\n\n      --   Let's Begin!   --\n\n"%lines)
	#Preparation
	print ("%s\nWelcome to the preparation level!\nHere, you'll catch pokemon to prepare for the monsters ahead.\n"%lines)
	prep1()
	inventory[0] = 'Pokeball - %s'%pokeball_count
	#Prep2 Check
	continueq = getInput("Great, you now have two pokemon. Do you want to continue hunting pokemon or proceed to the monster fight?\nType YES for prep level 2 or NO for monster fight\n", "Your response was not valid, please try again.", ["yes", "no"])
	def prep2check():
		if (continueq.lower() == "yes"):
			prep2()
		elif (continueq.lower() == "no"):
			monsterfight()
	prep2check()
	monsterfight()

# do you want to play function
def initiategame():
	startgame = getInput(
	"Do you want to play?\nType YES to play. if not, type NO\n", "I'm sorry, I didn't understand that, please try again.", ["yes", "no"]
	)
	if (startgame == "yes"):
		bootgame()
	elif (startgame == "no"):
		reinit = getInput("\nThat's ok, if change your mind, type PLAY\n", "I'm sorry, I didn't understand that, please try again.", ["play"])
		if (reinit == "play"):
			bootgame()

# run program
initiategame()
