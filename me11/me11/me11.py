#######################
#tsk1
#########################

with open("output.txt", "w") as file:
    for i in range(1, 1001):
        file.write(f"Line {i}: This is some text.\n")

filled_lines = 0
with open("output.txt", "r") as file:
    for line in file:
        if line.strip(): 
            filled_lines += 1

print(f"Number of filled lines: {filled_lines}")

#######################
#tsk2
#########################

with open("numbered_lines.txt", "w") as file:
    for i in range(1, 18):
        if i == 2:
            file.write("Line 2: Number is 2\n")
        elif i == 8:
            file.write("Line 8: Number is 8\n")
        elif i == 10:
            file.write("Line 10: Number is 10\n")
        elif i == 13:
            file.write("Line 13: Number is 13\n")
        elif i == 17:
            file.write("Line 17: Number is 17\n")
        else:
            file.write(f"Line {i}: This is a blank line.\n")

print("Text file created with the numbers written on specific lines.")

#######################
#tsk3
#########################
# with open("file1.txt", "w") as f1:
#     f1.write("This is the content of file1.txt\n")
#
# with open("file2.txt", "w") as f2:
#     f2.write("This is the content of file2.txt\n")
#
# print("Files file1.txt and file2.txt created.")


def merge_files(file1, file2, output_file):
    with open(output_file, "w") as out_f:
        with open(file1, "r") as f1:
            out_f.write(f1.read())

        out_f.write("\n")

        with open(file2, "r") as f2:
            out_f.write(f2.read())


file1 = "file1.txt"
file2 = "file2.txt"
output_file = "merged_output.txt"

merge_files(file1, file2, output_file)

with open(output_file, "r") as merged_f:
    print(merged_f.read())

#######################
#tsk4
#########################



def are_palindromes(line1, line2):
    line1_clean = ''.join(char.lower() for char in line1 if char.isalnum())
    line2_clean = ''.join(char.lower() for char in line2 if char.isalnum())
    return line1_clean == line2_clean[::-1]


def print_palindromic_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            if are_palindromes(lines[i].strip(), lines[j].strip()):
                print(f"'{lines[i].strip()}' and '{lines[j].strip()}' are palindromes of each other.")


def create_sample_file(filename):
    sample_content = [
        "level\n",
        "radar\n",
        "hello\n",
        "civic\n",
        "noon\n"
    ]

    with open(filename, 'w') as file:
        file.writelines(sample_content)


if __name__ == "__main__":
    filename = 'palindrome_test.txt'

    create_sample_file(filename)

    print_palindromic_lines(filename)

#######################
#tsk5
#########################

def split_file_into_chunks(input_file, max_lines=10):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()

        total_lines = len(lines)
        num_files = (total_lines + max_lines - 1) // max_lines

        for i in range(num_files):
            start_index = i * max_lines
            end_index = start_index + max_lines
            chunk_lines = lines[start_index:end_index]

            new_file_name = f'output_chunk_{i + 1}.txt'

            with open(new_file_name, 'w') as new_file:
                new_file.writelines(chunk_lines)

            print(f'Created: {new_file_name} with lines {start_index + 1} to {min(end_index, total_lines)}')

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")

if __name__ == "__main__":
    input_file_name = 'mexute.txt'
    split_file_into_chunks(input_file_name)


#######################
#tsk6
#########################

def remove_empty_lines(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()

        non_empty_lines = [line for line in lines if line.strip()]

        with open(output_file, 'w') as file:
            file.writelines(non_empty_lines)

        print(f'Successfully wrote {len(non_empty_lines)} non-empty lines to "{output_file}".')

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    input_filename = 'input_data.txt'
    output_filename = 'output_data.txt'

    remove_empty_lines(input_filename, output_filename)
