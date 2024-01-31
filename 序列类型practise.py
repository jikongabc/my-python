list1 = [32, 45, 22, 3, 12, 65, 1]
list1.sort()
print(list1)
print('max', end=':')
print(list1[6])
print('min', end=':')
print(list1[0])


list2 = [1, 2, 3, 4, 5]
list2.sort(reverse=True)
print(list2)

list3 = ['python', 'C', 'C++', 'Go', 'java']
list4 = [list3[0], list3[4]]
print('$'.join(list4))

print(len(list1))
list2.append(list1[6])
print(list2)
del list2[0]
print(list2)

# practise
print(list3[1:3:])
list3.insert(4, 'J_S')
print(list3)
print(list3.index('java'))
print(list2.count(1))

list5 = [1, 2, 3, 4, [5, 6]]
list6 = list5.copy()
import copy as cp

list7 = cp.deepcopy(list5)
del list5[4][1]
print(list5)
print(list6)
print(list7)
