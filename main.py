import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from sqlalchemy import *

import time

engine = create_engine("sqlite:///localhost.db",echo=True, future=True)

with engine.connect() as conn:
    conn.execute(text("INSERT INTO SpotifyPlaylistData (Name, Album, Artists, Duration) VALUES ('Off The Grid', 'Donda', 'Kanye West and Baby Keem', 3.000)"))
    conn.commit()




os.environ['SPOTIPY_CLIENT_ID'] = 'client-id'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'client_secret'
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost:3000/callback/'



scope = "playlist-read-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

'''

YOUR CODE FROM HERE ON OUT!!

'''
