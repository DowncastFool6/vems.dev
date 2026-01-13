if __name__=="__main__":
    total = 0

    for number in range(1,51):
        if number % 2 == 0:
            total += number
    
    print(f"The sum of all even numbers between 1 and 50 is: {total}")