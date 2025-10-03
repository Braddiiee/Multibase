import sys

def convert(value, from_base, to_base):

    if from_base == 0:
        num = ord(value)
    else:
        num = int(value, from_base)

    def to_bin(): return bin(num)
    def to_oct(): return oct(num)
    def to_hex(): return hex(num)
    def to_chr(): return chr(num)
    def to_ord(): return ord(num)
    def to_int(): return num

    switch = {
        2 : to_bin,
        8 : to_oct,
        16 : to_hex,
        0: to_chr,
        -1: to_ord,
        10 : to_int
    }

    try:
        return switch[to_base](num)
    except Exception as e:
        return f"Error: {e}"



def get_bases():
    arg = sys.argv[1:]
    while len(arg) != 2:
        print("Please enter a valid argument.\n -> python to-spec.py [from-base] [to-base] ")
        initial_base = input("Enter your initial base: ")
        second_base = input("Enter your additional base: ")
        arg = [initial_base, second_base]
    return arg
    

def get_value(): 
    while True:
        chars = input("What is your input? ")
        if chars:
            return chars
        print("You did not enter any input. Please try again.")


# def get_codes(text, characters):
#     char_codes = []
#     for char in text:
#         found = False
#         for item in characters:
#             if char == item["char"]:
#                 char_codes.append(item["code"])
#                 found = True
#                 break
#         if not found:
#             print(f"Unrecognized character ${char}")
#     return char_codes

def to_format(code, spec):
    if ( code < 32 and code != 10 ) or code > 126 :
        print(f"Error: Invalid character code {code}. Exiting.")
        sys.exit(1)
    
    return format(code, spec)


def get_number(arg):

    numbers = {
        "binary": 2,
        "octal": 8,
        "decimal": 10, 
        "hexadecimal": 16, 
        "character": 0,
        "ord": -1,
    }

    if arg in numbers:
        return numbers[arg]
    else:
        print("Invalid format! Choose: binary, octal, decimal, hexadecimal, character.")
        retry = input("Do you want to retry again? (Y/N)").strip().lower()
        if retry == "y":
            return get_number(input("Enter spec1: "))
        else:
            sys.exit(1)



def feed():
    arg = get_bases()

    initial_basename = arg[0]
    convert_basename = arg[1]

    text = get_value()
    
    initial_base = get_number(initial_basename)
    convert_base = get_number(convert_basename)
    

    converted_value = convert(text, initial_base, convert_base)
    print(f'{converted_value}')


def main():
    feed()

main()