def extract_digits(user_input):
    if type(user_input) is int:
        return [int(digit) for digit in str(user_input)]
    if type(user_input) is str:
        return [ord(letter)-ord('а')+1 for letter in user_input.lower()]



def magic_sum(numbers_list):
    s = sum(numbers_list)
    while s > 9:
        s = sum(extract_digits(s))
    return s


your_name = input("Введите свое имя: ")
print(f"Магическое число имени {your_name}: {magic_sum(extract_digits(your_name))}")
b_year = int(input('Введите год Вашего рождения: '))
b_month = int(input('Введите месяц Вашего рождения: '))
b_day = int(input('Введите числ Вашего рождения: '))
print(f"Магическое Вашего рождения: {magic_sum(extract_digits(b_day+b_month+b_year))}")
