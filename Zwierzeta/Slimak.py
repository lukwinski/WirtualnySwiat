from Zwierzeta import Zwierze

class Slimak(Zwierze.Zwierze):
    
    def __init__(self, tura, x, y, swiat):
        Zwierze.Zwierze.__init__(self, tura, "S", x, y, 1, 1, swiat)
        