# Module 04

## Description

In this program we will be using exception handling to correct all programs to ensure accuracy.

## Author

Presley McFarlane-Goolcharan

## Code Modification 1

- Added ValueError handling if the program cannot locate the data file within its specified directory.

## Code Modification 2

- In Validation 1 section I raised my own TypeError exception, caught it and appended it to the rejected transaction tuple where we printed the rejected transactions at the end of the transaction report.
- In Validation 2 section I raised ValueError exception, caught it and appended it to the rejected transaction tuple that was printed at the bottom of the transaction report.
- In the valid transaction section in the program I added another transaction counter as I noticed we were dividing by zero because at the top of the program the "transaction_counter" was set to 0.

## Code Modification 3

- In the Correcting ZeroDivisionError sections I added a try block to only calculate the average if the "transaction_counter" variable was greater than 0 and if the "transaction_counter" variable was = 0 we raise the ZeroDivisionError, catch it and printed my own error message.
- I also added formatting to the customer account balance, transaction history and average transaction amount thar prints to the console, for example the balance should print out as: $1,000.00.

## Code Modification 4

- Fixed indentation in the collecting invalid records section, tabbed over section so it aligns with the rest of the code.
- Fixed transaction type check for "withdraw", changed from "withdrawal". That was probably why I was getting the "ZeroDivisionError" code.

## Code Modification 5

- Fixed the appending to the rejected list so it only happens once through the Validation checks if it fails both validations.
