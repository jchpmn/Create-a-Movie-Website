import fresh_tomatoes
import media

new_hope = media.Movie("New Hope", "Sci fi space opera",
						"http://imgc.allpostersimages.com/images/P-473-488-90/67/6751/7TAZ100Z/posters/star-wars-episode-iv-new-hope-classic-movie-poster.jpg",
						# noqa
						"https://youtu.be/9gvqpFbRKtQ")

empire_stikes_back = media.Movie("Empire Strikes Back",
						"Sci fi space opera",
						"http://imgc.allpostersimages.com/images/P-473-488-90/83/8385/8ZJJ300Z/posters/star-wars-episode-5.jpg",
						# noqa
						"https://youtu.be/96v4XraJEPI")

return_of_the_jedi = media.Movie("Return of the Jedi",
					 	"Sci fi space opera",
					 	"http://imgc.allpostersimages.com/images/P-473-488-90/56/5662/G4FUG00Z/posters/return-of-the-jedi.jpg",
					 	# noqa
					 	"https://youtu.be/XgB4gaY2dWE")

phantom_menace = media.Movie("Phantom Menace", "Sci fi space opera",
						"http://imgc.allpostersimages.com/images/P-473-488-90/27/2757/E76TD00Z/posters/star-wars-episode-i.jpg",
						# noqa
						"https://youtu.be/bD7bpG-zDJQ")

attack_of_the_clones = media.Movie("Attack of the Clones", "Sci fi space opera",
						"http://imgc.allpostersimages.com/images/P-473-488-90/7/789/LLEI000Z/posters/star-wars-episode-ii-attack-of-the-clones.jpg",
						# noqa
						"https://youtu.be/gYbW1F_c9eM")

revenge_of_the_sith = media.Movie("Revenge of the Sith", "Sci fi space opera",
						"http://imgc.allpostersimages.com/images/P-473-488-90/38/3899/G5RJF00Z/posters/star-wars-episode-3.jpg",
						# noqa
						"https://youtu.be/5UnjrG_N8hU")

movies = [phantom_menace, attack_of_the_clones, revenge_of_the_sith, new_hope, empire_stikes_back, return_of_the_jedi]
""" List which contains the variables for each movie which are passed
to fresh_tomatoes to create the links to the movie trailers """
fresh_tomatoes.open_movies_page(movies)
""" Recieves the list of movies and creates a website which has the
movie trailers """