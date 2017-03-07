from Zwierzeta import Zwierze

class Dzik(Zwierze.Zwierze):
    
    def __init__(self, tura, x, y, swiat):
        Zwierze.Zwierze.__init__(self, tura, "D", x, y, 10, 10, swiat)
        
        
    def akcja(self):
        for xd in range(2):
            Zwierze.Zwierze.akcja(self)
            