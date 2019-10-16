import itertools
from Tkinter import *
from booksearch import *
from bookcheckout import *
from bookreturn import *

#Function that simply convert the Student ID into a simple message(Available/Not Available)
def availability(s):
    if s==0:
        return "Available"
    else:
        return "Not available"    

#Function that opens a window to in order to checkout books 
def check_book_id():
    #Function that checks the student and book ID in order to be withdrawned 
    def check_id1():
        student_id1=id_entry2.get()
        book_id =id_entry1.get()
        type_count1=0
        try:#verify the number to be integer
            val2 = int(book_id)
        except ValueError:        
            type_count1=1
        type_count2=0
        try:#verify the number to be integer
            val3 = int(student_id1)
        except ValueError:      
            type_count2=1
        x=1
        if type_count2==0 and int(student_id1)>=1000 and int(student_id1)<=9999 :
            x=0
        else:
            x=1
        if x==0 and type_count1==0 and int(book_id)>=1 and int(book_id)<=len(book_list):
            if int(book_list[int(book_id)-1][3]) == 0 :
                msg_label14 = Label(window, text= "        Checkout confirmed       ",command = book_checkout(int(book_id),int(student_id1)))
                msg_label14.grid(row=2, column=1)
                check_button6.grid_forget()       
            else:
                msg_label19 = Label(window, text= "Book loaned to someone else ")
                msg_label19.grid(row=2, column=1)
        else:
            msg_label13 = Label(window, text= "Student or book ID incorrect")
            msg_label13.grid(row=2, column=1)
    window = Tk()
    msg_label15 = Label(window, text="Please enter the book ID:")
    msg_label15.grid(row=1, column=0)
    id_entry1 = Entry(window)# the "Entry" widget is for getting a user input. 
    id_entry1.grid(row=1, column=1)    
    msg_label18 = Label(window, text="Please enter your student ID:")
    msg_label18.grid(row=0, column=0)
    id_entry2 = Entry(window)# the "Entry" widget is for getting a user input. 
    id_entry2.grid(row=0, column=1)     
    check_button6 = Button(window, text="check",command=check_id1)
    check_button6.grid(row=2, column=0)
    window.mainloop()

#Function that opens a window and searches for books
def search_book_menu(): 
    #Function that calls another funcion(booksearch.py,line 26) and display a list of books
    def show_book_list1():
        book_name=id_entry3.get()# getting the user id
        book_search1=book_search(book_name)
        search_list=list(book_list2 for book_list2,_ in itertools.groupby(book_list2))
        if search_list ==[]:
            window=Tk()
            msg_label22 = Label(window, text="No books with such name")
            msg_label22.grid(row=1, column=1)
            window.mainloop()
        else:
            window=Tk()
            msg_label22 = Label(window, text="                                             ")
            msg_label22.grid(row=1, column=1)            
            msg_label11 = Label(window, text="Book ID")
            msg_label11.grid(row=2, column=0)    
            msg_label8 = Label(window, text="Title of the book")
            msg_label8.grid(row=2, column=1)
            msg_label9 = Label(window, text="Autor of the book   ")
            msg_label9.grid(row=2, column=2)
            msg_label10 = Label(window, text="Availability of the book")
            msg_label10.grid(row=2, column=3)
            msg_label7 = Label(window, text="")
            msg_label7.grid(row=3, column=0)
            for bk in range (len(search_list)):
                msg_label12 = Label(window, text=search_list[bk][0])
                msg_label12.grid(row=bk+4, column=0)        
                msg_label4 = Label(window, text=search_list[bk][1])
                msg_label4.grid(row=bk+4, column=1)
                msg_label5 = Label(window, text=search_list[bk][2])
                msg_label5.grid(row=bk+4, column=2)
                msg_label6 = Label(window, text=availability(search_list[bk][3]))
                msg_label6.grid(row=bk+4, column=3)
            check_button5 = Button(window, text="Checkout books",command=check_book_id)
            check_button5.grid(row=len(search_list)+5, column=1) 
            window.mainloop()
    window = Tk()    
    msg_label20 = Label(window, text="Please enter a")
    msg_label20.grid(row=0, column=0)
    msg_label21 = Label(window, text="word or the entire title of the book in lower or upper cases:")
    msg_label21.grid(row=0, column=1)
    id_entry3 = Entry(window)# the "Entry" widget is for getting a user input. 
    id_entry3.grid(row=0, column=2)
    check_button8 = Button(window, text="check",command=show_book_list1)
    check_button8.grid(row=0, column=3)
    window.mainloop()

#Function that opens a window with information regarding all books
def show_book_list():
    window = Tk()
    msg_label11 = Label(window, text="Book ID")
    msg_label11.grid(row=0, column=0)    
    msg_label8 = Label(window, text="Title of the book")
    msg_label8.grid(row=0, column=1)
    msg_label9 = Label(window, text="Autor of the book   ")
    msg_label9.grid(row=0, column=2)
    msg_label10 = Label(window, text="Availability of the book")
    msg_label10.grid(row=0, column=3)
    msg_label7 = Label(window, text="")
    msg_label7.grid(row=1, column=0)
    for bk in range (len(book_list)):
        msg_label12 = Label(window, text=book_list[bk][0])
        msg_label12.grid(row=bk+2, column=0)        
        msg_label4 = Label(window, text=book_list[bk][1])
        msg_label4.grid(row=bk+2, column=1)
        msg_label5 = Label(window, text=book_list[bk][2])
        msg_label5.grid(row=bk+2, column=2)
        msg_label6 = Label(window, text=availability(book_list[bk][3]))
        msg_label6.grid(row=bk+2, column=3)
    check_button5 = Button(window, text="Checkout books",command=check_book_id)
    check_button5.grid(row=len(book_list)+3, column=1)    
    window.mainloop()

#Function which opens a window where user can introduce the book ID to return a book
def book_ret():
    #Function that checks if the book is available or not in order to be returned 
    def check_book():
        book_id1=id_entry4.get()
        type_count3=0
        try:#verify the number to be integer
            val4 = int(book_id1)
        except ValueError:      
            type_count3=1
        if type_count3 == 0 and int(book_id1)>=1 and int(book_id1)<=len(book_list):
            if int(book_list[int(book_id1)-1][3]) == 0:
                msg_label24 = Label(window, text= "Book already available")
                msg_label24.grid(row=1, column=1)
            else:
                msg_label25 = Label(window, text= "          Return confirmed         ",command = book_return(int(book_id1)))
                msg_label25.grid(row=1, column=1)
                check_button9.grid_forget()  
        else:
            msg_label13 = Label(window, text= "    Book ID incorrect    ")
            msg_label13.grid(row=1, column=1)

    window = Tk()
    msg_label23 = Label(window, text="Please enter the book ID:")
    msg_label23.grid(row=0, column=0)
    id_entry4 = Entry(window)# the "Entry" widget is for getting a user input. 
    id_entry4.grid(row=0, column=1)     
    check_button9 = Button(window, text="return",command = check_book)
    check_button9.grid(row=1, column=0)
    window.mainloop()

#Function which opens a window where user can introduce the book ID to delete a book from the access loan window(line197)
def delete_but():
    #Function that delete any books of choise from the list
    def delete_function():
        book_id2=id_entry5.get()
        type_count7=0
        try:#verify the number to be integer
            val7 = int(book_id2)
        except ValueError:      
            type_count7=1
        if type_count7 == 0 and int(book_id2)>=1 and int(book_id2)<=len(book_list1):
            if int(book_list1[int(book_id2)-1][4]) > 30 :
                msg_label25 = Label(window, text= "                   Book deleted                   ",command=del_book(book_id2) )
                msg_label25.grid(row=1, column=1)
                check_button9.grid_forget()                                   
            else:
                msg_label24 = Label(window, text= "Book loan period under 30 days")
                msg_label24.grid(row=1, column=1)
        else:
            msg_label13 = Label(window, text= "           Book ID incorrect           ")
            msg_label13.grid(row=1, column=1)

    window = Tk()
    msg_label23 = Label(window, text="Please enter the book ID:")
    msg_label23.grid(row=0, column=0)
    id_entry5 = Entry(window)# the "Entry" widget is for getting a user input. 
    id_entry5.grid(row=0, column=1)     
    check_button9 = Button(window, text="delete",command=delete_function)
    check_button9.grid(row=1, column=0)
    window.mainloop()

#Function which access the list of all books with a preiod of loan over 30 days 
def access_loan():
    window = Tk()
    msg_label29 = Label(window, text="Books that exceeded loan period of 30 days:")
    msg_label29.grid(row=0, column=2)       
    msg_label29 = Label(window, text="")
    msg_label29.grid(row=0, column=3)        
    msg_label28 = Label(window, text="")
    msg_label28.grid(row=1, column=0)        
    msg_label11 = Label(window, text="Book ID")
    msg_label11.grid(row=2, column=0)    
    msg_label8 = Label(window, text="Title of the book")
    msg_label8.grid(row=2, column=1)
    msg_label9 = Label(window, text="Autor of the book   ")
    msg_label9.grid(row=2, column=2)
    msg_label10 = Label(window, text="Student ID")
    msg_label10.grid(row=2, column=3)
    msg_label7 = Label(window, text="  Days of loaning period")
    msg_label7.grid(row=2, column=4) 
    for bk in range (len(book_weed)):
        msg_label12 = Label(window, text=book_weed[bk][0])
        msg_label12.grid(row=bk+4, column=0)        
        msg_label4 = Label(window, text=book_weed[bk][1])
        msg_label4.grid(row=bk+4, column=1)
        msg_label5 = Label(window, text=book_weed[bk][2])
        msg_label5.grid(row=bk+4, column=2)
        msg_label6 = Label(window, text=book_weed[bk][3])
        msg_label6.grid(row=bk+4, column=3)
        msg_label27 = Label(window, text=book_weed[bk][4])
        msg_label27.grid(row=bk+4, column=4)
    check_button5 = Button(window, text="Delete book",command=delete_but)
    check_button5.grid(row=len(book_weed)+5, column=2)    
    window.mainloop()

#Function that display a few instruction for the user in order to use the application easier and properly
def Help():
    window =Tk()
    msg_label29 = Label(window, text="Hello, here is some information of how to properly use the Library application:")
    msg_label29.grid(row=0, column=0)       
    msg_label29 = Label(window, text="")
    msg_label29.grid(row=1, column=0)        
    msg_label28 = Label(window, text="1. Always exit all windows after checking out, returning or deleting any books in order")
    msg_label28.grid(row=2, column=0)        
    msg_label11 = Label(window, text="order for the program to update the booklists.                                                               ")
    msg_label11.grid(row=3, column=0)    
    msg_label8 = Label(window, text="2. Deleting a book would be allowed only if the loan period has exceeded 30 days.     ")
    msg_label8.grid(row=4, column=0)
    msg_label9 = Label(window, text="3. Checking out books will always require again the Student ID for safety reasons.      ")
    msg_label9.grid(row=5, column=0)
    msg_label10 = Label(window, text="4. When checking out a book, automatically the loan period will be set to 1 day.          ")
    msg_label10.grid(row=6, column=0)
    msg_label7 = Label(window, text="5. In the search menu, you can enter letters in capital or not, because the program     ")
    msg_label7.grid(row=7, column=0) 
    msg_label34 = Label(window, text="will automatically change to lowercase or uppercase depending of the title                 ")
    msg_label34.grid(row=8, column=0) 
    window.mainloop()

#Function that checks if the input is a student ID or not(4 digit number) and opens the main menu
def check_id():
    student_id=id_entry.get()# getting the user id
    type_count=0
    try:#verify the number to be integer
        val = int(student_id)
    except ValueError:        
        type_count=1
    if type_count==0 and int(student_id)>=1000 and int(student_id)<=9999:
        msg_label.grid_forget()
        id_entry.grid_forget()
        check_button1.grid_forget()
        msg_label40 = Label(window, text="Student ID:")
        msg_label40.grid(row=0, column=1)
        msg_label41 = Label(window, text=student_id)
        msg_label41.grid(row=1, column=1)
        check_button10 = Button(window, text="Help",command = Help)
        check_button10.grid(row=0, column=2)
        check_button2 = Button(window, text="    Search for book      ",command = search_book_menu)
        check_button2.grid(row=3, column=0)
        check_button3 = Button(window, text="Check for available books",command = show_book_list)
        check_button3.grid(row=3, column=1)
        check_button4 = Button(window, text="     Return books        ",command = book_ret)
        check_button4.grid(row=3, column=2)
        check_button7 = Button(window, text="   Access loan history   ",command= access_loan)
        check_button7.grid(row=4, column=1)
    else:
        msg_label2 = Label(window, text= "Only students have access")
        msg_label2.grid(row=3, column=1)
        msg_label16 = Label(window, text= "Enter a valid student ID")
        msg_label16.grid(row=4, column=1)
window = Tk()
msg_label = Label(window, text="Please enter your student ID:")
msg_label.grid(row=0, column=1)
id_entry = Entry(window)# the "Entry" widget is for getting a user input. 
id_entry.grid(row=1, column=1)
check_button1 = Button(window, text="check",command=check_id)
check_button1.grid(row=2, column=1)
window.mainloop()
