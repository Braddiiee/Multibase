#include <stdio.h>

int main() {
  
  double initialValue;
  char initialBase;
  char secondaryBase;
  
  printf("Enter your initial value: ");
  scanf("%lf", &initialValue);

  printf("What is the base for your initial value? ");
  scanf("\n%c", &initialBase);

  printf("What is the base for your secondary value? ");
  scanf("\n%c", &secondaryBase);
  

  printf("%lf", &initialValue);
  printf("%c", &initialBase);
  printf("%c", &secondaryBase);

  
  return 0;
}