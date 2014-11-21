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
		#player1
		self.altuve = DataObject()
		self.altuve.name = 'Jose Altuve'
		self.altuve.__img = 'http://a.espncdn.com/combiner/i?img=/i/headshots/mlb/players/full/31662.png&w=350&h=254'
		self.altuve.__at_bats = 660
		self.altuve.__hits = 225
		self.altuve.__strike_outs = 53
		self.altuve.__walks = 36
		#player2
		martinez = DataObject()
		martinez._name = 'Victor Martinez'
		martinez._img = 'http://a.espncdn.com/combiner/i?img=/i/headshots/mlb/players/full/5007.png&w=350&h=254'
		martinez._at_bats = 561
		martinez._hits = 188
		martinez._strike_outs = 42
		martinez._walks = 70
		#player3
		brantley = DataObject()
		brantley._name = 'Michael Brantley'
		brantley._img = 'http://a.espncdn.com/combiner/i?img=/i/headshots/mlb/players/full/30043.png&w=350&h=254'
		brantley._at_bats = 611
		brantley._hits = 200
		brantley._strike_outs = 56
		brantley._walks = 52
		#player4
		beltre = DataObject()
		beltre._name = 'Adrian Beltre'
		beltre._img = 'http://a.espncdn.com/combiner/i?img=/i/headshots/mlb/players/full/3878.png&w=350&h=254'
		beltre._at_bats = 549
		beltre._hits = 178
		beltre._strike_outs = 74
		beltre._walks = 57
		#player5
		abreu = DataObject()
		abreu._name = 'Jose Abreu'
		abreu._img = 'http://a.espncdn.com/combiner/i?img=/i/headshots/mlb/players/full/33095.png&w=350&h=254'
		abreu._at_bats = 556
		abreu._hits = 176
		abreu._strike_outs = 131
		abreu._walks = 51