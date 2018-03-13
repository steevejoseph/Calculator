import tkinter as tk
from tkinter import CENTER
import math
import scientific


class Basic(object):
    def __init__(self, mode="Normal"):
        self.mode = mode
        self.button = []

        self.numbers = "789456123"

        self.root = tk.Tk()
        self.root.title('Calculator')
        self.root.resizable(0, 0)

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.view = tk.Menu(self.menu)
        self.menu.add_cascade(label='View', menu=self.view)
        self.view.add_command(label='Basic', command=lambda: self.change_mode(0))
        self.view.add_command(label='Scientific', command=lambda: self.change_mode(1))
        self.view.add_command(label='Close', command=lambda: self.root.destroy())

        self.help = tk.Menu(self.menu)
        self.menu.add_cascade(label='Help', menu=self.help)
        self.help.add_command(label='About', command=lambda: self.display_help())


        self.display = tk.Entry(self.root, width=15)
        self.display.grid(row=0, column=0, columnspan=5)
        self.create_number_buttons()
        self.create_operation_buttons()

        self.root.mainloop()

    def change_mode(self, mode):
        if mode == 0:
            self.root.destroy()
            calculator = Basic()
        else:
            self.root.destroy()
            calculator = scientific.Scientific()

    def display_help(self):
        self.help = tk.Tk()

        self.help.title('About')

        self.author_text = tk.Label(self.help, text='Author: Michael Burleson', justify=CENTER)
        self.author_text.grid(row=0, column=0)
        self.text = tk.Label(self.help, text='This calculator was created using\n the python package, tkinter.\n To change modes, '
                                  'select the \'view\' menu\n and select the desired mode.\nThank you!\n')
        self.text.grid(row=1, column=0)

        self.close_button = tk.Button(self.help, text='Close', justify=CENTER, command=lambda: self.help.destroy())
        self.close_button.grid(row=2, column=0)

        self.help.mainloop()

    def create_input(self, index, num):
        self.display.insert(index, str(num))

    def clear_input(self, index):
        self.display.delete(0, index)

    def display_error(self):
        self.clear_input(len(self.display.get()))
        self.create_input(0, "Error")

    def calculate(self, equation, opcode):
        if opcode == 0:
            try:
                self.total = eval(equation)
                self.clear_input(len(self.display.get()))
                self.create_input(0, self.total)
            except:
                self.display_error()
        elif opcode == 1:
            try:
                self.entry = float(self.display.get())
                self.clear_input(len(self.display.get()))
                self.create_input(0, (self.entry / 100))
            except:
                self.display_error()
        elif opcode == 2:
            try:
                self.entry = float(self.display.get())
                self.clear_input(len(self.display.get()))
                total = math.sqrt(self.entry)
                if total % 1 == 0:
                    self.create_input(0, int(total))
                else:
                    self.create_input(0, "%.8f" % total)
            except:
                self.display_error()

    def create_button(self, name, text, op, row, column):
        name = tk.Button(self.root, text=text, padx=10, pady=10,
                         command=lambda: self.create_input(len(self.display.get()), op))
        name.grid(row=row, column=column)

    def create_number_buttons(self):
        i = 0
        for row in range(1, 4):
            for column in range(1, 4):
                self.button.append(
                    tk.Button(self.root, text=self.numbers[i], padx=10, pady=10,
                              command=lambda x=self.numbers[i]: self.create_input(len(self.display.get()), x)))
                self.button[i].grid(row=row, column=column, padx=1, pady=1)
                i += 1

        # Number 0
        self.create_button("zero_button", "0", "0", 4, 1)

        # Decimal
        self.create_button("dec_button", ".", ".", 4, 2)

    def create_operation_buttons(self):
        # Addition
        self.create_button("add_button", "+", "+", 4, 4)

        # Subtraction
        self.create_button("sub_button", "-", "-", 3, 4)

        # Division
        self.create_button("div_button", "÷", "/", 1, 4)

        # Multiplication
        self.create_button("mult_button", "x", "*", 2, 4)

        # Equal
        self.equal_button = tk.Button(self.root, text="=", padx=10, pady=10,
                                      command=lambda: self.calculate(self.display.get(), 0))
        self.equal_button.grid(row=4, column=3)

        # Clear
        self.clear_button = tk.Button(self.root, text="C", padx=10, pady=10,
                                      command=lambda: self.clear_input(len(self.display.get())))
        self.clear_button.grid(row=1, column=0)

        # Negative
        self.neg_button = tk.Button(self.root, text="±", padx=10, pady=10,
                                    command=lambda: self.create_input(len(self.display.get()), "-"))
        self.neg_button.grid(row=2, column=0)

        # Percent
        self.perc_button = tk.Button(self.root, text="%", padx=10, pady=10,
                                     command=lambda: self.calculate(self.display.get(), 1))
        self.perc_button.grid(row=3, column=0)

        # Square root
        self.sqrt_button = tk.Button(self.root, text="√", padx=10, pady=10,
                                     command=lambda: self.calculate(self.display.get(), 2))
        self.sqrt_button.grid(row=4, column=0)