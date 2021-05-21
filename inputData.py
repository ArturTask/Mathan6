import math
def inputGo():
    print("y' = -y*ln(y)/x причем y(1) = exp(1)") # общ решение: y = exp(C/x) C=const    ||   частное: y = exp(1/x)
    print("")                                       # тогда y' = -exp(1/x)/(x^2)
    # не забудьте, что правая часть - логарифм, поэтому x>=0.2, в противном случае prevFXY<<prevY и при их сложении
    # PrevY <0 а логарифм можно взять только от неотриц. числа
    print("Введите интервал [a,b] и шаг(h)")
    hey = input().split()
    a,b,h = float(hey[0]),float(hey[1]),float(hey[2])
    # a, b, h, e = -10, 3, 0.1, 0.1
    e = 0.1
    print(f"Интервал интегрирования : [{a},{b}]")
    print(f"шаг h = {h}")
    print(f"точность e = {e}")

    answer = [a, b, h, e]

    return answer





