from Zwierzeta import Zwierze

class Leniwiec(Zwierze.Zwierze):
    
    def __init__(self, tura, x, y, swiat):
        Zwierze.Zwierze.__init__(self, tura, "L", x, y, 2, 1, swiat)
        self.czyRuszal = False
        
    def akcja(self):
        if self.czyRuszal == False:
            Zwierze.Zwierze.akcja(self)
            self.czyRuszal = True
            print "Leniwiec sie ruszyl"
        else:
            self.czyRuszal = False
            