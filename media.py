import webbrowser

class Movie():

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		""" This function takes in parameters for movie data and creates variables
		for title, storyline, poster image, and a movie trailer info """
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		""" Opens a browser and displays poster images with links to 
		movie trailers """
		webbrowser.open(self.trailer_youtube_url)
