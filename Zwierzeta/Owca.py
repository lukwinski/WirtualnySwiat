from Zwierzeta import Zwierze

class Owca(Zwierze.Zwierze):
    
    def __init__(self, tura, x, y, swiat):
        Zwierze.Zwierze.__init__(self, tura, "O", x, y, 4, 4, swiat)
        