try:
    num1, num2 = eval(input("Enter two numbers, separated by a comma : "))
    result = num1 / num2
    print("Result is", result)
    #using multiple except bloc for different type of error


except ZeroDivisionError:
    print("Division by ero is error !!")

except SyntaxError:
    print("Comma is missing. Enter nmbers separated by comma like this 1, 2")

except:
    print("Wrong input")

else:
    print("No exceptions")

finally:
    print("This will excute no matter what")