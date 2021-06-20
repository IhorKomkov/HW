# class work
#<----------------------------------------->
# d = {3: 4, 15: 8, 13: 11, 8: 2}
# print (d)
# print (d.get(13))
# print (list(d.keys()))
# print (list(d.values()))


# task 1
#<----------------------------------------->
d = {3: 4, 15: 8, 13: 11, 8: 2}


#keys sum
# ansk = 0
# for i in d.keys():
#     ansk = ansk + i
# print (ansk)


#val sum
# ansv = 0
# for i in d.values():
#     ansv = ansv + i
# print (ansv)


#all sum
# ansall = 0
# for i in (list(d.keys()) + list(d.values())):
#     ansall = ansall + i
# print (ansall)

#all sum alternative
# ansall = 0
# for k, v in d.items():
#     ansall = ansall + k + v
# print (ansall)
