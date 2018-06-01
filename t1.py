#########################################################################################
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

vh=0
nh=0

# vh = 190
# nh = 10
# print(bruto(nh,vh))
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
    buff=str(dd)+'/'+str(mm)+'/'+str(aa)
    return buff

# dd=0
# mm=0
# aa=0
#
# print(diaseg(dd,mm,aa))

#########################################################################################
# (3) Um programa recebe como entrada dois horarios (no formato de 12 horas)
# e informa o numero de minutos que se passou entre eles.
#########################################################################################
def minutos(h1,m1,p1,h2,m2,p2):
    hs = 0
    ms = 0
    hb = 0

    if(h1 > 11 or h2 > 11 or h1 < 0 or h2 < 0):
        return -1
    if(m1 > 59 or m2 > 59 or m1 < 0 or m2 < 0):
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
        
    if(p1 == 'pm' and p2 == 'am'):
        if(m1 < m2):
            ms = (60-m1)+m2
            if(ms > 59):
                ms = ms-60
                hb = hb+1
            hb = hb-1
        if(m1 > m2):
            ms = (60-m1)+m2
            hb= hb-1
        if(m1 == m2):
            ms = 0
        hs = (24-h1)+h2  
        
        
    hs = hs + hb
    minutos = (hs*60) + ms
    #print(str(hs)+' '+str(ms)+' '+'minutos: '+str(minutos))
    return minutos

#minutos(10,50,'am',10,55,'pm')

#########################################################################################
# (4) Analise a funcao descrita a seguir e, aplicando a tecnica de particionamento de classes
#  de equivalencia, apresente os casos de testes oriundos da aplicacao desta
#  tecnica (apresente tambem toda a aplicacao da tecnica)
#  A funcao NEXTDATE recebe 4 parametros (dia, mes, ano, diaSemana) e retorna
#  a data subsequente a data representada pelos parametros.
#  Eis as condicoes:  1=< mes =< 12  1 =< dia =< 31  1900 =< ano <=2100
#  diaSemana = True a mostra o dia da semana  diaSemana = False
#  a nao mostra o dia da semana
#########################################################################################
    
def nextdate(dia, mes, ano, diaSemana):
    import datetime    
    
    if(dia < 1 or dia > 31):
        return -1
    if(mes < 1 or mes > 12):
        return -1
    if(ano < 1900 or ano > 2100):
        return -1
    if(diaSemana != 'True' and diaSemana != 'False'):
        return-1
        
    dia=dia+1

    if(dia == 32):
        dia=1
        mes=mes+1

    if(mes == 13):
        mes=1
        ano=ano+1
        if(ano == 2101):
            return -1
    day = datetime.datetime(ano,mes,dia)
        
    if( diaSemana == 'True'):
        aux = datetime.datetime.weekday(day)
        if(aux == 0):
            diaS = ' - Segunda-Feira'
        if(aux == 1):
            diaS = ' - Terça-Feira'
        if(aux == 2):
            diaS = ' - Quarta-Feira'
        if(aux == 3):
            diaS = ' - Quinta-Feira'
        if(aux == 4):
            diaS = ' - Sexta-Feira'
        if(aux == 5):
            diaS = ' - Sábado'
        if(aux == 6):
            diaS = ' - Domingo'                  
            
        buff=str(dia)+'/'+str(mes)+'/'+str(ano)+diaS
        return buff
    if(diaSemana == 'False'):
        buff=str(dia)+'/'+str(mes)+'/'+str(ano)
        return buff 

#print(nextdate(1,1,2100,'True'))    
