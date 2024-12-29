FILEPATH = "todos.txt"

def get_todos(filepath = FILEPATH):
    """ Read a text file and return the list of to-do items """
    # with context manager, dont need to close file
    with open(filepath,"r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath = FILEPATH):
    """ Write the to-do items list in the text file """
    # Store list with more todos back to text file (overwriting previous)
    with open(filepath,"w") as file:
        file.writelines(todos_arg)

# Hidden varible __name__ is __main__ when functions.py is executed directly. When being imported __name__ is sth else
if __name__ == "__main__":
    print("Hello")
    print(get_todos())