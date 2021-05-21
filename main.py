import inputData
import IntegralCounter
import drawAnswer

while True:
    try:
        data = inputData.inputGo() # a,b,h,e
        ans = IntegralCounter.countEyler(data[0],data[1],data[2],data[3])
        print("\nМетод Эйлера:")
        IntegralCounter.printAnswer(ans)
        drawAnswer.drawPls(ans,"Эйлер")
    except Exception:
        print("\nповторите ввод границ и шага для метода Эйлера\n")
        continue

    try:
        print("\n\nМетод Адамса")
        ans2 = IntegralCounter.countAdams(data[0],data[1],data[2],data[3])
        IntegralCounter.printAnswer(ans2)
        drawAnswer.drawPls(ans2,"Адамс")
    except Exception:
        print("\nповторите ввод границ и шага для метода Адамса\n")
        continue



