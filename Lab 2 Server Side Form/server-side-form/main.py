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
        
        #when url params are present print results page
        if self.request.GET:
        	#GET method variables 
        	bread = self.request.GET['bread']
        	cheese = self.request.GET['cheese']
        	topping = self.request.GET['topping']
        	where = self.request.GET['where']
        	name = self.request.GET['name']

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
