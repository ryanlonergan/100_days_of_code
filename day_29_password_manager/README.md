# Password Manager

<table border='0'>
<tr>
  <td>
  This project creates a GUI password manager that stores details for a user locally and also generates strong random passwords. A simple GUI is made using <a href="https://docs.python.org/3/library/tkinter.html">tkinter</a> and asks the user for details about what they want stored. If they are unsure what password to use, a random password can be generated using numbers, symbols and both lowercase and uppercase letters. Before storing the details, it asks the user for confirmation that the details are correct through a <a href="https://docs.python.org/3/library/tkinter.messagebox.html">messagebox</a> window and then stores the details in a text file on the local machine.
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
          <td align='center'><em>Random Module, Tkinter, Messagebox,</em></td>
        </tr>
      </table>
    </div>
  </td>
</tr>
</table>

This day was a good exercise in learning more about <a href="https://docs.python.org/3/library/tkinter.html">tkinter</a> and <a href="https://docs.python.org/3/library/tkinter.messagebox.html">messagebox</a>. I cannot say tkinter is my favorite or completely intuitive, but there is a lot of documentation to read through and examples online which makes it easier. Due to how Windows and Apple differ in their own UI, making my tkinter window  look correct was more of a challenge until I found out about the "sticky" option within the `.grid()` method. Instead of specifying how wide an element needs to be, you can make it stick to a cardinal direction. Also, I found out about some other methods that made coding easier, such as `random.shuffle()` to mix up the order of the chosen letters, symbols and numbers while in a list and then `"".join()` to put easily everything in the list into a string. Overall, I was glad about how this project came together and it was one of the first projects that I could see myself using often.

<img src="https://ryanlonergan.github.io/assets/img/100_days/day_29_pw_manager.png" alt="Screenshot of Password Manager" width=500>
