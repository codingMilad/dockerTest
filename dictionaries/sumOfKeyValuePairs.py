# D1 = {2: 8, 5: 20, 3: 15}
# #gives back the sum of the value
# def total():
#   sum = 0
#   for i, j in D1.items():
#     sum += j
#   return sum

# print(total())

#gives back the sum of key value pair
D1 = {2: 8, 5: 20, 3: 15}
total = []

for i in D1:
  total.append(i + D1[i])
print(total)


