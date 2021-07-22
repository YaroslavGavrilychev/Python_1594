sec = int(input('Пожалуйста, введите время в секундах: '))
min = sec // 60
hours = min // 60
day = hours // 24
print(f"%02d дн %02d час %02d мин %02d сек " % (day, hours % 24, min % 60, sec % 60))