list=[2,4,9,7,6,3]
max=0
s_max=0
t_max=0
min=10000
s_min=10000
t_min=10000
i=0
while i<len(list):
    if list[i]>max:
        max=list[i]
    if list[i]<min:
        min=list[i]
    i=i+1
    k=max*min
i=0
while i<len(list):
    if list[i]>s_max and list[i]!=max:
        s_max=list[i]
    if list[i]<s_min and list[i]!=min:
        s_min=list[i]
    i=i+1
    l=s_max*s_min

i=0
while i<len(list):
    if list[i]>t_max and list[i]!=max and list[i]!=s_max:
        t_max=list[i]
    if list[i]<t_min and list[i]!=min and list[i]!=s_min:
        t_min=list[i]
    i=i+1
    m=t_max*t_min
n=k+l+m
print(n)