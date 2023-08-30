import functions

import PySimpleGUI as sG

label = sG.Text("Type in a to-do:")
input_text = sG.InputText(tooltip="Enter todo")
add_button = sG.Button(button_text="Add", )

window = sG.Window('My to-do App', layout=[[label], [input_text, add_button]])
window.read()
window.close()
