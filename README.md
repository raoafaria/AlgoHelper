**Sorting, Fibonacci & Deduplication Python Program**

This Python program offers three functionalities:

1)Fibonacci Sequence Call Stack: Display the recursive call stack for calculating the Fibonacci sequence.

2)Merge K Sorted Arrays: Merge K sorted arrays into one sorted array.

3)Remove Duplicates from Sorted Array: Remove duplicate values from a sorted array.

**How to Run**

Clone the repository *or* download the sorting_fib_dedup.py file.

Navigate to the directory where sorting_fib_dedup.py is located using your terminal or command prompt.

Run the program:

python sorting_fib_dedup.py

**Menu Options**


Once you run the program, the following menu will be displayed:

*Menu:*

1. Fibonacci Sequence Call Stack
2. Merge K Sorted Arrays
3. Remove Duplicates from Sorted Array
4. Exit

   
*1. Fibonacci Sequence Call Stack*

When you select option 1, you will be asked to input a number for the Fibonacci sequence.
The program will then display the recursive call stack (e.g., fib(5) -> fib(4) -> fib(3) -> fib(2) -> fib(1)).

*2. Merge K Sorted Arrays*
   
When you select option 2, you will be prompted to enter the number of sorted arrays you want to merge.

Valid input: A single integer (e.g., 3 for three arrays).
You will then be asked to input each array. You can input the arrays using spaces or commas between elements (e.g., 1 3 7 or 1,3,7).

The program will merge the arrays and display the sorted result.

*3. Remove Duplicates from Sorted Array*

When you select option 3, you will need to input a sorted array.
The program will remove any duplicate values and return the cleaned array.

*4. Exit*
Select option 4 to exit the program.

**Notes:**
1. The program supports input with both commas and spaces to separate elements in the arrays for merging and deduplication tasks.
2. The Fibonacci calculation uses a naive recursive approach. You may want to optimize it with memoization for larger numbers.
