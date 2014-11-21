#Page class is our superclass
class Page(object):
	def __init__(self):
		#html elements found in head
		self._head = '''<!DOCTYPE HTML>
<html>
	<head>
		<title></title>
	</head>
	<body>'''
		#html elements belong here
		self._body = ''
		#html closing elements
		self._close = '''
	</body>
</html>'''
	#function responsible for returning Page variables
	def print_out(self):
		return self._head + self._body + self._close
		
#ContentPage subclass 		
class ContentPage(Page):
	def __init__(self):
		#init as subclass of our Page superclass
		super(ContentPage, self).__init__()
		#html form tags
		self._form_open = '<form method = "GET">'
		self._form_close = '</form>'
		#array to hold array of href values from mainhandler
		self.__buttons = []
		self._button_link = ''
	
	#getter 
	@property
	def buttons(self):
		pass
	
	#setter takes self.__buttons and sets equal to 
	#value from mainhandler
	@buttons.setter
	def buttons(self, arr):
		self.__buttons = arr
		#loop through each array in arr 
		#concatenate to form links
		for item in arr:
			self._button_link += '<a href="' + item[0] + '">' + item[1] + '</a>'
	
	#polymorphic use of print_out
	#html elements and <a> links returned	
	def print_out(self):
		return self._head + self._body + self._form_open + self._button_link + self._form_close + self._close