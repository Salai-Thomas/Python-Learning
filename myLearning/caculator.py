def adding(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def division(num1,num2):
    return num1 / num2
print("Select Operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Division")

while True:
    operator = input("Choose operator (1,2,3,4) : ")

    if operator in ("1","2","3","4"):
        first_num = float(input("Enter first Number :"))
        sec_num = float(input("Enter Second Number : "))

        if operator == "1":
            result = adding(first_num,sec_num)
            print(f"{first_num} + {sec_num} = {result}")
        elif operator == "2":
            result = subtract(first_num,sec_num)
            print(f"{first_num} - {sec_num} = {result}")
        elif operator == "3":
            result = multiply(first_num,sec_num)
            print(f"{first_num} x {sec_num} = {result}")
        elif operator == "4":
            result = division(first_num,sec_num)
            print(f"{first_num} / {sec_num} = {result}")

        again = input("Do you want to contniue (yes/no) : ").lower()
        if again == 'no':
            print("Bye!")
            break

    else:
        print("Invalid Number.Try Again!")