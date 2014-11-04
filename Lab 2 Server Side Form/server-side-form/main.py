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
        	pass

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
