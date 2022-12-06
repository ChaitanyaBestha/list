# b_num = list(input("Input a binary number: "))
# value = 0
# for i in range(len(b_num)):
#     digit = b_num.pop()
#     if digit == '1':
#         value = value + pow(2, i)
# print("The decimal value of the number is", value)

n=["001011010","1011"]
a=len(n)
i=0
m=[]
k=0
while i<=a:
    b=n[i]%10
    k=k+b*2**i
    n=n//10
    m.append(k[i])
    i=i+1
print("the decimal value of number is:",m)