import functions

import PySimpleGUI as sG

label = sG.Text("Type in a to-do:")
input_text = sG.InputText(tooltip="Enter todo", key="todo")
add_button = sG.Button(button_text="Add", )
list_view = sG.Listbox(values=functions.readfile(), key="todos", enable_events=True, size=(45, 10))
edit_button = sG.Button("edit")
complete_button = sG.Button("Complete")
exit_button = sG.Button("exit", size=(4, 1))

column1 = [[label], [input_text], [list_view], [exit_button]]
layoutcolumn1 = sG.Column(column1)

column2 = [[add_button], [edit_button], [complete_button]]
layoutcolumn2 = sG.Column(column2)

window = sG.Window('My to-do App',
                   layout=[[layoutcolumn1, layoutcolumn2]],
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

        case "Complete":
            todos = functions.readfile()
            todos.remove(value['todos'][0])
            functions.writefile(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        case "exit":
            break
        case sG.WIN_CLOSED:
            break

window.close()
