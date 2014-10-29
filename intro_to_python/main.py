first_name = "Anthony"
last_name = "Kluba"

print first_name + ' ' + last_name

# response = raw_input("Enter your name ")
# print "Hello ", response

birth_year = 1991
current_year = 2014
age = current_year - birth_year
#print age
#print "You are " + str(age) + " years old"

budget = 90

if budget > 100:
	brand = "nike"
	print "You can buy " + brand + " shoes."
elif budget > 70:
	#print "better head to Wal-Mart"
	pass
else:
	#print "No can't buy shoes"
	pass
	
characters = ['Anthony', 'Sammi', 'Jamie']
characters.append('Steve')
#print characters[3]

movies = dict()
movies = {"StarWars":"Luke","Hangover":"Allen"}
#print movies["StarWars"]

'''
i = 0
while i<9:
	print "The count is", i
	i = i+1
'''
'''
for i in range(0,10):
	print "The count is", i
	i = i+1
'''

rappers = ["bigdog", "hommieG", "capYa"]
for r in rappers:
	#print r
	pass
	
def calc_area(h, w):
	area = h * w
	#print area
	return area
	
a = calc_area(20,40);
#print "The area is " + str(a) + "sqFt"

weight = 180
height = 71
message = '''
'''


