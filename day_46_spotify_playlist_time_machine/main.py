import pandas as pd
from bs4 import BeautifulSoup
import requests
import json
import spotipy
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


# todo I think I will put this all in a separate script that runs if it doesn't find the token.txt file

# Get Spotify OAuth from a .gitignore'd config file
with open('config.json', 'r') as data_file:
    config = json.load(data_file)
    spotify_client_id = config['spotify_client_id']
    spotify_client_secret = config['spotify_client_secret']
url_redirect = 'https://example.com'

auth = spotipy.oauth2.SpotifyOAuth(client_id=spotify_client_id,
                                   client_secret=spotify_client_secret,
                                   redirect_uri=url_redirect,
                                   scope='playlist-modify-private')
# cache_path='token.txt') no longer needed
access_tok = auth.get_cached_token()  # .get_access_token() is being deprecated so I believe the token.txt is not needed
bearer_token = access_tok['access_token']

# todo
'''
format may look like this

try:
    with open config.json:
        bearer_token
    continue
except missing
    get token
    recursion
except failure
    get token
    recursion
    
Maybe it is better to not put it in a recursion loop - continues to fail indefinitely 
come back to it tomorrow

put in a counter that stops after 3 tries
if count < 4:
 try
else:
print('something isn't right')
break

'''

# with open('token.txt', 'r') as token_file:
#     token_data = token_file.read()
#     token_dict = json.loads(token_data)
#     bearer_token = token_dict['access_token']
#
sp = spotipy.Spotify(auth=bearer_token)
user_details = sp.current_user()
print(user_details['id'])


# her code may want to try tomorrow
'''
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=YOUR UNIQUE CLIENT ID,
        client_secret=YOUR UNIQUE CLIENT SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]






'''
