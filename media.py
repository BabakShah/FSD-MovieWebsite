# Project: Movies Website

import webbrowser

class Movie():

    def __init__(self,title,poster,trailer,writer,date):
        
        self.title = title
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
        self.screen_writer = writer
        self.launch_date = date


