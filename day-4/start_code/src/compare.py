def compare(num1, num2):
    if num1 < num2:
        return f"{num1} is less than {num2}"
    elif num1 > num2:
        return f"{num1} is greater than {num2}"
    elif num1 == num2:
        return "Both numbers are equal"
    else:
        return "Incorrect types"