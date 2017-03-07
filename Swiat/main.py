import sys
sys.path.append("D:\swiat\WirtualnySwiat")
import Gui

from Swiat import Swiat

klasa = Swiat(20,20)

klasa.rysujSwiat()

app = Gui.Gui(None, klasa)
app.title('Swiat')
app.mainloop()

while 1:
    
    sys.stdin.readline()
    
    klasa.wykonajTure()
    klasa.rysujSwiat()
    
    
    


