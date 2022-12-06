list=['9',10.8,19,2,'6']
sum=0
i=0
while i<len(list):
    if type(list[i])==str:
        sum=sum+int(list[i])
    else:
        sum=sum+list[i]
    i=i+1
print(sum) 
print(int(sum))   

