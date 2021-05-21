import math

def countY(x, y):  # это наше f(xi,yi) - правая часть диф уравнения
    return -y * math.log(y) / x


def exactCountY(x):  # это точное значение
    return math.exp(1 / x)




def countEyler(a,b,h,e):
    counter = 0
    prevY = math.exp(1)
    # print(f"a = {a}")
    if(a<0.2):
        a=0.2

    prevFXY = countY(a,math.exp(1))

    x=a
    tempAnswer = [counter,a,prevY,countY(a, math.exp(1)),exactCountY(a),prevY**h - prevY**(2*h)]
    answer = [tempAnswer]
    while(x<b):
        if(x+h==0):
            x+=h
        counter+=1
        x = x+h
        temp = prevY
        prevY = prevY + h*prevFXY
        # print(f"x = {x}")
        # print(f"prevY = {prevY}")
        # print(f"prevFXY = {prevFXY}")
        prevFXY = countY(x,temp)

        tempAnswer = [counter,x,prevY,prevFXY,exactCountY(x),prevY**h - prevY**(2*h)]
        answer.append(tempAnswer)

    return answer

def printAnswer(ans):
    mySin = 0
    print("i         Xi        Yi          f(xi,yi)     точное зн-ие      R")
    for i in range(len(ans)):
        print(
            f"{ans[i][0]:.0f}       {ans[i][1]:.3f}     {ans[i][2]:.3f}       {ans[i][3]:.3f}        {ans[i][4]:.3f}            {ans[i][5]:.4f}")
        if(abs(ans[i][2]-ans[i][4])>mySin):
            mySin = abs(ans[i][2]-ans[i][4])
    print(f"Погрешность(e) =  {abs(mySin):.3f}")

def countAdams(a,b,h,e):
    if (a < 0.2):
        a = 0.2
    # shortAns = countEyler(a,b,h,e)[:3] # взял первые 4 значения
    f1=0 # delta Fi
    f2=0 # delta^2 Fi
    f3=0 # delta^3 Fi
    x=a
    counter =0
    prevY = math.exp(1)
    prevFXY = countY(a,prevY)

    tempAnswer = [counter,x,prevY,prevFXY,exactCountY(a),(prevY**h - prevY**(2*h))/15]
    answer = [tempAnswer]
    while(x<b):
        x+=h
        counter+=1

        if(counter==1): # уже знаем предыдущую
            y = prevY + h*prevFXY
        elif(counter==2): # уже знаем 2
            f1 = answer[1][3] - answer[0][3]
            y = prevY + h*prevFXY + h*h*f1/2
        elif(counter==3): # уже знаем 3
            f1 = answer[2][3] - answer[1][3]
            f2 = answer[2][3] - 2*answer[1][3] + answer[0][3]
            y = prevY + h * prevFXY + h * h * f1 / 2 + 5*h*h*h*f2/12
        else: # нормальная работа с 4 известными точками
            f1 = answer[counter-1][3] - answer[counter-2][3]
            f2 = answer[counter-1][3] - 2 * answer[counter-2][3] + answer[counter-3][3]
            f3 = answer[counter-1][3] - 3 * answer[counter-2][3] + 3 * answer[counter-3][3] - answer[counter-4][3]
            y = prevY + h * prevFXY + h * h * f1 / 2 + 5 * h * h * h * f2 / 12 + 3 * h * h * h * h * f3/8
        prevFXY = countY(x, y)
        prevY = y
        tempAnswer = [counter, x, y, prevFXY, exactCountY(x),(prevY**h - prevY**(2*h))/15]
        answer.append(tempAnswer)
    return answer


