'''
Created on 11 cze 2014

@author: Adrian
'''
import sys

class Organizm:
    
    def __init__(self, tura, idd, x, y, sila, inic, swiat):
        self.__turaPowstania = tura
        self.__id = idd
        self.__poz_x = x
        self.__poz_y = y
        self.__sila = sila
        self.__inicjatywa = inic
        self.swiat = swiat
        self.__czyWykonal = False
        
           
    def getId(self):
        return self.__id
        
    def getSila(self):
        return self.__sila
        
        
    def setSila(self, s):
        self.__sila = s
       
        
    def setPoz(self, x, y):
        self.__poz_x = x
        self.__poz_y = y
        
    def getX(self):
        return self.__poz_x
        
    def getY(self):
        return self.__poz_y
        
    def getTuraPowstania(self):
        return self.__turaPowstania
        
    def setTuraPowstania(self, tura):
        self.__turaPowstania = tura
    
    def getInic(self):
        return self.__inicjatywa

    def setCzywykonal(self, czy):
        self.__czyWykonal = czy
        
    def getCzywykonal(self):
        return self.__czyWykonal

    def akcja(self):
        pass
        
    def kolizja(self, gosc):
        pass
    
    def rysowanie(self):
        sys.stdout.write(self.__id+' ')
        
        