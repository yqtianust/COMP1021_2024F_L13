def f():
    num1 = int(input("1st number"))
    num2 = int(input("2nd number"))
    num3 = int(input("3rd number"))
    
    if num1 == num2:
        print("Message 1: First and second numbers are the same.")
    
    if num3 < 2 or num3 > 10:
        print("Message 2: The third number is not between 2 and 10.")

    total_numbers = abs(num2 - num1) + 1
    
    if total_numbers <= num3:
        print("Message 3: Not enough numbers to print two lines.")
    
    # swap num1 and num2 if num1>num2
    if num1 > num2 :
        temp = num1
        num1 = num2
        num2 = temp
    
    
    # num_of_printed_number_in_this_row
    num_in_row = 0
    
    for i in range(num1, num2 + 1):
        print(i, end="") 
        num_in_row = num_in_row + 1

        if num_in_row % num3 != 0:
            print("", end=",")
        else:
            print("")
            num_in_row = 0

    if num_in_row != 0:
        print()

    if total_numbers % num3 == 0:
        print("0 number is needed")
    else:
        remaining = num3 - num_in_row
        if remaining == 1:
            print("1 numbers are needed.")
        else:
            print(remaining, "numbers are needed.")

f()