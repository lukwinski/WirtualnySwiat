import Tkinter

class Gui(Tkinter.Tk):
    def __init__(self,parent, swiat):
        Tkinter.Tk.__init__(self,parent)
        self.swiat = swiat
        self.initialize()
        
    def initialize(self):
        self.grid()
        
        self.w = Tkinter.Canvas(self, width=400, height=400)
        self.w.grid(column=2, row=1)
        

        button = Tkinter.Button(self,text=u"Nowa tura !", command=self.OnButtonClick)
        button.grid(column=1,row=0)
        
    
    def OnButtonClick(self):
        self.swiat.wykonajTure()
        self.swiat.rysujSwiat()
        
        for row in range(self.swiat.getRozmY()):
            for col in range(self.swiat.getRozmX()):
                if self.swiat.zwrocOrganizm(col, row) is not None:
                    typ = self.swiat.zwrocOrganizm(col, row).getId()
                    
                    if typ == 'T':
                        self.w.create_rectangle(0+row*20, 0+col*20, 20+row*20, 20+col*20, fill="green")
                    elif typ == 'M':
                        self.w.create_rectangle(0+row*20, 0+col*20, 20+row*20, 20+col*20, fill="yellow")
                    elif typ == 'G':
                        self.w.create_rectangle(0+row*20, 0+col*20, 20+row*20, 20+col*20, fill="blue")
                    elif typ == 'D':
                        self.w.create_rectangle(0+row*20, 0+col*20, 20+row*20, 20+col*20, fill="black")
                    elif typ == 'L':
                        self.w.create_rectangle(0+row*20, 0+col*20, 20+row*20, 20+col*20, fill="pink")
                    elif typ == 'O':
                        self.w.create_rectangle(0+row*20, 0+col*20, 20+row*20, 20+col*20, fill="white")
                    elif typ == 'S':
                        self.w.create_rectangle(0+row*20, 0+col*20, 20+row*20, 20+col*20, fill="orange")
                    elif typ == 'W':
                        self.w.create_rectangle(0+row*20, 0+col*20, 20+row*20, 20+col*20, fill="red")
            
                    
                else:
                    self.w.create_rectangle(0+row*20, 0+col*20, 20+row*20, 20+col*20, fill="grey")
        
        
      
    
