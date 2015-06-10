import webbrowser


class Movie():
    # Create new instance of Movie with given attributes
    def __init__(self, title, storyline, poster_image_url,
                 trailer_youtube_url, release_year):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.release_year = release_year

    # Open webbrowser with the URL of the given Movie's Youtube URL
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
