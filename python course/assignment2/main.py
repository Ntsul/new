########
# task1
############

num = int(input('enter the number: '))

if num % 2 == 0:
    print("even")
else:
    print('odd')



################
# task2
##############3

txt = input('enter the text: ')
txt1 = 'small'
txt2 = 'tall'
txt3 = 'middle'



print(txt1 in txt)
print(txt2 in txt)
print(txt3 in txt)

if txt1 not in txt:
    pass
else:
    print('small')

if txt2 not in txt:
    pass
else:
    print('tall')


if txt3 not in txt:
    pass
else:
    print('middle')

###############
# task3
###########

num1 = int(input('enter the first number: '))
num2 = int(input('enter the second number: '))
opr = input('enter operator (-, +, *, /): ')

# num2 or num1 != 0
# if num1 or num2 = 0
#     print('error')

if opr == '-':
    print(float(num1 - num2))
else:
    pass
if opr == '+':
    print(float(num1 + num2))
else:
    pass
if opr == '*':
    print(float(num1 * num2))
else:
    pass
if opr == '/':
    print(float(num1 / num2))
else:
    pass


