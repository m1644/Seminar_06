
__all__ = ['is_leap_year', 'is_valid_date']

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
