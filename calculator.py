# Author: Michael Burleson
import tkinter as tk
import math

# minor optimization 
# apparently [] is 5x faster than list()
# https://youtu.be/YjHsOrOOSuI?t=19m30s
button = []


numbers = ("789456123")

root = tk.Tk()
root.title('Michael\'s Calculator')

menu = root.winfo_toplevel()
root.menuBar = tk.Menu(menu)
menu['menu'] = root.menuBar

root.subMenu = tk.Menu(root.menuBar)
root.menuBar.add_cascade(label='View', menu=root.subMenu)
root.subMenu.add_command(label='Basic')
root.subMenu.add_command(label='Scientific')

def create_input(index, num):
	display.insert(index, str(num))

def clear_input(index):
	display.delete(0, index)

def display_error():
	clear_input(len(display.get()))
	create_input(0, "Error")

# Opcodes: 0 = basic operations, 1 = percent, 2 = square root
def calculate(equation, opcode):
	if(opcode == 0):
		try:
			total = eval(equation)
			clear_input(len(display.get()))
			create_input(0, total)
		except:
			display_error()
	elif(opcode == 1):
		try:
			entry = float(display.get())
			clear_input(len(display.get()))
			create_input(0, (entry/100))
		except:
			display_error()
	elif(opcode == 2):
		try:
			entry = float(display.get())
			clear_input(len(display.get()))
			total = math.sqrt(entry)
			if(total % 1 == 0):
				create_input(0, int(total))
			else:
				create_input(0, "%.8f" % total)
		except:
			display_error()

def create_button(name, text, op, row, column):
	name = tk.Button(root, text=text, highlightbackground="#3E4149", padx=10, pady=10, command=lambda: create_input(len(display.get()), op))
	name.grid(row=row, column=column)

def create_number_buttons():
	i = 0
	for row in range(1, 4):
		for column in range(1, 4):
			button.append(tk.Button(root, text=numbers[i], highlightbackground="#3E4149", padx=10, pady=10, command=lambda x = numbers[i]: create_input(len(display.get()), x)))
			button[i].grid(row=row, column=column, padx=1, pady=1)
			i += 1

	# Number 0
	create_button("zero_button", "0", "0", 4, 1)

	# Decimal
	create_button("dec_button", ".", ".", 4, 2)

def create_operation_buttons():
	# Addition
	create_button("add_button", "+", "+", 4, 4)

	# Subtraction
	create_button("sub_button", "-", "-", 3, 4)

	# Division
	create_button("div_button", "÷", "/", 1, 4)

	# Multiplication
	create_button("mult_button", "x", "*", 2, 4)

	# Equal
	equal_button = tk.Button(root, text="=", highlightbackground="#3E4149", padx=10, pady=10, command=lambda: calculate(display.get(), 0))
	equal_button.grid(row=4, column=3)

	# Clear
	clear_button = tk.Button(root, text="C", highlightbackground="#3E4149", padx=10, pady=10, command=lambda: clear_input(len(display.get())))
	clear_button.grid(row=1, column=0)

	# Negative
	neg_button = tk.Button(root, text="±", highlightbackground="#3E4149", padx=10, pady=10, command=lambda: create_input(len(display.get()), "-"))
	neg_button.grid(row=2, column=0)

	# Percent
	perc_button = tk.Button(root, text="%", highlightbackground="#3E4149", padx=10, pady=10, command=lambda: calculate(display.get(), 1))
	perc_button.grid(row=3, column=0)

	# Square root
	sqrt_button = tk.Button(root, text="√", highlightbackground="#3E4149", padx=10, pady=10, command=lambda: calculate(display.get(), 2))
	sqrt_button.grid(row=4, column=0)

display = tk.Entry(root, width=15)
display.grid(row=0, column=0, columnspan=5)
create_number_buttons()
create_operation_buttons()

root.mainloop()