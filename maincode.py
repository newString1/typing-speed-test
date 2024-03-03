from tkinter import *
from turtle import width
# from PIL import ImageTk,Image
import time

#root window is for selecting difficulty level
root=Tk()
root.title('Typing Speed Test')
root.iconbitmap("D:\code\PROJECTS\my projects\Python Project\icon.ico")
root.geometry('400x400')

#easy function
def easy():
    #opening file that consists 100 most used english words
    with open(r"D:\code\PROJECTS\my projects\Python Project\100_Most_used_words.txt",'r') as f:
        temp=f.read()
        words=temp.split()
    #converting into set and back into list to get random order list    
    words=list(set(words))
    #creating another window for typing test
    top=Toplevel()
    frame2 = LabelFrame(top,text="Start Typing",padx=10,pady=10)
    
    n=0
    txt1=' '.join(words[:40])
    txt=' '.join(words[:8])+'\n'+' '.join(words[8:16])+'\n'+' '.join(words[16:24])+'\n'+' '.join(words[24:32])+'\n'+' '.join(words[32:40])
    #perf_counter() is for knowing exact time in seconds when the test has started and ended
    StartTime=time.perf_counter()
    wordsdisp=Label(frame2,text=txt,font=('comicsans',17)).pack()
    e=Entry(frame2,width=50,font=17)
    e.pack()
    def done(words):
        #checking time in seconds after the end button is pressed
        EndTime=time.perf_counter()
        t3='Your typing speed is: %.2f WPM' %((len(e.get().split())*60)/(EndTime-StartTime))
        speed1=Label(frame2,text=t3,bg='green').pack()
        
        writtentxt=e.get().split()
        #splitting the written words to know how many words are written
        writtenlength=len(e.get().split())
        correct=0
        #for loop is to get accuracy of typing
        for i in range(writtenlength):
            if writtentxt[i]==words[i]:
                correct+=1 
        t4='Your typing accuracy is: %.2f ' %((correct*100)/len(e.get().split()))
        accuracy1=Label(frame2,text=t4).pack()       
    button_end=Button(frame2,text='End',font=17,command=lambda:done(words))
    button_end.pack()    
    frame2.pack(padx=10,pady=10)

#hard function
def hard():
    #opening file that consists 500 most used english words and symbols 
    with open(r"D:\code\PROJECTS\my projects\Python Project\500_Most_used_words.txt",'r') as f:
        temp=f.read()
        words=temp.split()
    #converting into set and back into list to get random order list    
    words=list(set(words))
    #creating another window for typing test
    top=Toplevel()
    frame2 = LabelFrame(top,text="Start Typing",padx=10,pady=10)
    
    n=0
    txt1=' '.join(words[:40])
    txt=' '.join(words[:8])+'\n'+' '.join(words[8:16])+'\n'+' '.join(words[16:24])+'\n'+' '.join(words[24:32])+'\n'+' '.join(words[32:40])
    #perf_counter() is for knowing exact time in seconds when the test has started and ended
    StartTime=time.perf_counter()
    wordsdisp=Label(frame2,text=txt,font=('comicsans',17)).pack()
    e=Entry(frame2,width=50,font=17)
    e.pack()
    def done(words):
        #checking time in seconds after the end button is pressed
        EndTime=time.perf_counter()
        sp=(len(e.get().split())*60)/(EndTime-StartTime)
        t3='Your typing speed is: %.2f WPM' %(sp)
        speed1=Label(frame2,text=t3,bg='green').pack()
        
        writtentxt=e.get().split()
        #splitting the written words to know how many words are written
        writtenlength=len(e.get().split())
        correct=0
        #for loop is to get accuracy of typing
        for i in range(writtenlength):
            if writtentxt[i]==words[i]:
                correct+=1 
        accu=((correct*100)/len(e.get().split()))
        t4='Your typing accuracy is: %.2f ' %(accu)
        accuracy1=Label(frame2,text=t4).pack()  
    button_end=Button(frame2,text='End',font=17,command=lambda:done(words))
    button_end.pack()    
    frame2.pack(padx=10,pady=10)


frame = LabelFrame(root,text="Level",padx=5,pady=5)
select_label=Label(frame,text="Select Level",font=('comicsans',20))
easy_button=Button(frame,text='Easy',height=5,width=20,command=easy,fg='green',font=20)
hard_button=Button(frame,text='Hard',height=5,width=20,command=hard,fg='red',font=20)

mainLabel=Label() 
frame.pack(padx=5,pady=5)
select_label.pack()
easy_button.pack()
hard_button.pack()


root.mainloop()  