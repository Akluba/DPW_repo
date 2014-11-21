'''
Anthony Kluba
DPW1411
Lab3 Dynamic Site
11/20/14
'''
import webapp2
from pages import Page, ContentPage

class MainHandler(webapp2.RequestHandler):
    def get(self):
        
        #create instance of FormPage
        page = ContentPage()
        #arrays passed to buttons in ContentPage Class
        page.buttons = [['/?player=1','name1'],['/?player=2','name2'],['/?player=3','name3'],['/?player=4','name4'],['/?player=5','name5']]
        
        self.response.write(page.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
