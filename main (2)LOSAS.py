##########################################
# task 1
################

# my_list = [36, 73, 1, 7, 54, 100, 237, 34, 76, 10, 7, 9, 12, 34, 49]
#
#
# third_element = my_list[2]
# ninth_element = my_list[8]
# fourteenth_element = my_list[13]
#
# result = third_element + ninth_element + fourteenth_element
#
# print(result)

##########################################
# task 1 example 2
################

# my_list = [36, 73, 1, 7, 54, 100, 237, 34, 76, 10, 7, 9, 12, 34, 49]
#
#
# arch = [2, 8, 13]
#
#
# result = sum(my_list[i] for i in arch)
#
#
# print(result)




##########################################
# task 2
# #######################################


# import random
#
# random_list = [random.randint(1, 80) for _ in range(20)]
#
# odd_num = [num for num in random_list if num % 2 != 0]
#
# if odd_num:  # Check if the list is not empty
#     smallest = odd_num[0]
#     largest = odd_num[0]
#
#     for num in odd_num:
#         if num < smallest:
#             smallest = num
#         if num > largest:
#             highest = num
#
#     print("Odd values:", odd_num)
#     print("Smallest odd :", smallest)
#     print("Highest odd :", largest)
# else:
#     print("The list does not contain any odd values.")

#######################################################
#task2 exp 2
################

# import random
#
# random_list = [random.randint(1, 100) for _ in range(20)]
#
# odd_values = [num for num in random_list if num % 2 != 0]
#
# if odd_values:
#     smallest = largest = odd_values[0]
#
#     for num in odd_values:
#         if num < smallest:
#             smallest = num
#         if num > largest:
#             largest = num
#
#     print("Odd values:", odd_values)
#     print("Smallest odd value:", smallest)
#     print("Largest odd value:", largest)
# else:
#     print("No odd values found in the list.")


##########################################
# task 3
################


# my_llist = [43, '22', 12, 66, 210, ["hi"]]
#
#
# index_of_210 = my_llist.index(210)
# print("Index of 210:", index_of_210)
#
# my_llist[5].append("hello")
#
# my_llist.remove(my_llist[2])
# print("List after removing element at index 2:", my_llist)
#
# my_llist_2 = my_llist.copy()
# my_llist_2.clear()
#
# print("my_llist:", my_llist)
# print("my_llist_2:", my_llist_2)



##########################################
# task 3 exp2
################

#
# my_llist = [43, '22', 12, 66, 210, ["hi"]]
#
#
# index_of_210 = my_llist.index(210)
# print("Position of 210:", index_of_210)
#
#
# my_llist[5].append("hello")
#
#
# element_to_remove = my_llist[2]  # Get the element at index 2 to remove it
# my_llist.remove(element_to_remove)  # Remove it using remove()
# print("Updated list after removing the element:", my_llist)
#
#
# my_llist_2 = my_llist[:]  # Create a copy using slicing
# my_llist_2.clear()  # Clear my_llist_2
#
#
# print("Final my_llist:", my_llist)
# print("Final my_llist_2:", my_llist_2)

##########################################
# task 4
################


# matrix_a = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# matrix_b = [
#     [9, 8, 7],
#     [6, 5, 4],
#     [3, 2, 1]
# ]
#
#
# if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
#     raise ValueError("Matrices must have the same dimensions")
#
#
# result = [[0 for _ in range(len(matrix_a[0]))] for _ in range(len(matrix_a))]
#
#
# for i in range(len(matrix_a)):
#     for j in range(len(matrix_a[0])):
#         result[i][j] = matrix_a[i][j] + matrix_b[i][j]
#
#
# print("Sum of the two matrices:")
# for row in result:
#     print(row)


##########################################
# task 4 exp 2
################


# matrix_1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# matrix_2 = [
#     [9, 8, 7],
#     [6, 5, 4],
#     [3, 2, 1]
# ]
#
#
# if len(matrix_1) == len(matrix_2) and len(matrix_1[0]) == len(matrix_2[0]):
#
#     result = []
#
#     for i in range(len(matrix_1)):
#
#         row = []
#         for j in range(len(matrix_1[0])):
#
#             row.append(matrix_1[i][j] + matrix_2[i][j])
#         result.append(row)
#
#
#     print("Sum:")
#     for row in result:
#         print(row)
# else:
#     print("Error: Both matrices must be of the same shape.")

#######################################
#task 5
###########################################

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# transposed = [[0 for _ in range(3)] for _ in range(3)]
#
# for i in range(3):
#     for j in range(3):
#         transposed[j][i] = matrix[i][j]
#
# print("Original matrix:")
# for row in matrix:
#     print(row)
#
# print("\nTransposed matrix:")
# for row in transposed:
#     print(row)
#
#######################################
#task 5 ex 2
###########################################


#
# data_matrix = [
#     [5, 6, 7],
#     [8, 9, 10],
#     [11, 12, 13]
# ]
#
# transposed_matrix = [[0 for _ in range(3)] for _ in range(3)]
#
# for i in range(3):
#     for j in range(3):
#         transposed_matrix[j][i] = data_matrix[i][j]
#
# print("Original data_matrix:")
# for row in data_matrix:
#     print(row)
#
# print("\nTransposed matrix:")
# for row in transposed_matrix:
#     print(row)

#######################################
#task 6
###########################################

# import random
#
# random_matrix_1 = [[random.randint(1, 50) for _ in range(4)] for _ in range(4)]
#
# # Print the matrix
# print("Matrix random_matrix_1:")
# for row in random_matrix_1:
#     print(row)



#######################################
#task 6  ex 2
###########################################
import random

num_matrix = [[random.randint(20, 70) for _ in range(4)] for _ in range(4)]

# Print the matrix
print("\nMatrix num_matrix:")
for row in num_matrix:
    print(row)
