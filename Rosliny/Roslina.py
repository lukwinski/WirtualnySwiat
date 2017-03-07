'''
Created on 11 cze 2014

@author: Adrian
'''

import random

from Organizm import Organizm 

class Roslina(Organizm.Organizm):
    
    def __init__(self, tura, idd, x, y, sila, inic, swiat):
        Organizm.Organizm.__init__(self, tura, idd, x, y, sila, inic, swiat)
        
    def akcja(self):
        
        czywykonywac = random.randint(0,100)
        
        if czywykonywac < 10:
            
            kierx = random.randint(-1,1)
            kiery = random.randint(-1,1)
        
            if self.getX() + kierx >= 0 and self.getX() + kierx < self.swiat.getRozmX():
                if self.getY() + kiery >= 0 and self.getY() + kiery < self.swiat.getRozmY():
                    if ( self.swiat.zwrocOrganizm(self.getX() + kierx, self.getY() + kiery ) == None ):
                        self.swiat.stworzOrganizm(self.getId(), self.getX() + kierx, self.getY() + kiery )
                        print "zasiano nowy", self.getId()
            
    def kolizja(self, gosc):
        print "Roslina ", self.getId(), "zostala zjedzona przez ", gosc.getId()
        
        temp = gosc
        
        self.swiat.usunOrganizm(gosc.getX(), gosc.getY())
        temp.setPoz(self.getX(), self.getY())
        self.swiat.dodajOrganizm(temp, self.getX(), self.getY())
        
                    
                