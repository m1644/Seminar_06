
__all__ = ['create_riddles_dictionary', 'guess_riddle', 'add_result', 'print_results']

_RESULTS = {}

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

def add_result(riddle, attempt):
    _RESULTS[riddle] = attempt

def print_results():
    print('------------------------')
    print("Результаты угадывания:")
    for riddle, attempt in _RESULTS.items():
        print(f"Загадка: {riddle}")
        print(f"Отгадана с попытки: {attempt}")
        print()
