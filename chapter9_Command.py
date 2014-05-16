import sys

# GENERAL WAY ---------------------------
class Window:
    def exit(self):
        sys.exit(0)

class Document:
    def __init__(self, filename):
        self.filename = filename
        self.contents = "This file cannot be modified"

    def save(self):
        with open(self.filename, 'w') as file:
            file.write(self.contents)

class ToolbarButton:
    def __init__(self, name):
        self.name = name

    def click(self):
        self.command.execute()

class MenuItem:
    def __init__(self, name):
        self.name = name

    def click(self):
        self.command.execute()
    
class KeyboardShortcut:
    def __init__(self, name):
        self.name = name

    def click(self):
        self.command.execute() #or self.command() if is __call__able

class SaveCommand:
    def __init__(self, document):
        self.document = document

    def execute(self): #def __call__(self): to make SaveCommand __call__able
        self.document.save()

class ExitCommand:
    def __init__(self, window):
        self.window = window

    def execute(self):
        self.window.exit()
# ----------------------------------
        
# PYTHON WAY -----------------------
class WindowP:
    def exit(self):
        sys.exit(0)

class MenuItemP:
    def click(self):
        self.command()

# ----------------------------------
        
if __name__=='__main__':
    # GENERAL WAY-----------------------
    window = Window()
    exit = ExitCommand(window)
    exit_menu = MenuItem('Exit')
    exit_menu.command = exit
    
    document = Document('chapter9_Command.txt')
    save = SaveCommand(document)

    save_button = ToolbarButton('save')
    save_button.command = save

    save_keystroke = KeyboardShortcut("s")
    save_keystroke.command = save

    # ----------------------------------
    
    # PYTHON WAY -----------------------
    windowP = WindowP()
    menu_itemP = MenuItemP()
    menu_itemP.command = window.exit
    # ----------------------------------
