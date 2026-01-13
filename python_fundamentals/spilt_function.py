if __name__=="__main__":

    phrase = input("Enter a phrase: \n")
    print(f"\nPhrase: {phrase}")
    
    #Takes the phrase entered by the user and splits the words into separate items stored in a list
    split_phrase = phrase.split()

    #Converts list to set and prints the set
    phrase_set = set(split_phrase)
    print(f"\nPhrase stored in a set: {phrase_set}")

    if len(phrase_set) > 5:
        print(f"\nThe list in alphabetic order: {phrase_set}")
    else:
        removed_count = len(split_phrase) - len(phrase_set)
        print(f"\nNumber of repeated words removed: {removed_count}")
