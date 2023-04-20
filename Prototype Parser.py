#!/usr/bin/env python
# coding: utf-8

# In[4]:


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import lyricsgenius

# Set up authorization credentials
client_id = '07005604eeb94c15a4b055cb290847f8'
client_secret = '24690934174c407583a9410363206c14'
genius_access_token = "Bjc_l29KgRjxlf7pNJ-vM7zEDKG5xbf12fJ4K1TDZdWKW2jjh87Jqy7wz38ocUCu"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
genius = lyricsgenius.Genius(genius_access_token)
# Search for a song on Spotify based on lyrics

def get_spotify_uri_from_lyrics(lyrics):
    # search for the song title and artist using the lyricsgenius package
    song = genius.search_song(lyrics)
    if not song:
        print('Could not find song with the given lyrics')
        return

    # search for the song on Spotify using the spotipy package
    result = sp.search(q='{} {}'.format(song.title, song.artist), type='track')

    # extract the Spotify URIs of the songs from the search results
    spotify_uris = []
    for item in result['tracks']['items']:
        spotify_uri = item['uri']
        spotify_uris.append(spotify_uri)

    # return the list of Spotify URIs
    if len(spotify_uris) > 0:
        print('Spotify URIs: {}'.format(', '.join(spotify_uris)))
        return spotify_uris
    else:
        print('Could not find song on Spotify')
        
def get_lyrics_from_uri(uri):
    # extract the track ID from the Spotify URI
    track_id = uri.split(':')[-1]

    # use the Spotipy package to get the track's information
    track = sp.track(track_id)

    # use the LyricsGenius package to fetch the lyrics
    lyrics = genius.search_song(track['name'], track['artists'][0]['name'])

    if lyrics is not None:
        return lyrics.lyrics
    else:
        return 'No lyrics found for this song'

get_spotify_uri_from_lyrics("And all the lights that lead us there are blinding")
get_lyrics_from_uri("spotify:track:1qPbGZqppFwLwcBC1JQ6Vr")

