# Movie Web Scraper

<table border='0'>
<tr>
  <td>
  This project scrapes a curated list of top movies by <a href='https://www.hollywoodreporter.com/lists/100-best-films-ever-hollywood-favorites-818512'>The Hollywood Reporter</a> and returns a list of the movie titles and their ranking in a sorted text file. It uses <a href='https://www.crummy.com/software/BeautifulSoup/bs4/doc/'>Beautiful Soup</a> to parse the website's HTML and to search through its tags and CSS classes, finding the desired information. It then uses list comprehension and slicing to sort through the data before adding it to a text file.
  <br>
  <br>
  This day also includes another .py file that performs a similiar process on <a href='https://news.ycombinator.com/news'>YCombinator's Hacker News</a> and returns the title and link for the news article with the highest score for the day.
  </td>
  <td>
    <div>
      <table>
        <tr>
          <td align='center' colspan="2"><strong>Quick Project Stats</strong></td>
        </tr>
        <tr>
          <td>Difficulty</td>
          <td align='center'>3/5</td>
        </tr>
        <tr>
          <td>Frustration</td>
          <td align='center'>4/5</td>
        </tr>
        <tr>
          <td>Key Concepts</td>
          <td align='center'><em>Beautiful Soup, Web Scraping</em></td>
        </tr>
      </table>
    </div>
  </td>
</tr>
</table>


Any comments for the day.

- https://www.empireonline.com/movies/features/best-movies-2/
- [what i used](https://www.hollywoodreporter.com/lists/100-best-films-ever-hollywood-favorites-818512)
- Issue with react.js instead of pure html
    - kept on returning empty lists
    - not obvious until you use soup.prettify() to see what the page returned
    - One way to fix was to use selenium web driver, but that was coming up later in the course
    - elected for simpler option of using a different website
