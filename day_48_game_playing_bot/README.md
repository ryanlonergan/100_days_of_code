# Game Playing Bot

<table border='0'>
<tr>
  <td>
  This project automatically plays <a href='https://orteil.dashnet.org/cookieclicker/'>the Cookie Clicker Idle Game</a> using the Selenium WebDriver to handle all the clicking and upgrades through its code. Elements in the game are found through Selenium and are organized through list comprehension. The <code>time</code> library is also used to create timers for the bot's logic, spacing out commands as needed.
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
          <td align='center'>3/5</td>
        </tr>
        <tr>
          <td>Key Concepts</td>
          <td align='center'><em>Selenium WebDriver, Time Module</em></td>
        </tr>
      </table>
    </div>
  </td>
</tr>
</table>

This day's project is another example of the course's external resources changing and making the project much harder than intended. As the course is meant to represent real life work as much as possible, it uses many outside sources for web scraping or other information that they have no control over. While this method is useful and great for teaching, it can also introduce issues when these resources change. For this project, the <a href='https://orteil.dashnet.org/cookieclicker/'>Cookie Clicker Idle Game</a> had a UI update that increased in complexity and used more JavaScript to dynamically change many elements. While these changes made for a better game and UX, it made automating the game more of a challenge, but I was able to power through it and came away with code I was satisfied with. I just wish the course used the <a href='https://orteil.dashnet.org/experiments/cookie/'>classic version</a> of the game that is not updated anymore.

As for the actual coding, it was my first time using <a href='https://www.selenium.dev/documentation/en/webdriver/'>Selenium</a> and I really enjoyed it. I had some prior experience with web scraping but ran into its limits many times before. However, Selenium gets around many issues with its WebDrivers that control browsers, such as the <a href='https://chromedriver.chromium.org/downloads'>ChromeDriver</a>. For example, in the <a href='https://github.com/ryanlonergan/100_days_of_projects/tree/main/day_47_amazon_price_tracker'>day 47 project</a>, it was difficult to convince Amazon that the script was not a bot, but Selenium had no issues and was able to do it in a few lines of code as shown in the `notes.py` file. The use of CSS selectors is still something I need practice with, but there are many online resources, such as <a href='https://saucelabs.com/resources/articles/selenium-tips-css-selectors
'>this one by Sauce Labs</a>, and I plan to incorporate Selenium into my projects much more in the future.
