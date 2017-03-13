import webbrowser
"""
Define a Movie class which contains a movie's tile, storyline, poster image
and it trailer from Youtube
"""

class Movie():
  def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
    """
    The __init__ method
    Args:
        movie_title (str): The title of one movie.
        movie_storyline (str): The story line of one movie.
        poster_image (str): The link of a poster image of the movie.
        trailer_youtube (str): The youtube link of a movie's trailer.
    """
    self.title = movie_title
    self.storyline = movie_storyline
    self.poster_image_url = poster_image
    self.trailer_youtube_url = trailer_youtube  
  
  """
  show trailer from a youtube link
  """
  def show_trailer(self):
    webbrowser.open(self.trailer_youtube_url)
