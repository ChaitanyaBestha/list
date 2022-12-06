numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
min=1000
a=len(numbers)
i=0
while i<a:
    if numbers[i]<min:
        min=numbers[i]
    i=i+1
print(min)