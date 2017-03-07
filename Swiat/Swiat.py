'''
Created on 10 cze 2014

@author: Adrian
'''

from Rosliny import Mlecz, Guarana, Trawa

from Zwierzeta import Owca, Wilk, Leniwiec, Dzik, Slimak

import sys

class Swiat:
    
    def __init__(self, sizex, sizey):
        
        self.__size_x = sizex
        
        self.__size_y = sizey
        
        self.__nrTury = 1
        
        
        
        self.__organizmy = [[0 for col in range(sizex)] for row in range(sizey)]
        
        self.__iloscOrg = 0
        
        for tmp in range(sizey):
            for tmp2 in range(sizex):
                self.__organizmy[tmp][tmp2] = None
                
        self.__organizmy[2][3] = Trawa.Trawa(0, 3, 2, self)
        self.__organizmy[5][6] = Guarana.Guarana(0, 6, 5, self)
        self.__organizmy[7][7] = Mlecz.Mlecz(0, 7, 7, self)
        self.__organizmy[5][10] = Leniwiec.Leniwiec(0, 10, 5, self)
        self.__organizmy[8][2] = Dzik.Dzik(0, 2, 8, self)
        self.__organizmy[13][18] = Owca.Owca(0, 18, 13, self)
        self.__organizmy[4][16] = Wilk.Wilk(0, 16, 4, self)
        self.__organizmy[9][15] = Slimak.Slimak(0, 15, 9, self)
        
        self.sortujOrg()
              
    def rysujSwiat(self):
        for row in range(self.__size_y):
            for col in range(self.__size_x):
                if self.__organizmy[row][col] is not None:
                    self.__organizmy[row][col].rysowanie()
                else:
                    sys.stdout.write('. ')
            print
            
    def getRozmX(self):
        return self.__size_x
    
    def getRozmY(self):
        return self.__size_y
    
    def getNrTury(self):
        return self.__nrTury
    
    def stworzOrganizm(self, idd, x, y):
        
        if idd == 'T':
            self.__organizmy[y][x] = Trawa.Trawa(self.getNrTury(), x, y, self)
        elif idd == 'M':
            self.__organizmy[y][x] = Mlecz.Mlecz(self.getNrTury(), x, y, self)
        elif idd == 'G':
            self.__organizmy[y][x] = Guarana.Guarana(self.getNrTury(), x, y, self)
        elif idd == 'D':
            self.__organizmy[y][x] = Dzik.Dzik(self.getNrTury(), x, y, self)
        elif idd == 'L':
            self.__organizmy[y][x] = Leniwiec.Leniwiec(self.getNrTury(), x, y, self)
        elif idd == 'O':
            self.__organizmy[y][x] = Owca.Owca(self.getNrTury(), x, y, self)
        elif idd == 'S':
            self.__organizmy[y][x] = Slimak.Slimak(self.getNrTury(), x, y, self)
        elif idd == 'W':
            self.__organizmy[y][x] = Wilk.Wilk(self.getNrTury(), x, y, self)
            
            
            
    def sortujOrg(self):
        self.sortOrg = [];
        
        for row in range(self.__size_y):
            for col in range(self.__size_x):
                if self.__organizmy[row][col] is not None:
                    self.sortOrg.append(self.__organizmy[row][col])
                
        
            
    def wykonajTure(self):
        
        self.sortujOrg()
        
        for obiekt in self.sortOrg:
            obiekt.akcja()
            
        self.__nrTury = self.__nrTury+1
            
    def dodajOrganizm(self, dodawany, x, y):
        self.__organizmy[y][x] = dodawany
        
    def zwrocOrganizm(self, x, y):
        return self.__organizmy[y][x]
            
    def usunOrganizm(self, x, y):
        self.__organizmy[y][x] = None