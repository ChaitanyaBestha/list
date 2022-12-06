numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
max=0
a=len(numbers)
i=0
while i<a:
    if numbers[i]>max:
        max=numbers[i]
    i=i+1
print(max)
        