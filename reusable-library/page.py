class FormPage(object):
	def __init__(self):
		self.__head = """
<!DOCTYPE HTML>
<html>
	<head>
		<title>BAC</title>
		<link href="css/style.css" rel="stylesheet" type="text/css" >
	</head>
	<body>
	"""
		self.body = """
		<div id="container">
			<h1>Form</h1>
			<form method="GET">
					<div class="option_box">
						<label for="sex">Sex?</label>
						<input type="radio" name="sex" value="male">Male
						<input type="radio" name="sex" value="female">Female
					</div>
					
					<div class="option_box">
						<label for="weight">Body weight?</label> 
						<input type="text" name="weight" />	
					</div>
					
					<div class="option_box">
						<label for="drink">Drink of choice?</label>
						<select name="drink">
							<option value="beer">Beer</option>
							<option value="wine">Wine</option>
							<option value="shot">Shots</option>
						</select> 
					</div>
					
					<div class="option_box">
						<label for="number">How many drinks?</label> 
						<input type="text" name="number" />	
					</div>
					
					<div class="option_box">
						<label for="hours">How many hours since first drink?</label> 
						<input type="text" name="hours" />	
					</div>
				
					
					
					<input type="submit" value="Calculate!" />
				</form>
			</div>
			<div id="car_img"></div>"""
		self.__close = """
	</body>
</html>
	"""

	def print_out(self):
		all = self.__head + self.body + self.__close
		return all
		
		
		
class ResultPage(object):
	def __init__(self):
		self.__head = """
<!DOCTYPE HTML>
<html>
	<head>
		<title>BAC</title>
		<link href="css/style.css" rel="stylesheet" type="text/css" >
	</head>
	<body>
	"""
		self.body = "<h1>Results</h1>"
		self.result = ""
		self.__close = """
	</body>
</html>
	"""

	def print_out(self):
		all = self.__head + self.body + self.result + self.__close
		return all