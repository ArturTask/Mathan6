import matplotlib.pyplot as plt

def drawPls(answer,title):
    fig = plt.figure()
    axes = fig.add_subplot(111)
    plt.grid()

    x = []
    y = []
    for i in range(len(answer)):
        x.append(answer[i][1])
        y.append(answer[i][2])
    axes.plot(x,y,c="black",label="полученное решение")

    y = []
    for i in range(len(answer)):
        y.append(answer[i][4])
    axes.plot(x, y, c="red", label="точное решение")
    axes.legend()

    plt.title(title)
    plt.show()
