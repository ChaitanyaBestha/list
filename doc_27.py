# Given 3 digits a, b, and c. The task is to find all the possible combinations from these digits.
# Examples:
# Input: [1, 2, 3]
# Output:
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1


# a=[1,2,3]
# a=[0,9,8]
# for i in range(len(a)):
#     for j in range(len(a)):
#         for k in range(len(a)):
#             if a[i]!=a[j] and a[j]!=a[k] and a[k]!=a[i]:
#                 print(a[i],a[j],a[k])
a=[0,7,8]
i=0
while i<len(a):
    print(a[i])
    i=i+1
    j=0
    while j<len(a):
        if a[i]!=a[j]:
            print(a[j])
        j=j+1
        k=0
        while k<len(a):
            if a[i]!=a[k] and a[j]!=a[k]:
                print(a[k]) 
            k=k+1          

            
