from booksearch import *
from bookweed import *

#Function that modify in database.txt the withdrawned book's information(last elemnt(0) with the student ID)
def book_checkout(book_nr1,id_user1):
    book_checkout1(book_nr1,id_user1)
    f=open("database.txt","w")
    for i in range(len(book_list)):
        if int(book_list[i][0])==int(book_nr1):
            f.write(str(book_list[i][0])+";"+book_list[i][1]+";"+book_list[i][2]+";"+str(id_user1)+"\n")
        else:
            f.write(str(book_list[i][0])+";"+book_list[i][1]+";"+book_list[i][2]+";"+str(book_list[i][3])+"\n")
    f.close()

#Function that modify in logfile.txt the withdrawned book's information(4th element(0) with the student ID and last element(0) with 1(nr of loaned days))
def book_checkout1(book_nr2,id_user2):
    f=open("logfile.txt","w")
    for i2 in range(len(book_list1)):
        if int(book_list1[i2][0])==int(book_nr2):
            f.write(str(book_list1[i2][0])+";"+book_list1[i2][1]+";"+book_list1[i2][2]+";"+str(id_user2)+";" + "1" +"\n")
        else:
            f.write(str(book_list1[i2][0])+";"+book_list1[i2][1]+";"+book_list1[i2][2]+";"+str(book_list1[i2][3])+";"+str(book_list1[i2][4])+"\n")
    f.close()

