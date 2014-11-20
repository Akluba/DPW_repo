#DataObject is a superclass acting as template
class DataObject(object):
	def __init__(self):
		#attributes of baseball player
		self._name = ''
		self._team = ''
		self._at_bats = 0
		self._hits = 0
		self._strike_outs = 0
		self._walks = 0
		self._hit_bys 0
		
#Data subclass of DataObject		
class Data(DataObject):
	def __init__(self):
		#init as subclass of DataObject superclass
		super(Data, self).__init__()