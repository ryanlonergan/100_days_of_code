# Spotify Playlist Time Machine

<table border='0'>
<tr>
  <td>
  This page is a template to copy and paste for each day. I don't like the table borders, but they are controlled by github. It looks pretty clean, so oh well.
  </td>
  <td>
    <div>
      <table>
        <tr>
          <td align='center' colspan="2"><strong>Quick Project Stats</strong></td>
        </tr>
        <tr>
          <td>Difficulty</td>
          <td align='center'>X/5</td>
        </tr>
        <tr>
          <td>Frustration</td>
          <td align='center'>X/5</td>
        </tr>
        <tr>
          <td>Key Concepts</td>
          <td align='center'><em>List a few</em></td>
        </tr>
      </table>
    </div>
  </td>
</tr>
</table>


Any comments for the day.

problems with searching

- before regex for artist names in searches - 33/100 missing
- year in search term - 3/100 missing - just decided to exclude in case of 
- fixing those allowed all to come through
- her version used to just search for song title and year - not very accurate, but less problems 

another example from song titles
- 15 missing - all had (From some movie)
- added split  on (, but needed to use a character escape \
- only 3 missing

artist titles and . inside them
- replace('.', '') actually caused more songs to be missing
- tried to catch edge cases, but seemed to be better to leave it in



If you want to run the project yourself, you will need to make a `config.json` file with the following variables:

    "spotify_client_id"  # Personal ID for Spotify Developer App
    "spotify_client_secret"  # Personal Token for Spotify Developer App

The relevant APIs and their functions in the project are:
- [Spotipy - Library for Interacting with Spotify](https://spotipy.readthedocs.io/en/latest/)
