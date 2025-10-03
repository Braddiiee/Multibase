#1010101

def evaluate(binary, negative = False):

    binary = str(binary)
    binaryCount = len(str(binary))
    
    digits = []
    counter = 0

    if binaryCount > 0:

        for number in str(binary):

            if number not in ["0", "1"]: 
                counter += 1
            else:
                binaryCount -= 1
                digit = int(number) * pow(2, binaryCount)
                digits.append(int(digit))

        if counter > 0:
            print("Invalid binary operation. JS ")


        if negative == False:
            return(sum(digits))
        else:
            return( (sum(digits))  * -1)

    else:
        print("Invalid amount of digits.")
