from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='Placeholder',
            fill=THEME_COLOR,
            font=('Arial', 18, 'italic')
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score_label = Label(text='Score: 0', bg=THEME_COLOR, fg='white')
        self.score_label.grid(column=1, row=0)

        true_image = PhotoImage(file='./images/true.png')
        self.true_button = Button(image=true_image, borderwidth=0, highlightthickness=0, command=self.choose_true)
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file='./images/false.png')
        self.false_button = Button(image=false_image, borderwidth=0, highlightthickness=0, command=self.choose_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """
        Checks if there is a next question and changes the GUI if there is or ends the quiz if there isn't
        """
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You have reached the end of the quiz.')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def choose_true(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def choose_false(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        """
        Flashes the screen green or red if the user gets the questions right or wrong
        :param is_right:  bool
        """
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
