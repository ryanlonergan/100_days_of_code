import pandas as pd
from bs4 import BeautifulSoup
import requests
import json
import spotipy
import os
# Todo Find out if I need this
from spotipy.oauth2 import SpotifyClientCredentials

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

# todo move all of this to oauth script - doesn't need to be here - easier to sort out there
# Gets bearer token through existing token.txt file or requests ones from Spotify if token.txt does not exist
# if new token is needed, requires accepting app access via spotify and need to copy and paste redirect url int cmd line
try:
    with open('token.txt', 'r') as token_file:
        token_data = token_file.read()
        token_dict = json.loads(token_data)
        bearer_token = token_dict['access_token']
except FileNotFoundError:
    # Get Spotify OAuth from a .gitignore'd config file
    with open('config.json', 'r') as data_file:
        config = json.load(data_file)
        spotify_client_id = config['spotify_client_id']
        spotify_client_secret = config['spotify_client_secret']
    url_redirect = 'https://example.com'

    auth = spotipy.oauth2.SpotifyOAuth(client_id=spotify_client_id,
                                       client_secret=spotify_client_secret,
                                       redirect_uri=url_redirect,
                                       show_dialog=True,
                                       scope='playlist-modify-private',
                                       cache_path='token.txt')

    # it sometimes says .get_access_token() is being deprecated, but not always, not sure what is going on with spotipy
    access_tok = auth.get_access_token()
    bearer_token = access_tok['access_token']


# This section does a quick check to ensure that the recorded bearer token is still good
# If it fails, it deletes the old token.txt file and requests it again
# This action does require the user to copy and paste in their redirect url once they accept the app access from spotify
try:
    sp = spotipy.Spotify(auth=bearer_token)
    user_details = sp.current_user()
    print(sp.current_user()['id'])   # todo Figure out if this is needed later, do I need to call it again?
except spotipy.client.SpotifyException:
    os.remove('token.txt')

    # Get Spotify OAuth from a .gitignore'd config file
    with open('config.json', 'r') as data_file:
        config = json.load(data_file)
        spotify_client_id = config['spotify_client_id']
        spotify_client_secret = config['spotify_client_secret']
    url_redirect = 'https://example.com'

    auth = spotipy.oauth2.SpotifyOAuth(client_id=spotify_client_id,
                                       client_secret=spotify_client_secret,
                                       redirect_uri=url_redirect,
                                       show_dialog=True,
                                       scope='playlist-modify-private',
                                       cache_path='token.txt')

    # it sometimes says .get_access_token() is being deprecated, but not always, not sure what is going on with spotipy
    access_tok = auth.get_access_token()
    bearer_token = access_tok['access_token']

print('good')