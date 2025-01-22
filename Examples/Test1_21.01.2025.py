# ЗАДАНИЕ: Простое математическое приложение (Калькулятор)
# Напишите программу, которая выполняет базовые математические операции:
# +, -, *, /
# Программа должна запрашивать у пользователя два числа и операцию, а затем выводить результат.

Result = 0
Operations = ['+', '-', '*', '/']

def err():
	print('Ошибка ввода  данных')
	exit()

def Calculation():
	try:
		print('Введите первое число:')
		x = input()
		x = float(x)
	except:
		err()

	try:
		print('Введите операцию(+, -, *, /):')
		o = input()
		if o in Operations:
			print('Знак  операции введен верно')
		else:
			err()
	except:
		err()

	try:
		print('Введите второе число:')
		y = input()
		y = float(y)
	except:
		err()

	if o == '+':
		return x + y
	elif o == '-':
		return x - y
	elif o == '*':
		return x * y
	else:
		if y == 0:
			print('Делить на ноль нельзя')
			return 0
		else:
			return x / y

Result = Calculation()
print(Result)
