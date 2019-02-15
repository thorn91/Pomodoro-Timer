"""
Pomodoro Timer

Enter time in minutes.  Display is in seconds.
"""

from time import sleep
from tkinter import Tk, Entry, Button, Label, StringVar, messagebox, mainloop


class Pomodoro:
    def __init__(self):
        self.work_time = 0  # default time
        self.root = Tk()
        self.root.configure(background='black')
        self.timer = StringVar()
        self.cycle_count = 0

        # Initial setup
        self.root.geometry('100x100')
        self.entry = Entry(self.root)
        self.button = Button(text="Enter", command=self.get_time)
        self.timer_label = Label(self.root, textvariable=self.timer.get())
        self.entry.pack()
        self.button.pack()
        self.timer_label.pack()

        # Display messagebox
        mainloop()

    def get_time(self):
        # Get and display user work time and convert from minutes to seconds
        self.work_time = int(self.entry.get()) * 60
        self.timer_label.config(text=self.work_time)

        # Start coutndown
        self.countdown()

        # boxy = messagebox.showinfo(title="Hello!", message=self.work_time)

    def countdown(self):
        ''' Cycle pattern: work time -> 5 mins -> work time -> 5 mins -> work time -> 15 mins '''
        countdown_time = int(self.work_time)# * 60

        while countdown_time > 0:
            sleep(1)
            countdown_time -= 1
            self.timer_label.config(text=countdown_time)
            self.root.update()

        # Update cycle count
        self.cycle_count += 1
        
        # Call short or long break then repeat
        if self.cycle_count == 3:
            self.finish_cycles()
        elif self.cycle_count == 1 or self.cycle_count == 2:
            messagebox.showinfo(title="Timer Done", message="Time for a short break!")
            self.break_time(0)
        else:
            messagebox.showinfo(title="Timer Done", message="Time for a long break!")
            self.break_time(1)

        self.countdown()

    def break_time(self, sentinal):
        # Sentinal determines break length
        if sentinal == 0:
            countdown_time = 60 * 5
        else:
            countdown_time = 60 * 10
            
        while countdown_time > 0:
            sleep(1)
            countdown_time -= 1
            self.timer_label.config(text=countdown_time)
            self.root.update()
            messagebox.showinfo(title="Timer Done", message="Timer done!")


    def finish_cycles(self):
        messagebox.showinfo(title="Timer Done", message="You're done!")
        exit()            



if __name__ == "__main__":
    p = Pomodoro()
