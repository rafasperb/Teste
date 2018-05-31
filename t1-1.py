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

# (3) Um programa recebe como entrada dois horarios (no formato de 12 horas)
# e informa o numero de minutos que se passou entre eles.

def minutos(h1,m1,p1,h2,m2,p2):
    hs = 0
    ms = 0
    hb = 0

    if(h1 > 11 or h2 > 11):
        return -1
    if(m1 > 59 or m2 > 59):
        return -1

    if(p1 == 'pm'):
        h1 = h1+12
    if(p2 == 'pm'):
        h2 = h2+12

    if(p1 == 'am' and p2 == 'am' or p1 == 'pm' and p2 == 'pm'):
        if(h1 == h2 and m1 == m2):
            hs=0
            ms=0
        if(h1 == h2 and m1 < m2):
            hs=0
            ms = m2-m1

        if(h1 == h2 and m1 > m2):
            hs=23
            ms = (60-m1)+m2

        if(h1 < h2 and m1 < m2):
            hs = (h2-h1)
            ms = m2-m1

        if(h1 > h2 and m1 > m2):
            ms = (60-m1)+m2
            hs = (24-h1)+h2
            hb = hb-1

        if(h1 < h2 and m1 > m2):
            hs = (h2-h1)
            ms = (60-m1)+m2

        if(h1 > h2 and m1 < m2):
            ms = m2-m1
            hs = (24-h1)+h2

        if(h1 < h2 and m1 == m2):
            hs = (h2-h1)
            ms = 0

        if(h1 > h2 and m1 == m2):
            ms = 0
            hs = (24-h1)+h2

    if(p1 == 'am' and p2 == 'pm'):
        if(m1 < m2):
            ms = m2-m1
        if(m1 > m2):
            ms = (60-m1)+m2
            hb = hb-1

        hs = h2-h1
    hs = hs + hb
    minutos = (hs*60) + ms
    # print(str(hs)+' '+str(ms)+' '+'minutos: '+str(minutos))

print(minutos(13,00,'pm',1,01,'pm'))
