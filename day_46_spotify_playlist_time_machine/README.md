# Spotify Playlist Time Machine

<table border='0'>
<tr>
  <td>
  This project scrapes records from the <a href='https://www.billboard.com/charts/hot-100'>Billboard Top 100</a> and creates a playlist of the top songs on Spotify for a certain date. It asks a user for what date the playlist should be for and then uses <a href='https://www.crummy.com/software/BeautifulSoup/bs4/doc/'>Beautiful Soup</a> to create a dataframe of the songs from the Billboard page. It then uses <a href='https://spotipy.readthedocs.io/en/latest/'>Spotipy</a> to interact with the <a href='https://developer.spotify.com/documentation/web-api/'>Spotify API</a>, handling the OAuth security and any requests. Song and artist names are then processed using regular expression before Spotipy searches for the tracks to add to a playlist it creates.
  </td>
  <td>
    <div>
      <table>
        <tr>
          <td align='center' colspan="2"><strong>Quick Project Stats</strong></td>
        </tr>
        <tr>
          <td>Difficulty</td>
          <td align='center'>4/5</td>
        </tr>
        <tr>
          <td>Frustration</td>
          <td align='center'>5/5</td>
        </tr>
        <tr>
          <td>Key Concepts</td>
          <td align='center'><em>Beautiful Soup, Authentication, OAuth, Regular Expression</em></td>
        </tr>
      </table>
    </div>
  </td>
</tr>
</table>

This day continues the trend of frustration for the course as using <a href='https://spotipy.readthedocs.io/en/latest/'>Spotipy</a> was not an easy process. At first, I was excited for the day as I am an avid Spotify user and wanted to use my own data for other data science projects, but the documentation for the library is not very helpful and at times cryptic, leaving me unsure about what the library could do or how to go about using it. This obstacle complicated the project greatly and I had to split the project across a few days to make it less of a headache. In the end, I was able to Google or experiment with the library enough to eventually get Spotipy to work as I wanted, but the poor documentation really obstructed the process.

To add to the day's confusion, once I got the search working it would frequently tell me that about one third of the songs were missing for my test date, April 23rd, 2020 which was the start of the stay at home order in Washington State. At first I thought that maybe Spotify did not have the streaming rights for the songs, but thought that was strange as it was only a year ago and their library is vast. I altered my code to print the name and artist of the songs to console when the search could not find them and I was surprised to find that a lot of the missing songs were popular and I could find them easily when I searched Spotify manually. Originally, the code included searching with the year as a search term, but I realized that songs could appear on the list even if they were not released that year and I decided to remove it as a search term. I also noticed that the search was handling songs with artist features poorly as it believed the entire string, i.e. Person Featuring Person 2, was the artist's name. To remedy this error, I used regular expression to split the artist strings on a few common keywords with `re.split()` and just searched with the first artist returned. From making these 2 changes, only 3 out of 100 songs were missing, vastly improving the accuracy.

Next, I tried a list from about 30 years ago to further improve how the search functioned. This time, 15 songs were missing, but many of them had '<em>(From some movie)'</em> in their titles which caused errors. Again, I used `re.split()` to process the song titles, but had to use a raw string and character escapes for my regular expression filter to work. I also tried using `.replace()` to remove periods from the artist names, but this change actually caused more songs to be unfound as some artists included punctuation as part of their stylized names leading me to revert this filter. Overall, the 15 missing songs were reduced to only 3 and when I tried making a playlist for my birthday, only 5 songs were missing with 3 songs not being on Spotify and 2 songs were unfound since Billboard made errors with either the song title or artist name, leaving me confident in my regular expression filters.

If you want to run the project yourself, you will need to make a `config.json` file with the following variables:

    "spotify_client_id"  # Personal ID for Spotify Developer App
    "spotify_client_secret"  # Personal Token for Spotify Developer App

    # Both of these are found through creating an app on the Spotify Developer Portal

The relevant APIs and their functions in the project are:
- [Spotipy - Library for Interacting with Spotify](https://spotipy.readthedocs.io/en/latest/)
