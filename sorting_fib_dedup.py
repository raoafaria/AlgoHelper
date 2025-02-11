import heapq

# Fibonacci function with a call stack for debugging
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

# Function to track the Fibonacci call stack for debugging
def fibonacci_call_stack(n):
    call_stack = []

    def trace_fib(n):
        call_stack.append(f"fib({n})")
        if n == 0:
            return 0
        if n == 1:
            return 1
        return trace_fib(n - 1) + trace_fib(n - 2)

    trace_fib(n)
    return " -> ".join(call_stack)

# Merge K sorted arrays using a min-heap
def merge_k_sorted_arrays(arrays):
    min_heap = []
    result = []

    # Push the first element of each array along with its array index and element index
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(min_heap, (arr[0], i, 0))

    while min_heap:
        val, list_idx, elem_idx = heapq.heappop(min_heap)
        result.append(val)

        # Push the next element from the same array if available
        if elem_idx + 1 < len(arrays[list_idx]):
            heapq.heappush(min_heap, (arrays[list_idx][elem_idx + 1], list_idx, elem_idx + 1))

    return result

# Function to remove duplicates from a sorted array
def remove_duplicates(arr):
    if not arr:
        return []

    write_index = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[write_index] = arr[i]
            write_index += 1

    return arr[:write_index]

# Helper function to handle input with both spaces and commas
def parse_input(input_str):
    return list(map(int, input_str.replace(",", " ").split()))

# Main menu to execute different functions
def main():
    while True:
        print("Menu:")
        print("1. Fibonacci Sequence Call Stack")
        print("2. Merge K Sorted Arrays")
        print("3. Remove Duplicates from Sorted Array")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            n = int(input("Enter a number for Fibonacci sequence: "))
            print(fibonacci_call_stack(n))
        elif choice == "2":
            k = int(input("Enter number of sorted arrays: "))
            arrays = []
            for i in range(k):
                arrays_input = input(f"Enter sorted array {i + 1}: ")
                arrays.append(parse_input(arrays_input))
            print("Merged Sorted Array:", merge_k_sorted_arrays(arrays))
        elif choice == "3":
            arr = parse_input(input("Enter sorted array: "))
            print("Array after removing duplicates:", remove_duplicates(arr))
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
