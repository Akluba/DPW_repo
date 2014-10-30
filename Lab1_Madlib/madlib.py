'''
Anthony Kluba
DPW1411
Madlib
'''

# Opening message to be printed
print "Welcome to the python Madlib, please provide answers to the following questions:"

# Collecting string inputs from user
hero_name = raw_input("Please choose one of these super heroes! Batman, Superman, or Spiderman ")
city_name = raw_input("Enter a city name ")
verb = raw_input("Enter a verb (-ing form!) ")
# Collecting number inputs from user
countdown_number = raw_input("Enter a number between 1-10 ")
height_number = raw_input("Now a number between 1-100 ")
attack_number = raw_input("A number between 1-3 ")
attack2_number = raw_input("And finally, another number between 1-3 ")

# Variable dependant on countdown_number
patience_level = ''

# Array containing different attacks possible
attack_area = ["head","stomach","butt"]
attack_type = ["chops", "punches", "kicks"]

# Dictionary referencing villian to chosen super hero
villians = dict()
villians = {"Batman":"Bane","Superman":"General Zod","Spiderman":"Green Goblin"}

# Mathematical operation 1 - Converting user input number into feet
feet = int(height_number) / 12
# Mathematical operation 2 - Converting user input number into inches
inches = int(height_number) % 12

# Function determining amount of damange done with attack combo
def attack_points(p1, p2):
	''' Returns a value based on the combination of attack_area and attack_type selected by input'''
	attack_sum = int(p1) + int(p2)
	print attack_sum
	if attack_sum == 6:
		return 100
	elif attack_sum == 5:
		return 85
	elif attack_sum == 4:
		return 65
	elif attack_sum == 3:
		return 45
	else:
		return 25

# Calling function	
damage_done = attack_points(attack_number, attack2_number)

# Condition Statement 1 - discribing villian patience level
if int(countdown_number) > 8:
	patience_level = "tolerantly"
elif int(countdown_number) > 5:
	patience_level = "anxiously"
else:
	patience_level = "eagerly"

# Madlib Section containing -- hero_name , city_name , verb , villian name(dictionary) , countdown_number 
print "Today started out like any normal day in " + city_name + ". All around are cars driving, birds chirping, children " + verb + ", WAIT! WHAT'S THAT?! It's " + villians[hero_name] + ", standing " + str(feet) + " feet " + str(inches) + " inches tall! He demands " + hero_name + " to show his face in " + countdown_number + " seconds and begins to " + patience_level + " count down." 

# Madlib Section containing --  loop
i = int(countdown_number)
while i > 0:
	# Condition Statement 2 - if villian's patience level is either he adds mississippi to the count down
	if patience_level == "tolerantly" or patience_level == "anxiously":
		print i, " Mississippi.."
	else:
		print i
	i = i-1
	
# Madlib Section containing -- hero_name , villian name(dictionary) , attacks(array)
print "Out of nowhere " + hero_name + " shows up, " + attack_type[int(attack_number)-1] + " " + villians[hero_name] + " in the " + attack_area[int(attack2_number)-1] + " for a total damage amount of " + str(damage_done) + " points!"
