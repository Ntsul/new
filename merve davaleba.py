############################
# task 1
###########################

from collections import Counter

def are_anagrams(str1, str2):

    return Counter(str1) == Counter(str2)


print(are_anagrams("Listen", "Silent"))
print(are_anagrams("Hello", "olleH"))
print(are_anagrams("Not", "Anagram"))

############################
# task 2
###########################

def count_char_in_string(string, char):

    return string.count(char)


print(count_char_in_string("hello world", "o"))
print(count_char_in_string("hello world", "l"))
print(count_char_in_string("python", "p"))

############################
# task 3
###########################

from functools import reduce

def fibonacci_sequence(n):

    if n <= 0:
        return []

    return reduce(lambda fib_list, _: fib_list + [fib_list[-1] + fib_list[-2]], range(n - 2), [0, 1])[:n]


print(fibonacci_sequence(10))
print(fibonacci_sequence(5))
print(fibonacci_sequence(1))
print(fibonacci_sequence(0))