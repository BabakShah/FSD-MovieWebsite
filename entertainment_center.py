# Project: Movies Website
import media
import fresh_tomatoes

# Creating three instances of the class Movie: toy_story, avatar and lucy
toy_story = media.Movie("Toy Story",
	"https://1.bp.blogspot.com/-4CEJ24flM5U/T-ePLTwLdyI/AAAAAAAAHcQ/GGYVN8SVxG0/s1600/Toy+Story+%281995%29+1.jpg",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc",
	"John Lasseter",
	"22 November 1995 (USA)")

avatar = media.Movie("Avatar",
	"http://img13.deviantart.net/34fd/i/2011/058/8/8/avatar_jake_and_neytiri_poster_by_remus09-d3aiukt.jpg",
	"https://www.youtube.com/watch?v=_V1lLSS9lCc",
	"James Cameron",
	"18 December 2009 (USA)")

lucy = media.Movie("Lucy",
	"https://www.newdvdreleasedates.com/images/posters/large/lucy-2014-04.jpg",
	"https://www.youtube.com/watch?v=UXs4CtMv_3o",
	"Luc Besson",
	"25 July 2014 (USA)")

# Storing the movie instances in an array list
movies = [toy_story, avatar, lucy]

""" Calling open_movies_page() function from fresh_tomatoes.py file 
	to display the movies on a webpage. We pass the movies array (list
	of movies) as a parameter of the function.
"""
fresh_tomatoes.open_movies_page(movies)
