# Flight Deal Tracker Capstone

<table border='0'>
<tr>
  <td>
  This project project is a continuation from the previous day and adds some additional functionality. The key difference is that instead of sending a text, it sends an email to a list of users. People can signup with a public facing <a href="https://www.replit.com">Replit</a> and Sheety manages the email list on Google Sheets. If a flight is found, it emails all users the deal and provides a direct link to book the trip on Google Flights. There also is additional error handling and the program will now check for flights with layovers if there are limited flights due to Covid. 
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
          <td align='center'><em>APIs and OOP</em></td>
        </tr>
      </table>
    </div>
  </td>
</tr>
</table>

This day of the project was not much better than the previous. Covid still added significant issues which required more workarounds. To get the project to work on day 39, I had already implemented error handling that then got in the way for this day. If I had known the scope of the project from the beginning, I would have been able to handle it a lot easier and my time could have been more focused for both days. Furthermore, Covid still added more challenges as this day included the ability to continue to check for flights if there were no direct flights available. However, travel is definitely not back to normal yet and it was hard to find anywhere that did not have a direct flight from Seattle that did with just one layover. I eventually got around this by finding some smaller airports in Japan that only had domestic travel and a few layovers, but it took some time to figure out a location to test to even see if my code worked. The low number of API requests from Sheety and Tequila's poor documentation did not help with this day either. Overall, I am glad to get it done and while it was annoying, it did teach me a lot about troubleshooting.

If you want to run the project yourself, you will need to make a `config.json` file needing the following variables:

    "tequila_api"
    "sheety_endpoint"
    "sheety_users_endpoint"  # New from previous day
    "sheety_bearer_token"
    "twilio_account_sid"
    "twilio_auth_token"
    "twilio_phone_number"
    "my_phone_number"
    "my_email"  # New from previous day
    "email_password"  # New from previous day

The relevant APIs and their functions in the project are:
- [Tequila - Flight Information](https://tequila.kiwi.com)
- [Sheety - Google Sheets Editor](https://dashboard.sheety.co/)
- [Twilio - SMS Messaging](https://www.twilio.com/)
 