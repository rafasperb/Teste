def setH(s,h):
    if(h == True):
        s = 1 #sensor habilitado
    if(h == False):
        s = 0 #sensor desabilitado

def setTemp(s,t):
    temperatura = t

def setRad(s,r):
    radiacao = r

def isH(s):
    if(s == 1):
        return True
    if(s == 0):
        return False

def isAlerta(s):
    if(s == 0):
        return 0
    if(s == 1):
        if(radiacao > 7):
            return 3
        if(radiacao > 5 or temperatura > 40):
            return 2
        if(radiacao > 1 or temperatura > 30):
            return 1

s = 0
t = 0
r = 0 
temperatura = 0
radiacao = 0
h = False
