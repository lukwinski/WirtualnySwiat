'''
Created on 11 cze 2014

@author: Adrian
'''
from Rosliny import Roslina

class Guarana(Roslina.Roslina):
    
    def __init__(self, tura, x, y, swiat):
        Roslina.Roslina.__init__(self, tura, "G", x, y, 0, 0, swiat)
    
    def kolizja(self, gosc):
        print "Guarana zostala zjedzona przez ", gosc.getId()
        
        temp = gosc
        
        self.swiat.usunOrganizm(gosc.getX(), gosc.getY())
        temp.setPoz(self.getX(), self.getY())
        self.swiat.dodajOrganizm(temp, self.getX(), self.getY())
        gosc.setSila(gosc.getSila() + 3)