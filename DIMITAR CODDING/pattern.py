p1 = 1

for i in range(0, 9):
    for j in range(1, i + 1):
        print(i, end=' ')
        i = i + 1
    print()

##################################
# name = 'Mario'
# k = ''
#
# for i in range(len(name)):
#     current_value = i
#     for j in range(current_value, i + 1):
#         k += name[j]
#     print(k)