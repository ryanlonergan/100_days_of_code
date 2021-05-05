# ISS Tracker

<table border='0'>
<tr>
  <td>
  This project detects if the International Space Station (ISS) is overhead and will email the user if they should be able to see it in the night sky. It uses an API to find the latitude and longitude of the space station and determines if it is within 5 degrees of the user's latitude and longitude. It then uses another API to determine if the sun has set and has not risen yet, so it is dark enough to see the ISS. If these cases pass, it then emails the user to notify them that they may be able to see the ISS and should look out for it.
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
          <td align='center'>3/5</td>
        </tr>
        <tr>
          <td>Key Concepts</td>
          <td align='center'><em>API Requests, datetime Module</em></td>
        </tr>
      </table>
    </div>
  </td>
</tr>
</table>

I thought this project was a great way to introduce API calls and how to use multiple different ones within the logic of your program. Personally, I never knew the ISS travelled as fast as it does at 4.76 miles (ca. 7.66 km) per second and orbits the Earth about every 90 minutes. These facts make it very possible to see it on any given night and by running constantly on your machine or on an online option, such as [AWS Lambda](https://aws.amazon.com/lambda/) or
[Python Anywhere](https://www.pythonanywhere.com/), it should not be long before you get an email telling you to be on the lookout.


However, this project was not without its challenges which mainly revolved around timezones. I think that the project was not designed to have this issue, but it was instead introduced by accident since they are based in London which is UTC +0. The Sunrise Sunset API returns values in UTC +0 time, so people living in different parts of the world need to make adjustments, which was not overly simple to do. I was able to develop a solution that should work no matter where you are located, regardless of daylight savings time, and also requires no changes from the user, but it took quite a lot of time looking around the [datetime module documentation](https://docs.python.org/3/library/datetime.html) to figure it out.


If you want to run the project yourself, you will need to make a `config.json` file with the following variables:

    "email"  # Your email address
    "password"  # Your email password

The relevant APIs and their functions in the project are:
- [ISS Current Location - returns overhead longitude and latitude of ISS](http://open-notify.org/Open-Notify-API/ISS-Location-Now/)
- [Sunrise Sunset - returns sunrise and sunset times based on latitude and longitude](https://api.sunrise-sunset.org/)
