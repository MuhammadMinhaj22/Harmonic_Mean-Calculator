def harmonic_mean(value):
    n = len(value)
    if n == 0:
        return 0 
    reciprocal_sum = sum(1 / x for x in value if x != 0)
    if reciprocal_sum == 0:
        return 0
    return n / reciprocal_sum


while True:
    user_input = input("Press Enter to continue or type 'e' to exit: ")
    if user_input.lower() == 'e':
        break

    try:
        i = float(input("Enter first number: "))
        i1 = float(input("Enter second number: "))
        i2 = float(input("Enter third number: "))

        values = [i,  i1, i2]
        result =harmonic_mean(values)
        print(f"Harmonic Mean: {result:.2f}\n")
    except ValueError:
        print("Invalid input. Please enter numeric values only.\n")
