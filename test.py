from tkinter import ttk,StringVar,Tk
from tkinter import *
from tkinter import messagebox
import mainpro
def convertunit():
    def navigateb():
        w.destroy()
        mainpro.world()
    w=Tk()
    w.title("unit converter")
    w.geometry("1000x300+0+0")
    w.configure(background="#424949")
    labelh=Label()
    leftmainframe=Frame(w,width=761,height=101,bd=8,relief="raise",bg="#424949")
    leftmainframe.place(x=100,y=100)
    rightmainframe=Frame(w,width=761,height=75,bd=8,relief="raise",bg="#424949")
    rightmainframe.place(x=100,y=210)
    tempback=Button(w,text="⮪",bg="black",fg="white",font=('arial',20,'bold'),width=2,command=navigateb)
    tempback.place(x=3,y=3)
    #-------------------------------------variable declaration------------------------------------------------
     
    value0=StringVar()
    value1=StringVar()
    convert=DoubleVar()
    ans=DoubleVar()
    lh=Label(text="CONVERSION CALCULATOR",bg="#424949",fg="white",font=('arial', 30, 'bold'))
    lh.place(x=210,y=30)
    #--------------------------------------conversion functionality------------------------------------------

    def method():

    #---------------------------------------------Km----------------------------------------------------
        if value0.get() == "Km":
            if value1.get() == "Km":
                convert1 = float(convert.get() * 1)
                ans.set(convert1)
            if value1.get() == "m":
                convert1 = float(convert.get() * 1000)
                ans.set(convert1)
            if value1.get() == "cm":
                convert1 = float(convert.get() * 100000)
                ans.set(convert1)
            if value1.get() == "mm":
                convert1 = float(convert.get() * 1000000)
                ans.set(convert1)
            if value1.get() == "micrometer":
                convert1 = float(convert.get() * 1000000000)
                ans.set(convert1)
            if value1.get() == "nanometer":
                convert1 = float(convert.get() * 1000000000000)
                ans.set(convert1)
            if value1.get() == "mile":
                convert1 = float(convert.get() * 0.621371)
                ans.set(convert1)
            if value1.get() == "yard":
                convert1 = float(convert.get() * 1093.61)
                ans.set(convert1)
            if value1.get() == "foot":
                convert1 = float(convert.get() * 3280.84)
                ans.set(convert1)
            if value1.get() == "inch":
                convert1 = float(convert.get() * 39370.1)
                ans.set(convert1)
            if value1.get() == "decimeter":
                convert1 = float(convert.get() * 10000)
                ans.set(convert1)
            if value1.get() == "decameter":
                convert1 = float(convert.get() * 100)
                ans.set(convert1)
    #------------------------------------------------------meter----------------------------------------------
        if value0.get() == "m":
            if value1.get() == "Km":
                convert1 = float(convert.get() * 0.001)
                ans.set(convert1)
            if value1.get() == "m":
                convert1 = float(convert.get() * 1)
                ans.set(convert1)
            if value1.get() == "cm":
                convert1 = float(convert.get() * 100)
                ans.set(convert1)
            if value1.get() == "mm":
                convert1 = float(convert.get() * 1000)
                ans.set(convert1)
            if value1.get() == "micrometer":
                convert1 = float(convert.get() * 1000000)
                ans.set(convert1)
            if value1.get() == "nanometer":
                convert1 = float(convert.get() * 1000000000)
                ans.set(convert1)
            if value1.get() == "mile":
                convert1 = float(convert.get() * 0.000621371)
                ans.set(convert1)
            if value1.get() == "yard":
                convert1 = float(convert.get() * 1.09361)
                ans.set(convert1)
            if value1.get() == "foot":
                convert1 = float(convert.get() * 3.28084)
                ans.set(convert1)
            if value1.get() == "inch":
                convert1 = float(convert.get() * 39.3701)
                ans.set(convert1)
            if value1.get() == "decimeter":
                convert1 = float(convert.get() * 10)
                ans.set(convert1)
            if value1.get() == "decameter":
                convert1 = float(convert.get() * 0.1)
                ans.set(convert1)
    #------------------------------------------------cm-------------------------------------------------------
        if value0.get() == "cm":
            if value1.get() == "Km":
                convert1 = float(convert.get() *0.001)
                ans.set(convert1)
            if value1.get() == "m":
                convert1 = float(convert.get() * 0.01)
                ans.set(convert1)
            if value1.get() == "cm":
                convert1 = float(convert.get() * 1)
                ans.set(convert1)
            if value1.get() == "mm":
                convert1 = float(convert.get() * 10)
                ans.set(convert1)
            if value1.get() == "micrometer":
                convert1 = float(convert.get() * 10000)
                ans.set(convert1)
            if value1.get() == "nanometer":
                convert1 = float(convert.get() * 10000000)
                ans.set(convert1)
            if value1.get() == "mile":
                convert1 = float(convert.get() / 160934.4)
                ans.set(convert1)
            if value1.get() == "yard":
                convert1 = float(convert.get() / 91.44)
                ans.set(convert1)
            if value1.get() == "foot":
                convert1 = float(convert.get() / 30.48)
                ans.set(convert1)
            if value1.get() == "inch":
                convert1 = float(convert.get() / 2.54)
                ans.set(convert1)
            if value1.get() == "decimeter":
                convert1 = float(convert.get() / 10)
                ans.set(convert1)
            if value1.get() == "decameter":
                convert1 = float(convert.get() * 0.001)
                ans.set(convert1)
    #-------------------------------------------------millimeter-----------------------------------------------
        if value0.get() == "mm":
            if value1.get() == "Km":
                convert1 = float(convert.get() / 1000000)
                ans.set(convert1)
            if value1.get() == "m":
                convert1 = float(convert.get() * 0.001)
                ans.set(convert1)
            if value1.get() == "cm":
                convert1 = float(convert.get() * 0.1)
                ans.set(convert1)
            if value1.get() == "mm":
                convert1 = float(convert.get() * 1)
                ans.set(convert1)
            if value1.get() == "micrometer":
                convert1 = float(convert.get() * 1000)
                ans.set(convert1)
            if value1.get() == "nanometer":
                convert1 = float(convert.get() /1000000)
                ans.set(convert1)
            if value1.get() == "mile":
                convert1 = float(convert.get() / 1609000)
                ans.set(convert1)
            if value1.get() == "yard":
                convert1 = float(convert.get() / 914.4)
                ans.set(convert1)
            if value1.get() == "foot":
                convert1 = float(convert.get() / 304.8)
                ans.set(convert1)
            if value1.get() == "inch":
                convert1 = float(convert.get() / 25.4)
                ans.set(convert1)
            if value1.get() == "decimeter":
                convert1 = float(convert.get() / 100)
                ans.set(convert1)
            if value1.get() == "decameter":
                convert1 = float(convert.get() /10000)
                ans.set(convert1)
    #----------------------------------------------micrometer---------------------------------------------
        if value0.get() == "micrometer":
            if value1.get() == "Km":
                convert1 = float(convert.get() / 1000000000)
                ans.set(convert1)
            if value1.get() == "m":
                convert1 = float(convert.get() / 1000000)
                ans.set(convert1)
            if value1.get() == "cm":
                convert1 = float(convert.get() /10000)
                ans.set(convert1)
            if value1.get() == "mm":
                convert1 = float(convert.get() / 1000)
                ans.set(convert1)
            if value1.get() == "micrometer":
                convert1 = float(convert.get() * 1)
                ans.set(convert1)
            if value1.get() == "nanometer":
                convert1 = float(convert.get() * 1000)
                ans.set(convert1)
            if value1.get() == "mile":
                convert1 = float(convert.get() / 1609000000)
                ans.set(convert1)
            if value1.get() == "yard":
                convert1 = float(convert.get() / 914400)
                ans.set(convert1)
            if value1.get() == "foot":
                convert1 = float(convert.get() / 304800)
                ans.set(convert1)
            if value1.get() == "inch":
                convert1 = float(convert.get() / 25400)
                ans.set(convert1)
            if value1.get() == "decimeter":
                convert1 = float(convert.get() / 100000)
                ans.set(convert1)
            if value1.get() == "decameter":
                convert1 = float(convert.get() /10000000)
                ans.set(convert1)
    #---------------------------------------------nanometer------------------------------------------------------
        if value0.get() == "nanometer":
            if value1.get() == "Km":
                convert1 = float(convert.get() / 1000000000000)
                ans.set(convert1)
            if value1.get() == "m":
                convert1 = float(convert.get() / 1000000000)
                ans.set(convert1)
            if value1.get() == "cm":
                convert1 = float(convert.get() /10000000)
                ans.set(convert1)
            if value1.get() == "mm":
                convert1 = float(convert.get() / 1000000)
                ans.set(convert1)
            if value1.get() == "micrometer":
                convert1 = float(convert.get() / 1000)
                ans.set(convert1)
            if value1.get() == "nanometer":
                convert1 = float(convert.get() * 1)
                ans.set(convert1)
            if value1.get() == "mile":
                convert1 = float(convert.get() / 1609000000000000)
                ans.set(convert1)
            if value1.get() == "yard":
                convert1 = float(convert.get() / 914400000)
                ans.set(convert1)
            if value1.get() == "foot":
                convert1 = float(convert.get() / 304800000)
                ans.set(convert1)
            if value1.get() == "inch":
                convert1 = float(convert.get() / 25400000)
                ans.set(convert1)
            if value1.get() == "decimeter":
                convert1 = float(convert.get() / 100000000)
                ans.set(convert1)
            if value1.get() == "decameter":
                convert1 = float(convert.get() /10000000000)
                ans.set(convert1)
    #---------------------------------------------------mile-------------------------------------------------
        if value0.get() == "mile":
            if value1.get() == "Km":
                convert1 = float(convert.get() *1.60934)
                ans.set(convert1)
            if value1.get() == "m":
                convert1 = float(convert.get() *1609.34)
                ans.set(convert1)
            if value1.get() == "cm":
                convert1 = float(convert.get() *160934.4)
                ans.set(convert1)
            if value1.get() == "mm":
                convert1 = float(convert.get() *1609000)
                ans.set(convert1)
            if value1.get() == "micrometer":
                convert1 = float(convert.get() *1609000000)
                ans.set(convert1)
            if value1.get() == "nanometer":
                convert1 = float(convert.get() * 1609000000000)
                ans.set(convert1)
            if value1.get() == "mile":
                convert1 = float(convert.get() * 1)
                ans.set(convert1)
            if value1.get() == "yard":
                convert1 = float(convert.get() * 1760)
                ans.set(convert1)
            if value1.get() == "foot":
                convert1 = float(convert.get() * 5280)
                ans.set(convert1)
            if value1.get() == "inch":
                convert1 = float(convert.get() * 63360)
                ans.set(convert1)
            if value1.get() == "decimeter":
                convert1 = float(convert.get() *16093.44)
                ans.set(convert1)
            if value1.get() == "decameter":
                convert1 = float(convert.get() *160.934)
                ans.set(convert1)
    #---------------------------------------------------------yard------------------------------------------------
        if value0.get() == "yard":
            if value1.get() == "Km":
                convert1 = float(convert.get() /1093.613)
                ans.set(convert1)
            if value1.get() == "m":
                convert1 = float(convert.get() /1.094)
                ans.set(convert1)
            if value1.get() == "cm":
                convert1 = float(convert.get() *91.44)
                ans.set(convert1)
            if value1.get() == "mm":
                convert1 = float(convert.get() *914.4)
                ans.set(convert1)
            if value1.get() == "micrometer":
                convert1 = float(convert.get() *914400)
                ans.set(convert1)
            if value1.get() == "nanometer":
                convert1 = float(convert.get() * 914400000)
                ans.set(convert1)
            if value1.get() == "mile":
                convert1 = float(convert.get() /1760)
                ans.set(convert1)
            if value1.get() == "yard":
                convert1 = float(convert.get() * 1)
                ans.set(convert1)
            if value1.get() == "foot":
                convert1 = float(convert.get() * 3)
                ans.set(convert1)
            if value1.get() == "inch":
                convert1 = float(convert.get() * 36)
                ans.set(convert1)
            if value1.get() == "decimeter":
                convert1 = float(convert.get() *9.144)
                ans.set(convert1)
            if value1.get() == "decameter":
                convert1 = float(convert.get() / 10.936)
                ans.set(convert1)
    #---------------------------------------------foot--------------------------------------------
        if value0.get() == "foot":
            if value1.get() == "Km":
                convert1 = float(convert.get() /3280.84)
                ans.set(convert1)
            if value1.get() == "m":
                convert1 = float(convert.get() /3.281)
                ans.set(convert1)
            if value1.get() == "cm":
                convert1 = float(convert.get() *30.48)
                ans.set(convert1)
            if value1.get() == "mm":
                convert1 = float(convert.get() *304.8)
                ans.set(convert1)
            if value1.get() == "micrometer":
                convert1 = float(convert.get() *304800)
                ans.set(convert1)
            if value1.get() == "nanometer":
                convert1 = float(convert.get() * 304800000)
                ans.set(convert1)
            if value1.get() == "mile":
                convert1 = float(convert.get() /5280)
                ans.set(convert1)
            if value1.get() == "yard":
                convert1 = float(convert.get() /3)
                ans.set(convert1)
            if value1.get() == "foot":
                convert1 = float(convert.get() * 1)
                ans.set(convert1)
            if value1.get() == "inch":
                convert1 = float(convert.get() * 12)
                ans.set(convert1)
            if value1.get() == "decimeter":
                convert1 = float(convert.get() *3.048)
                ans.set(convert1)
            if value1.get() == "decameter":
                convert1 = float(convert.get() / 32.808)
                ans.set(convert1)
    #----------------------------------------------inch----------------------------------------------
        if value0.get() == "inch":
            if value1.get() == "Km":
                convert1 = float(convert.get() /39370.079)
                ans.set(convert1)
            if value1.get() == "m":
                convert1 = float(convert.get() /39.37)
                ans.set(convert1)
            if value1.get() == "cm":
                convert1 = float(convert.get() *2.54)
                ans.set(convert1)
            if value1.get() == "mm":
                convert1 = float(convert.get() *25.4)
                ans.set(convert1)
            if value1.get() == "micrometer":
                convert1 = float(convert.get() *25400)
                ans.set(convert1)
            if value1.get() == "nanometer":
                convert1 = float(convert.get() * 25400000)
                ans.set(convert1)
            if value1.get() == "mile":
                convert1 = float(convert.get() /63360)
                ans.set(convert1)
            if value1.get() == "yard":
                convert1 = float(convert.get() /36)
                ans.set(convert1)
            if value1.get() == "foot":
                convert1 = float(convert.get() * 12)
                ans.set(convert1)
            if value1.get() == "inch":
                convert1 = float(convert.get() * 1)
                ans.set(convert1)
            if value1.get() == "decimeter":
                convert1 = float(convert.get() *0.254)
                ans.set(convert1)
            if value1.get() == "decameter":
                convert1 = float(convert.get() / 393.701)
                ans.set(convert1)
    #---------------------------------------------------decimeter-------------------------------------------------------------
        if value0.get() == "decimeter":
            if value1.get() == "Km":
                convert1 = float(convert.get() /1000)
                ans.set(convert1)
            if value1.get() == "m":
                convert1 = float(convert.get()/10 )
                ans.set(convert1)
            if value1.get() == "cm":
                convert1 = float(convert.get()*10 )
                ans.set(convert1)
            if value1.get() == "mm":
                convert1 = float(convert.get()*100 )
                ans.set(convert1)
            if value1.get() == "micrometer":
                convert1 = float(convert.get() *100000 )
                ans.set(convert1)
            if value1.get() == "nanometer":
                convert1 = float(convert.get() *100000000)
                ans.set(convert1)
            if value1.get() == "mile":
                convert1 = float(convert.get() /16093.44)
                ans.set(convert1)
            if value1.get() == "yard":
                convert1 = float(convert.get() /9.144)
                ans.set(convert1)
            if value1.get() == "foot":
                convert1 = float(convert.get() /3.048)
                ans.set(convert1)
            if value1.get() == "inch":
                convert1 = float(convert.get() *3.937)
                ans.set(convert1)
            if value1.get() == "decimeter":
                convert1 = float(convert.get() *1)
                ans.set(convert1)
            if value1.get() == "decameter":
                convert1 = float(convert.get() * 0.01)
                ans.set(convert1)
    #----------------------------------------------------decameter----------------------------------------------
        if value0.get() == "decameter":
            if value1.get() == "Km":
                convert1 = float(convert.get() /100)
                ans.set(convert1)
            if value1.get() == "m":
                convert1 = float(convert.get() *10)
                ans.set(convert1)
            if value1.get() == "cm":
                convert1 = float(convert.get()*1000 )
                ans.set(convert1)
            if value1.get() == "mm":
                convert1 = float(convert.get()*10000 )
                ans.set(convert1)
            if value1.get() == "micrometer":
                convert1 = float(convert.get() *10000000 )
                ans.set(convert1)
            if value1.get() == "nanometer":
                convert1 = float(convert.get() *10000000000)
                ans.set(convert1)
            if value1.get() == "mile":
                convert1 = float(convert.get() /160.9344)
                ans.set(convert1)
            if value1.get() == "yard":
                convert1 = float(convert.get() *10.936)
                ans.set(convert1)
            if value1.get() == "foot":
                convert1 = float(convert.get() *32.808)
                ans.set(convert1)
            if value1.get() == "inch":
                convert1 = float(convert.get() *393.701)
                ans.set(convert1)
            if value1.get() == "decimeter":
                convert1 = float(convert.get() *100)
                ans.set(convert1)
            if value1.get() == "decameter":
                convert1 = float(convert.get() * 0.01)
                ans.set(convert1)

        
            
    #-----------------------------------exit functionality------------------------------------------------
    def uexit():
        fexit=messagebox.askyesno("exit system","do you want to quit?")
        if fexit > 0:
            w.destroy()
            return
    #------------------------------------Reset functionality---------------------------------------------
    def reset():
        value0.set("")
        value1.set("")
        convert.set("0.0")
        ans.set("0.0")
    #------------------------------------End Of Functionalitites----------------------------------------

    entvalue=Entry(leftmainframe,font=('arial',19,'bold'),textvariable=convert,bd=2,width=29,justify='center')
    entvalue.place(x=-2,y=-2)

    box1=ttk.Combobox(leftmainframe,textvariable=value0,state='readonly',font=('arial',20,'bold'),width=20)
    box1['values']=('   ','Km','m','cm','mm','micrometer','nanometer','mile','yard','foot','inch','decimeter','decameter')
    box1.current(0)
    box1.place(x=420,y=-2)

    Output=Label(leftmainframe,font=('arial',20,'bold'),textvariable=ans,bd=2,width=24,relief='sunken',bg="white")
    Output.place(x=-2,y=43)


    box2=ttk.Combobox(leftmainframe,textvariable=value1,state='readonly',font=('arial',20,'bold'),width=20)
    box2['values']=('   ','Km','m','cm','mm','micrometer','nanometer','mile','yard','foot','inch','decimeter','decameter')
    box2.current(0)
    box2.place(x=420,y=43)
    bconvert=Button(rightmainframe,text='CONVERT',padx=2,pady=2,bd=2,fg='black',font=('arial',20,'bold'),width=16,height=1,command=method,bg="#c0c0c0")
    bconvert.place(x=2,y=0)
    breset=Button(rightmainframe,text='RESET',padx=2,pady=2,bd=2,fg='black',font=('arial',20,'bold'),width=14,height=1,command=reset,bg="#c0c0c0")
    breset.place(x=244,y=0)
    bexit=Button(rightmainframe,text='EXIT',padx=2,pady=2,bd=2,fg='black',font=('arial',20,'bold'),width=14,height=1,command=uexit,bg="#c0c0c0")
    bexit.place(x=493,y=0)
    w.mainloop()

