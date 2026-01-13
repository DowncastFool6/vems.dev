if __name__=="__main__":

    code = input("Enter a promoption code: ").strip()

    if len(code)==10:
        if code.startswith("PROMO-"):
            if code [6 : 10].isdigit():
                print("Valid code. Discount applied!")
            else:
                print("Invalid code: the numeric part must have 4 digits.")
        else:
            print("Invalid code: does not start with 'PROMO-'")
    else:
        print("Invalid code: it must have 10 characters")

