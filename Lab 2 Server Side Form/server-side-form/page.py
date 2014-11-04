class Page(object):
	def __init__(self):
		#var containing html elements for head
		self.head = """
<!DOCTYPE HTML>
<html>
	<head>
		<title>Build A Burger!</title>	
		<link href="css/style.css" rel="stylesheet" type="text/css" /> 	
	</head>
	<body>"""
		#var containing html form elements
		self.form = """
		<header>
			<h1>Build'n Burgers</h1>
		</header>
		<div id="container">
			<form method="GET">
				<div class="option_box">
					<label for="bread" autofocus="autofocus">What type of bread?</label><br>
					<div class="burger_option">
						<input type="radio" name="bread" value="white">White<br>
						<input type="radio" name="bread" value="potato">Potato<br>
						<input type="radio" name="bread" value="pretzel">Pretzel<br>
					</div>
				</div>
				<div class="option_box">
					<label for="cheese">Any Cheese?</label>
					<div class="burger_option">
						<select name="cheese" autofocus="autofocus">
							<option value="no">No Cheese</option>
							<option value="american">American</option>
							<option value="swiss">Swiss</option>
							<option value="cheddar">Cheddar</option>
						</select> 
					</div>
				</div>
				<div class="option_box">
					<label for="topping">Choose a Topping?</label>
					<div class="burger_option">
						<select name="topping" autofocus="autofocus">
							<option value="the regular">The Regular</option>
							<option value="bacon">Bacon</option>
							<option value="mac n' cheese">Mac N' Cheese</option>
							<option value="fried egg">Fried Egg</option>
						</select> 
					</div> 		
				</div>
				<div class="option_box">
					<label for="where" autofocus="autofocus">For Here or ToGo?</label><br>
					<div class="burger_option">
						<input type="radio" name="where" value="for here">Here<br>
						<input type="radio" name="where" value="togo">ToGo
					</div>
				</div>
				<div class="option_box" id="last_box">
					<label for="name">Name For Order?</label> 
					<div class="burger_option">
						<input id="cust_name" type="text" name="name" autofocus="autofocus" placeholder="What's your name?" />
					</div>
				</div>
				
				<input id="submit_button" type="submit" value="Complete Order!" />
			</form>
		</div>"""
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