class FavoriteMovies(object):
	def __init__(self):
		self.__movie_list = []
		
	def add_movie(self, m):
		self.__movie_list.append(m)
		print m.title
		
	def compile_list(self):
		output = ''
		for movie in self.__movie_list:
			output += 'Title: ' + movie.title + " Year: " + str(movie.year)
		return output
			
	def calc_time_span(self):
		years = []
		for movie in self.__movie_list:
			years.append(movie.year)
		
		years.sort()
		num = len(years)-1
		span = years[num] - years[0]
		return 'the age span is: ' + str(span)


class MovieData(object):
	def __init__(self):
		self.title = ''
		self.__year = 0
		self.director = ''
		
	@property
	def year(self):
		return self.__year
		
	@year.setter
	def year(self, y):
		self.__year = y
		