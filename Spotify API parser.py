#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install spotipy


# In[5]:


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set up authorization credentials
client_id = '4fdf0c9814f04bf2a858554336140450'
client_secret = '5512f23f0a9048f28140e217c5db1b29'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Function 1: Search for tracks
def search_tracks(query):
    results = sp.search(query, type='track')
    return results['tracks']['items']

# Function 2: Get track details
def get_track(track_id):
    track = sp.track(track_id)
    return track

# Function 3: Get artist details
def get_artist(artist_id):
    artist = sp.artist(artist_id)
    return artist

# Function 4: Get album details
def get_album(album_id):
    album = sp.album(album_id)
    return album

# Function 5: Get recommendations
def get_recommendations(track_ids):
    recommendations = sp.recommendations(seed_tracks=track_ids, limit=10)
    return recommendations['tracks']


# In[14]:


results = search_tracks('muse')
for track in results:
    print(track['name'])


# In[12]:


track = get_track('3n3Ppam7vgaVa1iaRUc9Lp')
print(track['name'], track['artists'][0]['name'])


# In[13]:


artist = get_artist('12Chz98pHFMPJEknJQMWvI')
print(artist['name'], artist['genres'][0])


# In[9]:


album = get_album('6peEdPVO73WtgGah5sEhX4')
print(album['name'], album['artists'][0]['name'])


# In[11]:


track_ids = ['3n3Ppam7vgaVa1iaRUc9Lp', '7ouMYWpwJ422jRcDASZB7P', '2takcwOaAZWiXQijPHIx7B']
recommendations = get_recommendations(track_ids)
for track in recommendations:
    print(track['name'], track['artists'][0]['name'])

