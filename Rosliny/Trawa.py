'''
Created on 11 cze 2014

@author: Adrian
'''
from Rosliny import Roslina

class Trawa(Roslina.Roslina):

    def __init__(self, tura, x, y, swiat):
        Roslina.Roslina.__init__(self, tura, "T", x, y, 0, 0, swiat)
