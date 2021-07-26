prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90, 70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29, 8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]

#_______A
#_______Вариант 1

print(f"\n\n{'*' * 35} A_1\n")

for i in prices:
    rub, kop = str(f"{i:.2f}").split(".")
    print(f"{rub} руб {int(kop):02d} коп,", end=" ")

#_______Вариант 2

print(f"\n\n{'*' * 35} A_2\n")

for i in prices:
    rub, kop = int(i // 1), int(f"{i % 1:.02f}"[2:])
    print(f"{rub} руб {kop:02d} коп,", end=" ")

#_______B

print(f"\n\n{'*' * 35} B\n")
print(f"ID base: {id(prices)} - {prices}")
prices.sort()
print(f"ID change: {id(prices)} - {prices}")

#_______C & D

print(f"\n{'*' * 35} C & D\n")
n_list = sorted(prices, reverse=True)
print(f"ID change: {id(n_list)} - {n_list}\n{n_list[:5][::-1]}")