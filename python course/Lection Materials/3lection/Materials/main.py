# leqciis masala
# cycles
# ####
# Nested Operator
# ###################
# number1 = int(input('enter a number:'))
# number2 = int(input('enter a number:'))
# operator = input('enter a operator')
#
# ### pirveli varianti
#
# if operator == '/':
#     if number2 == 0:
#         print('cannot Divided by zero')
#     else:
#         print(number1 / number2)
# else:
#     print('operator is not /')
#
# ##meore varianri
# if operator == '/' and number2 != 0:   # != nishnavs ro ar udris// == udris
#     print(number1 / number2)
# else:
#     print('operator is not /')
# from random import random
# from tkinter.tix import Meter
#
# from unicodedata import numeric

# ######################################
# CYCLES
# #######
# 1 იტერატორი
# იტერატორი არის ობიექტი,რომელიც შიეცავს თვლად რაოდენობას
# მოიცავს iter და  next
# სტრინგი იტერატორად არ ითვლება ის არის სტრინგის ტიპის და არა იტერატორის
# ფუნქცია iter()
# ის საშუალებას გვაძლევს თითოეულ ქარაქთერს მივწვდეთ სათითაოდ მაგრამ თანმიმდევრულად
# ფუნქციას მაშინ ვეძახით როცა ()-ფრჩხილები აქვს დაწერილი
# next -ს უნდა ჩავუწეროთ იტერატორის ტექსტი თორე არ იმუშავებს
###########
# Iterator
##############
#
# txt = "Hello Python"
# iterator_txt = iter(txt)

# H = next(iterator_txt)
# print(H) ese marto H daibechdeba radgan cvladshia moqceuli
#amitom next unda shevitanot printshive
#
# print(next(iterator_txt))
# print(next(iterator_txt))
# print(next(iterator_txt))
# print(next(iterator_txt))
####ramden printsac gavushvebt imden shemdeg asos dabechdavs.
# magram zedmets ver dabechdavs da errors amoagdebs.
#amis agmosafxvrelad unda gamoviyenot CYCLE ro tavisitve daiweros yvela simbolo da gacherdeba tavisit

## იტერაცია ნიშნავს ერთი და იგივე ბლოკის განმეორებით გაშვებას,რისთვისაც ვიყენებთ ციკლის ოპერატორებს, ესენია:
#While და  For
#იტერაცია გვაქვს 2 სახის: სასრული და უსასრულო(მიმდინარეობს იქამდე სანამ ოპერატორებისთვის გადაცემული პირობა არის True

###
####While cycle  ჭირდება ორი წერტილი :
###აუცილებლად უნდა დადვცეთ კონდიცია(იგივე პრინტი)(+ - ....) და მივუთითოთ სასრული ციკლი ##########
###პირდაპი ვერ გადვცემთ რო იმოქმედოს. უნდა ჩავუწეროთ ბლოკში ყველა ინფო


# ##დაბჭდავს 0დან 9 ჩათვლით რადგან +1 პტინტის მერეა მითითებული
# number = 0
# while number < 10:
#     print(number)
#     number += 1
# print('Finished while cycle')
#
# ##დაბჭდავს 1დან 10 ჩათვლით რადგან +1 პტინტამდეა მითითებული
# number = 0
# while number < 10:
#     number += 1
#     print(number)
# print('Finished while cycle')

# while True:
#     number = int(input('enter a number: '))
#     if number > 0:
#         print(number)
#         break
# print('while finished')

########continue and brake
# number = 0
# while True:
#     if number == 5:
#         number += 1
#         continue  #anu gadaaxteba 5
#     if number == 10:   #10mde dabechdavs gacherdeba 9ze
#         break
#     print(number)
#     number +=1

##else

# number= 0
# while number < 10:
#     print(number)
#     number += 1
# else:
#     print('else block')
########

#For Cycle
## i aris droebiti cvladi
#in aris wevrobis anu magalitad for i in range(): range abrunebs  iteratoris objects

#range_number = [0, 1, 2, 3, 4]
# iterator_range = iter(range_number)          ES ARIS GASHLASHI.igive shedegs idzeva dabla for in.
# i = next(iterator_range)
#print(i)
# for i in range(5):
#     if i == 2:
#         print(i)
####
# for i in range(5, 11):
#         print(i)
####
# for i in range(5, 11, 2):
#         print(i)


####
# txt = 'Me'
# for char in txt:
#     print(char)


#####nested cycles chadgmuli ciklebi

# for i in range(5):
#     for j in range(5):
#         print(i, j)

########
# number = 0
# while number <5:
#     number1 = 0
#     while number <5:
#         print(number, number1)       #####igivea rac for in mara meti wera chirdeba da usasruloa es. for sasrulia
#         number += 1
#     number += 1

#######################
#random
###########
# import random
#
# random_number = random.randint(1, 10)
# print(random_number)





###########
#task1
#########
# number = int(input('enter the number:'))
# print(number)
#
# while number > 0:
#
#     print(number)
#     number -= 1

###########
#task2
########


total_sum = 0

while True:
    num = input('Enter a positive number or type "sum" to show the total: ')
    if num == 'sum':
        print(total_sum)
        break
    elif int(num) > 0:  #  positive integer
        total_sum += int(num)
    else:
        print("Please enter a valid number.")

#######task3
########
#
# import random
# random_number = random.randint(0, 15)
# print(random_number)
# num_of_lives = 5
# # num2 = int(input('Enter the number: '))
# while num_of_lives > 0:
#     chance = int(input('Guess the number: '))
#     if random_number == chance:
#         print("Congrats, you have guessed the number")
#
#     if random_number < chance:
#         print('Entered number is greater')
#     elif random_number > chance:
#         print('entered number is less')
#     else:
#         break
#     num_of_lives -=1

