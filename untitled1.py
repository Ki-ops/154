from tkinter import *
import random
root=Tk()
root.title("3d Arrays")
root.geometry("500x500")
lbl=Label(root)
array_3d=[[["1","2","3","4","5","6"],["heads","tails"],["A","B","C","D","E","F","G","H","I","J"]]]

print(array_3d[0][0][3])

def new_word():
    r1=random.randint(0,5)
    r2=random.randint(0,1)
    r3=random.randint(0, 9)
    
    letter1=str(array_3d[0][0][r1])
    letter2=str(array_3d[0][1][r2])
    letter3=str(array_3d[0][2][r3])
    
    lbl["text"]=letter1+" "+letter2+" "+letter3+" "

btn=Button(root,text="Get letter",command=new_word)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)

lbl.place(relx=0.5,rely=0.6,anchor=CENTER)
    
root.mainloop()



