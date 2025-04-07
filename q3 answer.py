def update_dictionary(dct, key, value):
    if key in dct:       # using if to sort if key already exist in dictionary
        print(dct[key])  # print oringal value if key exist
        dct[key]=value   # update value to defined new value
    else:
        dct[key]=value   # if key does not exist, define new key-value pair in dictionary
    return dct

update_dictionary({}, "name", "Alice")    #Task 2 Q1
update_dictionary({"age": 25}, "age", 26) #Task 2 Q2
