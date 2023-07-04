from my_modules.riddle_game_3 import create_riddles_dictionary, guess_riddle, add_result, print_results


''' Задание_6
Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки, с которой она угадана).
📌Функция формирует словарь с информацией о результатах отгадывания.
📌Для хранения используйте защищённый словарь уровня модуля.
📌Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
📌Для формирования результатов используйте генераторное выражение.
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
        add_result(riddle, result)
    print_results()

if __name__ == "__main__":
    main()
