import spotipy
import spotipy as spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from time import sleep


class sporify_handler():

    def __init__(self, CLIENT_ID, CLIENT_SECRET):

        self.CLIENT_SECRET = CLIENT_SECRET
        self.CLIENT_ID = CLIENT_ID


    def get_current_session(self):
        scope = "user-read-playback-state,user-modify-playback-state"
        sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(client_id=self.CLIENT_ID,
                              client_secret=self.CLIENT_SECRET,
                              redirect_uri="http://localhost:8888/callback",
                              scope='user-read-playback-state,user-modify-playback-state'))
        # Shows playing devices
        res = sp.devices()
        # pprint(res)

        # Change track
        # sp.start_playback(uris=['spotify:track:0HUTL8i4y4MiGCPId7M7wb'])

        # print(sp.artist())
        # print(sp.album())
        # print(sp.show())
        # print(sp.audio_analysis())
        # pprint(type(sp.current_playback()))
        # pprint(sp.current_playback())
        return sp.current_playback()

    def get_cleaned_song_info(self):
        """

        :return: array of strings: [song, artist, album].
        """
        current_playback_dict = self.get_current_session()
        if current_playback_dict == None:
            print("Nothing is currently playing")
            return None
        # pprint(current_playback_dict)
        song_name = current_playback_dict['item']['name']
        album_name = current_playback_dict['item']['album']['name']
        artists_names = current_playback_dict['item']['artists']
        first_artist = artists_names[0]['name']
        # pprint(song_name)
        # pprint(album_name)
        # pprint(first_artist)
        return [song_name,first_artist,album_name]

if __name__ == "__main__":
    # pprint(get_cleaned_song_info())
    print("Hello")