import random


__all__ = ['number_guessing_game']

def number_guessing_game():
    lower_bound, upper_bound, max_attempts = map(int, input("Введите нижнюю границу, верхнюю границу и количество попыток (через пробел): ").split())
    secret_number = random.randint(lower_bound, upper_bound)
    for attempt in range(max_attempts):
        guess = int(input(f"Попытка {attempt + 1}/{max_attempts}. Угадайте число: "))
        if guess == secret_number:
            print("Поздравляем! Вы угадали число!")
            return True
        elif guess < secret_number:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")
    print(f"К сожалению, попытки исчерпаны. Загаданное число было: {secret_number}")
    return False

if __name__ == "__main__":
    number_guessing_game()
