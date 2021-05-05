# Rain Alert

<table border='0'>
<tr>
  <td>
  This project checks the upcoming weather for a location and sends a text message to bring an umbrella if it is likely to rain. It uses the <a href="https://openweathermap.org/api/one-call-api">OpenWeather API</a> to find the forecast for a location based on longitude and latitude and the program processes the returned data for the next 12 hours. If it detects that there will be rain, it uses the <a href="https://www.twilio.com/">Twilio API</a> to send a text message to the user. This program could be run locally, but was designed to be run daily in the morning on an online environment, such as <a href="https://aws.amazon.com/lambda/">AWS Lambda</a> or <a href="https://www.pythonanywhere.com/">PythonAnywhere</a>, to act as a daily reminder.
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
          <td align='center'><em>APIs, Security, SMS Messages</em></td>
        </tr>
      </table>
    </div>
  </td>
</tr>
</table>

From this day, I was excited to learn how to send text messages through Python, but was somewhat disappointed to learn it cost money as a third party solution was needed. For Twilio, I was given a $15 trial balance and then it cost $0.0075 per message, so 68 messages over several projects only took $0.51 from my balance. Not bad overall, but I was curious about other options as Twilio had some restrictions on accounts without credit cards attached to them to limit spam. An alternative I found that was easy and completely free to use was the <a href="https://docs.python.org/3/library/smtplib.html">smtplib library</a> to send a text message to a phone number from an email, which just requires the phone number and the extension of the phone carrier. The extension varies by carrier, but can be easily Googled. However, it is not a SMS, but a MMS, so your experience may vary. Overall, it was a good introduction about sending messages through Python and I will continue exploring other ways of doing so to find the method I like best.

If you want to run the project yourself, you will need to make a `config.json` file with the following variables:

    "owm_api_key"  # Your key for the OpenWeather API
    "twilio_account_sid"  # Your Twilio account ID
    "twilio_auth_token"  # Your Twilio authentication token
    "twilio_phone_number"  # Your Twilio account phone number
    "my_phone_number"  # Your personal Twilio verified phone number

The relevant APIs and their functions in the project are:
- [OpenWeather One Call API - Weather Data](https://openweathermap.org/api/one-call-api)
- [Twilio - SMS Messaging](https://www.twilio.com/)
