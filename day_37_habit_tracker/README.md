# Habit Tracker

<table border='0'>
<tr>
  <td>
  This project interacts with the <a href="https://docs.pixe.la/">Pixela API</a> to track habits through pixels and color, similar to the GitHub contribution graph. It goes through all the different interactions with the API, including initial user creation, graph creation, adding pixels, updating pixels and also deleting pixels.
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
          <td align='center'>1/5</td>
        </tr>
        <tr>
          <td>Key Concepts</td>
          <td align='center'><em>Types of API Requests</em></td>
        </tr>
      </table>
    </div>
  </td>
</tr>
</table>

I really like the idea behind this API. The project was very simple, so there is not much to comment about, but the GitHub style tracking that <a href="https://pixe.la/">Pixela</a> provides is kind of addicting as you see your graph grow as you complete more work. I know I enjoy seeing my graph change as I make more contributions on GitHub and this is another way to track progress for anything you desire. The customizability with color and other options that <a href="https://pixe.la/">Pixela</a> offers is really great as well and has some unique features, such as color schemes being selected by their names in Japanese. However, the best thing <a href="https://pixe.la/">Pixela</a> offers is <a href="https://docs.pixe.la/">great documentation</a> that I am very grateful for after using some APIs that are a pain to figure out how to use. Overall, I am very impressed by the <a href="https://pixe.la/">Pixela API</a> and encourage others to check it out if it sounds interesting.

I would also like to point out the `strftime()` formatting method from the `datetime` module. This project was the first time I learned about it and it makes changing dates to whatever format you need extremely easy. I wish I knew about it much earlier as it would have saved me so much time and frustration. Its documentation can be found <a href="https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior">here</a>.


If you want to run the project yourself, you will need to make a `config.json` file with the following variables:

    "pixela_username"  # Your Pixela username
    "pixela_token":  # Your Pixela security token
