# Converts a binary string to the intended integer (base-2).
from evaluate import evaluate 

def flipper(binary):
    digits = []
    counter = 0

    for number in binary:

        if number not in ["0", "1"]: 
                counter += 1
                break
        else:
            if number == "0":
                digits.append("1")
            else:
                digits.append("0")

    if counter > 0:
        print("Invalid binary operation. ")
        return None

    return "".join(digits)

def bin_to_twos(binary):

    # print(f"Regular Binary: {binary}")
    length = len(binary)

    ones_binary = flipper(binary)
    # print(f"One's Complement: {ones_binary}")

    ones_number = evaluate(ones_binary)
    # print(f"One's Number: {ones_number}")

    twos_number = ones_number + 1
    # print(f"Two's Number: {twos_number}")


    twos_binary = bin(twos_number)[2:]
    
    if len(twos_binary) < length:
         additional = length - len(twos_binary)
         zeros = "0" * additional
         twos_binary = zeros + twos_binary

    # print(f"Two's Binary: {twos_binary} \n")


    return twos_binary

def twos_to_bin(twos_complement):

    # print(f"Two's Complement: {twos_complement}")
    length = len(twos_complement)

    flipped_binary = flipper(twos_complement)
    # print(f"Flipped Binary: {flipped_binary}")

    flipped_number = evaluate(flipped_binary)
    # print(f"Flipped Number: {flipped_number}")

    original_number = flipped_number - 1
    # print(f"Original Number: {original_number}")


    original_binary = bin(original_number)[2:]
    
    if len(original_binary) < length:
         additional = length - len(original_binary)
         zeros = "0" * additional
         original_binary = zeros + original_binary

    # print(f"Original Binary: {original_binary} ")


    return original_binary



    

if __name__ == "__main__":
    bin_to_twos("1000")
    twos_to_bin("0110")