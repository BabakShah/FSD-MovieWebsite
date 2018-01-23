# Project: Movies Website
import webbrowser

class Movie():
	"""This class creates attributes of movies.

	Attributes:
		title (str): Movie's title.
		poster_image_url (str): Movie's poster.
		trailer_youtube_url (str): Movie's trailer.
		screen_writer (str): Movie's writer.
		launch_date (str): Movie's launch date.

	Methods:
		__init__ method: initializes the class.
	"""
    def __init__(self,title,poster,trailer,writer,date):
        """initializes the class.

        Args:
            Movie's title, poster, trailer, writer and launch date

        Returns:
        	Nothing.
        """
        self.title = title
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
        self.screen_writer = writer
        self.launch_date = date


