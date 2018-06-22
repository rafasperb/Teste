from t2 import Sensor
from random import randint

SS = []
S1 = []
S2 = []
S3 = []

S1.append(Sensor(6,10,False))
S2.append(Sensor(10,10,False))
S3.append(Sensor(9,10,False))

SS.append(S1)
S1.append(randint(50, 100))
SS.append(S2)
S2.append(randint(50, 100))
SS.append(S3)
S3.append(randint(50, 100))


i=0

if(S1[0].temp == S2[0].temp):
    print(S1[0].temp)
else:
    if(S1[0].temp == S3[0].temp):
        print(S1[0].temp)
    else:   
         if(S2[0].temp == S3[0].temp):
            print(S2[0].temp)
         else:
              if(S1[1] > S2[1] and S1[1] > S3[1]):
                print(S1[0].temp)  
              else:
                   if(S2[1] > S1[1] and S2[1] > S3[1]):
                     print(S2[0].temp)     
                   else:
                        if(S3[1] > S1[1] and S3[1] > S2[1]):
                            print(S3[0].temp)                





#for i in range(0,3):
#    aux = (SS[i][0].temp * SS[i][1])/100
#    SS[i].append(aux)#posição 2
#
#i=0
#for i in range(0,3):
#    #aux = (SS[i][0].temp - SS[i][2])
#    aux = (8 - SS[i][2])
#    SS[i].append(aux)#posição 3
#
#if(SS[0][3] < SS[1][3] and SS[0][3] < SS[2][3]):
#    print("1")
#
#if(SS[1][3] < SS[0][3] and SS[1][3] < SS[2][3]):
#    print("2")
#    
#if(SS[2][3] < SS[0][3] and SS[2][3] < SS[1][3]):
#    print("3")        
#
#
print(SS[0][1])
print(SS[1][1])
print(SS[2][1])
