import tkinter
from tkinter import messagebox as m
t=tkinter.Tk()
t.config(bg="black")
t.geometry("1000x1000")
t.title("PYTHON")
def check_user_id(num):
	try:
		fpin=open(num+".txt",'r')
	except FileNotFoundError:
		messagebox.showinfo("Error","Invalid Credentials!\nTry Again!")
		return 0
	fpin.close()
	return 
def created():
    m.showinfo("file","File created successfully")
class bio():   

    def biodata(self):
        new=tkinter.Tk()
        new.config(bg="pink")
        new.title("Newpage")
        new.geometry("1000x900")
        h=tkinter.Label(new,text='BMI Survey',bg='blue',fg='white',font=('Ariel',20))
        h.pack()
        expl=tkinter.Label(new,text='Get you health data to doctors quickly!',bg='blue',fg='white',font=('Ariel',10))
        expl.pack()
        q1=tkinter.Label(new,text='First and last name: ',bg='blue',fg='white',font=('Ariel',20)).place(x=0,y=100)
        e1=tkinter.Entry(new,fg='blue',bg='white',font=('Ariel',20))
        e1.place(x=285,y=100)#placement of entries
    
        q2=tkinter.Label(new,text='Enter your height (cm): ',bg='blue',fg='white',font=('Ariel',20)).place(x=0,y=150)
        e2=tkinter.Entry(new,fg='blue',bg='white',font=('Ariel',20))
        e2.place(x=285,y=150)
    
        q3=tkinter.Label(new,text='Enter your weight (kg): ',bg='blue',fg='white',font=('Ariel',20)).place(x=0,y=200)
        e3=tkinter.Entry(new,fg='blue',bg='white',font=('Ariel',20))
        e3.place(x=285,y=200)
    
        q4=tkinter.Label(new,text='Enter any health risks: ',bg='blue',fg='white',font=('Ariel',20)).place(x=0,y=250)
        e4=tkinter.Entry(new,fg='blue',bg='white',font=('Ariel',20))
        e4.place(x=285,y=250)
    
        q5=tkinter.Label(new,text='Enter your age(#only): ',bg='blue',fg='white',font=('Ariel',20)).place(x=0,y=300)
        e5=tkinter.Entry(new,fg='blue',bg='white',font=('Ariel',20))
        e5.place(x=285,y=300)
    
    
    
        sub = tkinter.Button(new, text="submit", bg='red', fg='white', font=('Arial', 40),
                     command=lambda: data.data(self, e1.get(), e2.get(), e3.get(), e4.get(), e5.get()))
        sub.place(x=0, y=500)

        new.mainloop()
b=bio()
class data(bio):
    def data(self, name, height, weight, hr, age):  # Pass the input values as arguments
        height_m=float(height)/100  # Convert height to meters
        weight_kg=float(weight)
        bmi=float(weight_kg/(height_m * height_m))#BMI equation
        file_path = f"F:/cleo/datas/{name}.txt"

        with open(file_path, 'w') as f:
            f.write(f"\n\nName: {name}\nHeight: {height}\nWeight: {weight}\nHealth Risks: {hr}\nAge: {age}")
            f.write(f"\nBMI is: {bmi}")  # Corrected way to insert BMI value
            if bmi<18.5:    #to find which group of bmi You are
                f.write(f"\nUNDERWEIGHT")
            elif bmi>=18.5 or bmi<=24.9:
                f.write(f"\nNORMAL WEIGHT")
            elif bmi>=25 or bmi<=29.9:
                f.write(f"\nOVERWEIGHT")
            elif bmi>30:
                f.write(f"\nOBESE")
            else:
                pass
            created()
def des():
    t.destroy()
def check_log_in(num,pin):
	
	if( (is_number(name))  or (is_number(pin)==0) ):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		
	else:
		
		b.biodata()
def loginto():
    #t.withdraw()
    des()
    login=tkinter.Tk()
    login.config(bg="black")
    login.geometry("1000x1000")
    login.title("Loogin page")
    u=tkinter.Label(login,text='IGN INTO HOSPITAL Database',bg='blue',fg='white',font=('Ariel',30))
    u.pack()
    u=tkinter.Label(login,text='                             ',bg='black',fg='white',font=('Ariel',20))
    u.pack()
    u=tkinter.Label(login,text='Please type your username: ',bg='blue',fg='white',font=('Ariel',20)).place(x=0,y=89)
    e=tkinter.Entry(login,fg='blue',bg='white',font=('Ariel',20))
    e.pack()
    u=tkinter.Label(login,text='Please type your password: ',bg='blue',fg='white',font=('Ariel',20)).place(x=0,y=122)
    p=tkinter.Entry(login,fg='black',bg='white',font=('Ariel',20),show='*')
    p.pack()
    sub = tkinter.Button(login, text="submit", bg='red', fg='white', font=('Arial', 40),
                     command=lambda: check_log_in(e,p)).place(x=0, y=170)
    login.mainloop()
def create_account_window():
    des()
    crwn = tkinter.Tk()
    crwn.geometry("600x300")
    crwn.title("Create Account")
    crwn.configure(bg="SteelBlue1")
    
    l1 = tkinter.Label(crwn, text="Enter Name:", font=("Times", 16), relief="raised")
    l1.pack()
    
    e1 = tkinter.Entry(crwn)
    e1.pack()
    
    l3 = tkinter.Label(crwn, text="Enter desired PIN:", font=("Times", 16), relief="raised")
    l3.pack()
    e3 = tkinter.Entry(crwn, show="*")
    e3.pack()

    b = tkinter.Button(crwn, text="Submit", font=("Times", 16),
                   command=lambda: write( e1.get().strip(), e3.get().strip()))
    b.pack()
    l2 = tkinter.Label(crwn, text="Reopen page to login", font=("Times", 16), relief="raised")
    l2.pack()
    crwn.bind("<Return>", lambda x: write(e1.get().strip(), e3.get().strip()))
    crwn.mainloop()
    
u=tkinter.Label(t,text='SIGN INTO HOSPITAL Database',bg='blue',fg='white',font=('Ariel',30))
u.pack()
u=tkinter.Label(t,text='                             ',bg='black',fg='white',font=('Ariel',20))
u.pack()
u=tkinter.Button(t,text='LOG IN',bg='blue',fg='white',font=('Ariel',20),command=loginto())
u.pack()
u=tkinter.Label(t,text='                             ',bg='black',fg='white',font=('Ariel',20))
u.pack()
a=tkinter.Button(t,text='CREATE NEW ACCOUNT',bg='blue',fg='white',font=('Ariel',20))
a.pack()
t.mainloop()
