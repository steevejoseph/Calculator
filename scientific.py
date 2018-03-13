import tkinter as tk
from tkinter import CENTER
import math
import basic


class Scientific(object):

    def __init__(self, mode="Scientific"):

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

        self.display = tk.Entry(self.root, width=25)
        self.display.grid(row=0, column=0, columnspan=10)

        self.help = tk.Menu(self.menu)
        self.menu.add_cascade(label='Help', menu=self.help)
        self.help.add_command(label='About', command=lambda: self.display_help())

        self.create_number_buttons()
        self.generate_operation_buttons()

        self.root.mainloop()

    def change_mode(self, mode):
        if mode == 0:
            self.root.destroy()
            calculator = basic.Basic()
        else:
            self.root.destroy()
            calculator = Scientific()

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

    def calculate(self, equation, opcode, opnum):
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
                if opnum == 0:
                    total = math.sqrt(self.entry)
                elif opnum == 1:
                    total = math.sin(self.entry)
                elif opnum == 2:
                    total = math.cos(self.entry)
                elif opnum == 3:
                    total = math.tan(self.entry)
                elif opnum == 4:
                    total = math.asin(self.entry)
                elif opnum == 5:
                    total = math.acos(self.entry)
                elif opnum == 6:
                    total = math.atan(self.entry)
                elif opnum == 7:
                    total = math.pow(math.e, self.entry)
                elif opnum == 8:
                    total = math.log10(self.entry)
                elif opnum == 9:
                    total = math.log(self.entry)
                elif opnum == 10:
                    total = math.pow(self.entry, 2)
                elif opnum == 11:
                    total = math.pow(self.entry, -1)
                elif opnum == 12:
                    total = math.degrees(self.entry)
                elif opnum == 13:
                    total = math.radians(self.entry)
                if total % 1 == 0:
                    self.create_input(0, int(total))
                else:
                    self.create_input(0, "%.8f" % total)
            except:
                self.display_error()
        elif opcode == 3:
            self.clear_input(len(self.display.get()))
            self.create_input(len(self.display.get()), 3.14159265)

    def create_button(self, text, op, row, column):
        button = tk.Button(self.root, text=text, padx=10, pady=10,
                         command=lambda: self.create_input(len(self.display.get()), op))
        button.grid(row=row, column=column)

    def create_operation_button(self, text, opcode, opnum, row, column):
        button = tk.Button(self.root, text=text, padx=10, pady=10,
                           width=5, command=lambda: self.calculate(self.display.get(), opcode, opnum))
        button.grid(row=row, column=column)

    def create_number_buttons(self):
        i = 0
        for row in range(2, 5):
            for column in range(5, 8):
                self.button.append(
                    tk.Button(self.root, text=self.numbers[i], padx=10, pady=10,
                              command=lambda x=self.numbers[i]: self.create_input(len(self.display.get()), x)))
                self.button[i].grid(row=row, column=column, padx=1, pady=1)
                i += 1

        # Number 0
        self.create_button("0", "0", 5, 5)

        # Decimal
        self.create_button(".", ".", 5, 6)

    def generate_operation_buttons(self):
        # Addition
        self.create_button("+", "+", 5, 8)

        # Subtraction
        self.create_button("-", "-", 4, 8)

        # Division
        self.create_button("÷", "/", 3, 8)

        # Multiplication
        self.create_button("x", "*", 2, 8)

        # Equal
        self.equal_button = tk.Button(self.root, text="=", padx=10, pady=10,
                                      command=lambda: self.calculate(self.display.get(), 0, 0))
        self.equal_button.grid(row=5, column=7)

        # Clear
        self.clear_button = tk.Button(self.root, text="C", padx=10, pady=10,
                                      command=lambda: self.clear_input(len(self.display.get())))
        self.clear_button.grid(row=2, column=4)

        # Negative
        self.neg_button = tk.Button(self.root, text="±", padx=15, pady=10,
                                    command=lambda: self.create_input(len(self.display.get()), "-"))
        self.neg_button.grid(row=3, column=4)

        # Percent
        self.perc_button = tk.Button(self.root, text="%", padx=10, pady=10,
                                     command=lambda: self.calculate(self.display.get(), 1, 0))
        self.perc_button.grid(row=4, column=4)

        # Square root
        self.sqrt_button = tk.Button(self.root, text="√", padx=10, pady=10,
                                     command=lambda: self.calculate(self.display.get(), 2, 0))
        self.sqrt_button.grid(row=5, column=4)

        sin_button = self.create_operation_button("sin", 2, 1, 2, 0)
        cos_button = self.create_operation_button("cos", 2, 2, 2, 1)
        tan_button = self.create_operation_button("tan", 2, 3, 2, 2)
        arcsin_button = self.create_operation_button("arcsin", 2, 4, 3, 0)
        arccos_button = self.create_operation_button("arccos", 2, 5, 3, 1)
        arctan_button = self.create_operation_button("arctan", 2, 6, 3, 2)
        euler_button = self.create_operation_button("e**x", 2, 7, 4, 0)
        log_button = self.create_operation_button("log", 2, 8, 4, 1)
        ln_button = self.create_operation_button("ln", 2, 9, 4, 2)
        square_button = self.create_operation_button("x**2", 2, 10, 5, 0)
        inverse_button = self.create_operation_button("x**-1", 2, 11, 5, 1)

        # Pi
        pi_button = tk.Button(self.root, text="π", padx=10, pady=10,
                              width=5, command=lambda: self.calculate(self.display.get(), 3, 0))
        pi_button.grid(row=5, column=2)