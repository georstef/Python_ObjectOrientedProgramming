''' interface
class Forder:
    def __init__(self, name):
        self.name = name
        self.children = {}

    def add_child(self, child):
        pass

    def move(self, new_path): #common method
        pass
    
    def delete(self):#common method
        pass
    
class File:
    def __init__(self, name, contents):
        self.name = name
        self.contents = contents

    def move(self, new_path): #common method
        pass

    def delete(self):#common method
        pass
'''        
#-------------------------------------------------------
class Component:
    def __init__(self, name):
        self.name = name

    def move(self, new_path):
        new_folder = get_path(new_path)
        del(self.parent.children[self.name])
        new_folder.children[self.name] = self
        self.parent = new_folder

    def delete(self):
        #delete from the parent the child with the current name
        del(self.parent.children[self.name])

class Folder(Component):
    def __init__(self, name):
        self.name = name
        self.children = {}

    def add_child(self, child):
        child.parent = self
        self.children[child.name] = child

class File(Component):
    def __init__(self, name, contents):
        self.name = name
        self.contents = contents

root = Folder('')
def get_path(path):
    names = path.split('/')[1:]
    node = root
    for name in names:
        node = node.children[name]
    return node

if __name__=='__main__':
    folder1 = Folder('folder1')
    folder2 = Folder('folder2')

    root.add_child(folder1)
    root.add_child(folder2)

    folder11 = Folder('folder11')
    folder1.add_child(folder11)

    file111 = File('file111', 'contents')
    folder11.add_child(file111)

    file21 = File('file21', 'other contents')
    folder2.add_child(file21)

    print(root.children)
    print(folder2.children)
    
