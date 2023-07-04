
__all__ = ['guess_riddle']

def guess_riddle(riddle, options, attempts):
    for attempt in range(1, attempts + 1):
        guess = input(f"Попытка {attempt}: Введите ваш ответ: ").strip().lower()
        if guess in options:
            print("Поздравляем, вы угадали!")
            return attempt
        print("Неверный ответ. Попробуйте еще раз.")
    print("Попытки исчерпаны. Вы не смогли отгадать загадку.")
    return 0
