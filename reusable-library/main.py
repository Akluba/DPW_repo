'''
Anthony Kluba
DPW1411
Reusable Library
11/11/14
'''
import webapp2
from page import FormPage

class MainHandler(webapp2.RequestHandler):
    def get(self):
    
    	#create an instance of FormPage
    	form = FormPage()
        
        #print form page to browser
        self.response.write(form.print_out())
        

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
