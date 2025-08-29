def bread_selection(): 
    bread_list = ["White", "Brown", "Italian", "Granary"]
    count=0
    print("We have the following breads: ")
    while count < len(bread_list): # prints out each item on the list
        print(count+ 1, " ", bread_list[count])
        count += 1
    bread_selected=int(input("Which bread did you want? Enter a number"))
    return bread_list[bread_selected - 1 ] #returns back a string

#main program
print("Welcome to Sam's Sandwhich Shop")
bread_choice=bread_selection()# creating a variable that calls up the bread function and returns the choice
print(f"Your selected bread: {bread_choice}")