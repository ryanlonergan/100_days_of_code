import pandas as pd
from bs4 import BeautifulSoup
import requests
from oauth import get_bearer
import json
import spotipy
import os

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

bearer_token = get_bearer()
bearer_check(bearer_token)

sp = spotipy.Spotify(auth=bearer_token)
user_details = sp.current_user()
print(sp.current_user()['id'])





# This section does a quick check to ensure that the recorded bearer token is still good
# If it fails, it deletes the old token.txt file and requests it again
# This action does require the user to copy and paste in their redirect url once they accept the app access from spotify
def bearer_check(bearer_token):
    """
    Checks the recorded bearer token to make sure it works and is not expired. If an exception is raised, it removes
    the token.txt file that acts as a cache and requests a new token
    :param bearer_token: bearer token string to check
    :return: verified bearer token string
    """
    try:
        sp = spotipy.Spotify(auth=bearer_token)
        user_details = sp.current_user()
        print(user_details['id'])   # todo Figure out if this is needed later, do I need to call it again?
    except spotipy.client.SpotifyException:
        os.remove('token.txt')
        bearer_token = get_oauth()
    finally:
        return bearer_token