'''
Anthony Kluba
DPW1411
Lab2 Server Side Form
11/4/14
'''
import webapp2
#from page.py import all
from page import *

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #create instance of Page()
        page = Page()
        
        #submit button from click uses GET method
        #causes results to be displayed
        if self.request.GET:
        	#GET method variables 
        	bread = self.request.GET['bread']
        	cheese = self.request.GET['cheese']
        	topping = self.request.GET['topping']
        	where = self.request.GET['where']
        	name = self.request.GET['name']
        	
        	result = '''
        	<header>
        		<h1>{name}'s Burger Order</h1>
        	</header>
        	<div id="result_container">
        		<div id="burger_img"></div>
        		<div id="result_text">
		        	<p>We have a juicy burger with {cheese} cheese</p>
		        	<p>On top a freshly baked {bread} bun</p>
		        	<p>Topped with {topping}</p>
		        	<p>This order is {where}</p>
		        </div>
	        </div>
        	'''
        	#format result to be printed 
        	result = result.format(**locals())
        	#write content to browser
        	self.response.write(page.head + result + page.close)
        #form to be displayed in browser until GET method
        else:
        	self.response.write(page.head + page.form + page.close)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
