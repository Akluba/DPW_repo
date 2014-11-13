#containing html elements for form view
class FormPage(object):
	def __init__(self):
		self.__head = """
<!DOCTYPE HTML>
<html>
	<head>
		<title>BAC</title>
		<link href="css/style.css" rel="stylesheet" type="text/css" >
		<link href='http://fonts.googleapis.com/css?family=Source+Sans+Pro:400,700,200' rel='stylesheet' type='text/css'>
		<script>
		function validateForm() {
		    var sex = document.forms["form"]["sex"].value,
		    	weight = document.forms["form"]["weight"].value,
		    	drink = document.forms["form"]["drink"].value,
		    	number = document.forms["form"]["number"].value,
		    	hours = document.forms["form"]["hours"].value;
		    	
		    if (sex==null || sex=="") {
		        alert("Please enter Sex");
		        return false;
		    }else if(weight==null || weight==""){
		    	alert("Please enter Weight");
		        return false;
		    }else if(drink==null || drink==""){
		    	alert("Please enter drink type");
		        return false;
		    }else if(number==null || number==""){
		    	alert("Please enter number of drinks");
		        return false;
		    }else if(hours==null || hours==""){
		    	alert("Please enter hours since first drink");
		        return false;
		    }
		}
		</script>
	</head>
	<body>
	"""
		self.body = """
		<div id="container">
			<div id="page_text">
				<h1>Having a hard time deciding on whether to drive or not?</h1> 
				<h2>Use this blood alcohol concentration calculator to find which ride you need to take!</h2>
			</div>
			<form name="form" method="GET" onsubmit="return validateForm()">
				<div id="questions">
					<div class="option_box">
						<label for="sex">Sex?</label>
						<input type="radio" name="sex" value="male">Male
						<input type="radio" name="sex" value="female">Female
					</div>
					<div class="option_box">
						<label for="weight">Body weight?</label>
						<input type="text" class="input_num" name="weight" />	
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
						<input type="text" class="input_num" name="number" />	
					</div>
					<div class="option_box">
						<label for="hours">How many hours since first drink?</label>
						<input type="text" class="input_num" name="hours" />	
					</div>
					<input type="submit" id="submit_button" value="Calculate!" />
				</div>
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
		
		
#containing html to be displayed on results
class ResultPage(object):
	def __init__(self):
		self.__head = """
<!DOCTYPE HTML>
<html>
	<head>
		<title>BAC</title>
		<link href="css/style.css" rel="stylesheet" type="text/css" >
		<link href='http://fonts.googleapis.com/css?family=Source+Sans+Pro:400,700,200' rel='stylesheet' type='text/css'>
	</head>
	<body>
		<div id="container">
	"""
		self.result = ""
		self.__close = """
		</div>
	</body>
</html>
	"""

	def print_out(self):
		all = self.__head + self.result + self.__close
		return all