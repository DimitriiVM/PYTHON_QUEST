def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка ввода! Введите корректное число.")

def get_operation():
    operations = ['+', '-', '*', '/']
    while True:
        operation = input("Введите операцию (+, -, *, /): ")
        if operation in operations:
            return operation
        print("Ошибка ввода! Введите одну из операций: +, -, *, /.")

def calculate(x, y, operation):
    if operation == '+':
        return x + y
    elif operation == '-':
        return x - y
    elif operation == '*':
        return x * y
    elif operation == '/':
        if y == 0:
            return "Ошибка: деление на ноль."
        return x / y

def main():
    print("Простое математическое приложение (Калькулятор)")
    x = get_number("Введите первое число: ")
    operation = get_operation()
    y = get_number("Введите второе число: ")
    result = calculate(x, y, operation)
    print(f"Результат: {result}")

if __name__ == "__main__":
    main()
