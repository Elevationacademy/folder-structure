def determine_biggest(num1, num2):
    return num1 if num1 > num2 else num2


biggest = determine_biggest(91234, 91241)
print("Biggest number is " + str(biggest))  # outputs: Biggest number is 91241

biggest = determine_biggest(91241, 91234)
print("Biggest number is " + str(biggest))  # outputs: Biggest number is 91241
