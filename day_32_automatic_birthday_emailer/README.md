# Automatic Birthday Emailer

<table border='0'>
<tr>
  <td>
  This project automatically sends out a randomized email message to anyone with a birthday on the day's date. It reads a csv file with a list of people, their birthdays and their emails and uses a condition to see if the current day is their birthday. It then chooses a random message from a list of templates, personalizes the message for the person and appends a random quote to the user's signature. Then, the message is emailed to the person and if the script is uploaded to an online Python environment (<a href="https://www.pythonanywhere.com/">PythonAnywhere</a>, <a href="https://aws.amazon.com/lambda/">AWS Lambda</a>, etc.), it can check for birthdays daily and the user never has to worry about forgetting one again.
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
          <td align='center'><em>Sending Emails with Smtplib</em></td>
        </tr>
      </table>
    </div>
  </td>
</tr>
</table>


At first glance, this project seems to be not too hard. With adequate understanding of the `random` library, list/dictionary comprehension and f-strings, things went fairly smoothly and I even added another feature to the project with a random quote to be edited into my signature for the message. However, my views quickly changed as I got to sending the email with the `smtplib` library. In the lessons, it seemed very easy to do, but when I tried it, my messages would not send. I looked for workarounds as some email clients needed some extra settings changed, but I seemed to be all set with my provider, Gmail. After some Googling, I found my issue and all I needed to do was add 3 numbers (port 587) to my `smtplib.SMTP` request and my code suddenly worked. However, that was not the end of my frustration as my message was displayed oddly when emailed. After more Googling, another simple solution was found as the f-string just needed `.encode('utf-8')` added to the end of it so the message was presented correctly. I liked the idea of the project and enjoyed it, but these two bugs added a lot of extra troubleshooting.

If you want to run the project yourself, you will need to make a `config.json` file with the following variables:

    "email"  # Your email address
    "password"  # Your email password
