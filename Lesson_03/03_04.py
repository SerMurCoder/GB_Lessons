"""
*(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате
«Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные
по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
#>>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}

Как поступить, если потребуется сортировка по ключам?

"""


def thesaurus_adv(*list_1):
    """Comment, documentation"""
    th_dict = {}
    string: str
    surname_letter: str
    name_letter: str
    for string in list_1:
        names_set = string.split(' ')
        surname_letter = names_set[-1].upper()[:1]
        name_letter = names_set[0].upper()[:1]
        new_values = th_dict.get(surname_letter, {})
        new_subvalues = new_values.get(name_letter, [])
        new_subvalues.append(string)
        new_values.update({name_letter: new_subvalues})
        th_dict.update({surname_letter: new_values})
    return th_dict


print(thesaurus_adv('иван Иванов', 'Мария Петрова', 'Петр Сидоров', 'Илья Павлов', 'Ирина Пупкина', 'Павел сухов'))
