def string_reverse(s):
    if type(s) == str:   #check if input is a string
        s = s[::-1]      #reverse string through slice syntax, starting from end of string to start of string using negative step -1
        return s
    else:
        print("Error: Function argument s needs to be a string")

string_reverse("Hello World") #Task 2 Q1
string_reverse("Python")      #Task 2 Q2
