# Create a program to take in a valid negative denary number between -128 and -1
# and display the appropriate two’s complement 8-bit binary sequence.

number = int(input("enter your denary number: "))

while number < -128 or number > -1:
    print("error. number must be between -128 and -1. please try again.")
    number = int(input("enter your denary number: "))

positive_number = abs(number)

tester = 128 
output = "" 

while positive_number >= 0 and tester >= 1:
    if positive_number - tester >= 0:
        output = output + '1' 
        positive_number = positive_number - tester 
    else:
        output = output + '0' 
    tester = tester / 2 

inverted_output = ""
for bit in output:
    if bit == '1':
        inverted_output += '0'
    else:
        inverted_output += '1'

carry = 1
final_output = ""
for bit in reversed(inverted_output):
    if bit == '1' and carry == 1:
        final_output = '0' + final_output
    elif bit == '0' and carry == 1:
        final_output = '1' + final_output
        carry = 0
    else:
        final_output = bit + final_output

print(final_output)