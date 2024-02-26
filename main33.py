def perform_operations(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    return addition, subtraction, multiplication, division

if __name__ == "__main__":
    num1 = 10
    num2 = 5
    result = perform_operations(num1, num2)
    print("Addition:", result[0])
    print("Subtraction:", result[1])
    print("Multiplication:", result[2])
    print("Division:", result[3])
