leqciis masala
cycles
####
Nested Operator
###################
number1 = int(input('enter a number:'))
number2 = int(input('enter a number:'))
operator = input('enter a operator')

### pirveli varianti

if operator == '/':
    if number2 == 0:
        print('cannot Divided by zero')
    else:
        print(number1 / number2)
else:
    print('operator is not /')

##meore varianri
if operator == '/' and number2 != 0:   # != nishnavs ro ar udris// == udris
    print(number1 / number2)
else:
    print('operator is not /')


######################################
CYCLES
#######
1 იტერატორი
იტერატორი არის ობიექტი,რომელიც შიეცავს თვლად რაოდენობას
მოიცავს iter და  next
სტრინგი იტერატორად არ ითვლება ის არის სტრინგის ტიპის და არა იტერატორის
ფუნქცია iter()
ის საშუალებას გვაძლევს თითოეულ ქარაქთერს მივწვდეთ სათითაოდ მაგრამ თანმიმდევრულად
ფუნქციას მაშინ ვეძახით როცა ()-ფრჩხილები აქვს დაწერილი
next -ს უნდა ჩავუწეროთ იტერატორის ტექსტი თორე არ იმუშავებს
###########
Iterator
##############

txt = "Hello Python"
iterator_txt = iter(txt)

H = next(iterator_txt)
print(H)


















