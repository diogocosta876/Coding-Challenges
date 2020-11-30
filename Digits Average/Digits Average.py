import math

def digits_average(n):
    SumNum = 1000
    tmp = 1
    i = 0
    while True:
        if n // tmp < 10:
            i += 1
            break
        else:
            tmp = tmp * 10
            i += 1
    print(i)

    while SumNum > 10:
        if n < 10:
            SumNum = n
            break
        SumNum = 0
        print(str(n) + " n")

        for i in range(i, 1, -1):
            if SumNum < 10 and SumNum != 0:
                break
            print("REITERATING " + str(i))
            print("SUM NUM " + str(SumNum))
            increasing = 0
            if SumNum != 0:
                n = SumNum
            for x in range(1, i):
                # print(str(10**(x+1)) + "numero a dividir")
                tmp = (n % (10 ** (x + 1)))
                print(str(tmp) + " tmp")
                # print("x: " + str(x))

                n1 = tmp // 10 ** x
                n2 = (tmp % 10 ** x) // 10 ** (x - 1)
                average = math.ceil((n1 + n2) / 2)

                increasing = increasing + average * 10 ** (x - 1)
                # print(str(n1) + " e " + str(n2))
                print("average: " + str(average))
                print(" ")
                print("increasing value: " + str(increasing))
                print(" ")
            SumNum = increasing
            print("riteration value: " + str(SumNum))
    return SumNum

print("FINAL ANSWER:  " + str(digits_average(int(input()))))