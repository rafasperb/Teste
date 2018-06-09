import t2
import unittest

class TestInicial(unittest.TestCase):

    def test_init(self):

        S = t2.Sensor(10,15,False)
        result1 = S.temp
        result2 = S.rad
        result3 = S.hab
        self.assertEqual(result1, 10)
        self.assertEqual(result2, 15)
        self.assertEqual(result3, False)

if __name__ == '__main__':
    unittest.main()
