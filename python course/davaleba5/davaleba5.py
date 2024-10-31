##########################################
# task 1
################


my_list = [36, 73, 1, 7, 54, 100, 237, 34, 76, 10, 7, 9, 12, 34, 49]


l_s = [2, 8, 13]


result = sum(my_list[i] for i in l_s)


print(result)




##########################################
# task 2
# #######################################


import random

random_list = [random.randint(1, 100) for _ in range(20)]

odd_values = [num for num in random_list if num % 2 != 0]

if odd_values:
    smallest = largest = odd_values[0]

    for num in odd_values:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    print("Odd values:", odd_values)
    print("Smallest odd value:", smallest)
    print("Largest odd value:", largest)
else:
    print("No odd values found in the list.")


##########################################
# task 3
################



my_llist = [43, '22', 12, 66, 210, ["hi"]]


index_of_210 = my_llist.index(210)
print("Position of 210:", index_of_210)


my_llist[5].append("hello")


element_to_remove = my_llist[2]  # Get the element at index 2 to remove it
my_llist.remove(element_to_remove)  # Remove it using remove()
print("Updated list after removing the element:", my_llist)


my_llist_2 = my_llist[:]  # Create a copy using slicing
my_llist_2.clear()  # Clear my_llist_2


print("Final my_llist:", my_llist)
print("Final my_llist_2:", my_llist_2)

##########################################
# task 4
################################################3


matrix_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]


if len(matrix_1) == len(matrix_2) and len(matrix_1[0]) == len(matrix_2[0]):

    result = []

    for i in range(len(matrix_1)):

        row = []
        for j in range(len(matrix_1[0])):

            row.append(matrix_1[i][j] + matrix_2[i][j])
        result.append(row)


    print("Sum:")
    for row in result:
        print(row)
else:
    print("Error: Both matrices must be of the same shape.")


#######################################
#task 5
###########################################



data_matrix = [
    [5, 6, 7],
    [8, 9, 10],
    [11, 12, 13]
]

transposed_matrix = [[0 for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        transposed_matrix[j][i] = data_matrix[i][j]

print("Original data_matrix:")
for row in data_matrix:
    print(row)

print("\nTransposed matrix:")
for row in transposed_matrix:
    print(row)

#######################################
#task 6
###########################################


import random

num_matrix = [[random.randint(20, 70) for _ in range(4)] for _ in range(4)]

# Print the matrix
print("\nMatrix num_matrix:")
for row in num_matrix:
    print(row)
