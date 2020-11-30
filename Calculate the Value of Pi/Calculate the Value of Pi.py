import random
import math
import statistics

multiplier = 1
TimesPiIsCalculated = 100
PiValues = []              #dicionário que irá conter as aproximações de Pi
Continue = True

while Continue:
    PiValues.clear()
    for i in range(TimesPiIsCalculated):
        IsInside = 0
        IsOutside = 0

        for j in range(1000 * multiplier):
            Coordinate = (random.uniform(-1.0,1.0), random.uniform(-1.0,1.0))   # gerar coordenadas de (-1,-1) a (1,1)
            dist = math.sqrt(Coordinate[0]**2 + Coordinate[1]**2)  #distancia dos pontos ao centro

            if dist < 1 and dist > -1:
                IsInside += 1
            else:
                IsOutside += 1

        AreaPercentage = IsInside/(1000 * multiplier)
        Pi = AreaPercentage * 4                         #Pi é igual à área do circulo
        PiValues.append(Pi)
        print("Pi " + str(i) + ":", Pi)                #pois pi*r^2 = A e r=1 logo pi=A
        print(statistics.stdev(PiValues))

    if statistics.stdev(PiValues) < 0.005:
        break
    else:
        multiplier *= 2


