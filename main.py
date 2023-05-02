import PySimpleGUI as sg
from zip_extract import do_extract
import os

# from zip_creator import make_archive

label1 = sg.Text("Select .zip file to Extract: ")
input1 = sg.Input(key="files1")
choose_button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input(key="folder1")
choose_button2 = sg.FolderBrowse("Choose", key="folder")
compress_button = sg.Button("Extract")
new_button = sg.Button("New")

success_message = sg.Text("", size=(30, 1), text_color="yellow", key="success_message")
error_message = sg.Text("", size=(30, 1), text_color="red", key="error_message")

# success_message = sg.Text("", size=(30, 1), text_color="yellow", key="success_message")
# error_message = sg.Text("", size=(30, 1), text_color="red", key="error_message")

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2], [compress_button, new_button], [error_message]])

while True:
    event, values = window.read()
    print(event)
    print(values)
    print(type(values))
    if event == sg.WINDOW_CLOSED:
        break
    if event == "Extract":
        filepath = values['files'].split(',')
        print(filepath)
        filepath[0]
        folder = values['folder']
        print(folder)
        result = do_extract(filepath, folder)
        try:
            if result:
                sg.popup("Zip file extracted successfully!")
            else:
                sg.popup("Only zip files allowed")
        except Exception as e:
            error_text = f"Error: {str(e)}"
            window['error_message'].update(error_text)
    if event == "New":
        window['files1'].update("")
        window['folder1'].update("")

