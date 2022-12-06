# list1 = [1,2,3,4,5,6]
# list2 = [2,3,1,0,6,7]
# diff=set(list1)-set(list2)
# print(diff) 

values = [[3, 4, 5, 1], [33, 6, 1, 2]]
v = values[0][0]
for row in range(0, len(values)):
    for column in range(0, len(values[row])):
        if v < values[row][column]:
            v = values[row][column]

