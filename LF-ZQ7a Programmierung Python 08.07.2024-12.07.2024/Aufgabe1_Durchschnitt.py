numbersArr = [3,6,12,67,54]
total = 0
average = 0

if len(numbersArr) != 0:
    for i in numbersArr:
        total += i
    average = total / len(numbersArr)      
    print(average)
    
else:
    print("Array is empty")