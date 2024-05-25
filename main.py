from datetime import date
from bs4 import BeautifulSoup
import requests

"""

Billboard Website: get top songs from a particular time

    - Scrape top 100 songs from a particular year
    - Create a Spotify Playlist with the songs found
    
NEED TO ADD - custom details:

    - access_token
    - user_id
    - playlist_name
    - playlist_description

"""
input_date = input("Write a date (YYYY/MM/DD): ").split("/")
date = date(year=int(input_date[0]), month=int(input_date[1]), day=int(input_date[2]))
date_formatted = date.strftime("%Y-%m-%d")

URL = f"https://www.billboard.com/charts/hot-100/{date_formatted}/"

response = requests.get(URL)
songs_webpage = response.text

soup = BeautifulSoup(songs_webpage, "html.parser")

song_title = soup.select("li ul li h3")
artist_name = soup.select("li ul li span")

songs = [song.getText().strip() for song in song_title]
names = [name.getText().strip() for name in artist_name if len(name.getText().strip()) > 2]

songs_dictionary = {names[i]: songs[i] for i in range(len(names))}

# Spotify Connection

# Spotify Connection data >> GET URI
access_token = 'your_token'
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

uri_list = []

# The search query
for artist_name, track_name in songs_dictionary.items():
    query = f"{track_name} artist:{artist_name}"

    # The search endpoint
    search_endpoint = 'https://api.spotify.com/v1/search'
    params = {
        'q': query,
        'type': 'track',
        'limit': 1
    }

    response = requests.get(search_endpoint, headers=headers, params=params)
    search_results = response.json()

    # Extracting the URI from the search results
    if search_results['tracks']['items']:
        track_uri = search_results['tracks']['items'][0]['uri']
        uri_list.append(track_uri)

# CREATE THE PLAYLIST AND ADD THE TRACKS

# User ID and playlist details
user_id = 'your_spotify_user_id'
playlist_name = 'your_playlist_name'
playlist_description = 'your_playlist_description'

# Create a new playlist
create_playlist_endpoint = f'https://api.spotify.com/v1/users/{user_id}/playlists'
create_playlist_data = {
    'name': playlist_name,
    'description': playlist_description,
    'public': False  # Set to True if you want the playlist to be public
}

response = requests.post(create_playlist_endpoint, headers=headers, json=create_playlist_data)
playlist = response.json()

# Add tracks to the playlist
playlist_id = playlist['id']
add_tracks_endpoint = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
tracks_to_add = {
    'uris': uri_list
}

response = requests.post(add_tracks_endpoint, headers=headers, json=tracks_to_add)

if response.status_code == 201:
    print('Tracks added successfully!')
else:
    print('Error adding tracks:', response.json())
