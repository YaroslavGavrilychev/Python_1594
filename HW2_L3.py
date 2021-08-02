tr_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(word):
    if word.istitle():
        return str(tr_dict.get(word.lower())).title()
    return tr_dict.get(word)


print(num_translate(input("Enter any number: ")))