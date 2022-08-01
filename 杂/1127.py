from math import sqrt

count = 0


# for i in range(1000, 10000):
#     a = int(str(i)[0])
#     b = int(str(i)[1:2])
#     c = int(str(i)[2:3])
#     d = int(str(i)[3:])
#     if len({a, b, c, d}) == 3:
#         count += 1
#
# print(count)

str = 'helloworld'
for i in range(len(str)):
    newStr = str[:i] + str[i+1:]
    print(newStr)
