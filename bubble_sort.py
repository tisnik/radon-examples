def bubbleSort(sequence):
    for i in range(len(sequence)-1, 0, -1):
        for j in range(i):
            if sequence[j] > sequence[j+1]:
                sequence[j], sequence[j+1] = sequence[j+1], sequence[j]


numbers = [1, 2, 3, 4, 5]
bubbleSort(numbers)
print(numbers)

numbers = [5, 4, 3, 2, 1]
bubbleSort(numbers)
print(numbers)
