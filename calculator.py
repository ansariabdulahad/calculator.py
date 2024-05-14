# common function for calculator
def calculator(num1=0, operator="", num2=0) :
    match operator :
        case '+' : return num1 + num2
        case '-' : return num1 - num2
        case '*' : return num1 * num2
        case '%' : return num1 % num2

# Addition operator
print("Addition : ", calculator(20, '+', 40))
print("Subtraction : ", calculator(20, '-', 40))
print("Multiplication : ", calculator(20, '*', 40))
print("Division : ", calculator(20, '%', 40))