import os, sys

# global variable (bad practice)
data_list = []

def load_file(path):
    f = open(path)     # file not closed
    content = f.read()
    return content

def process_data(text):
    # inefficient string building
    result = ""
    for i in range(len(text)):
        result = result + text[i]

    # undefined variable bug
    print("Processed length:", lenght)

    return result

def unsafe_exec(user_input):
    # security issue: unsafe use of eval
    return eval(user_input)

def main():
    filename = "non_existing_file.txt"   # will cause FileNotFoundError
    text = load_file(filename)
    data = process_data(text)

    # unused variable
    temp_var = 123

    user_code = input("Enter Python code: ")
    print(unsafe_exec(user_code))

main()
 import os, sys

# global variable (bad practice)
data_list = []

def load_file(path):
    f = open(path)     # file not closed
    content = f.read()
    return content

def process_data(text):
    # inefficient string building
    result = ""
    for i in range(len(text)):
        result = result + text[i]

    # undefined variable bug
    print("Processed length:", lenght)

    return result

def unsafe_exec(user_input):
    # security issue: unsafe use of eval
    return eval(user_input)

def main():
    filename = "non_existing_file.txt"   # will cause FileNotFoundError
    text = load_file(filename)
    data = process_data(text)

    # unused variable
    temp_var = 123

    user_code = input("Enter Python code: ")
    print(unsafe_exec(user_code))

main()
import os, sys

# global variable (bad practice)
data_list = []

def load_file(path):
    f = open(path)     # file not closed
    content = f.read()
    return content

def process_data(text):
    # inefficient string building
    result = ""
    for i in range(len(text)):
        result = result + text[i]

    # undefined variable bug
    print("Processed length:", lenght)

    return result

def unsafe_exec(user_input):
    # security issue: unsafe use of eval
    return eval(user_input)

def main():
    filename = "non_existing_file.txt"   # will cause FileNotFoundError
    text = load_file(filename)
    data = process_data(text)

    # unused variable
    temp_var = 123

    user_code = input("Enter Python code: ")
    print(unsafe_exec(user_code))

main()
import os, sys

# global variable (bad practice)
data_list = []

def load_file(path):
    f = open(path)     # file not closed
    content = f.read()
    return content

def process_data(text):
    # inefficient string building
    result = ""
    for i in range(len(text)):
        result = result + text[i]

    # undefined variable bug
    print("Processed length:", lenght)

    return result

def unsafe_exec(user_input):
    # security issue: unsafe use of eval
    return eval(user_input)

def main():
    filename = "non_existing_file.txt"   # will cause FileNotFoundError
    text = load_file(filename)
    data = process_data(text)

    # unused variable
    temp_var = 123

    user_code = input("Enter Python code: ")
    print(unsafe_exec(user_code))

main()
