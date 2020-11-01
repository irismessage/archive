#imports, duh
import random
import functools


#Entity parent class with general functionality
class Character(object):
  #Defaults
  #The Nameless One
  name = None
  damage = 20
  damage_mod = 1
  health = 100
  health_max = 100
  
  #Initialistion - defaults are too complicated
  #Why do the examples have those at the start
  def __init__(self, name, damage, damage_mod, health, health_max):
    self.name = name
    self.damage = damage
    self.damage_modifier = damage_mod
    self.health = health
    self.health_max = health_max
  
  #Attack method
  def attack(self, target):
    #I like to use exclamation marks everywhere
    print(self.name + " attacks " + target.name + "!")
   
    #Determine damage with modifier
    damage_output = self.damage*self.damage_mod
    #Call target's take damage method
    target.defend(damage_output)
    #Reset damage modifier
    self.damage_mod = 1
    
  #Method to take damage, pretty simple
  #Check for death is in children classes
  def defend(self, damage):
    self.health -= damage
    print(self.name + " takes " + str(damage) + " damage!")
  
  #Method to add health
  def heal(self, amount):
    print(self.name + " regains " + str(amount) + " health!")
    #Don't let it overflow
    if (self.health + amount) >= self.health_max:
      self.health = self.health_max
      print(self.name + "'s health is full!")
    else:
      self.health += amount
      
  #Commit die
  def die(self):
    #This is overridden
    print(name + " died!")

    
class Hero(Character):
  #For hero damage is high
  name = "Player"
  damage = 25
  #First hit is three times for fun
  damage_mod = 3
  #Health starts a bit low, why not
  health = 95
  health_max = 100
  #Potions is passed as an int
  potions = 1
  
  #List of potion objects also initialised
  def __init__(self, name, damage, damage_mod, health, health_max, potions):
    super(Hero, self).__init__(name, damage, damage_mod, health, health_max)
    
    self.potions = [Potion("George's Marvellous Medicine", 5) for i in range(potions)]
    
  #The hero can use items
  def use_from(self, items, target):
    #Check the list isn't empty
    if not items:
      print("You have none left!")
    #Pop and item and pop the item
    else:
      item = items.pop()
      print(self.name + " uses " + item.name + "!")
      item.use(target)
     
  #Defend is overridden with player health check
  #Might be better way to do this like death health floor?
  #I'm tied and these classes have enough attritubes already
  def defend(self, damage):
    super(Hero, self).defend(damage)
    
    if self.health <= 0:
      self.die()
  
  #Death line for player, then quit
  def die(self):
    print("You died!")
    print("Score: " + str(score))
    quit()
  
  
class Monster(Character):
  #Monster does low damage
  name = "Enemy"
  damage = 5
  damage_mod = 1
  #Their health starts at a three hit kill
  health = 75
  health_max = 100
  
  #Only default inits
  def __init__(self, name, damage, damage_mod, health, health_max):
    super(Monster, self).__init__(name, damage, damage_mod, health, health_max)
    
  #The monster can roar
  #I decided this could double their next hit
  #(After I said it wasn't very effective)
  #(I guess no one uses moves like this in pokemon so)
  def roar(self):
    print(self.name + " roars! It isn't very effective.")
    print(self.name + " will do double damage for the next turn.")
    self.damage_mod = 2
    
  #Again, death check added in inherit
  #Monsters run away at 1 health according to brief
  def defend(self, damage):
    super(Monster, self).defend(damage)
    
    if self.health <= 1:
      self.die()
    
  #It's "fainting" not "death" timmy
  def die(self):
    print(self.name + " 'runs away'!")
    score += 1
    del self
  
  

#Class for a potion
class Potion():
  name = "Potion"
  #I don't like this variable name
  #Amount potion heals
  #It's really underpowered in the brief
  amount = 5
  
  def __init__(self, name, amount):
    self.name = name
    self.amount = amount
  
  #Call heal method on user
  def use(self, user):
    user.heal(self.amount)
    
    

#Functions for options for player
def player_attack():
  hero.attack(monster)
def potion():
  hero.use_from(hero.potions, hero)
def die():
  hero.die()
  
player_options = {"attack": player_attack, "potion": potion, "die": die}


#Fuctions for npc options
#Also add suicide
def npc_attack():
  monster.attack(hero)
def roar():
  monster.roar()
def suicide():
  print(monster.name + " realises this is all futile and ceases to exist!")
  monster.die()
  
npc_options = {69: npc_attack, 30: roar, 1: suicide}
#Function to pick option with weights
def npc_choose(options):
  total = sum(npc_options.keys())
  selection = random.randint(0, total)
  
  running = 0
  for item in npc_options.items():
    running += item[0]
    if running >= selection:
      return item[1]


#Instantiate hero object
hero = Hero("Player", 25, 3, 95, 100, 1)
monster = None
score = 0
#Game loop
while True:
  #If there's not a monster, make one
  #No random values or monster types yet
  #But I need to go to bed
  if monster == None:
    monster = Monster("Enemy", 5, 1, 75, 100)
    print("A(n) " + monster.name + " appears!")
    
  #Monster does thing    
  npc_choose(npc_options)()
    
  #Player does thing
  #Get input with flag while loop
  successful_input = False
  while not successful_input:
    choice = raw_input("\n What do you want to do? ").lower()
    #Run option
    #When I made a text based adventure game ages ago I had a huge elif block
    #and some war crimes with eval()
    #Good times
    if choice in player_options.keys():
      player_options[choice]()
      successful_input = True
    #Otherwise print options and loop
    else:
      print("The options are: " + "; ".join(player_options.keys()))

      

#Le fin
#Saving broke right as I was about to test it
#Weird
#Might be to do with copy-pasting from and to a local backup I made
#Or special characters
