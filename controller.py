import ui

def button_click():
    ui.hello()
    command = ui.menu()
    if command == '1':
        print("here is instruction")
    if command == '2':
        print("here is input of number-op-number --> calculator")
    if command == '3':
        print("here is log of last 10 operations")