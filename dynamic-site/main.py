'''
Anthony Kluba
DPW1411
Lab3 Dynamic Site
11/20/14
'''
import webapp2
#importing from other py scripts
from pages import ContentPage
from data import Data

class MainHandler(webapp2.RequestHandler):
    def get(self):
        
        page = ContentPage()
        data = Data()
        
        print data.altuve
                
        #watching for GET method
        #result dependent on player
        if self.request.GET:
        	player = self.request.GET['player']
        	print player
        	if player == "altuve":
        		page.template(data.altuve)
        		self.response.write(page.template(data.altuve))
        	elif player == "martinez":
        		pass
        	elif player == "brantley":
        		pass
        	elif player == "beltre":
        		pass
        	elif player == "abreu":
        		pass
        #html written to browser before link is clicked
        else:
        	self.response.write(page.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
