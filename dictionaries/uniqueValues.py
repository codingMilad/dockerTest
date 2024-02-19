D1 = {'list1': [4, 7, 10, 20], 
      'list2': [7, 16, 9, 10], 
      'list3': [13, 10, 4, 8], 
      'list4': [7, 20, 6, 11]}

# def unique():
#   list = []
#   for i in D1:
#     if D1[i] not in list:
#       list.append(D1[i])
#     else:
#       list.remove(D1[i])
#   return list

# print(unique())

uniqueVals = list({val2 for val1 in D1.values() for val2 in val1 })

print(uniqueVals)
