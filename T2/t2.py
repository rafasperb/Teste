
class Sensor(object):
    def __init__(self, t, r, h):
        self.temp = t
        self.rad = r
        self.hab = h

    def setH(self,h):
        if(h == True):
            self.hab = True #sensor habilitado
        if(h == False):
            self.hab = False #sensor desabilitado

    def setTemp(self,t):
        self.temp = t

    def setRad(self,r):
        self.rad = r

    def isH(self):
        if(self.hab == True):
            return True
        if(self.hab == False):
            return False

    def isAlerta(self):
        if(self.hab == False):
            return 0
        if(self.hab == True):
            if(self.rad > 7):
                return 3
            if(self.rad > 5 or self.temp > 40):
                return 2
            if(self.rad > 1 or self.temp > 30):
                return 1
