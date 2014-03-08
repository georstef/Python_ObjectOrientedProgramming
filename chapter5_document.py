class Document:
    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ''

    def insert(self, character):
        if not hasattr(character, 'c'):
            character = Character(character)
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()

    def delete(self):
        del self.characters[self.cursor.position]

    def save(self):
        f = open(self.filename, 'w')
        f.write(''.join(self.characters))
        f.close()

    def forward(self):
        self.cursor.forward()

    def back(self):
        self.cursor.back()

    def __str__(self):
        '''
        instead of saying print(doc.string) we use print(doc)
        '''
        return ''.join(str(c) for c in self.characters)

    @property
    def string(self):
        return ''.join(self.characters)

class Cursor:
    def __init__(self, document):
        self.document = document
        self.position = 0

    def forward(self):
        self.position +=1

    def back(self):
        self.position -=1

    def home(self):
        while self.document.characters[self.position-1].c != '\n':
            self.back()
            if self.position == 0:
                break
            
    def end(self):
        while self.position < len(self.document.characters) and self.document.characters[self.position].c !='/n':
            self.back()

class Character:
    def __init__(self, c, bold=False, italic=False,underline=False):
        assert len(c) == 1
        self.c = c
        self.bold=bold
        self.italic=italic
        self.underline=underline

    def __str__(self):
        bold = '*' if self.bold else ''
        italic = '/' if self.italic else ''
        underline = '_' if self.underline else ''
        return bold+italic+underline+self.c
        
