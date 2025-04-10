def generate_fibonacci(n):
    fibonacci_series = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_series.append(a)
        a, b = b, a + b
    return fibonacci_series

# Example usage:
terms = int(input("Enter the number of Fibonacci terms to generate: "))
series = generate_fibonacci(terms)
print("Fibonacci Series:", series)
