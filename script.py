
def get_year_ending(number):
    number = number % 100
    if 21 > number > 4:
        return 'лет'

    number = number % 10

    if number == 1:
        return 'год'
    if 1 < number < 5:
        return 'года'
    return 'лет'
