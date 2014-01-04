import sys
from chapter2_notebook import Notebook, Note

class Menu:
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            '1': self.show_notes,
            '2': self.search_notes,
            '3': self.add_note,
            '4': self.modify_note,
            '5': self.quit
            }

    def display_menu(self):
        print('''
    NoteBook Menu

    1. Show all Notes
    2. Search Notes
    3. Add Note
    4. Modify Notes
    5. Quit
    ''')

    def run(self):
        while True:
            self.display_menu()
            choice = input('Enter an option: ')
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print('{0} is not a valid choice'.format(choice))
    
    def show_notes(self, notes = None):
        if not notes:
            notes = self.notebook.notes

        for note in notes:
            print("{0}: {1}\n{2}".format(note.id, note.tags, note.memo))

    def search_notes(self):
        filter = input('Search for what: ')
        notes = self.notebook.search(filter)
        if notes:
            self.show_notes(notes)
        else:
            print('Not found')

    def add_note(self):
        memo = input('Enter a memo: ')
        self.notebook.new_note(memo)
        print('New note has been added')

    def modify_note(self):
        id = input('Enter note id: ')
        memo = input('Enter a memo: ')
        tag = input('Enter a tag: ')

        if memo:
            self.notebook.modify_memo(id, memo)
        if tag:
            self.notebook.modify_tags(int(id), tag)

    def quit(self):
        print('Goodbye...')
        sys.exit(0)

if __name__ == '__main__':
    Menu().run()
