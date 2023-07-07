def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return -1

print(linear_search([4, 5, 3, 7, 2], 7))