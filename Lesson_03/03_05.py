"""
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх
списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

            Например:
#>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]


Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое
слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

"""
from random import randrange

def jokes(jokes_num,repeat=True):
    """Это документация на функцию"""
    joke_list = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    for i in range(jokes_num):
        print(joke_list)
        if repeat == True:
            joke = nouns[randrange(len(nouns))]+" "+adverbs[randrange(len(adverbs))]+" "+adjectives[randrange(len(adjectives))]
        else:
            try:
                joke = nouns.pop(randrange(len(nouns))) + " " + adverbs.pop(randrange(len(adverbs))) + " " + adjectives.pop(
                randrange(len(adjectives)))
            except ValueError:
                break
        joke_list.append(joke)
    return joke_list

print(jokes(9,False))

