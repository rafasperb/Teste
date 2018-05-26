# (1) Um metodo int bruto(int nh, vh) calcula o pagamento bruto semanal a partir do numero
#  de horas trabalhadas nh e do valor por hora vh.
#  Um trabalhador nao pode trabalhar mais do que 80hs por semana
#  e o valor hora maximo e de R$ 120,00 por hora.
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

# (2) Um metodo diaseg(int, dd,mm,aa) recebe tres valores correspondentes
# a uma data e calcula a data do dia seguinte. Sabendo
# que dd e [1;31], mm e [1;12] e aa e [1812;2024]

#########################################################################################

def diaseg(dd,mm,aa):
    if(dd < 1 or dd > 31):
        return -1
    if(mm < 1 or mm > 12):
        return -1
    if(aa < 1812 or aa > 2024):
        return -1

    dd=dd+1

    if(dd == 32):
        dd=1
        mm=mm+1

    if(mm == 13):
        mm=1
        aa=aa+1

    if(aa == 2025):
        return -1
    return dd, mm, aa

dd=31
mm=12
aa=2024

print(diaseg(dd,mm,aa))

#########################################################################################
