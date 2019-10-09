# Song class begins here
# It takes an argument and saves it in self.lyrics
class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
# Song class ends here

# happy_bday object being instantiated with a song
happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

# bulls_on_parade object being instantiated with a song
bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

# Both of the objects will get their respective songs
# happy_bday object calls the sing_me_a_song function
happy_bday.sing_me_a_song()
# bulls_on_parade object calls the sing_me_a_song function
bulls_on_parade.sing_me_a_song()
