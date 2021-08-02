#_____вариант 1

def thesaurus(*args):
    names_dict = {}
    for i in sorted(args):
        letter = i[0]
        if letter in names_dict:
            names_dict[letter] += [i]
        else:
            names_dict[letter] = [i]

    return names_dict


print(thesaurus("Иван", "Мария", "Петр", "Ярослав", "Фаина", "Артём", "Ксения"))



#_____вариант 2

def thesaurus(*args):
    main_list = {}
    for i in sorted(args):
        if i[0] not in main_list:
            main_list[i[0]] = list(filter(lambda element: element.startswith(i[:1]), args))
    print(main_list)


thesaurus("Пётр", "Барбара", "Максим", "Марго", "Илья", "Анжела", "Даниил", "Лариса" )