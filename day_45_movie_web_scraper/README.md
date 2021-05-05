# Movie Web Scraper

<table border='0'>
<tr>
  <td>
  This project scrapes a curated list of top movies by <a href='https://www.hollywoodreporter.com/lists/100-best-films-ever-hollywood-favorites-818512'>The Hollywood Reporter</a> and returns a list of the movie titles and their ranking in a sorted text file. It uses <a href='https://www.crummy.com/software/BeautifulSoup/bs4/doc/'>Beautiful Soup</a> to parse the website's HTML and to search through its tags and CSS classes, finding the desired information. It then uses list comprehension and slicing to sort through the data before adding it to a text file.
  <br>
  <br>
  This day also includes another .py file that performs a similar process on <a href='https://news.ycombinator.com/news'>YCombinator's Hacker News</a> and returns the title and link for the news article with the highest score for the day.
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

While the day's content was good, it was another instance of things outside of the course's control changing and making the day much harder than it should have been, similar to what happened with the flight tracker and COVID. Starting off with scraping <a href='https://news.ycombinator.com/news'>YCombinator's Hacker News</a>, concepts were explained and enough of a challenge was provided to make learning insightful, but not overly frustrating. However, scraping the movie list was an entirely different story. Originally, the site used a list compiled by <a href='https://www.empireonline.com/movies/features/best-movies-2/'>Empire Online</a>, but issues kept on coming up. Empty lists kept on being returned from <a href='https://www.crummy.com/software/BeautifulSoup/bs4/doc/'>Beautiful Soup</a> which was not always obvious unless steps were broken down and intermediate outputs were printed using `soup.prettify()` to see what was returned. I eventually discovered that the source on the website that I saw through my web browser was different than what Beautiful Soup returned and found that it was an issue with Empire Online switching to using `react.js` instead of pure HTML, resulting in two different versions of the website. With that knowledge, I could try to go with the results from Beautiful Soup, but they were very hard to read and sometimes the numbers or titles were missing, unordered or just incorrect. I could have also saved the HTML from the version that my browser rendered, essentially making a local copy of the page, but I thought that method defeated the purpose of the project as it was no longer scraping a live website. Another option would be to use <a href='https://www.selenium.dev/documentation/en/webdriver/'>Selenium WebDriver</a>, but that would have required quite a lot of extra work and Selenium would also be covered in the course within a few days. Instead, I elected to choose the simplest option and just used a list from a different website that still used HTML and found one curated by <a href='https://www.hollywoodreporter.com/lists/100-best-films-ever-hollywood-favorites-818512'>The Hollywood Reporter</a> instead. Once I made that change, everything was much simpler and I was able to finish up the project without any trouble. Overall, troubleshooting is a huge part of coding, so I have gotten used to it, but wish that the course would be better about catching and addressing these issues so that I could spend more of my time learning than finding workarounds.
