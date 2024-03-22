stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

# Type your code below
valid = True
mantissa = stdform[:stdform.find('x')]
exponent = stdform[stdform.find('^')+1:]
num_mantissa = mantissa.replace('.', '').replace('-', '')
num_exponent = exponent.replace('-', '')

if ' ' in stdform or stdform.count('.') > 1 or stdform.count('x') > 1 or stdform.count('^') > 1 or not num_exponent.isdecimal() or not num_mantissa.isdecimal():
    valid = False
if valid:
    print(f"This number in E notation is {mantissa}E{exponent}.")
else:
    print("Error converting to scientific E notation.")