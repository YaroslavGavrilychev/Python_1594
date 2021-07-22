day_sales = []
sum_num = 0
all_sum = 0

for i in range(1, 1000, 2):
    day_sales.append(i ** 3)

print(day_sales)

def a(num):
    cur_sum = 0
    for sym in str(num):
        cur_sum += int(sym)
    return  cur_sum % 7 == 0

for item in day_sales:
    if a(item):
        sum_num += item

print(sum_num)

for index in range(len(day_sales)):
    day_sales[index] += 17
    if a(day_sales[index]):
        all_sum += day_sales[index]

print(day_sales)
print(all_sum)