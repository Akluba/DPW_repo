class BacFormula(object):
	def __init__(self):
		#variable to be set by functions
		self.__gender_constant = 0
		self.__standard_drinks = 0
		
	def convert_sex(self, sex):
		'''converts sex string from user into gender constant num for BAC calculation'''
		#gender constant is part of bac equation, the value is determined by sex
		#_gender_constant var will be set by user's sex
		#male is .73
		if sex == 'male':
			self.__gender_constant = 0.73
		else: #female is equal to .66
			self.__gender_constant = 0.66
			
				
	def calc_drinks(self,type,num):
		'''calculates total number of liquid ounces of alcohol consumed'''
		#the following equations determine standard drink dependent on drink type
		#_standard_drink var will be set by user's type of drink
		#standard drink of beer is considered 12oz and is 5% alcohol
		if type == 'beer':
			self.__standard_drinks = float(num) * float(12) * float(.05) 
		elif type == 'wine': #standard drink of wine is considered 5oz and is 12% alcohol
			self.__standard_drinks = float(num) * float(5) * float(.12)
		elif type == 'shot': #standard drink of liquor is considered 1.25oz and is 40% alcohol
			self.__standard_drinks = float(num) * float(1.25) * float(.40)
		
	
	
	def calc_bac(self,weight,hours):
		'''figures out blood alcohol percent using figures from users input'''
		#variables set by functions
		drinks = float(self.__standard_drinks)
		sex = float(self.__gender_constant)
		#variables set from user input passed from mainhandler
		lbs = float(weight)
		time = float(hours)
		#formula used to calculate BAC level with vars inserted
		bac = round((drinks * 5.14) / (lbs * sex) - (.015 * time),3)
		#condition -- if bac is above .08 which is legal limit, return html containing over limit content
		if bac > .08:
			return """
		<h1>According to your BAC results, you are over the legal limit of .08. You need to hop in the nearest cab!</h1>
		<h2>Your BAC is: """  + str(bac) + """</h2>
		<div id="over_limit"></div> """
		else: #bac is below .08, return html containing under limit content
			return """
		<h1>According to your BAC results, you are under the legal limit of .08. Use caution, but you may legally drive home. </h1>
		<h2>Your BAC is: """  + str(bac) + """</h2>
		<div id="under_limit"></div> """
		

#Data Object incharge of storing user data
class UserInfo(object):
	def __init__(self):
		#attributes of user
		self.sex = ""
		self.weight = 0
		self.drink_type = ""
		self.__drink_num = 0
		self.__hours = 0
	
	#getter of self.__drink_num
	@property
	def drink_num(self):
		return self.__drink_num
	#getter of self.__hours	
	@property
	def hours(self):
		return self.__hours
		
	#set __drink_num equal to drink_num from instance in mainhandler
	@drink_num.setter
	def drink_num(self, num):
		self.__drink_num = num
	#set __hours equal to hours from instance in mainhandler
	@hours.setter
	def hours(self, hour):
		self.__hours = hour