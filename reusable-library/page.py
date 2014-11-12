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
		self.body = "<h1>Form</h1>"
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
		self.__close = """
	</body>
</html>
	"""

	def print_out(self):
		all = self.__head + self.body + self.__close
		return all