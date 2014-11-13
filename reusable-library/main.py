'''
Anthony Kluba
DPW1411
Reusable Library
11/11/14
'''
import webapp2
from lib import UserInfo, BacFormula
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
        
        	#creating an instance of BacFormula class
        	bac = BacFormula()
        	
        	#creating an instance of UserInfo to store information
        	user = UserInfo()
        	user.sex = self.request.GET['sex']
        	user.weight = self.request.GET['weight']
        	user.drink_type = self.request.GET['drink']
        	user.drink_num = self.request.GET['number']
        	user.hours = self.request.GET['hours']
        	
        	#send sex value to convert_sex function
        	bac.convert_sex(user.sex)
        	#sending drink_type and drink_num values to calc_drink fuction
        	bac.calc_drinks(user.drink_type, user.drink_num)
        	
        	#setting result to results of calc_bac function to be displayed
        	result.result = bac.calc_bac(user.weight,user.hours)
        
        	#write form page to browser
        	self.response.write(result.print_out())
        else:
	        #write form page to browser
	        self.response.write(form.print_out())
        

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
