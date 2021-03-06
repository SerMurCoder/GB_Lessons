"""
*(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с
числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
#>>> num_translate_adv("One")
"Один"
#>>> num_translate_adv("two")
"два"

"""


"""
Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
#>>> num_translate("one")
"один"
#>>> num_translate("eight")
"восемь"

Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для
перевода: какой тип данных выбрать, в теле функции или снаружи.

"""


def num_translate(input_str):
    numbers_dict = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    result = numbers_dict.get(input_str.lower(),'None')
    if result != 'None' and input_str[:1] == input_str[:1].upper():
        result = result[:1].upper() + result[1:]
    return result


print(num_translate("TeN"))
