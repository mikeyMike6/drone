import PySimpleGUI as sg

layout = [[sg.Text("Hello from another world")], [sg.Button("OK")]]

# tworzenie okna
window = sg.Window("Demo", layout)

# petla wydarzen
while True:
   event, values = window.read()
   if event == "OK" or event == sg.WIN_CLOSED:
      break

window.close()