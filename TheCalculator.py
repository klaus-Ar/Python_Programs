# This program is about creating an awesome calculator
import re
print('''
\"Welcome to the Advanced Calc.\"
''')

print('Type "quit" to exit the calc! \n')

last_num = 0
make = True
# Here I'm going to define a function and add the above variables as globals inside the function.
def previous_value():
    global last_num
    global make
    numbers = ""
# Here I'm going to make a conditional statement
    if last_num == 0:
        numbers = input("Enter the equation: ")
    else:
        numbers = input("Continue your operation: " + str(last_num))

    if numbers == 'quit':
        print('''
        Thank you for using me..!
        Have a nice day :-)''')
        make = False
    else:
        formula = re.sub('[a-zA-z.:,()" "]', "", numbers)
        if last_num == 0:
            last_num = eval(numbers)
        else:
            last_num = eval(str(last_num) + numbers)
# Here I'm making a loop. The loop ends only when the user typed 'quit'.!
while make :
    previous_value()

