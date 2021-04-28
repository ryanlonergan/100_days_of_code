import pandas as pd
from bs4 import BeautifulSoup
import requests
import json
import spotipy

# Can switch to an input to get custom dates, but I switch to a static date for testing
# May want to add some error checking to ensure date is in correct format though
# date = input('Which date would you like a playlist for? Enter the date in this format: YYYY-MM-DD: ')
date = '2020-03-23'
url = 'https://www.billboard.com/charts/hot-100/' + date

response = requests.get(url)
songs_for_date = response.text

soup = BeautifulSoup(songs_for_date, 'html.parser')
songs = soup.find_all(name='span', class_='chart-element__information__song text--truncate color--primary')
artists = soup.find_all(name='span', class_='chart-element__information__artist text--truncate color--secondary')

song_list = [song.text for song in songs]
artist_list = [artist.text for artist in artists]
ranking = range(1, 101)  # I included a rank column as the index bothered me a bit since the count starts from 0

songs_df = pd.DataFrame(list(zip(ranking, song_list, artist_list)), columns=['Rank', 'Song', 'Artist'])
# print(songs_df.to_string(index=False))  # prints the df without the index to avoid any confusion with rank

# Get Spotify OAuth from a .gitignore'd config file
with open('config.json', 'r') as data_file:
    config = json.load(data_file)
    spotify_client_id = config['spotify_client_id']
    spotify_client_secret = config['spotify_client_secret']
