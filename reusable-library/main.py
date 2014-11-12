'''
Anthony Kluba
DPW1411
Reusable Library
11/11/14
'''
import webapp2
from page import FormPage, ResultPage

class MainHandler(webapp2.RequestHandler):
    def get(self):
    
    	#creating an instance of FormPage
    	form = FormPage()
    	#creating an instance of ResultPage
    	result = ResultPage()
        
        #watching for GET method
        #grab variables and write results to browser
        if self.request.GET:
        	#write form page to browser
        	self.response.write(result.print_out())
        else:
	        #write form page to browser
	        self.response.write(form.print_out())
        

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
