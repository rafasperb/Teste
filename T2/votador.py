from t2 import Sensor

SS = []

S1 = Sensor(10,10,False)
S2 = Sensor(10,10,False)
S3 = Sensor(9,10,False)

SS.append(S1[0])
SS.append(67)

SS.append(S2)
SS.append(67)

SS.append(S3)
SS.append(67)

i=0

aux = SS[i][0].temp / SS[i][1]
SS[i][2] = SS[i][0].temp - aux


print(aux)
print(SS[i][2])
