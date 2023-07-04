
__all__ = ['create_riddles_dictionary', 'guess_riddle']

def create_riddles_dictionary():
    riddles = {
        "Зимой и летом, одним цветом?": ["ель", "елка"],
        "Два кольца, два конца, а посередине гвоздик?": ["ножницы"],
        "На раскрашенных страницах, много праздников хранится?": ["календарь"],
    }
    return riddles

def guess_riddle(riddle, options, max_attempts):
    for attempt in range(1, max_attempts + 1):
        guess = input(f"Попытка {attempt}: Введите ваш ответ: ").strip().lower()
        if guess in options:
            print("Поздравляем, вы угадали!")
            return attempt
        print("Неверный ответ. Попробуйте еще раз.")
    print("Попытки исчерпаны. Вы не смогли отгадать загадку.")
    return 0
