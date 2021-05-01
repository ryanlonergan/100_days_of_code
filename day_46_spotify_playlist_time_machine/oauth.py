import json
import spotipy


def get_oauth():
    """
    Uses stored client credentials to get oauth access token from Spotify
    Requires accepting app access via spotify browser redirect and user need to copy and paste redirect url into console

    :return: bearer token string
    """

    # Get Spotify client credentials from a .gitignore'd config file
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

    # it sometimes says .get_access_token() is being deprecated, but not always
    # not sure what is going on with spotipy
    access_tok = auth.get_access_token()
    return access_tok['access_token']


def get_bearer():
    """
    Gets bearer token through existing token.txt file or requests ones from Spotify through get_oauth function

    :return: bearer token string
    """

    try:
        # get existing bearer token and test it through bearer_test method
        with open('token.txt', 'r') as token_file:
            token_data = token_file.read()
            token_dict = json.loads(token_data)
            bearer_token_str = token_dict['access_token']
    except FileNotFoundError:
        # Requests a new bearer
        bearer_token_str = get_oauth()
    finally:
        return bearer_token_str
