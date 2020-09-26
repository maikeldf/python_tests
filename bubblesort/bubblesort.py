def bubblesort(list, reverse=0):
    lenght = len(list)
    for i in range(0, lenght-1):
        for j in range(0, lenght - i - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    
    if reverse:
        list.reverse()
    
    return list