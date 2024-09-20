import sys
import tkinter as tk 
from tkinter import IntVar, messagebox
import random
from tkinter import Scrollbar
from datetime import datetime
def main():
    root=tk.Tk()
    app=LoginPage(root)
    root.mainloop()
class LoginPage:
    def __init__(self,root):
        self.root=root
        self.root.title("Billing Login page")
        self.root.geometry("1000x500")
        self.title_label=tk.Label(root,text="Billing Management System",font=("Arial",20,"bold"),bg="lightblue",bd=8,relief=tk.RAISED)
        self.title_label.pack(side=tk.TOP,fill=tk.X)
        self.frame=tk.Frame(root,bg="lightgrey",bd=9,relief=tk.GROOVE)
        self.frame.place(x=100,y=80,height=350,width=400)
        self.label2=tk.Label(self.frame,text="Login",bd=3,font=("Arial",20,"bold"),relief=tk.SUNKEN)
        self.label2.pack(side=tk.TOP,fill=tk.X)
        self.label3=tk.LabelFrame(self.frame,text="Enter Details",font=("Serif",12,"bold"))
        self.label3.pack(fill=tk.BOTH,expand=tk.TRUE)
        self.label4=tk.Label(self.label3,text="Enter Username:",font=("Arial",12))
        self.label4.grid(row=0,column=0)
        self.ent_username=tk.Entry(self.frame,bd=4,relief=tk.GROOVE)
        self.ent_username.place(x=135,y=63)
        self.label5=tk.Label(self.label3,text="Enter Password:",font=("Arial",12))
        self.label5.grid(row=1,column=0)
        self.ent_password=tk.Entry(self.frame,bd=4,relief=tk.GROOVE,show="*")
        self.ent_password.place(x=135,y=90)
        self.lab_frame=tk.LabelFrame(self.label3,text="Options",font=("Arial",13),bd=4,relief=tk.SUNKEN)
        self.lab_frame.place(x=0,y=80,height=68,width=370)
        self.button=tk.Button(self.lab_frame,text="LOGIN",bd=4,width=15,command=self.login)
        self.button.grid(row=0,column=0)
        self.button1=tk.Button(self.lab_frame,text="BILLING",bd=4,width=15,command=self.billing,state="disabled")
        self.button1.grid(row=0,column=1)
        self.button2=tk.Button(self.lab_frame,text="RESET",bd=4,width=15,command=self.reset)
        self.button2.grid(row=0,column=2)
    def login(self):
        ent_username=self.ent_username.get()
        ent_password=self.ent_password.get()
        if self.ent_username.get()=="pooja" and self.ent_password.get()=="pooja234":
            self.button1.config(state="normal")
        else:
            tk.messagebox.showinfo("LOGIN INFO",f"Enter Correct Username or Password")
    def billing(self):
        self.newwindow=tk.Toplevel(self.root)
        self.app=Window2(self.newwindow)
    def reset(self):
        self.ent_username.delete(0,tk.END)
        self.ent_password.delete(0,tk.END)
class Window2:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x600")
        self.root.title("Billing Window")
        self.title_label=tk.Label(self.root,text="Billing Management System",font=("Arial",20,"bold"),relief=tk.RAISED,bd=8,bg="lightblue")
        self.title_label.pack(side=tk.TOP,fill=tk.X)
        ######################################
        bill_no=random.randint(100,1000)
        bill_no_tk=IntVar()
        bill_no_tk.set(bill_no)
        cal_var=tk.StringVar()
        cust_name=tk.StringVar()
        cust_no=tk.StringVar()
        date=tk.StringVar()
        item_pur=tk.StringVar()
        item_qty=tk.StringVar()
        cost_of_one=tk.StringVar()
        date.set(datetime.now())
        total_list=[]
        self.grnd_total=0
        ########################################
        self.frame1=tk.LabelFrame(self.root,text="Enter Details",bg="lightgrey",font=("Arial",20))
        self.frame1.place(x=190,y=58,width=400,height=500)
        self.lab1=tk.Label(self.frame1,text="Bill Number:",font=("Arial",12),bg="lightgrey")
        self.lab1.place(x=0,y=14)
        self.entry_1=tk.Entry(self.frame1,relief=tk.GROOVE,bd=5,textvariable=bill_no_tk)
        self.entry_1.place(x=150,y=10,width=140)
        self.lab2=tk.Label(self.frame1,text="Customer Name:",font=("Arial",12),bg="lightgrey")
        self.lab2.place(x=0,y=50)
        self.entry_2=tk.Entry(self.frame1,relief=tk.GROOVE,bd=5,textvariable=cust_name)
        self.entry_2.place(x=150,y=50,width=140)
        self.lab3=tk.Label(self.frame1,text="Customer Contact:",font=("Arial",12),bg="lightgrey")
        self.lab3.place(x=0,y=90)
        self.entry_3=tk.Entry(self.frame1,relief=tk.GROOVE,bd=5,textvariable=cust_no)
        self.entry_3.place(x=150,y=90,width=140)
        self.lab4=tk.Label(self.frame1,text="Date:",font=("Arial",12),bg="lightgrey")
        self.lab4.place(x=0,y=130)
        self.entry_4=tk.Entry(self.frame1,relief=tk.GROOVE,bd=5,textvariable=date)
        self.entry_4.place(x=150,y=130,width=140)
        self.lab5=tk.Label(self.frame1,text="Items purchased:",font=("Arial",12),bg="lightgrey")
        self.lab5.place(x=0,y=170)
        self.entry_5=tk.Entry(self.frame1,relief=tk.GROOVE,bd=5,textvariable=item_pur)
        self.entry_5.place(x=150,y=170,width=140)
        self.lab6=tk.Label(self.frame1,text="Item quantity:",font=("Arial",12),bg="lightgrey")
        self.lab6.place(x=0,y=210)
        self.entry_6=tk.Entry(self.frame1,relief=tk.GROOVE,bd=5,textvariable=item_qty)
        self.entry_6.place(x=150,y=210,width=140)
        self.lab7=tk.Label(self.frame1,text="Cost of one:",font=("Arial",12),bg="lightgrey")
        self.lab7.place(x=0,y=250)
        self.entry_7=tk.Entry(self.frame1,relief=tk.GROOVE,bd=5,textvariable=cost_of_one)
        self.entry_7.place(x=150,y=250,width=140)
        ##############Functions#########
        def default_bill():
            self.bill_text.insert(tk.END,"\n\t\tGeneral Store")
            self.bill_text.insert(tk.END,"\n\tSaini Garden, Gopal Ganj Sagar,MP")
            self.bill_text.insert(tk.END,"\n\tContact:+91 9345637890")
            self.bill_text.insert(tk.END,"\n===========================================")
            self.bill_text.insert(tk.END,f"Bill Number:{bill_no_tk.get()}")
        def generate_bill():
            self.bill_text.insert(tk.END,f"\nCustomer Name:{cust_name.get()}")
            self.bill_text.insert(tk.END,f"\nCustomer Contact:{cust_no.get()}")
            self.bill_text.insert(tk.END,f"\nDate:{date.get()}")
            self.bill_text.insert(tk.END,"\n===========================================")
            self.bill_text.insert(tk.END,f"\nItem Pur:{item_pur.get()}\tItem Quan:{item_qty.get()}\tCost of one:{cost_of_one.get()}")
            self.bill_text.insert(tk.END,"\n===========================================")
            self.add_btn.config(state="normal")
            self.total_btn.config(state="normal")
            self.save_btn.config(state="normal")
        def clear():
            cust_name.set("")
            cust_no.set("")
            item_pur.set("")
            item_qty.set("")
            cost_of_one.set("")
        def reset():
            total_list.clear()
            self.grnd_total=0
            self.add_btn.config(state="disabled")
            self.total_btn.config(state="disabled")
            self.save_btn.config(state="disabled")
            self.bill_text.delete("1.0",tk.END)
            default_bill()
        self.total_cost=0
        def add_btn():
            qty=int(item_qty.get())
            cones=int(cost_of_one.get())
            total=qty*cones
            total_list.append(total)
            self.total_cost+=total
            self.bill_text.insert(tk.END,f"\n{item_pur.get():}\t\t{item_qty.get()}\t\t{cost_of_one.get()}")
            self.bill_text.insert(tk.END,f"\n{total}")
            self.total_btn.config(state="normal")
            self.bill_text.insert(tk.END,"\n===========================================")
        def total_func():
            for item in total_list:
                self.grnd_total=self.grnd_total+item
            self.bill_text.insert(tk.END,"\n===========================================")
            self.bill_text.insert(tk.END,f"\t\t\tGrand Total:{self.grnd_total}")
            self.bill_text.insert(tk.END,"\n===========================================")
        def save_func():
            user_choice=messagebox.showinfo("Confirm",f"Do you want to save the bill {bill_no_tk.get()}")
            if user_choice:  # No need to check > 0, askyesno returns True for Yes, False for No
                bill_content = self.bill_text.get("1.0", tk.END)
                with open(r"C:\Users\phius\OneDrive\Desktop\projects\cafe.txt", "w") as con:   
                    con.write(bill_content)
                    messagebox.showinfo("Success", f"Bill {bill_no_tk.get()} has been saved successfully")  # Minor message correction
            else:
                return
                
        ############end##############
        self.button_frame=tk.LabelFrame(self.frame1,text="Options",bd=5,bg="lightgrey",font=("Arial",16))
        self.button_frame.place(x=0,y=290,width=400,height=150)
        self.add_btn=tk.Button(self.button_frame,text="Add",bd=2,font=("Arial",12),bg="white",width=10,height=2,command=add_btn)
        self.add_btn.grid(row=0,column=0,padx=2,pady=2)
        self.add_btn.bind("<Button-1>")
        self.button2=tk.Button(self.button_frame,text="reset",bd=2,font=("Arial",12),bg="white",width=10,height=2,command=reset)
        self.button2.grid(row=0,column=1,padx=2,pady=2)
        self.button2.bind("<Button-2>")
        self.total_btn=tk.Button(self.button_frame,text="Total",bd=2,font=("Arial",12),bg="white",width=10,height=2,command=total_func)
        self.total_btn.grid(row=0,column=2,padx=2,pady=2)
        self.total_btn.bind("<Button-3>")
        self.button4=tk.Button(self.button_frame,text="Generate",bd=2,font=("Arial",12),bg="white",width=10,height=2,command=generate_bill)
        self.button4.grid(row=1,column=0,padx=2,pady=2)
        self.button4.bind("<Button-4>")
        self.button5=tk.Button(self.button_frame,text="Clear",bd=2,font=("Arial",12),bg="white",width=10,height=2,command=clear)
        self.button5.grid(row=1,column=1,padx=2,pady=2)
        self.button5.bind("<Button-5>")
        self.save_btn=tk.Button(self.button_frame,text="Save",bd=2,font=("Arial",12),bg="white",width=10,height=2,command=save_func)
        self.save_btn.grid(row=1,column=2,padx=2,pady=2)
        self.save_btn.bind("<Button-6>")
        self.add_btn.config(state="disabled")
        self.total_btn.config(state="disabled")
        self.save_btn.config(state="disabled")
        #####################Calculator####################
        self.frame3=tk.LabelFrame(self.root,text="Calculator",bg="lightgrey",font=("Arial",12),relief=tk.GROOVE,bd=7)
        self.frame3.place(x=650,y=60,width=370,height=350)
        self.calc_display = tk.Entry(self.frame3, font=("Arial", 20, "bold"), bd=5, relief=tk.SUNKEN, width=22, justify="right",textvariable=cal_var)
        self.calc_display.grid(row=0, column=0, columnspan=4)
        def press_btn(event):
            text=event.widget.cget("text")
            if (text=="="):
                if(cal_var.get().isdigit()):
                    value=int(cal_var.get())
                else:
                    value=eval(self.calc_display.get())
                cal_var.set(value)
                self.calc_display.update()
            elif (text=="C"):
                pass
            else:
                cal_var.set(cal_var.get()+text)
                self.calc_display.update()
        self.button7=tk.Button(self.frame3,text="1",bg="white",relief=tk.RAISED,width=10,height=2,bd=5)
        self.button7.grid(row=2,column=0,padx=2,pady=2)
        self.button7.bind("<Button-1>",press_btn)
        self.button8=tk.Button(self.frame3,text="2",bd=5,bg="white",width=10,height=2,relief=tk.RAISED)
        self.button8.grid(row=2,column=1,padx=2,pady=2)
        self.button8.bind("<Button-1>",press_btn)
        self.button9=tk.Button(self.frame3,text="3",bd=5,bg="white",width=10,height=2,relief=tk.RAISED)
        self.button9.grid(row=2,column=2,padx=2,pady=2)
        self.button9.bind("<Button-1>",press_btn)
        self.button10=tk.Button(self.frame3,text="4",bd=5,bg="white",width=10,height=2,relief=tk.RAISED)
        self.button10.grid(row=3,column=0,padx=2,pady=2)
        self.button10.bind("<Button-1>",press_btn)
        self.button11=tk.Button(self.frame3,text="5",bd=5,bg="white",width=10,height=2,relief=tk.RAISED)
        self.button11.grid(row=3,column=1,padx=2,pady=2)
        self.button11.bind("<Button-1>",press_btn)
        self.button12=tk.Button(self.frame3,text="6",bd=5,bg="white",width=10,height=2,relief=tk.RAISED)
        self.button12.grid(row=3,column=2,padx=2,pady=2)
        self.button12.bind("<Button-1>",press_btn)
        self.button13=tk.Button(self.frame3,text="7",bd=5,bg="white",width=10,height=2,relief=tk.RAISED)
        self.button13.grid(row=4,column=0,padx=2,pady=2)
        self.button13.bind("<Button-1>",press_btn)
        self.button14=tk.Button(self.frame3,text="8",bd=5,bg="white",width=10,height=2,relief=tk.RAISED)
        self.button14.grid(row=4,column=1,padx=2,pady=2)
        self.button14.bind("<Button-1>",press_btn)
        self.button15=tk.Button(self.frame3,text="9",bd=5,bg="white",width=10,height=2,relief=tk.RAISED)
        self.button15.grid(row=4,column=2,padx=2,pady=2)
        self.button15.bind("<Button-1>",press_btn)
        self.button16=tk.Button(self.frame3,text="+",bd=5,bg="white",width=10,height=2,relief=tk.RAISED)
        self.button16.grid(row=2,column=3,padx=2,pady=2)
        self.button16.bind("<Button-1>",press_btn)
        self.button17=tk.Button(self.frame3,text="-",bd=5,bg="white",width=10,height=2,relief=tk.RAISED)
        self.button17.grid(row=3,column=3,padx=2,pady=2)
        self.button17.bind("<Button-1>",press_btn)
        self.button18=tk.Button(self.frame3,text="*",bd=5,bg="white",width=10,height=2,relief=tk.RAISED)
        self.button18.grid(row=4,column=3,padx=2,pady=2)
        self.button18.bind("<Button-1>",press_btn)
        self.button19=tk.Button(self.frame3,text="0",bd=5,bg="white",width=10,height=2,relief=tk.RAISED)
        self.button19.grid(row=5,column=0,padx=2,pady=2)
        self.button19.bind("<Button-1>",press_btn)
        self.button20=tk.Button(self.frame3,text="=",bd=5,bg="white",width=10,height=2,relief=tk.RAISED)
        self.button20.grid(row=5,column=1,padx=2,pady=2)
        self.button20.bind("<Button-1>",press_btn)
        self.button21=tk.Button(self.frame3,text=".",bd=5,bg="white",width=10,height=2,relief=tk.RAISED)
        self.button21.grid(row=5,column=2,padx=2,pady=2)
        self.button21.bind("<Button-1>",press_btn)
        self.button22=tk.Button(self.frame3,text="/",bd=5,bg="white",width=10,height=2,relief=tk.RAISED)
        self.button22.grid(row=5,column=3,padx=2,pady=2)
        self.button22.bind("<Button-1>",press_btn)
        ##########################BILL AREA###########################
        self.frame4=tk.LabelFrame(self.root,text="Billing area",font=("Arial",10),bg="lightgrey",relief=tk.SUNKEN)
        self.frame4.place(x=650,y=350,width=370,height=220)
        self.y_scroll=tk.Scrollbar(self.frame4,orient="vertical")
        self.bill_text=tk.Text(self.frame4,bg="white",yscrollcommand=self.y_scroll.set)
        self.y_scroll.config(command=self.bill_text.yview)
        self.y_scroll.pack(side="right",fill=tk.Y)
        self.bill_text.pack(fill=tk.BOTH,expand=True)
        default_bill()

if __name__=="__main__":
    main()
