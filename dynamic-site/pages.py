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
		#html elements linking players
		self._nav = '''
		<a href="?player=altuve">Jose Altuve</a>
		<a href="?player=martinez">Victor Martinez</a>
		<a href="?player=brantley">Michael Brantley</a>
		<a href="?player=beltre">Adrian Beltre</a>
		<a href="?player=abreu">Jose Abreu</a>
		'''
		self._result = ''
		
	@property
	def result(self):
		pass
		
	@result.setter
	def result(self, obj):
		self._result += '<h1>' + obj.name + '</h1>'
		self._result += '<img src="' + obj.img + '" alt="player_img">'
		self._result += '<h2>At Bats: ' + str(obj.at_bats) + '</h2>'
		self._result += '<h2>Hits: ' + str(obj.hits) + '</h2>'
		self._result += '<h2>Strike Outs: ' + str(obj.strike_outs) + '</h2>'
		self._result += '<h2>Walks: ' + str(obj.walks) + '</h2>'
				
	def print_out(self):
		return self._head + self._nav + self._result + self._close
		