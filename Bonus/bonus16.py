import PySimpleGUI as sG

label1 = sG.Text("Select Files: ", background_color="black")
label2 = sG.Text("Select Destination: ", background_color="black")

input1 = sG.InputText(tooltip="Choose files")
input2 = sG.InputText(tooltip="Choose Destination")

button1 = sG.FilesBrowse("Choose", button_color=("black", "white"))
button2 = sG.FolderBrowse("Choose", button_color=("black", "white"))

compress_button = sG.Button("Compress", button_color=("black", "white"))

window = sG.Window("File compressor", layout=[[label1, input1, button1], [label2, input2, button2],[compress_button]],
                   background_color="black")
window.read()
window.close()
