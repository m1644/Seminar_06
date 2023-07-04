import argparse


def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

def is_valid_date(date):
    day, month, year = map(int, date.split('.'))
    if year < 1 or year > 9999:
        return False
    if month < 1 or month > 12:
        return False
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        days_in_month[1] = 29
    if day < 1 or day > days_in_month[month - 1]:
        return False
    return True

def main():
    parser = argparse.ArgumentParser(description="Проверка даты")
    parser.add_argument('date', help="Введите дату в формате DD.MM.YYYY: ")
    args = parser.parse_args()
    if is_valid_date(args.date):
        print("Данная дата существует.")
        year = int(args.date.split('.')[2])
        if is_leap_year(year):
            print("Год является високосным.")
        else:
            print("Год не является високосным.")
    else:
        print("Данная дата не существует.")

if __name__ == '__main__':
    main()
