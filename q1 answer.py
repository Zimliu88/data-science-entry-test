def swap(x,y):

    if (isinstance(x,int) & isinstance(y,int)): #check if x & y are integers
        x,y = y,x                               #swap value if both are integers
        print (x,y)
    else:
        return -1                               #if not function returns -1 value

swap("Apple", 10)                               #task 2 q1
swap(9, 17)                                     #task 2 q2