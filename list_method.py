numbers = [10, 20, 30, 5, 8, 9, 29]
numbers.append(100)
numbers.insert(6, 99)
numbers.pop()
numbers.reverse()
#numbers.clear()
print(numbers)
print(99 in numbers)
numbers.append(5)
print(numbers.count(5))
numbers.sort()
print(numbers)
numbers2 = numbers.copy()
print(numbers2)