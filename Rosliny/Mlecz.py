'''
Created on 11 cze 2014

@author: Adrian
'''
from Rosliny import Roslina

class Mlecz(Roslina.Roslina):
    
    def __init__(self, tura, x, y, swiat):
        Roslina.Roslina.__init__(self, tura, "M", x, y, 0, 0, swiat)
    
    def akcja(self):
        
        for xd in range(3):
            
            Roslina.Roslina.akcja(self)
    
   
        