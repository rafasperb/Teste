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

class Testdiaseg(unittest.TestCase):

    def test_dia_menor_um(self):

        result = t1.diaseg(0,1,2000)
        self.assertEqual(result, -1)

    def test_dia_igual_um(self):

        result = t1.diaseg(1,1,2000)
        self.assertEqual(result, '2/1/2000')

    def test_dia_igual_31(self):

        result = t1.diaseg(31,1,2000)
        self.assertEqual(result, '1/2/2000')

    def test_dia_maior_31(self):

        result = t1.diaseg(32,1,2000)
        self.assertEqual(result, -1)

#########################################################
    def test_mes_menor_um(self):

        result = t1.diaseg(1,0,2000)
        self.assertEqual(result, -1)

    def test_mes_igual_um(self):

        result = t1.diaseg(31,1,2000)
        self.assertEqual(result, '1/2/2000')

    def test_mes_igual_12(self):

        result = t1.diaseg(31,12,2000)
        self.assertEqual(result, '1/1/2001')

    def test_mes_maior_12(self):

        result = t1.diaseg(32,13,2000)
        self.assertEqual(result, -1)
#########################################################
    def test_ano_menor_1812(self):

        result = t1.diaseg(1,1,1811)
        self.assertEqual(result, -1)

    def test_ano_igual_1812(self):

        result = t1.diaseg(1,1,1812)
        self.assertEqual(result, '2/1/1812')

    def test_ano_igual_2024(self):

        result = t1.diaseg(1,1,2024)
        self.assertEqual(result, '2/1/2024')

    def test_ano_maior_2024(self):

        result = t1.diaseg(1,1,2025)
        self.assertEqual(result, -1)
#########################################################
    def test_dia31_mes12_ano2000(self):

        result = t1.diaseg(31,12,2000)
        self.assertEqual(result, '1/1/2001')
#########################################################

class Testminutos(unittest.TestCase):

    def test_horario1_(self):

        result = t1.diaseg(0,1,2000)
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()
