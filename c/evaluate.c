#include <stdio.h>   // Include standard input/output library
#include <string.h>  // Include string library for strlen()
#include <math.h>    // Include math library for pow()
#include <stdbool.h> // Include bool type (for true/false values)

// Function declaration: takes a binary string and a flag for negativity
int evaluate(const char *binary, bool negative) {

    int binaryCount = strlen(binary); // Get the length of the binary string
    int digits[64];                   // Array to store converted digits (supports up to 64 bits)
    int counter = 0;                  // Counts invalid characters
    int sum = 0;                      // Holds total value
    int index = 0;                    // Tracks index in digits[]

    // Check if the binary string has at least one character
    if (binaryCount > 0) {

        // Loop through each character in the binary string
        for (int i = 0; i < binaryCount; i++) {

            char number = binary[i]; // Get the current character

            // Check if character is NOT '0' or '1'
            if (number != '0' && number != '1') {
                counter++; // Increment invalid counter
            } else {
                binaryCount--; // Decrease power position for next bit
                int digit = (number - '0') * pow(2, binaryCount); // Convert binary to decimal value
                digits[index++] = digit; // Store result in digits array
            }
        }

        // If invalid binary characters were found
        if (counter > 0) {
            printf("Invalid binary operation. JS\n");
        }

        // Sum all valid binary values
        for (int i = 0; i < index; i++) {
            sum += digits[i];
        }

        // Return negative or positive sum based on flag
        if (negative == false) {
            return sum;
        } else {
            return sum * -1;
        }

    } else {
        // If no digits in input, print error
        printf("Invalid amount of digits.\n");
        return 0;
    }
}

// Example usage
int main() {
    printf("%d\n", evaluate("1010101", false));  // Should print 85
    printf("%d\n", evaluate("1010101", true));   // Should print -85
    printf("%d\n", evaluate("10A101", false));   // Invalid input example
    return 0;
}
