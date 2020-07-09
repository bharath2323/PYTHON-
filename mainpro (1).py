from tkinter import *
from math import *
from string import *
import sqlite3
import tempconvert
import test

from tkinter import messagebox
global op###declaring global variables and initializing
op = " "
global ds
ds = " "
# creating window
def world():
    class mainframe():
        def __init__(self,root):
            root.configure(background="black")
            root.resizable(width=False, height=False)
            root.geometry("600x568")
            self.calc = Frame(root)
            self.calc.grid()
            self.textinput = StringVar()
            self.txtDisplay = Entry(self.calc, font=('arial', 20, 'bold'), bg="#424949", fg="white", textvariable=self.textinput, bd=30, width=28,
                          justify=RIGHT)
            self.txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
        def cleardata(self):
            self.s=sqlite3.connect("historycalc.db")
            self.cursor=self.s.cursor()
            self.cursor.execute("drop table historydb")
            messagebox.showinfo("","Data Has Been Dropped")
            self.hroot.destroy()
        def recents(self):
                self.hroot=Tk()
                self.hroot.configure(background="#424949")
                self.hroot.resizable(width=False, height=False)
                
                self.calch = Frame(self.hroot)
                self.calch.grid()
                self.labelhi=Label(self.calch,text="           HISTORY        ",fg="white",font=('arial', 20, 'bold'),bg="#424949").grid()
                self.c=sqlite3.connect("historycalc.db")
                self.cursor=self.c.cursor()
                self.show=self.cursor.execute("select * from historydb")
                for self.i in self.show:
                    self.labelhh=Label(self.calch,text=(self.i[0],"=",self.i[1]),font=('arial', 20, 'bold')).grid()
                self.clearh=Button(self.calch,text="❎ Clear History",font=('arial', 18, 'bold'),fg="white",bg="#424949",command=self.cleardata).grid()
                
                self.hroot.mainloop()
        def buttonf(self):
            self.i = 0
            self.btn = []
            self.numberpad = "789456123"
            for j in range(2, 5):
                for k in range(1, 4):
                    self.btn.append(Button(self.calc, width=6, height=2, font=('arial', 20, 'bold'), bd=4, text=self.numberpad[self.i]))
                    self.btn[self.i]["command"] = lambda y=self.numberpad[self.i]:self.display(y)
                    self.btn[self.i].grid(row=j, column=k, pady=1)
                    self.i += 1
            ######################################################################
            self.btnDelete = Button(self.calc, text=" ⮜", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949",
                               fg="white", command=lambda:self.display("X"),activebackground="#FF6347").grid(row=0,
                                                                                    column=4, pady=1)
            self.btnsc = Button(self.calc, text="SC", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                                bg="#424949", fg="white",command=lambda :self.scientific(root)).grid(row=1, column=0, pady=1)

            self.btnh = Button(self.calc, text="HI", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949", fg="white",command=self.recents).grid(row=2, column=0, pady=1)

            self.btnAllClear = Button(self.calc, text="CE", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                                 bg="#424949", fg="white", command=lambda:self.display("AC")).grid(row=1, column=1,
                                                                                                     pady=1)

            self.btnsqrt = Button(self.calc, text="√ ", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949",
                              fg="white",command=lambda:self.display("√ ") ).grid(row=1,column=2,pady=1)

            self.btnPow = Button(self.calc, text="^", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949", fg="white",
                             command=lambda:self.display("^")).grid(row=1,column=3, pady=1)

            self.btndiv = Button(self.calc, text="/", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949", fg="white",
                            command=lambda:self.display("/")).grid(row=1, column=4, pady=1)

            self.btnmul = Button(self.calc, text="x", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949", fg="white",
                            command=lambda:self.display("*")).grid(row=2, column=4, pady=1)

            self.btnsub = Button(self.calc, text="-", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949", fg="white",
                            command=lambda:self.display("-")).grid(row=3, column=4, pady=1)

            self.btnAdd = Button(self.calc,text="+", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949", fg="white",
                            command=lambda:self.display("+")).grid(row=4, column=4, pady=1)

            

            self.btnopen = Button(self.calc,text="(", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949", fg="white",
                              command=lambda:self.display("(")).grid(row=3, column=0, pady=1)

            self.btnZero = Button(self.calc,text="0", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                             command=lambda:self.display("0")).grid(row=5, column=2, pady=1)

            self.btnclose = Button(self.calc, text=")", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949",
                               fg="white",
                               command=lambda:self.display(")")).grid(row=4, column=0, pady=1)

            self.btnDot = Button(self.calc, text=".", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949", fg="white",
                            command=lambda:self.display(".")).grid(row=5, column=3, pady=1)
            self.btnCom = Button(self.calc, text=",", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949", fg="white",
                            command=lambda:self.display(",")).grid(row=5, column=1, pady=1)

            self.btnPm = Button(self.calc,text=chr(177), width=6, height=2, font=('arial', 20, 'bold'), bg="#424949", fg="white",
                           command=lambda:self.display("+-")).grid(row=5, column=0, pady=1)

            self.btnEquals = Button(self.calc, text="=", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949",
                               fg="white",
                               command=self.evaluate,activebackground="green").grid(row=5, column=4, pady=1)
            ######################################################################

            ##################scientific part#####################################
        def scientific(self,root):
            root.resizable(width=False,height=False)
            root.geometry("1170x568")
            self.label= Label(self.calc,text="SCIENTIFIC CALCULATOR",width=30,height=2,font=('arial',20,'bold'),bd=4,bg="#424949",fg="white").grid(row=0,column=5,columnspan=5,pady=1)
            
    ##################################### mouse click event functions   #################################################
            def sinl(eve):
                self.display("sin(")
            def sinr(eve):
                self.display("sin-1(")

            def cosl(eve):
                self.display("cos(")
            def  cosr(eve):
                self.display("cos-1(")

            def tanl(eve):
                self.display("tan(")
            def tanr(eve):
                self.display("tan-1(")
     #######################################################################################################           
                
            self.btnSin = Button(self.calc, text="sin", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949", fg="white",)
            self.btnSin.bind("<Button-1>",sinl)
            self.btnSin.bind("<Button-3>",sinr)
            self.btnSin.grid(row=1,column=5,pady=1)

            
            self.btnCos = Button(self.calc, text="cos", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949", fg="white")
            self.btnCos.bind("<Button-1>",cosl)
            self.btnCos.bind("<Button-3>",cosr)
            self.btnCos.grid(row=1, column=6, pady=1)
            
            self.btnTan = Button(self.calc, text="tan", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949", fg="white")
            self.btnTan.bind("<Button-1>",tanl)
            self.btnTan.bind("<Button-3>",tanr)
            self.btnTan.grid(row=1,column=7,pady=1)
            self.btnExp = Button(self.calc, text="x 10", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949",
                            fg="white",command=lambda:self.display(" x 10")).grid(row=1,column=8,pady=1)

            self.btnCube = Button(self.calc, text="x 100", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949",
                             fg="white",command=lambda:self.display(" x 100")).grid(row=1,column=9,pady=1)

            # =============================================================================================
            def sinhl(eve):
                self.display("sinh(")
            def sinhr(eve):
                self.display("sinh-1(")

            def coshl(eve):
                self.display("cosh(")
            def  coshr(eve):
                self.display("cosh-1(")

            def tanhl(eve):
                self.display("tanh(")
            def tanhr(eve):
                self.display("tanh-1(")

            self.btnASinh = Button(self.calc, text="sinh", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949",
                              fg="white")
            self.btnASinh.bind("<Button-1>",sinhl)
            self.btnASinh.bind("<Button-3>",sinhr)
            self.btnASinh.grid(row=2,column=5,pady=1)

            self.btnACosh = Button(self.calc, text="cosh", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949",
                              fg="white")
            self.btnACosh.bind("<Button-1>",coshl)
            self.btnACosh.bind("<Button-3>",coshr)
            self.btnACosh.grid(row=2, column=6, pady=1)

            self.btnATanh = Button(self.calc, text="tanh", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949",
                              fg="white")
            self.btnATanh.bind("<Button-1>",tanhl)
            self.btnATanh.bind("<Button-3>",tanhr)
            self.btnATanh.grid(row=2,column=7,pady=1)
            self.btnPi = Button(self.calc, text=" π", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949", fg="white",
                           command=lambda:self.display(" π")).grid(row=2,column=8,pady=1)
            self.btn2pi= Button(self.calc, text="2π", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949",
                             fg="white",command=lambda:self.display("6.283185307179586")).grid(row=2,column=9, pady=1)

            # ========================================================================================================
            self.btnmod = Button(self.calc, text="|x|", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949", fg="white",
                            command=lambda: self.display("abs(")).grid(row=3,column=5,pady=1)

            self.btnfact = Button(self.calc, text="n!", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949", fg="white",
                             command=lambda:self.display("n!(")).grid(row=3, column=6, pady=1)
            
            self.btnlog= Button(self.calc, text="log10", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949", fg="white",
                            command=lambda:self.display("log10(")).grid(row=3,column=7,pady=1)

            self.btnlnlog = Button(self.calc, text="ln", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949", fg="white",
                             command=lambda:self.display("ln(")).grid(row=3,column=8, pady=1)
            self.btnlogab= Button(self.calc, text="log(a,b)", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949", fg="white",
                             command=lambda:self.display("log(")).grid(row=3,column=9, pady=1)
          

           

            
            # ========================================================================================================
            self.btnnPr = Button(self.calc, text="nPr", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949", fg="white",
                                    command=lambda:self.display("nPr")).grid(row=4, column=5,pady=1)

            self.btnnCr = Button(self.calc, text="nCr", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949", fg="white",
                            command=lambda:self.display("nCr")).grid(row=4, column=6, pady=1)

            self.btnINV = Button(self.calc, text=" gcd(a,b)", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949",
                            fg="white",command=lambda:self.display(" gcd(")).grid(row=4,column=7,pady=1)

            self.btnceil = Button(self.calc, text="ceil", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949",
                             fg="white",command=lambda:self.display("ceil")).grid(row=4,column=8,pady=1)

            self.btnfloor = Button(self.calc, text="floor", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949",
                              fg="white",command=lambda:self.display("floor")).grid(row=4,column=9, pady=1)
            #===========================================================================================================
            self.btndeg = Button(self.calc, text="deg", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949",
                              fg="white",command=lambda:self.display("degrees(")).grid(row=5,column=5, pady=1)

            self.btnrad = Button(self.calc, text="rad", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949",
                              fg="white",command=lambda:self.display("radians(")).grid(row=5,column=6, pady=1)
            self.btne= Button(self.calc, text="e", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949",
                              fg="white",command=lambda:self.display("e")).grid(row=5,column=7, pady=1)
            self.btnexpon = Button(self.calc, text="e^x", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949",
                              fg="white",command=lambda:self.display("exp(")).grid(row=5,column=8,pady=1)
            self.btnMod = Button(self.calc, text="Mod", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#424949", fg="white",command=lambda:self.display("%")).grid(row=5, column=9, pady=1)

            #########################################################################
        def display(self,value):
            global op
            if(value=="X"):
                self.oplength=len(op)
                op=op[0:self.oplength-1]
                self.textinput.set(op)
            elif(value=="+-"):
                if(op[0]=="-"):
                    self.temps="" + op[1:]
                    op=self.temps
                    self.textinput.set(op)
            elif(value=="AC"):
                op=""
                self.textinput.set(op)
            else:
                op = op + str(value)
                self.textinput.set(op)
        def evaluate(self):
            global op
            global ds
            self.op1=op.replace("^","**")
            self.op2=self.op1.replace("√ ","sqrt")
            self.op3=self.op2.replace("sin-1","degrees(asin")
            self.op4=self.op3.replace("cos-1","degrees(acos")
            self.op5=self.op4.replace("tan-1","degrees(atan")
            self.op6=self.op5.replace("sinh-1","degrees(asinh")
            self.op7=self.op6.replace("cosh-1","degrees(acosh")
            self.op8=self.op7.replace("tanh-1","degrees(atanh")
            self.op9=self.op8.replace("n!","factorial")
            self.op10=self.op9.replace("π","pi")
            self.op11=self.op10.replace("ln(","log(")
            self.op12=self.op11.replace(" x 10","*10")
            self.op13=self.op12.replace(" x 100|","*100")
            op=self.op13
            if(op.find("nCr(")>-1):
                calcncr()
            if(op.find("nPr(")>-1):
                calcnpr()
            try:
                ds = eval(op)
                historydatabase()
                self.textinput.set(str(ds))
            except:
                messagebox.showinfo("ERROR","SYNTAX ERROR !! OR MATH ERROR !!")
    def calcncr():
        global op
        try:
            ncrl=op.find("nCr(")
            openb=op.find("(")
            closeb=op.find(")")
            ncrs=op[ncrl:closeb+1]
            op11=op[openb+1:closeb]
            comma=op11.find(",")
            num1=int(op11[:comma])
            num2=int(op11[comma+1:closeb])
            com=factorial(num1)//(factorial(num2)*factorial(num1-num2))
            op22=op.replace(str(ncrs),str(com))
            op=op22
        except:
            messagebox.showinfo("ERROR","SOMETHING WENT WRONG")
    def calcnpr():
        global op
        try:
            ncrl=op.find("nPr(")
            openb=op.find("(")
            closeb=op.find(")")
            ncrs=op[ncrl:closeb+1]
            op11=op[openb+1:closeb]
            comma=op11.find(",")
            num1=int(op11[:comma])
            num2=int(op11[comma+1:closeb])
            com=factorial(num1)//(factorial(num1-num2))
            op2=op.replace(str(ncrs),str(com))
            op=op2
        except:
            messagebox.showinfo("ERROR","SOMETHING WENT WRONG")
    def iExit():
        iExit = tkinter.messagebox.askyesno("Scientific Calculator", "Confirm if you want to exit")
        if iExit > 0:
            root.destroy()
            return
    root=Tk()
    mainobj=mainframe(root)
    mainobj.buttonf()

    def Standard():
        root.resizable(width=False, height=False)
        root.geometry("600x568")

    def temperatureconversion():
        root.destroy()
        tempconvert.trial()

    def conversioncalc():
        root.destroy()
        test.convertunit()

    def historydatabase():
        global op
        global ds
        hisc=sqlite3.connect("historycalc.db")
        cursor=hisc.cursor()
        cursor.execute("create table IF NOT EXISTS historydb(recent1 text,recent2 text)")
        cursor.execute("insert into historydb  values(?,?)",(op,ds))
        hisc.commit()
        op = "" + str(ds)
    
    

    ##############################################  menu ####################################################################
    menubar = Menu(mainobj.calc)

    filemenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="MODE", menu=filemenu,font=('arial',9,'bold'))
    filemenu.add_command(label="Standard", command=Standard,activebackground="black",font=('arial',9,'bold'))
    filemenu.add_command(label="Scientific", command=lambda:mainobj.scientific(root),activebackground="black",font=('arial',9,'bold'))
    filemenu.add_command(label="Temperatureconversion", command=temperatureconversion,activebackground="black",font=('arial',9,'bold'))
    filemenu.add_command(label="Conversion Calculator", command=conversioncalc,activebackground="black",font=('arial',9,'bold'))
    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=iExit,activebackground="black",font=('arial',9,'bold'))



    root.config(menu=menubar)

    root.mainloop()
world()
