#DataObject class of player with necessary attributes of all players
class DataObject(object):
	def __init__(self):
		#attributes of baseball player
		self.__name = ''
		self.__img = ''
		self.__at_bats = 0
		self.__hits = 0
		self.__strike_outs = 0
		self.__walks = 0
		
#Class contains instances of hard coded objects	
class Data(object):
	def __init__(self):
		#player1 instance 
		altuve = DataObject()
		altuve.name = 'Jose Altuve'
		altuve.img = 'http://a.espncdn.com/combiner/i?img=/i/headshots/mlb/players/full/31662.png&w=350&h=254'
		altuve.at_bats = 660
		altuve.hits = 225
		altuve.strike_outs = 53
		altuve.walks = 36
		#player2 instance
		martinez = DataObject()
		martinez.name = 'Victor Martinez'
		martinez.img = 'http://a.espncdn.com/combiner/i?img=/i/headshots/mlb/players/full/5007.png&w=350&h=254'
		martinez.at_bats = 561
		martinez.hits = 188
		martinez.strike_outs = 42
		martinez.walks = 70
		#player3 instance
		brantley = DataObject()
		brantley.name = 'Michael Brantley'
		brantley.img = 'http://a.espncdn.com/combiner/i?img=/i/headshots/mlb/players/full/30043.png&w=350&h=254'
		brantley.at_bats = 611
		brantley.hits = 200
		brantley.strike_outs = 56
		brantley.walks = 52
		#player4 instance
		beltre = DataObject()
		beltre.name = 'Adrian Beltre'
		beltre.img = 'http://a.espncdn.com/combiner/i?img=/i/headshots/mlb/players/full/3878.png&w=350&h=254'
		beltre.at_bats = 549
		beltre.hits = 178
		beltre.strike_outs = 74
		beltre.walks = 57
		#player5 instance
		abreu = DataObject()
		abreu.name = 'Jose Abreu'
		abreu.img = 'http://a.espncdn.com/combiner/i?img=/i/headshots/mlb/players/full/33095.png&w=350&h=254'
		abreu.at_bats = 556
		abreu.hits = 176
		abreu.strike_outs = 131
		abreu.walks = 51
		
		#array containing player instances
		self.player_array = [altuve, martinez, brantley, beltre, abreu]