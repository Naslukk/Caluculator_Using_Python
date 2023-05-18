from tkinter import *

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.display = Entry(master, width=25, justify=RIGHT, font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        self.create_button("1", 1, 0)
        self.create_button("2", 1, 1)
        self.create_button("3", 1, 2)
        self.create_button("+", 1, 3)

        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("-", 2, 3)

        self.create_button("7", 3, 0)
        self.create_button("8", 3, 1)
        self.create_button("9", 3, 2)
        self.create_button("*", 3, 3)

        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("C", 4, 2)
        self.create_button("/", 4, 3)

        self.create_button("=", 5, 0, columnspan=4)

    def create_button(self, text, row, column, columnspan=1, padx=5, pady=5):
        button = Button(self.master, text=text, padx=padx, pady=pady, command=lambda: self.button_click(text))
        button.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady)

    def button_click(self, text):
        if text == "C":
            self.display.delete(0, END)
        elif text == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(END, text)

root = Tk()
calculator = Calculator(root)
root.mainloop()
