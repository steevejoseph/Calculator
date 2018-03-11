import tkinter as tk
import math

# -*- coding: utf-6 -*-
"""Example Google style docstrings.


Hey Michael, thought I'd make a few edits.

Namely:

    * Tossed in some OO into the module, I think the Database App section covers that.
    * Adding some light documentation, since the topic really isn't covered in, well, anywhere.


Apparently Google has its own style guides for languages, even down to documentation.
Although doctrings aren't the MOST important thing right now, might as well pick up some good habits.
I deleted most of the blurbs that weren't crucial to this module, but left some nuggets.
Feel free to delete this. :)


This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension
    * Add Scientific and Normal Modes.

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html\

.. _Exact page where this was ripped from.
    http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html 🔥

.. _Numpy example is pretty lit as well. 🔥 🔥 🔥 
    http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html#example-numpy
"""


class Calculator(object):
    """The summary line for a class docstring should fit on one line.

    """

    def __init__(self, mode="Normal"):
        """Example of docstring on the __init__ method.

        The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.

        Either form is acceptable, but the two should not be mixed. Choose one
        convention to document the __init__ method and be consistent with it.

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            mode (str): Description of `mode`, either Scientific or Normal (default).
            param2 (:obj:`int`, optional): Description of `param2`. Multiple
                lines are supported.
            param3 (:obj:`list` of :obj:`str`): Description of `param3`.

        """

        self.mode = mode
        # minor optimization
        # apparently [] is 5x faster than list()
        # https://youtu.be/YjHsOrOOSuI?t=19m30s
        self.button = []
        """button: List of buttons."""

        self.numbers = ("789456123")
        """numbers: basic numberpad layout of ints"""

        self.root = tk.Tk()
        self.root.title('Michael\'s Calculator')

        self.menu = self.root.winfo_toplevel()
        self.root.menuBar = tk.Menu(self.menu)
        self.menu['menu'] = self.root.menuBar

        self.root.subMenu = tk.Menu(self.root.menuBar)
        self.root.menuBar.add_cascade(label='View', menu=self.root.subMenu)
        self.root.subMenu.add_command(label='Basic')
        self.root.subMenu.add_command(label='Scientific')

        self.display = tk.Entry(self.root, width=15)
        self.display.grid(row=0, column=0, columnspan=5)
        self.create_number_buttons()
        self.create_operation_buttons()

        self.root.mainloop()

    def create_input(self, index, num):
        self.display.insert(index, str(num))

    def clear_input(self, index):
        self.display.delete(0, index)

    def display_error(self):
        self.clear_input(len(self.display.get()))
        self.create_input(0, "Error")

    def calculate(self, equation, opcode):
        if (opcode == 0):
            try:
                self.total = eval(equation)
                self.clear_input(len(self.display.get()))
                self.create_input(0, self.total)
            except:
                self.display_error()
        elif (opcode == 1):
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
                if (total % 1 == 0):
                    self.create_input(0, int(total))
                else:
                    self.create_input(0, "%.8f" % total)
            except:
                self.display_error()

    def create_button(self, name, text, op, row, column):
        name = tk.Button(self.root, text=text, highlightbackground="#3E4149", padx=10, pady=10,
                         command=lambda: self.create_input(len(self.display.get()), op))
        name.grid(row=row, column=column)

    def create_number_buttons(self):
        i = 0
        for row in range(1, 4):
            for column in range(1, 4):
                self.button.append(
                    tk.Button(self.root, text=self.numbers[i], highlightbackground="#3E4149", padx=10, pady=10,
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
        self.equal_button = tk.Button(self.root, text="=", highlightbackground="#3E4149", padx=10, pady=10,
                                      command=lambda: self.calculate(self.display.get(), 0))
        self.equal_button.grid(row=4, column=3)

        # Clear
        self.clear_button = tk.Button(self.root, text="C", highlightbackground="#3E4149", padx=10, pady=10,
                                      command=lambda: self.clear_input(len(self.display.get())))
        self.clear_button.grid(row=1, column=0)

        # Negative
        self.neg_button = tk.Button(self.root, text="±", highlightbackground="#3E4149", padx=10, pady=10,
                                    command=lambda: self.create_input(len(self.display.get()), "-"))
        self.neg_button.grid(row=2, column=0)

        # Percent
        self.perc_button = tk.Button(self.root, text="%", highlightbackground="#3E4149", padx=10, pady=10,
                                     command=lambda: self.calculate(self.display.get(), 1))
        self.perc_button.grid(row=3, column=0)

        # Square root
        self.sqrt_button = tk.Button(self.root, text="√", highlightbackground="#3E4149", padx=10, pady=10,
                                     command=lambda: self.calculate(self.display.get(), 2))
        self.sqrt_button.grid(row=4, column=0)


def example_method(self, param1, param2):
    """Class methods are similar to regular functions.

    Note:
        Do not include the `self` parameter in the ``Args`` section.

    Args:
        param1: The first parameter.
        param2: The second parameter.
 
    Returns:
        True if successful, False otherwise.

    """
    return True


cal = Calculator()
