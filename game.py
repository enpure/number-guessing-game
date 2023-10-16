import random

def is_valid(user_input, upper_bound):
    if user_input.isdigit():
        user_number = int(user_input)
        if 1 <= user_number <= upper_bound:
            return True
    return False

def main_game():
    upper_bound = int(input("Введите верхнюю границу диапазона (от 1 до n): "))
    random_number = random.randint(1, upper_bound)
    attempts = 0  # Инициализировать счетчик попыток

    while True:
        user_input = input(f"Введите число от 1 до {upper_bound}: ")
        attempts += 1  # Увеличивать счетчик попыток на 1 с каждой итерацией
        
        if not is_valid(user_input, upper_bound):
            print('А может быть все-таки введем целое число от 1 до {upper_bound}?')
            continue

        user_number = int(user_input)
        if user_number < random_number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif user_number > random_number:
            print('Ваше число больше загаданного, попр
