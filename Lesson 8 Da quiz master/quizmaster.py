import pgzrun
import time

WIDTH=870
HEIGHT=650
TITLE="Dá Quiz Master!"
timeleft=10
questions='Question.txt'
is_game_over=False
score=0
questionindex=0
questionlist=[]
questioncount=0
messageboxdontlookweird=Rect(0,0,880,80)
messageboxdontlookweird.move_ip(0,0)
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
    screen.draw.filled_rect(messageboxdontlookweird,'yellow')
    screen.draw.filled_rect(questionbox,'red')
    screen.draw.filled_rect(timerbox,'orange')
    screen.draw.filled_rect(skipbox,'blue')
    for box in answerboxlist:
        screen.draw.filled_rect(box,'green')
    screen.draw.textbox("Skip",skipbox,color='orange',shadow=(0.5,0.5),scolor='dimgrey',angle=-90)
    screen.draw.textbox("Quizmaster's Quiz!",messagebox,color='red',shadow=(0.5,0.5),scolor='dimgrey')
    screen.draw.textbox(str(timeleft),timerbox,color='blue',shadow=(0.5,0.5),scolor='dimgrey')
    screen.draw.textbox(qu[0].strip(),questionbox,color='green',shadow=(0.5,0.5),scolor='dimgrey')
    index=1
    for i in answerboxlist:
        screen.draw.textbox(qu[index].strip(),i,color='red',shadow=(0.5,0.5),scolor='dimgrey')
        index=index+1
    
        

def update():
    move_box_or_else()
def move_box_or_else():
    messagebox.x=messagebox.x+1.5
    if messagebox.left>870:
        messagebox.right=70
    


def readquestions():
    global questioncount
    global questionlist
    q_file=open(questions,'r')
    for i in q_file:
        questionlist.append(i)
        questioncount=questioncount+1
    q_file.close()

def readnextquestion():
    global questionindex
    questionindex=questionindex+1
    return questionlist.pop(0).split(',')

def game_over():
    message=f'Game over.\n You were cooking, but now your cooked!\n You got {score} questions correct'
    qu=[message,'-','-','-','-',45]
    is_game_over=True
    timeleft=0


def correct_answer():
    global score
    score=score+1
    if questionlist:
        qu=readnextquestion()
        timeleft=10
    else:
        game_over()




def skipquestion():
    global timeleft
    global questionlist
    if questionlist and not is_game_over:
        qu=readnextquestion()
        timeleft=10
    else:
        game_over()
        

def updatetimeleft():
    global timeleft
    if timeleft:
        timeleft=timeleft-1
    else:
        game_over()

def on_mouse_down(pos):
    index=1
    for box in answerboxlist:
        if box.collidepoint(pos):
            if index is int(qu[5]):
                correct_answer()
            else:
                game_over()
        index=index+1
    if skipbox.collidepoint(pos):
        skipquestion()
            
readquestions()
qu=readnextquestion()
clock.schedule_interval(updatetimeleft,1)
pgzrun.go()