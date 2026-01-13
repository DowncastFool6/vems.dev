if __name__=="__main__":

    print(f"======= Enter 5 numbers for two sets. =======")
    first = input("Enter the first set: \n")
    
    #Takes the phrase entered by the user and splits the words into separate items stored in a list
    first_split = first.split()

    #Converts list to set and prints the set
    first_set = set(first_split)

    second = input("Enter the second set: \n")
    
    #Takes the phrase entered by the user and splits the words into separate items stored in a list
    second_split = second.split()

    #Converts list to set and prints the set
    second_set = set(second_split)
    print(f"\nFirst set of numbers: {first_set}")
    print(f"Second set of numbers: {second_set}")

    #Numbers is common
    common = first_set & second_set
    if len(common) == 0 :
        print("\nNo nummbers in common.")
    else:
        print(f"\nNumbers in common: {common}")

    #Difference in numbers
    difference = first_set - second_set
    if len(difference) == 0:
        print("\nNo nummbers in difference.")
    else:
        print(f"Difference in numbers: {difference}")

