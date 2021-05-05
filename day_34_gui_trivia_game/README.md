# GUI Trivia Game

<table border='0'>
<tr>
  <td>
  This project creates a GUI interface for a trivia game with dynamically updated questions through the <a href ="https://opentdb.com/api_config.php">Open Trivia Database API</a>. OOP is used to organize the program and its logic is divided by class to allow for easier changes, maintenance and troubleshooting. The questions are presented to the user through a UI made with <a href="https://docs.python.org/3/library/tkinter.html">Tkinter</a> and reacts to the user's answers to let them know if they were correct.
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
          <td align='center'>2/5</td>
        </tr>
        <tr>
          <td>Key Concepts</td>
          <td align='center'><em>OOP, APIs</em></td>
        </tr>
      </table>
    </div>
  </td>
</tr>
</table>

This day was a bit of a trial as I am still getting used to OOP best practices and when to use them. If I were to code the project within only the `main.py` file, I would have completed the project much faster, but the project pushed me out of my comfort zone and I welcomed the challenge. While it might have been easier to stick with what I am used to, I did see the benefits of using OOP and different classes to organize the project as making changes was much simpler as the project evolved. Improving my knowledge of OOP was one of the main reasons I wanted to do this course and I am glad that I became better at using it as the logic of when to use it makes more sense to me.

For the questions, the <a href ="https://opentdb.com/api_config.php">Open Trivia Database API</a> was used to retrieve randomized questions. The API is vastly customizable and the difficulty, number of questions and category can be changed easily within the parameters inside the `data.py` file. If I were to add to the project, customizing these parameters every time could be easily done as the program is structured to allow for such changes through OOP.

<img src="https://ryanlonergan.github.io/assets/img/100_days/day_34_trivia_game.png" alt="Screenshot of Trivia Game" width=275>
