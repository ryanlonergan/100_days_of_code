# Flight Deal Tracker Capstone

<table border='0'>
<tr>
  <td>
  This project finds flight deals and sends a text if there is a price lower than it has recorded previously. It reads from
  and manages a Google Sheet using the Sheety API and then uses the Tequila API to find flights for desired locations.
  If a deal is found, it uses the Twilio API to send a text. The project is segmented into different scripts based on
  function using OOP and automatically handles the inputs and outputs of the APIs.
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


Overall, this project was a mess. Due to COVID, there are still substantial barriers to travel even a year after the US
stay at home order was issued. This fact caused a lot of errors as there just was not any data for the flight API to
provide as there simply are not any flights. Furthermore, it was compounded by poor API documentation by Tequila and
also by low limits for API calls by Sheety. I was eventually able to solve my problems with Tequila through reading the
course's discussion board and also made a workaround for the Sheety API calls by hard coding the data. However, these
issues caused extra hours of frustration and I believe a lot of it could have been avoided if the project was better
designed. Nevertheless, when I was able to get the code to run perfectly, it was very satisfying and came away knowing a
lot more about troubleshooting.


If you want to run the project yourself, you will need to make a `config.json` file needing the following variables:

    "tequila_api"
    "sheety_endpoint"    
    "sheety_bearer_token"
    "twilio_account_sid"
    "twilio_auth_token"
    "twilio_phone_number"
    "my_phone_number"

The relevant APIs and their functions in the project are:
- [Tequila - Flight Information](https://tequila.kiwi.com)
- [Sheety - Google Sheets Editor](https://dashboard.sheety.co/)
- [Twilio - SMS Messaging](https://www.twilio.com/)
