import pgzrun

WIDTH=870
HEIGHT=650
TITLE="Dá Quiz Master!"

messagebox=Rect(0,0,880,80)
messagebox.move_ip(0,0)
questionbox=Rect(0,0,650,150)
questionbox.move_ip(20,100)
timerbox=Rect(0,0,150,150)
timerbox.move_ip(695,100)
skipbox=Rect(0,0,150,350)
skipbox.move_ip(695,280)
answerbox1=Rect(0,0,310,160)
answerbox1.move_ip(20,280)
answerbox2=Rect(0,0,320,160)
answerbox2.move_ip(350,280)
answerbox3=Rect(0,0,310,150)
answerbox3.move_ip(20,480)
answerbox4=Rect(0,0,320,150)
answerbox4.move_ip(350,480)

answerboxlist=[
    answerbox1,
    answerbox2,
    answerbox3,
    answerbox4
]


def draw():
    screen.clear()
    screen.fill('white')
    screen.draw.filled_rect(messagebox,'yellow')
    screen.draw.filled_rect(questionbox,'red')
    screen.draw.filled_rect(timerbox,'orange')
    screen.draw.filled_rect(skipbox,'blue')
    for box in answerboxlist:
        screen.draw.filled_rect(box,'green')
    screen.draw.textbox("Skip",skipbox,color='orange',shadow=(0.5,0.5),scolor='dimgrey',angle=-90)
    screen.draw.textbox("Quizmaster's Quiz!",messagebox,color='red',shadow=(0.5,0.5),scolor='dimgrey')
def update():
    pass


pgzrun.go()