#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        fibonacci_sequence = []
    elif length == 1:
        fibonacci_sequence = [0]
    else:
        fibonacci_sequence = [0, 1]  # Initialize with the first two Fibonacci numbers

        # Generate Fibonacci sequence up to the specified length
        while len(fibonacci_sequence) < length:
            next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_number)

    print(fibonacci_sequence)


