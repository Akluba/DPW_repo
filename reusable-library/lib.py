#Data Object incharge of storing user data
class UserInfo(object):
	def __init__(self):
		#attributes of user
		self.sex = ""
		self.__weight = 0
		self.drink_type = ""
		self.__drink_num = 0
		self.__hours = 0