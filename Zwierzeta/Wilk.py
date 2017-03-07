from Zwierzeta import Zwierze

class Wilk(Zwierze.Zwierze):
    
    def __init__(self, tura, x, y, swiat):
        Zwierze.Zwierze.__init__(self, tura, "W", x, y, 9, 5, swiat)
        