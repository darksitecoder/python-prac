lists = ['play', 'pause', 'stop']

# for x in range(len(lists)):
#     print(lists[x])

# x=0
# while x < len(lists):
#     print(lists[x])
#     x = x + 1

# [print(x) for x in lists]

# newlist = []
# for x in lists:
#     if 'u' in x:
#         newlist.append(x)

# print(newlist)

# newlist = [expression for item in iterable if condition == True]


newlist = [x for x in lists if 'u' in x]

print(newlist)