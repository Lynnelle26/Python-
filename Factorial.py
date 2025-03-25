def factorial():
    print ("Welcome the user to the Factorial Calculation program.")

    # Ask the user for the number they want to calculate the factorial of
    number = int(input("Please enter a positive integer to calculate its factorial: "))
    
    # Calculate the factorial using a loop
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        factorial = 1
        for i in range(1, number + 1):
            factorial *= i
        
        # Display the result
        print(f"The factorial of {number} is {factorial}.")

# Run the program
if __name__ == "__main__":
    factorial()