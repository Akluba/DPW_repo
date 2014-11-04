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