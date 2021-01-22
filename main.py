import tkinter
from tkinter import *

window=Tk()
window.geometry("700x600")
window.title("Personality Prediction")

window.config(background="#ffffff")
window.resizable(0,0)

questions=["If you see an interesting person or group, will you feel comfortable to approach them to start a conversation?",
           "At networking functions you are",
           "Do you",
           "When you see a wishing well do you throw a penny in and make a wish?",
           "If you were starting a new project, which of the following would be your first step?",
           "You are offered a job at a unproven startup company, how do you feel?",
           "If you get Rs.500 lying on road, then what would be your next step?",
           "What is more important to you in difficult conversation with a close friend?",
           "What is your natural reaction when a friend tells you about a problem?",
           "At what time you enter college for 8'o clock lecture?",
           "Do you like to work from a to-do list?",
           "Which of the following statements most accurately describes your work style?"]

answers_choice=[["yes","no"],
                ["Easy to approach","A little reserved"],
                ["speak easily and at length with strangers","Find little to say to stranger"],
                ["yes","no"],
                ["Begin by working on aspects", "Write down top goals for the project"],
                ["Excited, think of all the possibilities","No thanks, those things rarely succeed"],
                ["I got it, its mine","Its not right to keep others money and decide to donate it"],
                ["What the person says","How the person says it(tone, way of introducing the topic, body language"],
                ["I will help the person find a solution","I will listen very carefully so I can understand and connect with the person"],
                ["Before 8","After 8"],
                ["Yes","No"],
                ["I can't relax until completing everything I planned to do","I work best under pressure"],]
user_answer=[]
def startIsPressed():
    labeltext.destroy()
    btnStart.destroy()
    lblInstruction.destroy()
    startquiz()

def startquiz():
    background="#ffffff"
    global lblQuestion, r1,r2
    lblQuestion=Label(
        window,
        text=questions[0],
        font=("Consolas",16),
        width=500,
        justify="center",
        wraplength=400,
        background="#ffffff",
    )
    lblQuestion.pack(pady=(100,30))

    global radiovar
    radiovar=IntVar()
    radiovar.set(-1)

    r1=Radiobutton(
        window,
        text=answers_choice[0][0],
        font=("Times",14),
        value=0,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r1.pack(pady=5)

    r2=Radiobutton(
        window,
        text=answers_choice[0][1],
        font=("Times",14),
        value=1,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r2.pack(pady=5)
    


ques=1
def selected():
    global radiovar,user_answer,lblQuestion,r1,r2,ques
    x=radiovar.get()
    user_answer.append(x)
    #print(user_answer)
    radiovar.set(-1)
    if ques<12:
        lblQuestion.config(text=questions[ques])
        r1['text']=answers_choice[ques][0]
        r2['text']=answers_choice[ques][1]
        ques= ques+1
    else:
        calc()

countA=0
countB=0
def calc():
    global countA, countB
    global answer
    answer=""
    global user_answer
    for i in range(0,3):
        if(user_answer[i]==0):
            countA=countA+1
        else:
            countB=countB+1

    if(countA>countB):
        answer=answer+"E"#Extrovert
    else:
        answer=answer+"I"#Introvert

    countA=0
    countB=0
    for i in range(3,6):
        if(user_answer[i]==0):
            countA=countA+1
        else:
            countB=countB+1

    if(countA>countB):
        answer=answer+"N"#Intuition
    else:
        answer=answer+"S"#Sensing

    countA=0
    countB=0
    for i in range(6,9):
        if(user_answer[i]==0):
            countA=countA+1
        else:
            countB=countB+1

    if(countA>countB):
        answer=answer+"T"#Thinking
    else:
        answer=answer+"F"#Feeling

    countA=0
    countB=0
    for i in range(9,12):
        if(user_answer[i]==0):
            countA=countA+1
        else:
            countB=countB+1

    if(countA>countB):
        answer=answer+"J"#Judging
    else:
        answer=answer+"P"#Perceivers

    #print(answer)
    showresult(answer)

def showresult(answer):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    p_type=Label(
        window,
        background="#ffffff",
        text="Your personality type is "+answer,
        font=("Times",16)
    )
    p_type.pack(pady=100)
        
    a_label=Label(
        window,
        background="#ffffff",
        font=("Times",14)
    )

    if(answer=="INTJ"):
        a_label.configure(text="Imaginative and strategic thinkers, with a plan for everything.")
        
    elif(answer=="INTP"):
        a_label.configure(text="Innovative inventors with an unquenchable thirst for knowledge.")
        
    elif(answer=="ENTJ"):
        a_label.configure(text="Bold, imaginative and strong-willed leaders, always finding a way - or making one.")

    elif(answer=="ENTP"):
        a_label.configure(text="Smart and curious thinkers who cannot resist an intellectual challenge.")
        
    elif(answer=="INFJ"):
        a_label.configure(text="Quiet and mystical, yet very inspiring and tireless idealists.")

    elif(answer=="INFP"):
        a_label.configure(text="Poetic,kind and altruistic people, always eager to help a good cause.")
    
    elif(answer=="ENFJ"):
        a_label.configure(text="Charismatic and inspiring leaders, able to mesmerize their listeners.")
        
    elif(answer=="ENFP"):
        a_label.configure(text="Enthusiastic, creative and sociable free spirits, who can always find a reason to smile.")

    elif(answer=="ISTJ"):
        a_label.configure(text="Practical and fact-minded individuals, whose reliability cannot be doubted.")

    elif(answer=="ISFJ"):
        a_label.configure(text="Very dedicated and warm protectors, always ready to defend their loved ones.")

    elif(answer=="ESTJ"):
        a_label.configure(text="Excellent administrators, unsurpassed at managing things - or people.")

    elif(answer=="ESFJ"):
        a_label.configure(text="Extraordinarily caring, social and popular people, always eager to help.")
        
    elif(answer=="ISTP"):
        a_label.configure(text="Bold and practical experimenters, masters of all kinds of tools.")

    elif(answer=="ISFP"):
        a_label.configure(text="Flexible and charming artists, always ready to explore and experience something new.")

    elif(answer=="ESTP"):
        a_label.configure(text="Smart, energetic and very perceptive people, who truly enjoy living on the edge.")

    else:
        a_label.configure(text="Spontaneous, energetic and enthusiastic people - life is never boring around you.")

    a_label.pack(pady=10)
    
labeltext=Label(
    window,
    text="Personality Prediction",
    font=("Comic sans MS", "24", "bold"),
    background="#ffffff",
)
labeltext.pack(pady=(0,50))

btnStart=Button(
    window,
    text="START",
    command=startIsPressed
)
btnStart.pack()
lblInstruction=Label(
    window,
    text="Answer honestly, even if you dont like the answer",
    background="#ffffff",
    font=("Conselas",14),
    justify="center",
)
lblInstruction.pack(pady=(10,100))
window.mainloop()
