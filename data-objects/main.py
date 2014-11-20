
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        
        luke = Character()
        luke.name = "Luke Skywalker"
        luke.profession = "Jedi"
        luke.age = 29
        luke.home_planet = "Tattooine" 
        
        leia = Character()
        leia.name = "Leia Skywalker"
        leia.profession = "Princess"
        leia.age = luke.age
        leia.home_planet = "Alderan" 
        
        yoda = Character()
        yoda.name = "Yoda"
        yoda.profession = "Jedi"
        yoda.age = 800
        yoda.home_planet = "Dagobah"
        
        chars = [luke, leia, yoda]
        print chars[0].profession
        
class Character(object):
	def __init__(self):
		self.name = ""
		self.profession = ""
		self.age = 0
		self.home_planet = ""

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
