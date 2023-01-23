class Song:

    count = 0
    genres = []
    genre_count = {}
    artists = []
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.append(genre)
        cls.add_to_genre_count(genre)

    @classmethod
    def add_to_genre_count(cls, genre):
        if (cls.genre_count.__contains__(genre)):
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.append(artist)
        cls.add_to_artist_count(artist)

    @classmethod
    def add_to_artist_count(cls, artist):
        if (cls.artist_count.__contains__(artist)):
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
