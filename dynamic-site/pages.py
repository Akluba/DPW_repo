#Page class is our superclass
class Page(object):
	def __init__(self):
		#html elements found in head
		self._head = '''<!DOCTYPE HTML>
<html>
	<head>
		<title>American League Top5 Batting Average</title>
		<link href="css/style.css" rel="stylesheet" type="text/css" >
		<link href='http://fonts.googleapis.com/css?family=Source+Sans+Pro:400,700,200' rel='stylesheet' type='text/css'>
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
	
	#this is my polymorphic function 
	#an average site could use this function
	#to calculate site data
	def __calc_avg():
		pass
		
#ContentPage subclass 		
class ContentPage(Page):
	def __init__(self):
		#init as subclass of our Page superclass
		super(ContentPage, self).__init__()
		#html elements linking players
		self._nav = '''
		<div id="container">
			<div id="player_links">
				<a href="?player=altuve">Jose Altuve</a>
				<a href="?player=martinez">Victor Martinez</a>
				<a href="?player=brantley">Michael Brantley</a>
				<a href="?player=beltre">Adrian Beltre</a>
				<a href="?player=abreu">Jose Abreu</a>
			</div>
		'''
		#will contain html elements of player instance 
		self._result = ''
	
	#inactive getter
	@property
	def result(self):
		pass
	
	#polymorphic function overriding Page class __calc_avg
	#in ContentPage the function is used to
	#calculate players batting average
	def __calc_avg(self, obj):
		avg = float(obj.hits) / float(obj.at_bats)
		batting_average = round(avg,3)
		#return value to be printed 
		return batting_average
	
	#responsible for setting self._result
	#to html elements	
	@result.setter
	def result(self, obj):
		#pass obj to calc_avg function
		batting_avg = self.__calc_avg(obj)
	
		self._result += '''	<div id="player_info">\n				'''
		self._result += '''<h1>''' + obj.name + '''</h1>\n			'''
		self._result += '''	<img src="''' + obj.img + '''" alt="player_img">\n			'''
		self._result += '''</div>\n		'''
		self._result += '''	<div id="player_stats">\n				'''
		self._result += '<h2><strong>At Bats:</strong> ' + str(obj.at_bats) + '</h2>\n				'''
		self._result += '<h2 class="odd"><strong>Hits:</strong> ' + str(obj.hits) + '</h2>\n				'''
		self._result += '<h2><strong>Strike Outs:</strong> ' + str(obj.strike_outs) + '</h2>\n				'''
		self._result += '<h2 class="odd"><strong>Walks:</strong> ' + str(obj.walks) + '</h2>\n				'''
		self._result += '<h2><strong>Batting Average:</strong> ' + str(batting_avg) + '</h2>\n			'''
		self._result += '''</div>\n		'''
		self._result += '''</div>'''
		
	#function responsible for returning html elements 
	#to be written to browser		
	def print_out(self):
		return self._head + self._nav + self._result + self._close
		