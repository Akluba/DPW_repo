class BacFormula(object):
	def __init__(self):
		
		self.__gender_constant = 0
		
		
		
	def convert_sex(self, sex):
		'''converts sex string from user into gender constant num for BAC calculation'''
		if sex == 'male':
			self.__gender_constant = 0.68
		else:
			self.__gender_constant = 0.55
		



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