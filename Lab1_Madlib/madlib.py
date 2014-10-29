# One conditional statements w/ logical operator
# At least one function


# Opening message to be printed
print "Welcome to the python Madlib, please provide answers to the following questions:"

# Collecting string inputs from user
hero_name = raw_input("Please choose one of these super heroes! Batman, Superman, or Spiderman ")
city_name = raw_input("Enter a city name ")
verb = raw_input("Enter a verb (-ing form!) ")
# Collecting number inputs from user
countdown_number = raw_input("Enter a number between 1-10 ")
height_number = raw_input("Now a number between 1-100 ")
attack_number = raw_input("And finally, a number between 1-3 ")

# Variable dependant on countdown_number
patience_level = ''

# Array containing different attacks possible
attacks = ["head","stomach","butt"]

# Dictionary referencing villian to chosen super hero
villians = dict()
villians = {"Batman":"Bane","Superman":"General Zod","Spiderman":"Green Goblin"}

# Mathematical operation 1 - Converting user input number into feet
feet = int(height_number) / 12
# Mathematical operation 2 - Converting user input number into inches
inches = int(height_number) % 12

# Condition Statement 1 - discribing villian patience level
if int(countdown_number) > 8:
	patience_level = "tolerantly"
elif int(countdown_number) > 5:
	patience_level = "anxiously"
else:
	patience_level = "eagerly"

 

# Madlib Section containing -- 
print "Today started out like any normal day in " + city_name + ". All around are cars driving, birds chirping, children " + verb + ", WAIT! WHAT'S THAT?!"


# Madlib Section containing -- 


# Madlib Section containing --  loop
print "He repeated himself, here"
# Loop to repeat superhero's name
i = 0
while i < int(attack_number):
	print hero_name + ","
	i = i+1
print "in an evil voice."

