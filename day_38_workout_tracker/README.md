# Workout Tracker

<table border='0'>
<tr>
  <td>
  This project asks a user about their exercise in natural language and records detailed information in a workout log on Google Sheets. It sends details about the user and their exercise to the <a href="https://developer.nutritionix.com/docs/v2">Nutritionx API</a> which uses AI to analyze and return greater details, such as duration, distance or calories burned. The program then parses the returned data and uses <a href="https://dashboard.sheety.co/">Sheety</a> to update a Google Sheet file to log the activity. If the user entered multiple exercises, it will record each one as a different event automatically.
  </td>
  <td>
    <div>
      <table>
        <tr>
          <td align='center' colspan="2"><strong>Quick Project Stats</strong></td>
        </tr>
        <tr>
          <td>Difficulty</td>
          <td align='center'>2/5</td>
        </tr>
        <tr>
          <td>Frustration</td>
          <td align='center'>3/5</td>
        </tr>
        <tr>
          <td>Key Concepts</td>
          <td align='center'><em>API Posts and Formatting Responses</em></td>
        </tr>
      </table>
    </div>
  </td>
</tr>
</table>

This day was not too bad overall, but dealing with different APIs is always hit or miss depending on the documentation. After coming from <a href="https://github.com/ryanlonergan/100_days_of_projects/tree/main/day_37_habit_tracker">day 37</a> that used the great documentation from <a href="https://docs.pixe.la/">Pixela</a>, this day was not more challenging, but just frustrating as it was harder to find what I was looking for in the <a href="https://developer.nutritionix.com/docs/v2">Nutritionx documentation</a>. However, it was not too bad overall and I was able to find what I needed after enough time searching and experimenting to get the data I needed. Overall, it just made me more grateful for when I have good documentation to work with and more prepared to look through documentation that is not as clear.

If you want to run the project yourself, you will need to make a `config.json` file with the following variables:

    "nutritionix_app_id"  # Your ID for your Nutritionx app
    "nutritionix_api_key"  # Your API key for your Nutritionx app
    "sheety_endpoint"  # Your Sheety endpoint for the Google Sheets file
    "sheety_bearer_token":  # Your Sheety bearer token

The relevant APIs and their functions in the project are:
- [Nutritionx - Natural Language Parsing for Exercise](https://developer.nutritionix.com/docs/v2)
- [Sheety - Google Sheets Editor](https://dashboard.sheety.co/)
