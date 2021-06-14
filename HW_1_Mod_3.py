# task 1
#<----------------------------------------->
#l = []
#i = 1
#while i <= 5:
#    l.append(i)
#    i += 1
#<----------------------------------------->
#delete first and second func remove
#l.remove(1)
#l.remove(5)
#print (l)
#<----------------------------------------->
#delete first and second func pop
#l.pop(0)
#l.pop(len(l)-1)
#print (l)
#<----------------------------------------->
#delete first and second slise
#l_new = l[1:len(l)-1]
#print (l_new)

# task 2
#<----------------------------------------->
#l = [i for i in range(10, 21)]
#print(l)

# task 2
#<----------------------------------------->
# l = []
# for i in range(1,11):
#     if i < 4:
#         l.append(1)
#     elif i < 7:
#         l.append(2)
#     else:
#         l.append(3)
# print(l)

# task 3
#<----------------------------------------->
# l = [1 if i == 3 else i for i in range(1,4)] + [i for i in range(1,4)] * 2
# print(l)

# task 4
#<----------------------------------------->
# l = [1 if i == 3 else i for i in range(1,4)] + [i for i in range(1,4)] * 2
# ans = 0
# for i in l:
#     ans = ans + i
# print(ans)

# task 5
#<----------------------------------------->
# l1 = [1 if i == 3 else i for i in range(1,4)]
# l2 = [i for i in range(1,4)] * 2
# l3 = [i for i in range(1,10) if i % 2 == 0]
#
# el = [l1, l2, l3]
# l = []
# for i in el:
#     n = 0
#     for j in i:
#         if j == 2:
#             n += 1
#     l.append(n)
# print(l)

# task 6
#<----------------------------------------->
# l1 = [1 if i == 2 else i for i in range(1,4)]
# l2 = [i for i in range(1,4)] * 2
# l3 = [i for i in range(1,10) if i % 2 == 0]
# l4 = [0 if i == 2 else i for i in range(1,10)]
#
# el = [l1, l2, l3, l4]
# l = []
"""way 1"""
# for i in el:
#     if 2 not in i:
#         l.append(el.index(i))
# print(l)
"""way 2"""
# for i, val in enumerate(el):
#     if 2 not in val:
#         l += [i]
# print(l)

# task 7
#<----------------------------------------->
tu = (100, 'USA', 318.4)
ntu = tuple(list(tu) + ['j'])

print(ntu)
