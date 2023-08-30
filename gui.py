import functions

import PySimpleGUI as sG

label = sG.Text("Type in a to-do:")
input_text = sG.InputText(tooltip="Enter todo", key="todo")
add_button = sG.Button(button_text="Add", )

window = sG.Window('My to-do App', layout=[[label], [input_text, add_button]], font=("FiraCode Nerd Font", 14))

while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = functions.readfile()
            todos.append(value['todo'] + '\n')
            functions.writefile(todos)
        case sG.WIN_CLOSED:
            break

window.close()
