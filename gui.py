import functions

import PySimpleGUI as sG
import time
import os
import re

if not os.path.exists("todo.txt"):
    with open("todo.txt", 'w') as file:
        pass

text_regex = re.compile(r'\w+')
sG.theme("BluePurple")

clock = sG.Text("", key="clock")
label = sG.Text("Type in a to-do:")
input_text = sG.InputText(tooltip="Enter todo", key="todo")
add_button = sG.Button(button_text="Add", size=10, bind_return_key=True)
list_view = sG.Listbox(values=functions.readfile(), key="todos", enable_events=True, size=(45, 10))
edit_button = sG.Button("Edit", size=10)
complete_button = sG.Button("Complete", size=10)
exit_button = sG.Button("Exit", size=8)

column1 = [[clock], [label], [input_text], [list_view], [exit_button]]
layoutcolumn1 = sG.Column(column1)

column2 = [[add_button], [edit_button], [complete_button]]
layoutcolumn2 = sG.Column(column2)

window = sG.Window('My to-do App',
                   layout=[[layoutcolumn1, layoutcolumn2]],
                   font=("FiraCode Nerd Font", 14))

while True:
    event, value = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            try:
                assert text_regex.search(value['todo'].strip()) is not None, "Empty todo"
                todos = functions.readfile()
                todos.append(value['todo'].strip() + '\n')
                functions.writefile(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except AssertionError:
                sG.popup("No empty spaces allowed, Enter a valid todo")

        case "Edit":
            try:
                assert text_regex.search(value['todo'].strip()) is not None, "Empty todo"
                todos = functions.readfile()
                index = todos.index(value['todos'][0])
                todos[index] = value['todo'].strip() + '\n'
                functions.writefile(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sG.popup("Please select a todo first")
            except AssertionError:
                sG.popup("Enter a todo for the edit")

        case "todos":
            window['todo'].update(value=value['todos'][0])

        case "Complete":
            try:
                todos = functions.readfile()
                todos.remove(value['todos'][0])
                functions.writefile(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sG.popup("Please select a todo first")
        case "Exit":
            break
        case sG.WIN_CLOSED:
            break

window.close()
