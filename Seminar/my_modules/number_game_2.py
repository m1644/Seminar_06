import random
import argparse


__all__ = ['number_guessing_game']

def number_guessing_game(lower_bound, upper_bound, max_attempts):
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
    parser = argparse.ArgumentParser(description="Игра в угадывание числа.")
    parser.add_argument("lower_bound", type=int, help="Нижняя граница диапазона")
    parser.add_argument("upper_bound", type=int, help="Верхняя граница диапазона")
    parser.add_argument("max_attempts", type=int, help="Количество попыток")
    args = parser.parse_args()

    number_guessing_game(args.lower_bound, args.upper_bound, args.max_attempts)
