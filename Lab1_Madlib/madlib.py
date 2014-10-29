# At least 2 mathematical operators
# Two conditional statements
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

# Array containing different attacks possible
attacks = ["head","stomach","butt"]

# Dictionary referencing villian to chosen super hero
villians = dict()
villians = {"Batman":"Bane","Superman":"General Zod","Spiderman":"Green Goblin"}



 

# Madlib Section containing -- 
print "Today started out like any normal day in " + city_name + ". All around are cars driving, birds chirping, children " + verb + ", WAIT! WHAT'S THAT?!"


# Madlib Section containing --  loop
print "He repeated himself, here"
# Loop to repeat superhero's name
i = 0
while i < int(attack_number):
	print hero_name + ","
	i = i+1
print "in an evil voice."