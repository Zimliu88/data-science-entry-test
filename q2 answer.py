
def find_and_replace(lst, find_val, replace_val):
    if type(lst) == list:
        a = 0 
        while a<len(lst):             #using variable a in a loop to call out individual items in the list
            if lst[a]== find_val:
                lst[a] = replace_val  #replace item in list with replace_val if it matches find_val
            a += 1
        return lst
    else:
        print("Error: Function argument lst needs to be a list")

find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)                           #Task 2 Q1
find_and_replace(["apple", "banana", "apple"], "apple", "orange")    #Task 2 Q2
