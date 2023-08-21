import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
import json

# open file with keys and set the path to your credentials JSON file
credentials = "spotify_keys.json"
with open(credentials, "r") as keys:
    api_tokens = json.load(keys)

# read the keys and assign each to a variable
client_id = api_tokens["client_id"]
client_secret = api_tokens["client_secret"]

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# learn about more query strings for spotify here: https://developer.spotify.com/documentation/web-api/reference/#/operations/search
track_results = sp.search(q='year:2021', type='track', limit=50)

# return a list of song title
def get_tracks():
	# Using list comprehension
	# Get values of particular key in list of dictionaries
	songs = [ track['name'] for track in track_results['tracks']['items'] ]
	return songs