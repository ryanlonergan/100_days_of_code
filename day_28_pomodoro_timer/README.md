# Pomodoro Timer

<table border='0'>
<tr>
  <td>
  This project creates a Pomodoro timer to help with productivity using a GUI through <a href="https://docs.python.org/3/library/tkinter.html">tkinter</a>. It takes the duration for the work periods, short breaks and long breaks in seconds and uses floor division and other logic to format the countdown correctly using <code>.after()</code> to update the count. The program's logic is broken down into different functions and the UI updates itself to provide feedback based on the user's progress.
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
          <td align='center'>2/5</td>
        </tr>
        <tr>
          <td>Key Concepts</td>
          <td align='center'>Tkinter, <code>.after()</code> function</td>
        </tr>
      </table>
    </div>
  </td>
</tr>
</table>

I thought this day was a helpful introduction into setting and calling timed commands tied to certain events with `.after()`. It was somewhat of a challenge getting my head around how the event is called by the program, but once I did, it was fairly simple to set up and use. The program has some room for improvement as it is possible to set up multiple timers, but these can be fixed through disabling buttons if desired. While I may not use this program in my day to day life as I find Pomodoro too rigid, I am happy with how it came out overall. I just wish I could use `.after()` outside of tkinter after getting used to it, but I will have to look into alternatives for more general code.

<img src="https://ryanlonergan.github.io/assets/img/100_days/day_28_pomodoro.png" alt="Project Screenshot" width=450>
