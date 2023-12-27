#gui
import tkinter
from tkinter import messagebox as m
t=tkinter.Tk()
t.config(bg="black")
t.geometry("1000x1000")
t.title("PYTHON")

    
class bio():   

    def biodata(self):
        new=tkinter.Tk()
        new.config(bg="pink")
        new.title("Newpage")
        new.geometry("1000x900")
        h=tkinter.Label(new,text='Health Data Survey',bg='blue',fg='white',font=('Ariel',20))
        h.pack()
        q1=tkinter.Label(new,text='First and last name: ',bg='blue',fg='white',font=('Ariel',20)).place(x=0,y=100)
        e1=tkinter.Entry(new,fg='blue',bg='white',font=('Ariel',20))
        e1.place(x=285,y=100)
    
        q2=tkinter.Label(new,text='Enter your height: ',bg='blue',fg='white',font=('Ariel',20)).place(x=0,y=150)
        e2=tkinter.Entry(new,fg='blue',bg='white',font=('Ariel',20))
        e2.place(x=285,y=150)
    
        q3=tkinter.Label(new,text='Enter your weight: ',bg='blue',fg='white',font=('Ariel',20)).place(x=0,y=200)
        e3=tkinter.Entry(new,fg='blue',bg='white',font=('Ariel',20))
        e3.place(x=285,y=200)
    
        q4=tkinter.Label(new,text='Enter any health risks: ',bg='blue',fg='white',font=('Ariel',20)).place(x=0,y=250)
        e4=tkinter.Entry(new,fg='blue',bg='white',font=('Ariel',20))
        e4.place(x=285,y=250)
    
        q5=tkinter.Label(new,text='Enter your symptoms: ',bg='blue',fg='white',font=('Ariel',20)).place(x=0,y=300)
        e5=tkinter.Entry(new,fg='blue',bg='white',font=('Ariel',20))
        e5.place(x=285,y=300)
    
    
        sub=tkinter.Button(new,text="submit",bg='red',fg='white',font=('Ariel',40),command=data.data)
        sub.place(x=0, y=500)
        new.mainloop()
class data(bio):
    def data(self):
        name=e1.get()
        height=e2.get()
        weight=e3.get()
        hr=e4.get()
        symp=e5.get()
        f=open("data.txt",'w')
        f.write([name,height,weight,hr,symp])
        f.close()


def des():
    t.destroy()
def validate():
    user=e.get()
    pwd=p.get()
    if user=="co" and pwd=="1":
       # print("Login Success")
       m.showinfo("login","Login success")
       des()
       bio()   
    else:
       # print("invalid")
       m.showwarning("Failed","Invalid Username or Password")
'''
l=tkinter.Label(t,text="Welcome",bg="pink",fg="blue",font=("Algerian",18))

B=tkinter.Button(t,text="DONT PRESS THIS",bg='red',fg='white',font=('Times New Roman',40))


lb=tkinter.Listbox(t,bg='red',)
lb.insert(1,'h')
lb.insert(2,'e')
lb.insert(3,'l')
lb.insert(4,'l')
lb.insert(5,'o')
e=tkinter.Entry(t,fg="blue",bg="green",font=("Algerian",18))
e.pack()
B.pack()

lb.pack()
l.pack()
'''
u=tkinter.Label(t,text='Please type your username:',bg='blue',fg='white',font=('Ariel',20)).place(x=0,y=0)

e=tkinter.Entry(t,fg='blue',bg='white',font=('Ariel',20))
e.pack()
u=tkinter.Label(t,text='Please type your password:',bg='blue',fg='white',font=('Ariel',20)).place(x=0,y=32)

p=tkinter.Entry(t,fg='black',bg='white',font=('Ariel',20),show='*')
p.pack()
sub=tkinter.Button(t,text="submit",bg='red',fg='white',font=('Ariel',40),command=validate).place(x=0, y=100)


t.mainloop()
#.place(x=340,y=2)
#.place(x=340,y=102)

