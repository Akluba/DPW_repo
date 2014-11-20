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
		
		anthony = DataObject()
		anthony._name = 'Anthony Kluba'
		anthony._team = 'FullSail University'
		anthony._at_bats = 3
		anthony._hits = 3
		anthony._strike_outs = 2
		anthony._walks = 4
		anthony._hit_bys 1