# list
# fruits = ['apple', 'orange', 'banana']
# print(fruits[1].title())
# fruits[2] = 'strawberry';
# print(fruits)
# fruits.append('watermelon')
# print(fruits)
# fruits.insert(2, 'banana')
# print(fruits)
# del fruits[1]
# print(fruits)
# need = fruits.pop()
# print(fruits)
# print(need)
# fruits.remove('banana')
# print(fruits.__len__())

# sort
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort(reverse=True)
# print(cars)
# print(sorted(cars, reverse=False))
# print(cars)
# cars.reverse()
# print(cars)
# print(len(cars))
# print(cars[-1])

# for
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# for car in cars:
#     print("car name: " + car)
#
# for num in range(1, 6):
#     print("num: " + str(num))
#
# nums = list(range(1, 11, 5))
# for n in nums:
#     print("nums include: " + str(n))
#
# squares = []
# for value in range(1, 11):
#     value = value ** 2
#     squares.append(value)
# print(squares)
# print(min(squares))
# print(max(squares))
# print(sum(squares))
#
# arr = [value ** 2 for value in range(1, 21)]
# print(arr)
# total = range(1, 10000001)
# print(sum(total))
# part = total[100:110]
# for p in part:
#     print(p)
# copy = arr[:]
# copy.insert(0, 99)
# print(copy)

tuple = (11, 22)
print(tuple)
print(tuple[1])

seq = range(1, 10)
for s in seq:
    if s % 3 == 1:
        print("mod 1:" + str(s))
    elif s % 3 == 2:
        print("mod 2:" + str(s))
    else:
        print("mod 3:" + str(s))