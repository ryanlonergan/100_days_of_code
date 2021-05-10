# Amazon Price Tracker

<table border='0'>
<tr>
  <td>
  This project automatically tracks the prices on an Amazon page for a product and sends the user an email alert if the price drops below a threshold they are willing to pay for it. It uses the <code>requests</code> library to retrieve the HTML web page and uses additional header arguments to prevent Amazon from thinking it is a bot. Beautiful Soup then parses the page using the <code>lxml</code> parser and the relevant data is retrieved and cleaned to meet the script's needs. If it detects that the price is lower than the price threshold the user sets, it then emails them an alert using <code>SMTP</code>.
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
          <td align='center'><em>Beautiful Soup, Request Headers, SMTP</em></td>
        </tr>
      </table>
    </div>
  </td>
</tr>
</table>

This day was another project that was more frustrating than it needed to be. The main goal was to replicate the price tracking functionality that <a href='https://camelcamelcamel.com/'>camelcamelcamel</a> offers and getting the logic and flow for the project established was not hard. However, successfully parsing the Amazon web page was much more challenging than I initially imagined and even getting it to return the correct web page was a struggle. To limit the number of bots that access its pages, Amazon requires some additional header information that your web browser supplies when it regularly visits the site. This information can be viewed at <a href='http://myhttpheader.com/'>My HTTP Header</a> and to get the script to work, it becomes a matter of trial and error until you find the right arguments to add to your request. To further complicate the issue, once I thought I had my header correct, Amazon decided that it no longer liked it and I needed to mess with it further for it to work. To help with this process, I added in additional error handling to help make the problem more noticeable.

After I was able to get my request to work and I searched through the almost 16,000 lines of code that Beautiful Soup returned for the Amazon page, I thought I was pretty much finished with the project as I just had to set up the SMTP request. This process was something that I had done multiple times before and I was familiar with it, but I kept on getting authentication errors. There was nothing wrong with my code, but it took me some time to discover that Google turned off my less secure app access for my test email and I had to turn it back on <a href='https://myaccount.google.com/lesssecureapps'>here</a>. I have no idea why Google did this action, but perhaps it was because I did not use it recently and it is a security measure for them. Once I resolved this issue, my code worked and while I did become frustrated, I know that my troubleshooting skills improved as well.

If you want to run the project yourself, you will need to make a `config.json` file with the following variables:

    "email"  # Your email address
    "password"  # Your email password
