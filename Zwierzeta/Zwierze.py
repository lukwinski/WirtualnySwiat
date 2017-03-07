from Organizm import Organizm
import random

class Zwierze(Organizm.Organizm):

    def __init__(self, tura, idd, x, y, sila, inic, swiat):
        Organizm.Organizm.__init__(self, tura, idd, x, y, sila, inic, swiat)

    def akcja(self):

        licznik = 0


        kierx = random.randint(-1,1)
        kiery = random.randint(-1,1)

        while (self.getX()+ kierx < 0 or self.getX()+ kierx >= self.swiat.getRozmX()
               or self.getY()+kiery < 0 or self.getY()+kiery >= self.swiat.getRozmY() or (kierx == 0 and kiery == 0) ):

            kierx = random.randint(-1,1)
            kiery = random.randint(-1,1)

        if ( self.swiat.zwrocOrganizm(self.getX() + kierx, self.getY() + kiery ) == None ):
            self.swiat.usunOrganizm(self.getX(), self.getY())
            self.setPoz(self.getX() + kierx, self.getY() + kiery)
           
            self.swiat.dodajOrganizm(self, self.getX(), self.getY())
        else:
            self.swiat.zwrocOrganizm(self.getX()+kierx, self.getY()+kiery).kolizja(self)

    def kolizja(self, gosc):
        
        if self.getId() == gosc.getId():
            
            kierx = random.randint(-1,1)
            kiery = random.randint(-1,1)
            
            iloscProb = 0

            while (self.getX()+ kierx < 0 or self.getX()+ kierx >= self.swiat.getRozmX()
                   or self.getY()+kiery < 0 or self.getY()+kiery >= self.swiat.getRozmY() 
                   or (kierx == 0 and kiery == 0) or self.swiat.zwrocOrganizm(self.getX()+kierx, self.getY()+kiery) != None ):
                
                kierx = random.randint(-1,1)
                kiery = random.randint(-1,1)
                iloscProb = iloscProb + 1
                
                if iloscProb >10:
                    break
            
            if ( self.getX()+ kierx >= 0 and self.getX()+ kierx < self.swiat.getRozmX()
                   and self.getY()+kiery >= 0 and self.getY()+kiery < self.swiat.getRozmY() 
                   and (kierx != 0 and kiery != 0) and self.swiat.zwrocOrganizm(self.getX()+kierx, self.getY()+kiery) == None):
                
                self.swiat.stworzOrganizm(self.getId(), self.getX()+kierx, self.getY()+kiery)
                print "Powstal nowy ", self.getId()
                
        else:
            
            print gosc.getId(), " atakuje ", self.getId()
            
            
            if self.getSila() > gosc.getSila():
                print "Obronca wygral z sila ", self.getSila(), " vs ", gosc.getSila()
                self.swiat.usunOrganizm(gosc.getX(), gosc.getY())
                
            else:
                print "Atakujacy wygral z sila", gosc.getSila(), " vs ", self.getSila()
                
                temp = gosc
                
                self.swiat.usunOrganizm(temp.getX(), temp.getY())
                temp.setPoz(self.getX(), self.getY())
                self.swiat.dodajOrganizm(temp, self.getX(), self.getY())
                
            
            


