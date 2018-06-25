from t2 import Sensor
from random import randint

class Conf(Sensor):
    def __init__(self, t, r, h, c):
        super().__init__(t,r,h)
        self.conf = c

def Votador(a,b,c):

    if(a.temp == b.temp and a.rad == b.rad):
        if((c.conf - a.conf) > 20 and (c.conf - b.conf) > 20):
            return c
        else:
            return a
    else:
        if(a.temp == c.temp and a.rad == c.rad):
            if((b.conf - a.conf) > 20 and (b.conf - c.conf) > 20):
                return b
            else:
                return a
        else:
            if(b.temp == c.temp and b.rad == c.rad):
                if((a.conf - b.conf) > 20 and (a.conf - c.conf) > 20):
                    return a
                else:
                    return b
            else:
                if(a.conf > b.conf and a.conf > c.conf):
                    return a
                else:
                    if(b.conf > a.conf and b.conf > c.conf):
                        return b
                    else:
                        if(c.conf > a.conf and c.conf > b.conf):
                            return c
