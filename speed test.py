import tkinter as tk
import random
import time

# List of words for the typing test
words = ['python', 'java', 'programming', 'code', 'keyboard', 'developer', 'challenge', 'practice', 'speed', 'typing']

class SpeedTypingTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Speed Typing Test")
        self.word_to_type = tk.StringVar()
        self.user_input = tk.StringVar()
        self.word_to_type.set(random.choice(words))
        self.score = 0
        self.time_left = 30

        # GUI components
        self.word_label = tk.Label(root, textvariable=self.word_to_type, font=("Arial", 24))
        self.word_label.pack(pady=20)

        self.entry = tk.Entry(root, textvariable=self.user_input, font=("Arial", 18))
        self.entry.pack(pady=10)
        self.entry.bind('<Return>', self.check_word)

        self.info_label = tk.Label(root, text="Type the word above and press Enter", font=("Arial", 14))
        self.info_label.pack(pady=20)

        self.timer_label = tk.Label(root, text="Time left: 30 seconds", font=("Arial", 14))
        self.timer_label.pack()

        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
        self.score_label.pack()

        self.start_game()

    def check_word(self, event):
        if self.user_input.get() == self.word_to_type.get():
            self.score += 1
        self.word_to_type.set(random.choice(words))
        self.user_input.set('')
        self.score_label.config(text=f"Score: {self.score}")

    def countdown(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time left: {self.time_left} seconds")
            self.root.after(1000, self.countdown)
        else:
            self.timer_label.config(text="Time's up!")
            self.entry.config(state='disabled')

    def start_game(self):
        self.countdown()

# Create the main window
root = tk.Tk()
game = SpeedTypingTest(root)
root.mainloop()
