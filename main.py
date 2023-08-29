from tkinter import *

window=Tk()

window.title("BMI")
window.minsize(width=150,height=150)

def calc():
    a = my_entry1.get()
    b= my_entry2.get()

    if a == "" or b == "":
        my_text3= Label(text="Pls enter Number!!")
        my_text3.pack()
    else:
        try:
            bmi = int(a)/(float(b)*float(b))
            if bmi <= 18.4:
                my_text3= Label(text=f"Your Bmı is : {bmi:.2f} You are Underweight",font=40)
                my_text3.pack()
            elif bmi > 18.5 and  bmi < 24.9:
                my_text3= Label(text=f"Your Bmı is : {bmi:.2f} You are Normal",font=40)
                my_text3.pack()
            elif bmi >  25 and  bmi < 39.9:
                my_text3= Label(text=f"Your Bmı is : {bmi:.2f} You are Overweight",font=40)
                my_text3.pack()
            elif bmi >=40:
                my_text3= Label(text=f"Your Bmı is : {bmi:.2f} You are Obese",font=40)
                my_text3.pack()

        except:
            my_text3= Label(text="Pls enter Number!!")
            my_text3.pack()
            




my_text1= Label(text="Enter Your Weight (kg")
my_text1.pack()
my_entry1=Entry(width=10)
my_entry1.pack()
my_text2= Label(text="Enter Your Height (m)")
my_text2.pack()
my_entry2=Entry(width=10)
my_entry2.pack()

my_button = Button(text="calculater",command=calc)

my_button.pack()




window.mainloop()
