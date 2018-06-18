import t2
import unittest

class TestSensor(unittest.TestCase):

    def test_init(self):

        S = t2.Sensor(10,15,False)
        result1 = S.temp
        result2 = S.rad
        result3 = S.hab
        self.assertEqual(result1, 10)
        self.assertEqual(result2, 15)
        self.assertEqual(result3, False)  
        
        
    def test_setH(self):

        S = t2.Sensor(10,15,False)
        S.setH(True)
        result = S.hab
        self.assertEqual(result, True)

        S = t2.Sensor(10,15,True)
        S.setH(False)
        result = S.hab
        self.assertEqual(result, False)
        

    def test_setTemp(self):

        S = t2.Sensor(10,15,False)
        S.setTemp(40)
        result = S.temp
        self.assertEqual(result, 40)

    def test_setRad(self):

        S = t2.Sensor(10,15,False)
        S.setRad(40)
        result = S.rad
        self.assertEqual(result, 40)

    def test_isH(self):

        S = t2.Sensor(10,15,False)
        result = S.isH()
        self.assertEqual(result, False)

        S = t2.Sensor(10,15,True)
        result = S.isH()
        self.assertEqual(result, True)

    def test_isAlerta(self):

        S1 = t2.Sensor(10,15,False)
        result = S1.isAlerta()
        self.assertEqual(result, 0)

        S2 = t2.Sensor(10,15,True)
        result = S2.isAlerta()
        self.assertEqual(result, 3)

        S1 = t2.Sensor(45,6,True)
        result = S1.isAlerta()
        self.assertEqual(result, 2)

        S1 = t2.Sensor(35,3,True)
        result = S1.isAlerta()
        self.assertEqual(result, 1)
        
        S1 = t2.Sensor(20,1,True)
        result = S1.isAlerta()
        self.assertEqual(result, None)
        
        S1 = t2.Sensor(20,1,'blabla')
        result = S1.isAlerta()
        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()
