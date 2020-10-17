import random
import math
import statistics

PointsGenerated = 128000
TimesPiIsCalculated = 100
ValoresPi = []              #dicionário que irá conter as aproximações de Pi
i = 1

while i < TimesPiIsCalculated:
    IsInside = 0
    IsOutside = 0
    j = 1
    while j < PointsGenerated:
        Coordinate = (random.uniform(-1.0,1.0), random.uniform(-1.0,1.0))   # gerar coordenadas de (-1,-1) a (1,1)
        dist = math.sqrt(Coordinate[0]**2 + Coordinate[1]**2)  #distancia dos pontos ao centro
        if dist < 1 and dist > -1:
            IsInside += 1
        else:
            IsOutside += 1
        j += 1

    AreaPercentage = IsInside/PointsGenerated
    Pi = AreaPercentage * 4                         #Pi é igual à área do circulo
    ValoresPi.append(Pi)
    print("Pi " + str(i) + ":", Pi)                #pois pi*r^2 = A e r=1 logo pi=A
    i += 1

print(statistics.stdev(PiValues))





