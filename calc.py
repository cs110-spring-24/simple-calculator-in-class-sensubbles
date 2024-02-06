num1 = int(input("write down your first number: "))
op = input("write down your operation symbol: ")
num2 = int(input("write down your second number: "))

if op == "+":
	total = num1 + num2
	print(f"{num1} + {num2} is {total}")
if op == "-":
	total = num1 - num2
	print(f"{num1} - {num2} is {total}")
if op == "*":
	total = num1 * num2
	print(f"{num1} * {num2} is {total}")
if op == "/":
	total = num1 // num2
	print(f"{num1} / {num2} is {total}")
if op == "^":
	total = num1 ** num2
	print(f"{num1} to the power of {num2} is {total}")
if op == "//":
	total = num1 // num2
	print(f"the nearest integer of {num1} / {num2} is {total}")
if op == "%":
	total = num1 % num2
	print(f"The remainder of: {num1} / {num2} is {total}")