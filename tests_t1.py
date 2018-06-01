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

    def test_horario1_menor_0(self):

        result = t1.minutos(-1,10,'pm',10,10,'pm')
        self.assertEqual(result, -1)

    def test_horario2_menor_0(self):

        result = t1.minutos(10,10,'pm',-1,10,'pm')
        self.assertEqual(result, -1)

    def test_horario1_maior_11(self):

        result = t1.minutos(12,10,'pm',10,10,'pm')
        self.assertEqual(result, -1)

    def test_horario2_maior_11(self):

        result = t1.minutos(10,10,'pm',12,10,'pm')
        self.assertEqual(result, -1)

    def test_minutos1_menor_0(self):

        result = t1.minutos(10,-1,'pm',10,10,'pm')
        self.assertEqual(result, -1)

    def test_minutos2_menor_0(self):

        result = t1.minutos(10,10,'pm',10,-1,'pm')
        self.assertEqual(result, -1)

    def test_minutos1_maior_59(self):

        result = t1.minutos(10,60,'pm',10,10,'pm')
        self.assertEqual(result, -1)

    def test_minutos2_maior_59(self):

        result = t1.minutos(10,10,'pm',10,60,'pm')
        self.assertEqual(result, -1)

    def test_horario1pm_maior_horario2pm(self):

        result = t1.minutos(10,20,'pm',10,10,'pm')
        self.assertEqual(result, 1430)
    
    def test_horario1pm_menor_horario2pm(self):

        result = t1.minutos(10,20,'pm',10,30,'pm')
        self.assertEqual(result, 10)
        
    def test_horario1am_maior_horario2am(self):

        result = t1.minutos(10,20,'am',10,10,'am')
        self.assertEqual(result, 1430)
    
    def test_horario1am_menor_horario2am(self):

        result = t1.minutos(10,20,'am',10,30,'am')
        self.assertEqual(result, 10)

    def test_horario1pm_maior_horario2am(self):

        result = t1.minutos(10,20,'pm',10,10,'am')
        self.assertEqual(result, 710)
    
    def test_horario1pm_menor_horario2am(self):

        result = t1.minutos(10,20,'pm',10,30,'am')
        self.assertEqual(result, 730)          

    def test_horario1am_maior_horario2pm(self):

        result = t1.minutos(10,20,'am',10,10,'pm')
        self.assertEqual(result, 710)
    
    def test_horario1am_menor_horario2pm(self):

        result = t1.minutos(10,20,'am',10,30,'pm')
        self.assertEqual(result, 730)          
        
#########################################################

class TestNextdate(unittest.TestCase):

    def test_dia_menor_1(self):

        result = t1.nextdate(0,1,2000,'True')
        self.assertEqual(result, -1)
        
    def test_dia_maior_1(self):

        result = t1.nextdate(2,1,2000,'True')
        self.assertEqual(result, '3/1/2000 - Segunda-Feira')

    def test_dia_igual_31(self):

        result = t1.nextdate(31,1,2000,'True')
        self.assertEqual(result, '1/2/2000 - Terça-Feira')

    def test_dia_maior_31(self):

        result = t1.nextdate(32,1,2000,'True')
        self.assertEqual(result, -1)

    def test_mes_menor_1(self):

        result = t1.nextdate(1,0,2000,'True')
        self.assertEqual(result, -1)

    def test_mes_maior_1(self):

        result = t1.nextdate(2,1,2000,'True')
        self.assertEqual(result, '3/1/2000 - Segunda-Feira')      
        
    def test_mes_igual_12(self):

        result = t1.nextdate(1,12,2000,'True')
        self.assertEqual(result, '2/12/2000 - Sábado')

    def test_mes_maior_12(self):

        result = t1.nextdate(1,13,2000,'True')
        self.assertEqual(result, -1)

    def test_ano_menor_1900(self):

        result = t1.nextdate(1,1,1899,'True')
        self.assertEqual(result, -1)

    def test_ano_igual_1900(self):

        result = t1.nextdate(1,1,1900,'True')
        self.assertEqual(result, '2/1/1900 - Terça-Feira')

    def test_ano_igual_2100(self):

        result = t1.nextdate(1,1,2100,'True')
        self.assertEqual(result, '2/1/2100 - Sábado')

    def test_ano_maior_2100(self):

        result = t1.nextdate(1,1,2101,'True')
        self.assertEqual(result, -1)

    def test_true(self):

        result = t1.nextdate(1,1,2100,'True')
        self.assertEqual(result, '2/1/2100 - Sábado')

    def test_false(self):

        result = t1.nextdate(1,1,2100,'False')
        self.assertEqual(result, '2/1/2100')

    def test_diaSem(self):

        result = t1.nextdate(1,1,2100,'blablabla')
        self.assertEqual(result, -1)         

if __name__ == '__main__':
    unittest.main()
