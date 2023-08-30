from functions import writefile, readfile
import time
condition = True
create_time = f"It is {time.strftime('%b %d, %Y %H:%M:%S')}"
print(create_time)
while condition:

    decision = input("Type add, show, edit, complete or exit: ").strip().lower()

    if decision.startswith('add'):
        todo = decision[4:] + '\n'

        storeInput = readfile()

        storeInput.append(todo)

        writefile(storeInput)

    elif decision.startswith('show'):
        storeInput = readfile()

        todos = [i.capitalize().strip('\n') for i in storeInput]

        for index, i in enumerate(todos):
            print(f"{index + 1}. {i}")

    elif decision.startswith('edit'):
        try:
            number = int(decision[5:])
        except Exception:
            print("Expected a number in the list")
            continue

        storeInput = readfile()

        if 0 < number <= len(storeInput):
            newTodo = input('The Edited todo : ') + '\n'
            storeInput[number - 1] = newTodo

            writefile(storeInput)

    elif decision.startswith('exit'):
        condition = False

    elif decision.startswith('complete'):
        try:
            number = int(decision[9:])

            storeInput = readfile()

            todo_to_remove = storeInput[number - 1].strip('\n')

            storeInput.pop(number - 1)

            writefile(storeInput)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("Out of range!!")
            continue
        except ValueError:
            print("Enter a value please")
            continue

    else:
        print("Enter a valid task!")

print("Bye")

# Strings are immutable
