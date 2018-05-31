import t1
import unittest

class TestBruto(unittest.TestCase):

    def test_nHora_igual_menosUm(self):

        result = t1.bruto(-1,100)
        self.assertEqual(result, -1)

    def test_nHora_igual_0(self):

        result = t1.bruto(0,100)
        self.assertEqual(result, -1)

    def test_nHora_igual_1(self):

        result = t1.bruto(1,100)
        self.assertEqual(result, 100)

    def test_nHora_igual_79(self):

        result = t1.bruto(79,10)
        self.assertEqual(result, 790)

    def test_nHora_igual_80(self):

        result = t1.bruto(80,10)
        self.assertEqual(result, 800)

    def test_nHora_maior_80(self):

        result = t1.bruto(81,100)
        self.assertEqual(result, -1)
############################################
    def test_vHora_igual_menosUm(self):

        result = t1.bruto(10,-1)
        self.assertEqual(result, -1)

    def test_vHora_igual_0(self):

        result = t1.bruto(10,0)
        self.assertEqual(result, -1)

    def test_vHora_igual_1(self):

        result = t1.bruto(10,1)
        self.assertEqual(result, 10)

    def test_vHora_igual_119(self):

        result = t1.bruto(10,119)
        self.assertEqual(result, 1190)

    def test_vHora_igual_120(self):

        result = t1.bruto(10,120)
        self.assertEqual(result, 1200)

    def test_vHora_maior_120(self):

        result = t1.bruto(10,121)
        self.assertEqual(result, -1)

    def test_calculo_bruto(self):

        result = t1.bruto(40,100)
        self.assertEqual(result, 4000)

if __name__ == '__main__':
    unittest.main()
