import webbrowser

class Movie():

    """ This class stores all of your favourite movie details and their trailers

        Attributes:
            title : Title of the movie
            storyline : A breif storyline of the movie
            poster_image : url of the poster image of the movie to be displayed
            trailer_url : url of the trailer in youtube

    """

    def __init__(self, title, storyline, poster_image, trailer_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_url = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
