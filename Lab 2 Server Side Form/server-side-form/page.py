class Page():
	def __init__(self):
		self.title = "Build A Burger!" #var title for page
		self.css = "css/style.css" #var css path
		#var containing html elements for head
		self.head = """
<!DOCTYPE HTML>
<html>
	<head>
		<title>{self.title}</title>	
		<link href="{self.css}" rel="stylesheet" type="text/css" /> 	
	</head>
	<body>	
		"""
		#var containing html form elements
		self.form = """
		<form method="GET">
		
			<label for="bread" autofocus="autofocus">What type of bread?</label>
			<input type="radio" name="bread" value="white">White<br>
			<input type="radio" name="bread" value="potato">Potato<br>
			<input type="radio" name="bread" value="pretzel roll">Pretzel Roll<br>
		
			<label for="cheese">What type of cheese?</label>
			<select name="cheese" autofocus="autofocus">
				<option value="none">No Cheese</option>
				<option value="american">American</option>
				<option value="swiss">Swiss</option>
				<option value="cheddar">Cheddar</option>
			</select> 
			
			<label for="topping">Choose a Topping?</label>
			<select name="topping" autofocus="autofocus">
				<option value="The Regular">The Regular</option>
				<option value="Bacon">Bacon</option>
				<option value="MacnCheese">Mac n Cheese</option>
				<option value="Fried Egg">Fried Egg</option>
			</select>  		
				
			<label for="where" autofocus="autofocus">For Here or ToGo?</label>
			<input type="radio" name="where" value="here">Here<br>
			<input type="radio" name="where" value="togo">ToGo
			
			<label for="name">Name For Order?</label> 
			<input type="text" name="name" autofocus="autofocus" placeholder="What's your name?" />
		"""
		#var containing html closing elements
		self.close = """
	</body>
</html>
		"""
		#functions returning values
		def head(self):
			return self.head
			
		def form(self):
			return self.form
			
		def close(self):
			return self.close