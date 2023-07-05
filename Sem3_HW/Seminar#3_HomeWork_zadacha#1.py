#Zadacha #1

def find_dubles(array: list):
    search = set([i for i in array if array.count(i) > 1])
    return list(search)


print(find_dubles([1, 2, 3, 1, 2, 1, 2, 4, 5]))

