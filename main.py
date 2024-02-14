def remove_whitespace(string):
    return string.replace(" ", "")

def sign_of_number():
    sign = input("Enter a 0 or 1 for sign (0 means positive and 1 means negative):\n")

    if len(sign) > 1:
        print("The sign needs to be a single digit\n")
        sign_of_number()
    else:
        if sign == "0":
            print("Positive\n")
            return 1
        elif sign == "1":
            print("Negative\n")
            return -1
        else:
            print("The sign needs to be 0 or 1\n")
            sign_of_number()

            
def characteristic_of_number():
    decimal = 0
    while True:
        characters = (input("Enter an 11-digit binary number for the characteristic:\n"))
        characters = remove_whitespace(characters)
        if len(characters) != 11:
            print(f"The characteristic needs to be 11 digits.\nYour characteristic is {len(characters)} characters long.\n")
        else:
            valid_input = True
            for index, character in enumerate(characters):
                if character != "0" and character != "1":
                    print("The characteristic needs to be a binary number\n")
                    valid_input = False
                    break
                else:
                    if character == "1":
                        decimal += 2 ** (10 - index)
            if valid_input:
                break
    print(f"The 11 bit sequence represents the number {decimal}\nThe characteristic is {2**(decimal-1023)}\n")
    return 2**(decimal-1023)

def mantissa_of_number():
    decimal = 0
    while True:
        mantissa = (input("Enter an 52-digit binary number for the mantissa:\n"))
        mantissa = remove_whitespace(mantissa)
        if len(mantissa) != 52:
            print(f"The mantissa needs to be 52 digits.\nYour mantissa is {len(mantissa)} characters long.\n")
        else:
            valid_input = True
            for index, character in enumerate(mantissa):
                if character != "0" and character != "1":
                    print("The mantissa needs to be a binary number\n")
                    valid_input = False
                    break
                else:
                    if character == "1":
                        decimal += (0.5) ** (index+1)
            final_mantissa = 1+decimal
            if valid_input:
                break
    print(f"The mantissa is {decimal}\n")
    print(f"(1 + f) is {final_mantissa}\n")
    return final_mantissa

run_program = True

while run_program:
    print(f"The decimal number is: {sign_of_number()*characteristic_of_number()*mantissa_of_number()}\n\n")
    
