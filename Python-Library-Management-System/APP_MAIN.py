from FileHandling import *
import re
from LINKEDLIST import *         
from datetime import date 



def main():
    #print(date.today())
    librarian=LinkedList()
    student=LinkedList()
    book=LinkedList()
    student_book=LinkedList()

    file=filehandling("LibrarianData.txt")
    data=file.readData()
    tmp=librarian.head
    
    for i in data:
        mainData=i.strip("\n").split(",")
        librarian.insertEnd([mainData[0],mainData[1],mainData[2]])
    file.closeFile()
    #librarian.printList()
    
    file=filehandling("StudentData.txt")
    data=file.readData()
    for i in data:
        mainData=i.strip("\n").split(",")
        student.insertEnd([mainData[0],mainData[1],mainData[2],mainData[3]\
        ,mainData[4]])
    file.closeFile()
    #student.printList()

    file=filehandling("StudentBookData.txt")
    data=file.readData()
    for i in data:
        mainData=i.strip("\n").split(",")
        student_book.insertEnd([mainData[0],mainData[1],mainData[2],mainData[3],mainData[4]\
        ,mainData[5]])
    file.closeFile()
    #student_book.printList()

    file=filehandling("BookData.txt")
    data=file.readData()
    for i in data:
        mainData=i.strip("\n").split(",")
        book.insertEnd([mainData[0],mainData[1],mainData[2],mainData[3]])
    file.closeFile()
    #book.printList()

    
    while(True):
        try:
                
            print("\nSelect your Option\n")
            print("1.Registration")
            print("2.Login")
            print("3.Exit")
            ch=int(input("\n"))
            if ch==1:
                while True:
                        
                    print("\nSelect your Option\n")
                    print("1.Librarian Registration")
                    print("2.Student Registration")
                    print("3.Exit")
                    ch1=int(input("\n"))

                    if ch1==1:
                        l_id = input("\nEnter ID: ")
                        while True:
                            try:
                                                            
                                if type(l_id)==str and l_id!=None and len(l_id)>=4: # VALIDTION OF INPUT
                                    l_id1=l_id
                                    break

                                else:
                                    l_id=input("\nError: Enter Valid Book ID : ")
                                    continue
                            except:
                                continue

                        l_name = input("\nEnter the name : ")
                        while True:    
                            try:
                                
                                if type(l_name)==str and l_name!=None and len(l_name)>=4: # VALIDTION OF INPUT
                                    l_name1= l_name
                                    break

                                else:
                                    l_name= input("\nError: Enter Valid Book Name : ")
                                    continue
                            except:
                                continue

        
                        l_password=input("\nEnter Valid Password like Pass.word@25 : ")
                        x=True
                        while x:  
                        
                            try:
                                
                                if (len(l_password)<8 or len(l_password)>15):
                                    pass
                                elif not re.search("[a-z]",l_password):
                                    pass
                                elif not re.search("[0-9]",l_password):
                                    pass
                                elif not re.search("[A-Z]",l_password):
                                    pass
                                elif not re.search("[$#@.]",l_password):
                                    pass
                                elif re.search("\s",l_password):
                                    pass
                                else:
                                    
                                    l_password1 = l_password
                                    x=False
                                    break
                                if x:
                                    l_password = input("\nError: Enter Valid password like pass.word@25 : ")
                                    continue
                            except:
                                l_password = input("\nError: Enter Valid password like pass.word@25 : ")
                                continue
                        
                        librarian.insertEnd([l_id1,l_name1,l_password1])
                        librarian.printList()
                        file=filehandling("LibrarianData.txt","w")
                        tmp=librarian.head
                        while(tmp!=None):
                            l_data=tmp.data[0]+","+tmp.data[1]+","+tmp.data[2]+"\n"
                            file.writeData(l_data)
                            tmp=tmp.next
                        file.closeFile()

                    elif ch1==2:
                        prn = input("\nEnter PRN : ")
                        while True:
                            try:
                                if len(prn) != 10 or prn.isnumeric() == False or prn == None\
                                 and type(int(prn))==True: # VALIDTION OF INPUT
                                    raise PRN(" Enter 10 DIGIT PRN Number")
                                    
                                else:
                                    s_prn1 = prn
                                    break
                                

                            except PRN as e:
                                print(e)
                                prn = input()
                                continue
                        name = input("\nEnter the name : ")
                        while True:
                            try:
                                if name.isnumeric()==False and name!="" and len(name)!=1 : # VALIDTION OF INPUT
                                    s_name1 = name
                                    break

                                else:
                                    raise Exception("\nError: Enter Valid Name : ")
                                    
                            except Exception as e:
                                print(e)
                                name=input()
                                continue
                        email = input("\nEnter your email id : ")
                        while True:
                            try:
                                if email[-13:] != '@mitaoe.ac.in' or email==None: # VALIDTION OF INPUT
                                    
                                    raise Exception("\nEnter valid Mail ID like *********@mitaoe.ac.in : ")
                                    
                                else:
                                    s_email1 = email
                                    break

                            except Exception as e:
                                print(e)
                                email=input()
                                continue

                        contact = input("\nEnter the contact number : ")
                        while True:
                            try:
                                    
                                if len(contact) != 10 or contact.isnumeric() == False or contact=="" and type(int(contact))==True: # VALIDTION OF INPUT
                                    raise Exception("\nError: Enter 10 DIGIT Contact Number : ")
                                else:
                                    s_contact1 = contact
                                    break

                            except Exception as e:
                                print(e)
                                contact=input()
                                continue
                        password=input("\nEnter Valid Password like Pass.word@25 : ")
                        x=True
                        while x:  
                            try:
                                    
                                if (len(password)<8 or len(password)>15):
                                    pass
                                    
                                elif not re.search("[a-z]",password):
                                    pass
                                    
                                    
                                elif not re.search("[0-9]",password):
                                    pass
                                    
                                elif not re.search("[A-Z]",password):
                                    pass
                                    
                                elif not re.search("[$#@.]",password):
                                    pass
                                    
                                elif re.search("\s",password):
                                    pass
                                    
                                else:
                                    """
                                    encrypt=""
                                    for i in range(0,len(password)):
                                        encrypt=encrypt+chr(ord(password[i])-2)
                                        x=False
                                        break
                                    """
                                    s_password1 = password
                                    x=False
                                    break
                                    
                                
                                if x:
                                    password = input("\nError: Enter Valid Password like Pass.word@25 : ")
                                    
                                    continue
                            except:

                                password = input("\nError: Enter Valid Password like Pass.word@25 : ")
                                    
                                continue
                    
                        student.insertEnd([s_prn1,s_name1,s_email1,s_contact1,s_password1])
                        student.printList()
                        file=filehandling("StudentData.txt","w")
                        tmp=student.head
                        while(tmp!=None):
                            s_data=tmp.data[0]+","+tmp.data[1]+","+tmp.data[2]+","+tmp.data[3]+","+\
                            tmp.data[4]+"\n"
                            file.writeData(s_data)
                            tmp=tmp.next
                        file.closeFile()


                    elif ch1==3:
                        break
                    else:
                        print("\nWrong Choice")
                        


            elif ch==2:
                while True:
                        
                    print("\nSelect your Option\n")
                    print("1.Librarian Login")
                    print("2.Student Login")
                    print("3.Exit")
                    ch1=int(input("\n"))

                    if ch1==1:
                        x=True
                        while x:
                            try:    
                                id = input("\nEnter ID: ")
                                password=input("\nEnter Valid Password  : ")
                                tmp=librarian.head
                                while(tmp!=None):

                                    if id==tmp.data[0] and password==tmp.data[2]:
                                        print("\nLogin Successfully........")
                                        x=False
                                        break

                                    else:
                                        tmp=tmp.next
                                        continue  
                                    print("\nInvalid combination of Id and password")
                            except:
                                continue 
                        while True:

                            print("\nSelect your Option\n")
                            print("1.Add Book")
                            print("2.Delete Book")
                            print("3.Issue Book")
                            print("4.Return Book")
                            print("5.Available Books Details")
                            print("6.Issued Books Details")
                            print("7.Total Issued Books")
                            print("8.Total Available Books")
                            print("9.Delete Student")
                            print("10.Exit")
                            ch=int(input("\n"))
                            if ch==1:
                                b_id= input("\nEnter the Book Id : ")
                                while True:
                                    try:

                                        if type(b_id)==str and b_id!=None and len(b_id)>=4:\
                                         # VALIDTION OF INPUT
                                            b_id1= b_id
                                            break

                                        else:
                                            raise Exception("")

                                    except Exception as e:
                                        b_id=input("\nError: Enter Valid Book ID : ")
                                        continue
                            
                                b_name= input("\nEnter the Book Name : ")
                                while True:
                                    try:
                                        if type(b_name)==str and b_name!=None and \
                                        len(b_name)>=4: # VALIDTION OF INPUT
                                            b_name1= b_name
                                            break
                                        else:
                                            raise Exception("")
                                        

                                    except Exception as e:
                                        b_name=input("\nError: Enter Valid Book Name : ")
                                        continue
                                b_author= input("\nEnter the Book Author : ")
                                while True:
                                    try:
                                        if type(b_author)==str and b_author!=None and \
                                        len(b_author)>=4: # VALIDTION OF INPUT
                                            b_author1= b_author
                                            break
                                        else:
                                            raise Exception("")


                                    except Exception as e:
                                        b_author= input("\nError: Enter Valid Book Name : ")
                                        continue

                                b_publication= input("\nEnter the Book publication : ")
                                while True:
                                    try:
                                        if type(b_publication)==str and b_publication!=None\
                                         and len(b_publication)>=4: # VALIDTION OF INPUT
                                            b_publication1 = b_publication
                                            break
                                        else:
                                            raise Exception("")

                                    except Exception as e:
                                        b_publication=input("\nError: Enter Valid Book\
                                         publication : ")
                                        continue
                                book.insertEnd([b_id,b_name,b_author,b_publication])
                                file=filehandling("BookData.txt","w")
                                tmp=book.head
                                while(tmp!=None):
                                    b_data=tmp.data[0]+","+tmp.data[1]+","+tmp.data[2]+","+\
                                    tmp.data[3]+"\n"
                                    file.writeData(b_data)
                                    tmp=tmp.next
                                file.closeFile()

                            elif ch==2:
                                while True:
                                    print("\n Select your Option")
                                    print("1.Delete by Book Id")
                                    print("2.Exit")
                                    ch=int(input())
                                    if ch==1:
                                        b_id=input("\nEnter the Book Id : ")
                                        tmp=book.head
                                        while(tmp!=None):
                                            if tmp.data[0]==b_id:
                                                book.deleteNode(tmp.data[0])
                                                print("Book Record Successfully Deleted.....")
                                                file=filehandling("BookData.txt","w")
                                                tmp1=book.head
                                                while(tmp1!=None):
                                                    b_data=tmp1.data[0]+","+tmp1.data[1]+","+\
                                                    tmp1.data[2]+","+tmp1.data[3]+"\n"
                                                    file.writeData(b_data)
                                                    tmp1=tmp1.next
                                                file.closeFile()

                                                break
                                            else:
                                                tmp=tmp.next
                                                continue
                                            print("\nInvalid Book Id")
                                    elif ch==2:
                                        break
                                    else:
                                        print("\nWrong Choice")
                            elif ch==3:
                                x=True
                                while x:

                                    b_id=input("\nEnter the Book Id : ")
                                    prn=input("\nEnter the PRN : ")
                                    tmp=book.head
                                    while(tmp!=None):
                                        if tmp.data[0]==b_id:

                                            student_book.insertEnd([tmp.data[0],tmp.data[1]\
                                            ,tmp.data[2],tmp.data[3],prn,date.today()])
                                            print("Book return Successfully .....")
                                            file=filehandling("StudentBookData.txt","w")
                                            tmp1=student_book.head
                                            while(tmp1!=None):
                                    
                                                s_b_data=tmp1.data[0]+","+tmp1.data[1]+","+\
                                                tmp1.data[2]+","+tmp1.data[3]+","+tmp1.data[4]+\
                                                ","+str(tmp1.data[5]) +"\n"
                                                file.writeData(s_b_data)
                                                tmp1=tmp1.next
                                            file.closeFile()
                                            x=False
                                            break

                                        else:
                                            tmp=tmp.next
                                            continue
                                        print("\nGiven Input is Wrong")
                                    

                                    tmp=book.head
                                    while(tmp!=None):        
                                        if tmp.data[0]==b_id:
                                            book.deleteNode(b_id)
                                            file=filehandling("BookData.txt","w")
                                            tmp1=book.head
                                            while(tmp1!=None):
                                                b_data=tmp1.data[0]+","+tmp1.data[1]+","\
                                                +tmp1.data[2]+","+tmp1.data[3]+"\n"
                                                file.writeData(b_data)
                                                tmp1=tmp1.next
                                            file.closeFile()

                                            break
                                        else:
                                            tmp=tmp.next
                                            continue
                                        
                                
                            elif ch==4:
                                b_id=input("\nEnter the Book Id : ")
                                prn=input("\nEnter the PRN : ")
                                tmp=student_book.head
                                x=True
                                while x:
                            
                                    if tmp.data[0]==b_id and tmp!=None:
                                        book.insertEnd([tmp.data[0],tmp.data[1],\
                                        tmp.data[2]\
                                        ,tmp.data[3]])
                                        print("Book return Successfully .....")
                                        student_book.deleteNode(b_id)
                                        file=filehandling("BookData.txt","w")
                                        tmp1=book.head
                                        while(tmp1!=None):
                                            b_data=tmp1.data[0]+","+tmp1.data[1]+","+\
                                            tmp1.data[2]+","+tmp1.data[3]+"\n"
                                            file.writeData(b_data)
                                            tmp1=tmp1.next
                                        
                                        file.closeFile()
                                        tmp1=None
                                        file=filehandling("StudentBookData.txt","w")
                                        tmp1=student_book.head
                                        while(tmp1!=None):
                                            s_b_data=tmp1.data[0]+","+tmp1.data[1]+","+\
                                            tmp1.data[2]+","+tmp1.data[3]+","+tmp1.data[4]\
                                            +","+str(tmp1.data[5]) +"\n"
                                            file.writeData(s_b_data)
                                            tmp1=tmp1.next
                                            
                                        file.closeFile()
                                        tmp1=None
                                        d1=date.today()
                                        d2=date(int(tmp.data[5[0:4]]),int(tmp.data[5[5:7]\
                                        ]),int(tmp.data[5[8:10]]))
                                        print("\n2")
                                        d1=d1-d2
                                        days=d1.days
                                        if days>14:
                                            fine=(days-14)*2
                                            print("\nTotal Fine is ",fine)
                                        x=False
                                        continue
                                    else:
                                        x=True
                                        tmp=tmp.next
                                        continue
                                    print("\nGiven Input is Wrong")

                                            
                            elif ch==5:                
                                print("\nAvailable Book Details")
                                print("\nId\t\tName\t\t\t\t\tAuthor\t\tPublication")
                                file=filehandling("BookData.txt")
                                a_b_data=file.readData()
                                for data in a_b_data:
                                    
                                    mainData=data.strip("\n").split(",")
                                    
                                    print(mainData[0],"\t",mainData[1],"\t",mainData[2],"\t",mainData[3])

                                file.closeFile()

                            elif ch==6:
                                print("\nIssued Book Details")
        
                                print("\nId\t\tName\t\t\t\t\tAuthor\t\tPublication")
                            
                                file=filehandling("StudentBookData.txt")
                                i_b_data=file.readData()
                                for data in i_b_data:
                                    
                                    mainData=data.strip("\n").split(",")
                                    
                                    print(mainData[0],"\t",mainData[1],"\t",mainData[2]\
                                    ,"\t",mainData[3])

                                file.closeFile()

                            elif ch==7:
                                total_issue=student_book.size()
                                print("\nTotal Issued Books are ",total_issue)
                            elif ch==8:
                                total_available=book.size()
                                print("\nTotal Available Books are ",total_available)
                            elif ch==9:
                                prn=input("\nEnter the PRN : ")
                                tmp=student.head
                                while(tmp!=None):
                                    if tmp.data[0]==prn:
                                        student.deleteNode(tmp.data[0])
                                        print("Student Record Successfully Deleted.....")
                                        file=filehandling("StudentData.txt","w")
                                        tmp1=student.head
                                        while(tmp1!=None):
                                            s_data=tmp1.data[0]+","+tmp1.data[1]+","+\
                                            tmp1.data[2]+","+tmp1.data[3]+","+\
                                            tmp1.data[4]+"\n"
                                            file.writeData(s_data)
                                            tmp1=tmp1.next
                                        file.closeFile()

                                        break
                                    else:
                                        tmp=tmp.next
                                        continue


                            elif ch==10:
                                break
                            else:
                                print("\nWrong Choice")
                                continue


                    
                    elif ch1==2:
                        x=True
        
                        while x:
                            try:    
                                prn = input("\nEnter PRN: ")
                                password=input("\nEnter  Password  : ")
                                tmp=student.head
                                while(tmp!=None):
                                    """
                                    for i in range(0,len(password)):
                                        decrypt=decrypt+chr(ord(password[i])+2)
                                        self.__password = decrypt
                                    """ 
                                    if prn==tmp.data[0] and password==tmp.data[4]:
                                        print("\nLogin Successfully........")
                                        x=False
                                        break

                                    else:
                                        tmp=tmp.next
                                        continue  
                                    print("\nInvalid combination of PRN and password") 
                            except:
                                continue
                        
                        while True:
                            print("\nSelect your Option\n")
                            print("1.Search Book")
                            print("2.Display Issued Book Details")
                            print("3.Exit")
                            ch=int(input("\n"))
                            if ch==1:
                                while True:
                                    print("\n Select your Option")
                                    print("1.Search by Book Name")
                                    print("2.Search by Book Author")   
                                    print("3.Search by Book Publication")  
                                    print("4.Exit")
                                    ch=int(input("\n"))
                                    if ch==1:
                                        b_name1=input("\nEnter the Book Name : ")
                                
                                        print("\nId\t\t\tName\t\t\t\tAuthor\t\tPublication")
                                        tmp=book.head
                                        while(tmp!=None):
                                            if b_name1==tmp.data[1]:
                                                print(tmp.data[0],"\t",tmp.data[1],"\t",\
                                                tmp.data[2],"\t",tmp.data[3])      
                                            tmp=tmp.next          
                                            
                                    elif ch==2:
                                        b_author1=input("\nEnter the Book Author : ")
                                
                                        print("\nId\t\t\tName\t\t\t\tAuthor\t\tPublication")
                                        tmp=book.head
                                        while(tmp!=None):
                                            if b_author1==tmp.data[2]:
                                                print(tmp.data[0],"\t",tmp.data[1],"\t",\
                                                tmp.data[2],"\t",tmp.data[3])      
                                            tmp=tmp.next 

                                    elif ch==3:
                                        b_author1=input("\nEnter the Book Publication : ")
                                
                                        print("\nId\t\t\tName\t\t\t\tAuthor\t\tPublication")
                                        tmp=book.head
                                        while(tmp!=None):
                                            if b_author1==tmp.data[3]:
                                                print(tmp.data[0],"\t",tmp.data[1],"\t",\
                                                tmp.data[2],"\t",tmp.data[3])      
                                            tmp=tmp.next                                         
                                    elif ch==4:
                                        break
                                    else:
                                        print("\nWrong Choice")
                                           

                                
                            elif ch==2:
                                print("\nIssued Book Details")
                                print("\nId\t\tName\t\t\t\t\tAuthor\t\tPublication")
                            
                                file=filehandling("StudentBookData.txt")
                                i_b_data=file.readData()
                                for data in i_b_data:
                                    
                                    mainData=data.strip("\n").split(",")
                                    
                                    print(mainData[0],"\t",mainData[1],"\t",mainData[2]\
                                    ,"\t",mainData[3])

                                file.closeFile()

                            elif ch==3:
                                break
                            else:
                                print("\nWrong Choice")
                                                    

                    elif ch1==3:
                        break
                    else:
                        print("\nWrong Choice")
                        
            elif ch==3:
                break
            else:
                print("\nWrong Choice")
                

        except:
            #print("\nWrong Choice")
            continue

main()