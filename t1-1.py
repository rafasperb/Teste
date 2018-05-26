# (1) Um método int bruto(int nh, vh) calcula o pagamento bruto semanal a partir do número
#  de horas trabalhadas nh e do valor por hora vh.
#  Um trabalhador não pode trabalhar mais do que 80hs por semana
#  e o valor hora máximo é de R$ 120,00 por hora.
#########################################################################################
def bruto(nh , vh):
    if ( nh < 1 or nh > 80):
        return -1
    if ( vh < 1 or vh > 120):
        return -1
    return nh * vh

vh = 190
nh = 10
print(bruto(nh,vh))
#########################################################################################
