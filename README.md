# Module 04

## Description

In this program we will be using exception handling to correct all programs to ensure accuracy.

## Author

Presley McFarlane-Goolcharan

## Code Modification [1]

- Added ValueError handling if the program cannot locate the data file within its specified directory.

## Code Modification [2]

- In Validation 1 section I raised my own TypeError exception, caught it and appended it to the rejected transaction tuple where we printed the rejected transactions at the end of the transaction report.
- In Validation 2 section I raised ValueError exception, caught it and appended it to the rejected transaction tuple that was printed at the bottom of the transaction report.
- In the valid transaction section in the program I added another transaction counter as I noticed we were dividing by zero because at the top of the program the "transaction_counter" was set to 0.