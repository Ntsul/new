
##########################################
# task 1
#########################################################

user_input = input("Enter the text: ")

if user_input == user_input[::-1]:
    print("The entered text is a palindrome.")
else:
    print("The entered text is not a palindrome.")



##########################################
# task 2 example 1
#################################################

user_input = input("Enter the text: ")
ascii_values = list(map(ord, user_input))
print("The ASCII values are:", ascii_values)

###################################################
# task 2 ### 2
##############################################################

user_input = input("Enter the text: ")
ascii_values = [ord(char) for char in user_input]
print("The ASCII_Vs are:", ascii_values)