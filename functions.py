def readfile(filename="todo.txt"):
    """ Returns a list of lines stored in the file."""
    with open(filename, 'r') as file:
        return file.readlines()


def writefile(todo, filename="todo.txt"):
    """ Writes  a list of lines to the given file."""
    with open(filename, 'w') as file:
        file.writelines(todo)

