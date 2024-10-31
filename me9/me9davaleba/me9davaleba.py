
#task1
#########################

int_list = [10, 20, 30, 40]

def insert_number(num):
    global int_list
    int_list.append(num)
    return int_list

insert_number(50)
print(int_list)

# #######################
# task2
# ######


def sum_recursive(n):
    if n > 6:
        return 0
    else:
        return n + sum_recursive(n + 1)

result = sum_recursive(2)
print(f"The sum of the numbers from 2 to 6 is: {result}")


########################
#task3
#######

def reverse_string(s, index=None):
    if index is None:
        index = 0
    if index == len(s):
        return ""

    return reverse_string(s, index + 1) + s[index]


txt = "Python"
reversed_output = reverse_string(txt)
print("Input:", txt, "Output:", reversed_output)

########################
#task4
#######
#
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci_numbers = []
for i in range(9):
    fibonacci_numbers.append(fibonacci(i))

print(fibonacci_numbers)
