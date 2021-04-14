# Stock Alert

<table border='0'>
<tr>
  <td>
  This project monitors the closing stock prices for a company and if it detects a significant change, it texts the user the change along with recent news articles. It uses the <a href="https://www.alphavantage.co/documentation/">Alpha Vantage API</a> to find details about stock prices and filters the returned data to find the last two closing prices to calculate the percent change. If the change meets the significance threshold, it then retrieves breaking news articles using <a href="https://newsapi.org/docs">News API</a> and texts up to three articles along with the percent change to the user.
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
          <td align='center'>2/5</td>
        </tr>
        <tr>
          <td>Key Concepts</td>
          <td align='center'><em>Processing API Responses</em></td>
        </tr>
      </table>
    </div>
  </td>
</tr>
</table>

Overall, this project was relatively straightforward. After getting used to the Twilio API, sending texts became fairly simple and I just had to get used to the two new APIs the project uses. The most challenging aspect was getting used to the format of the data that they returned and being able to parse it to find the needed information. Of course the documentation was vital for this task, but there also was an <a href="http://jsonviewer.stack.hu/">online json viewer</a> that was invaluable for its help. I could have also tried to pretty print the output using either the `pprint` or `json` modules, but I found copying and pasting the output into the online viewer much simpler and I quickly bookmarked the site for future reference. Once I understood the data structures that the APIs returned, I just had to slice the outputs to get the data I needed and tidy up my code to finish up the project.

If you want to run the project yourself, you will need to make a `config.json` file with the following variables:

    "twilio_account_sid"  # Your Twilio account ID
    "twilio_auth_token"  # Your Twilio authentication token
    "twilio_phone_number"  # Your Twilio account phone number
    "my_phone_number"  # Your personal Twilio verified phone number
    "alpha_vantage_api_key"  # Your API key for Alpha Vantage
    "newsapi_api_key"  # Your API key for News API

The relevant APIs and their functions in the project are:
- [Twilio - SMS Messaging](https://www.twilio.com/)
- [Alpha Vantage - Stock Information](https://www.alphavantage.co/documentation/)
- [News API - Breaking News Articles](https://newsapi.org/docs)
