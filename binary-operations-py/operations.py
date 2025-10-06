from evaluate import evaluate 
from adjust import adjust

# Indirect binary calculations

arithmetic_functions = ["+", "-", "*", "/"]
bitwise_operators = ["&", "|",  "~", "^" , "<<", ">>"]

def get_expression():
    while True:
        expression = input("What is your binary expression [binary number] [operation] [binary number]? ")
        
        expressions = expression.strip().split(" ")

        is_signed = False
        operation_type = None

        if len(expressions) != 3:
            print("Invalid number of expressions.")
            continue

        first_binary, operation, second_binary = expressions

        if operation.strip() not in (arithmetic_functions + bitwise_operators):
            print("You have an invalid operation. Use either +, -, * or / or &, |, ~, ^, << ad >>")
            continue

        if operation.strip() in arithmetic_functions:
            signed = input("Is your number in signed or two's complement form? [SN/tc] ? ").strip().lower()
            operation_type = "arithmetic"

            if signed == "y":
                is_signed = True

        else:
            operation_type = "bitwise"
            is_signed = False

        return first_binary, operation, second_binary, operation_type, is_signed

def arithmetic(first_number , operation, second_number):


    if operation == "+":
        total = first_number + second_number
    elif operation == "-":
        total = first_number - second_number
    elif operation == "*":
        total = first_number * second_number
    else:
        total = int(first_number / second_number)


    print(f"Result (decimal): {total}")

    binary_result = bin(total)[2:]
    # binary_result = adjust(first_number, binary_result)

    print(f"Result (binary): {binary_result}")

def bitwise(first_number , operation, second_number=None):

    if operation == "&":
        result = first_number & second_number 
    elif operation == "|":
        result = first_number | second_number
    elif operation == "~":
        result = ~first_number
    elif operation == "^":
        result = first_number ^ second_number
    elif operation == ">>":
        result = first_number >> second_number
    elif operation == "<<":
        result = first_number << second_number
    else:
        print("Unknown bitwise operator.")

    print(f"Result (decimal): {result}")
    print(f"Result (binary): {bin(result)[2:] if result >= 0 else '-' + bin(result)[3:]}")


def evaluate_signed(binary):
    is_negative = False 

    if binary[0] == "0":
        is_negative = False
    else:
        is_negative = True

    binary = binary[1:]

    return binary, is_negative


def perform_binary():
    first_binary, operation, second_binary, operation_type, signed = get_expression()

    if operation_type == None:
        print("You do not have a valid operation type.")

    elif operation_type == "arithmetic":

        if signed == True:
            first_binary, is_negative = evaluate_signed(first_binary)
            second_binary, is_negative = evaluate_signed(second_binary)

            first_number = evaluate(first_binary, is_negative)
            second_number = evaluate(second_binary, is_negative)

        else:
            first_number = evaluate(first_binary)
            second_number = evaluate(second_binary)

        arithmetic(first_number, operation, second_number)

    else:
        first_number = evaluate(first_binary)
        second_number = evaluate(second_binary) if operation != "~" else None
        bitwise(first_number, operation, second_number)


if __name__ == "__main__":
    perform_binary()