import tkinter
import random
'''
  The are 3 kind of layout managers in Python
  
  Pack <- example of this type in this module
  Grid
  Place
  
'''
class DiceFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)

        #new object Button (1st parameter the parent object/frame)
        die = tkinter.Button(self, text="Roll", command=self.roll)
        die.pack()#makes button visible

        #new object StringVar()
        self.roll_result = tkinter.StringVar()

        #new object Label (1st parameter the parent object/frame)
        label = tkinter.Label(self, textvariable=self.roll_result)
        label.pack()#makes label visible

        self.pack()#makes the whole frame visible

    def roll(self):
        #everytime the roll_result object changes it refreshes the label
        self.roll_result.set(random.randint(1, 6))


class PackFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        button1 = tkinter.Button(self, text = "expand fill")
        button1.pack(expand=True, fill="both", side="left")
        
        button2 = tkinter.Button(self, text = "anchor ne pady")
        button2.pack(anchor="ne", pady=5, side="left")
        
        button3 = tkinter.Button(self, text = "anchor se padx")
        button3.pack(anchor="se", padx=5, side="left")

class TwoPackFrames(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        button1 = tkinter.Button(self, text="ipadx")
        button1.pack(ipadx=215)
        
        packFrame1 = PackFrame(self)
        packFrame1.pack(side="bottom", anchor="e")
        
        packFrame2 = PackFrame(self)
        packFrame2.pack(side="bottom", anchor="w")
        
        self.pack()

        
if __name__=='__main__':
    root = tkinter.Tk()
    #DiceFrame(master=root).mainloop()
    TwoPackFrames(master=root).mainloop()
                        
                             
