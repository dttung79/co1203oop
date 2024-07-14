from tkinter import *

class GUIProgram02:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("300x50")
        self.window.title("GUI Example 02")

        self.input_txt = Entry(self.window, width=10)
        self.input_txt.focus()
        self.input_txt.grid(column=0, row=0)

        self.btn = Button(self.window, text="Click Me", command=self.clicked)
        self.btn.grid(column=1, row=0)

        self.output = StringVar(self.window)
        self.txt = Entry(self.window, width=30, textvariable=self.output, state="readonly")
        self.txt.grid(column=2, row=0)

    def clicked(self):
        res = "Hello " + self.input_txt.get()
        self.output.set(res)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    program = GUIProgram02()
    program.run()
