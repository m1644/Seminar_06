from my_modules.riddle_game_2 import create_riddles_dictionary, guess_riddle


''' Задание_5
Добавьте в модуль с загадками функцию, которая хранит словарь списков.
📌Ключ словаря - загадка, значение - список с отгадками.
📌Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.
'''


def main():
    riddles = create_riddles_dictionary()
    attempts = 3
    print(f"Загадки: \n{riddles.keys()}")
    print(f'Осталось попыток: {attempts}')

    for riddle, options in riddles.items():
        result = guess_riddle(riddle, options, attempts)

        if result > 0:
            print(f"Загадка отгадана с {result} попытки.")
        else:
            print("Вы исчерпали все попытки. Попробуйте еще раз!")

if __name__ == "__main__":
    main()
