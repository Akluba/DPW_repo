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
        
        #creating instances of imported classes
        page = ContentPage()
        data = Data()
            
        #watching for GET method
        #result dependent on player
        if self.request.GET:
        	player = self.request.GET['player']
        	print player
        	#sending objects to setter on player link
        	if player == "altuve":
        		print data.player_array[0]
        		page.result = data.player_array[0]
        	elif player == "martinez":
        		print data.player_array[1]
        		page.result = data.player_array[1]
        	elif player == "brantley":
        		print data.player_array[2]
        		page.result = data.player_array[2]
        	elif player == "beltre":
        		print data.player_array[3]
        		page.result = data.player_array[3]
        	elif player == "abreu":
        		print data.player_array[4]
        		page.result = data.player_array[4]
        	#html elements written to browser	
        	self.response.write(page.print_out_result())
        		
        #html written to browser before link is clicked
        else:
        	self.response.write(page.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
