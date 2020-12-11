from tkinter import *
from tkinter.ttk import Combobox
import names
import tkinter.messagebox



class Names:
    def __init__(self,root):
        self.root=root
        self.root.title("Random Names")
        self.root.geometry("300x300")
        self.root.iconbitmap("logo920.ico")
        self.root.resizable(0,0)


        name_category=StringVar()



        def on_enter1(e):
            but_random['background']="black"
            but_random['foreground']="cyan"  
        def on_leave1(e):
            but_random['background']="SystemButtonFace"
            but_random['foreground']="SystemButtonText"

            

        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"  
        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"

        
        def random():
            if name_category.get()!="Select Name Category":
                if name_category.get()=="Male":
                    males=names.get_full_name(gender='male')
                    lab_name.config(text=males)
                if name_category.get()=="Female":
                    females=names.get_full_name(gender='female')
                    lab_name.config(text=females)

            else:
                tkinter.messagebox.showerror("Error","Please Select Categories")



        def clear():
            name_category.set("Select Name Category")
            lab_name.config(text="")

#===============frame===============================#
        
        mainframe=Frame(self.root,width=300,height=300,relief="ridge",bd=3,bg="gray77")
        mainframe.place(x=0,y=0)


        size_list=["Male","Female"]
        En_len=Combobox(mainframe,values=size_list,font=('arial',13),width=21,state="readonly",textvariable=name_category)
        En_len.set("Select Name Category")
        En_len.place(x=40,y=20)

        but_random=Button(mainframe,width=18,text="Random",font=('times new roman',13),cursor="hand2",command=random)
        but_random.place(x=60,y=80)
        but_random.bind("<Enter>",on_enter1)
        but_random.bind("<Leave>",on_leave1)

        but_clear=Button(mainframe,width=18,text="Clear",font=('times new roman',13),cursor="hand2",command=clear)
        but_clear.place(x=60,y=150)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)

        lab_name=Label(mainframe,text="",font=('times new roman',16),bg="gray77")
        lab_name.place(x=80,y=230)


if __name__ == "__main__":
    root=Tk()
    Names(root)
    root.mainloop()