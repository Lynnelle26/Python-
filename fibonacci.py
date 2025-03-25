def main():
    print("Welcome to the Fibonacci Sequence program!")
    
    # Ask the user for how many terms they want
    n = int(input("How many Fibonacci terms would you like to generate? "))
    
    # Handle small values of n
    if n <= 0:
        print("Please enter a positive number.")
        return
    
    # First two Fibonacci numbers
    a, b = 0, 1
    fib_sequence = [a]
    
    # Generate the sequence
    for _ in range(1, n):
        a, b = b, a + b  # Update a and b
        fib_sequence.append(a)
    
    # Print the sequence
    print(f"The first {n} terms of the Fibonacci sequence are:")
    print(fib_sequence)

# Run the program
if __name__ == "__main__":
    main()

