'''
Anthony Kluba
DPW1411
Reusable Library
11/11/14
'''
import webapp2
from lib import MovieData, FavoriteMovies

from page import ResultsPage
class MainHandler(webapp2.RequestHandler):
    def get(self):
        
        p = ResultsPage()
        lib = FavoriteMovies()
        
        md1 = MovieData()
        md1.title = "title of movie"
        md1.year = 1991
        md1.director = "AKluba"
        lib.add_movie(md1)
        
        md2 = MovieData()
        md2.title = "sammi sweeney"
        md2.year = 1992
        md2.director = "SSweeney"
        lib.add_movie(md2)
        
        
        p.body = lib.compile_list() + lib.calc_time_span()
        self.response.write(p.print_out())
        

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
