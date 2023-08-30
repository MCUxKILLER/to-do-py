import functions

import PySimpleGUI as sG

label = sG.Text("Type in a to-do:")
input_text = sG.InputText(tooltip="Enter todo", key="todo")
add_button = sG.Button(button_text="Add", )
list_view = sG.Listbox(values=functions.readfile(), key="todos", enable_events=True, size=(45, 10))
edit_button = sG.Button("edit")

window = sG.Window('My to-do App', layout=[[label], [input_text, add_button], [list_view, edit_button]],
                   font=("FiraCode Nerd Font", 14))

while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = functions.readfile()
            todos.append(value['todo'] + '\n')
            functions.writefile(todos)
            window['todos'].update(values=todos)

        case "edit":
            todos = functions.readfile()
            index = todos.index(value['todos'][0])
            todos[index] = value['todo'] + '\n'
            functions.writefile(todos)
            window['todos'].update(values=todos)

        case "todos":
            window['todo'].update(value=value['todos'][0])

        case sG.WIN_CLOSED:
            break

window.close()
