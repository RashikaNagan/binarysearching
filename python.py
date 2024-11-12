numbers = [2,5,7,3,45,21,67,85,23,12]

def binarysearching(n):
    numbers.sort()
    startingindex = 0
    endingindex = len(numbers) -1 
    middleindex = (startingindex +endingindex) // 2 #gives only the integer -> floor division
    while startingindex<=endingindex:
        middleindex = (startingindex +endingindex) // 2
        if n == numbers[middleindex]:
            return middleindex
        elif n>= numbers[middleindex]:
            startingindex = middleindex + 1
        elif n<= numbers[middleindex]:
            endingindex = middleindex - 1   
    return ("not found")
print(binarysearching(99))