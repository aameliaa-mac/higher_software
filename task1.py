# Create a program to take in a valid denary number between 0 and 255, and display the appropriate 8-bit binary sequence.

number = int(input("enter your denary number: "))

while number < 0 or number > 255:
    print("error. number must be between 0 and 255. please try again.")
    number = input ("enter your denary number: ")

tester = 128 
current_number = number 
output = "" # won't actually 'add' the number to the output 

while current_number >= 0 and tester >= 1:
    if current_number - tester >= 0:
        output = output + '1' 
        current_number = current_number - tester 
    else:
        output = output + '0' 
    tester = tester / 2 

print(output)
