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
        self.response.write(page.print_out())
                	

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
