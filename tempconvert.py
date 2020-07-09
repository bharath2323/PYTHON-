from tkinter import *
from mainpro import *
def trial():
    class converter:
        def Temperature_conversion(self):
            temp=int((var.get()  -32)* 5/9)
            convert = str(temp) + "° Celsius"
            label2.config(text=convert)
        def Temperature_conversion1(self):
            temp=int((var.get()+32)* 9/5)
            convert = str(temp) + " Fahrenheit"
            label2.config(text=convert)
           
    tmobj=converter()
    root1 =Tk()
    root1.title("Temperature Converter")
    root1.resizable(0,0)
    def navigateback():
        root1.destroy()
        world()
    var = DoubleVar()

    label1 = Label(root1, text="Temperature Converter",padx=16,pady=16,bd=16,fg="white",font=('arial',30,'bold'),bg="red",relief='raise',width=20,height=3)
    label1.pack()

    slider = Scale(root1, variable=var,   from_ =-40, to =300,length=500,tickinterval=20,orient=HORIZONTAL)
    slider.pack(anchor =CENTER)
    label2 = Label(root1,padx=16,pady=16,bd=16,fg="white",font=('arial',30,'bold'),bg="red",relief='sunk',width=20,height=3)
    label2.pack()

    label3 = Label(root1, text=" ")
    label3.pack()

    button1=Button(root1,text="Convert to Fahrenheit",padx=16,pady=16,bd=16,width=20,font=('arial',20,'bold'),command= tmobj.Temperature_conversion1,fg="white",bg="black")
    button1.pack(side =RIGHT)
    button=Button(root1, text="Convert to Celsius",padx=16,pady=16,bd=16,width=20,font=('arial',20,'bold'),command= tmobj.Temperature_conversion,fg="white",bg="black")
    button.pack(side =LEFT)
    tempback=Button(root1,text="⮪",bg="red",fg="white",font=('arial',20,'bold'),width=2,command=navigateback)
    tempback.place(x=3,y=3)
    root1.mainloop()

