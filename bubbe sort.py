def bubbleSort(list):
    for passnum in range(len(list)-1,0,-1):
        sorted = True
        for i in range(passnum):
                if list[i]>list[i+1]:
                    temp = list[i]
                    list[i] = list[i+1]
                    list[i+1] = temp
                    sorted = False

        if sorted == True:
            break

list = [1, 2, 4, 3, 5, 6]
bubbleSort(list)

print(list)

