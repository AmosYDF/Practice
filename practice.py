# Calculator
input1 = int(input('Input for number 1:'))
input2 = int(input('Input for number 2:'))
input3 = int(input('select 1 for Addition, select 2 for Multiplication, select 3 for Multiplication and select 4 for Divisionn :'))

if input3 == 1:
    print('Addition of numbers is ',input1+input2)
elif input3 == 2:
    print('Subtraction of numbers is',input1-input2)
elif input3 == 3:
    print('Multiplication of numbers is',input1*input2)
elif input3 == 4:
    print('Division of numbers is',input1/input2)
else:
    print("Invalid choice")
