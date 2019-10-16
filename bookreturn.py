from booksearch import *
from bookweed import *

#Function that modify in database.txt the returned book's information(last elemnt(Student ID) with 0)
def book_return(book_nr1):
    book_return1(book_nr1)
    f=open("database.txt","w")
    for i in range(len(book_list)):
        if int(book_list[i][0])==int(book_nr1):
            f.write(str(book_list[i][0])+";"+book_list[i][1]+";"+book_list[i][2]+";"+"0"+"\n")
        else:
            f.write(str(book_list[i][0])+";"+book_list[i][1]+";"+book_list[i][2]+";"+str(book_list[i][3])+"\n")
    f.close()

#Function that modify in database.txt the returned book's information(4th element(Student ID) with 0 and last element(nr of loaned days) with 0)
def book_return1(book_nr2):
    f=open("logfile.txt","w")
    for i2 in range(len(book_list1)):
        if int(book_list1[i2][0])==int(book_nr2):
            f.write(str(book_list1[i2][0])+";"+book_list1[i2][1]+";"+book_list1[i2][2]+";"+"0"+";" + "0" +"\n")
        else:
            f.write(str(book_list1[i2][0])+";"+book_list1[i2][1]+";"+book_list1[i2][2]+";"+str(book_list1[i2][3])+";"+str(book_list1[i2][4])+"\n")
    f.close()

