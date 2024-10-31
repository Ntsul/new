##########
# tsk1
###########################

txt = input('Enter the sentence: ')
print(txt)
words = txt.lower().split()
wordcount = {}
for i in words:
    if i in wordcount:
        wordcount[i] += 1
    else:
        wordcount[i] = 1

print(wordcount)


##########
# tsk2
###########################

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter a mathematical operator (+, -, *, /): ")


operations = {
    '+': num1 + num2,
    '-': num1 - num2,
    '*': num1 * num2,
    '/': num1 / num2 if num2 != 0 else 'Cannot divide by zero'
}

result = operations.get(operator, 'Invalid operator!')

print(f"Result: {result}")

##########
# tsk3
###########################

squares = {x: x**2 for x in range(1, 11)}

print(squares)


##########
# tsk4
###########################


departments = {
    'HR': [
        {'first_name': 'Alice', 'last_name': 'Johnson', 'age': 30, 'salary': 5000},
        {'first_name': 'Bob', 'last_name': 'Smith', 'age': 40, 'salary': 5500}
    ],
    'IT': [
        {'first_name': 'Charlie', 'last_name': 'Brown', 'age': 25, 'salary': 6000},
        {'first_name': 'David', 'last_name': 'Wilson', 'age': 35, 'salary': 6200}
    ]
}

for department, employees in departments.items():
    total_salary = sum(emp['salary'] for emp in employees)
    avg_salary = total_salary / len(employees)
    print(f"Average salary in {department}: {avg_salary}")