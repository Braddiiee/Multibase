#include <stdio.h>   // For printf
#include <string.h>  // For strlen
#include <stdlib.h>  // For malloc

// Function to pad a binary string with zeros on the left 
char* adjust(const char *original, const char *result) {
    
    int length = strlen(original);   // Get length of the original binary string

    // Check if result is shorter than original
    if (strlen(result) < length) {
        int additional = length - strlen(result);  // Calculate how many zeros to add

        // Allocate memory for new string (additional zeros + result + null terminator)
        char *result_binary = (char *)malloc(length + 1);  

        // Create string of zeros to pad the left side
        for (int i = 0; i < additional; i++) {
            result_binary[i] = '0';  // Add '0' characters to beginning
        }

        // Copy the result string after the zeros
        strcpy(result_binary + additional, result);

        result_binary[length] = '\0'; // Null-terminate the final string

        return result_binary;  // Return the new zero-padded string
    }

    // If no adjustment is needed, just return a copy of result
    char *copy = (char *)malloc(strlen(result) + 1);
    strcpy(copy, result);
    return copy;
}

// Example usage
int main() {
    char *adjusted = adjust("1010101", "1011");  // Pad "1011" to match "1010101" length
    printf("Adjusted: %s\n", adjusted);          // Output: Adjusted: 0001011
    free(adjusted);                              // Free allocated memory
    return 0;
}
