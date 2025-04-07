def find_first_negative(lst):
    a = 0
    while a<len(lst):       # loop through individual items of list using while loop
        if lst[a] < 0:      # using if loop to check if item of list is negative
            return lst[a]    
            break           # if yes, return value and break the while loop
        a += 1             
        if a == len(lst):   # when index = length of list, finish looping through the list
            return "No negatives"

find_first_negative([3, 5, -1, 7, -2, 8])  #Task 2 Q1
find_first_negative([2, 10, 7, 0])         #Task 2 Q2
