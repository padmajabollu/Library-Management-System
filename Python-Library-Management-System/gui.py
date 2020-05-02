
from tkinter import *
from tkinter import ttk
import random
from datetime import datetime
import tkinter.messagebox


class Book(object):


    def __init__(self,b_id,b_title,b_author,b_publication):
        
        self.b_id = b_id
        self.b_title = b_title
        self.b_author = b_author
        self.b_publication = b_publication


class Library:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("920x520+0+0")
        self.root.configure(background='powder blue')


        BookID=StringVar()
        BookAuthor=StringVar()
        BookPublication=StringVar()
        BookTitle=StringVar()
        

        def iReset():
            BookID.set("")
            BookAuthor.set("")
            BookPublication.set("")
            BookTitle.set("")
            
        def iReset2():
            self.bookdisplydata.delete("1.0",END)
           
        def iExit():
            iExit=tkinter.messagebox.askyesno("Library Management System","Confirm You want to exit?")
            if iExit > 0:
                root.destroy()
                return
        
        def iDisplayData():
           self.bookdisplydata.insert(END,"Book ID:"+BookID.get()+"\n"+"Book Author:"+BookAuthor.get()+"\n"+"Book Title:"+BookTitle.get()+"\n"+"Book Publication:"+BookPublication.get()+"\n")
            
        """
        def addbook():
            book_list=[]
            b_id=BookID.get()
            b_author=BookAuthor.get()
            b_publication=BookPublication.get()
            b_title=BookTitle.get()

            book_list.append(Book(b_id,b_author,b_publication,b_title))
         """   

        def idisplayall():
            
                
            book_list=[]
            b_id=BookID.get()
            
            if type(b_id)==str and b_id!=None and len(b_id)>=4: # VALIDTION OF INPUT
                b_id= b_id
                
        
            else:
                tkinter.messagebox.showerror("Input not valid","Please enter valid Book ID!!")
                return
                    
                
                
            b_author=BookAuthor.get()
            if type(b_author)==str and b_author!=None and len(b_author)>=4: # VALIDTION OF INPUT
                    b_author= b_author

        
            else:
                tkinter.messagebox.showerror("Input not valid","Please enter valid book author!!")
                return
                    
            
                        

            
            b_title=BookTitle.get()
            if type(b_title)==str and b_title!=None and len(b_title)>=4: # VALIDTION OF INPUT
                    b_title= b_title

        
            else:
                tkinter.messagebox.showerror("Input not valid","Please enter valid book title!!")
                return
                
                    
            b_publication=BookPublication.get()
            if type(b_publication)==str and b_publication!=None and len(b_publication)>=4: # VALIDTION OF INPUT
                    b_publication = b_publication
                    

        
            else:
                tkinter.messagebox.showerror("Input not valid","Please enter valid book publication!!")
                return
                

            
            book_list.append(Book(b_id,b_author,b_publication,b_title))
            
            
            if  book_list == []:
                tkinter.messagebox.showerror("Input not valid","First insert the record")
                
                 
            else:
                for i in book_list:
                    self.bookdisplydata.insert(END,"Book ID:"+i.b_id+"\n"+"Book Author:"+i.b_author+"\n"+"Book Title:"+i.b_title+"\n"+"Book Publication:"+i.b_publication+"\n")
                
                
            

                
            










            
                    #===================Frame==================
        #main frame
        MainFrame = Frame(self.root)
        MainFrame.grid()

        
        #Title frame
        TitleFrame = Frame(MainFrame,width=1350,padx=20,bd=20,relief=RIDGE)
        TitleFrame.pack(side=TOP)
        self.lblTitle=Label(TitleFrame,width=39,font=('arial',25,'bold'),text="\tLibrary Management System\t",padx=12)
        self.lblTitle.grid()

        #button frame
        ButtonFrame=Frame(MainFrame,bd=20,width=1350,height=50,padx=20,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        # frame
        DataFrame=Frame(MainFrame,bd=20,width=1100,height=50,padx=20,relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        #add book label frame
        DataFrameLEFT = LabelFrame(DataFrame,bd=10,width=400,height=320,padx=20,relief=RIDGE,font=('arial',12,'bold'))
        DataFrameLEFT.pack(side=LEFT)

        
        #addbook text display
        
        DataFrameRIGHT = LabelFrame(DataFrame,bd=10,width=400,height=300,padx=20,relief=RIDGE,font=('arial',12,'bold'))
        DataFrameRIGHT.pack(side=RIGHT)

        #===================widget=========================================================================================================================
        
        self.bookdisplydata=Text(DataFrameRIGHT,font=('arial',14,'bold'),width=30,height=12,padx=8,pady=20)
        self.bookdisplydata.grid(row=0,column=0)

        """
        ListOfBooks=['c','c++','java','computer network','Python','System enginerring',
                     'c','c++','java','computer network','Python','System enginerring',
                     'c','c++','java','computer network','Python','System enginerring']


        for i in ListOfBooks:
            
            self.bookdisplydata.insert(END,i)
        """
        #=======================================================================================================
        

      
        #===================widget=========================================================================================================================

        self.lblBookID = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Book ID:",padx=2,pady=2)
        self.lblBookID.grid(row=0,column=0,sticky=W)
        self.txtBookID = Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=BookID,width= 25)
        self.txtBookID.grid(row=0,column=1)
        

        
            

            
           


        self.lblBookAuthor = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Book Author:",padx=2,pady=2)
        self.lblBookAuthor.grid(row=1,column=0,sticky=W)
        self.txtBookAuthor=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=BookAuthor,width=25)
        self.txtBookAuthor.grid(row=1,column=1)

        self.lblBookTitle = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Book Title:",padx=2,pady=2)
        self.lblBookTitle.grid(row=2,column=0,sticky=W)
        self.txtBookTitle=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=BookTitle,width=25)
        self.txtBookTitle.grid(row=2,column=1)

        self.lblBookPublication = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Book Publication:",padx=2,pady=2)
        self.lblBookPublication.grid(row=3,column=0,sticky=W)
        self.txtBookPublication=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=BookPublication,width=25)
        self.txtBookPublication.grid(row=3,column=1)
        
            
       #====================================================================================================================

        
        









        

        #=============================Buttons==================================================================
        self.btnDisplayData=Button(ButtonFrame,text="Add and Display Data",font=('arial',12,'bold'),width=19,bd=4,command=idisplayall)
        self.btnDisplayData.grid(row=0,column=0)

        self.btnReset=Button(ButtonFrame,text="Reset",font=('arial',12,'bold'),width=19,bd=4,command=iReset)
        self.btnReset.grid(row=0,column=2)

        self.btnExit=Button(ButtonFrame,text="Exit",font=('arial',12,'bold'),width=18,bd=4,command=iExit)
        self.btnExit.grid(row=0,column=3)

        self.btnResetDisplay=Button(ButtonFrame,text="Reset Display Field",font=('arial',12,'bold'),width=18,bd=4,command=iReset2)
        self.btnResetDisplay.grid(row=0,column=1)
        
        

        
        
        
        
        


        

        
        



        
if __name__ == '__main__':
    root = Tk()
    application = Library(root)
    root.mainloop()
    
