from booksearch import *

book_list1 =[]

#Function that add books to book_list1
def add_books1(book_nr1,book_title1,book_autor1,id_user1,days1):
    book_list1.append([book_nr1,book_title1,book_autor1,id_user1,days1])
    return book_list1
f1 = open('logfile.txt','r')
for line1 in f1:
    line1 = line1.strip()
    line1 = line1.split(';')
    add_books1(int(line1[0]), line1[1], line1[2], int(line1[3]),int(line1[4]))
f1.close()

book_weed = []

for i1 in range (len(book_list1)):
    if book_list1[i1][4] > 30:
        book_weed.append(book_list1[i1])

#Function that overwrite the database.txt file, deleting a book with it's information, only by providing it's book ID
def del_book(book_nr3):
    del_book1(book_nr3)
    f=open("database.txt","w")
    for p in range (len(book_list)):
        if (p+1)<int(book_nr3):
            f.write(str(book_list[p][0])+";"+book_list[p][1]+";"+book_list[p][2]+";"+str(book_list[p][3])+"\n")
        elif (p+1)>int(book_nr3):
            f.write(str(p)+";"+book_list[p][1]+";"+book_list[p][2]+";"+str(book_list[p][3])+"\n")

#Function that overwrite the logfile.txt file, deleting a book with it's information, only by providing it's book ID
def del_book1(book_nr4):
    f=open("logfile.txt","w")
    for p4 in range (len(book_list1)):
        if (p4+1)<int(book_nr4):
            f.write(str(book_list1[p4][0])+";"+book_list1[p4][1]+";"+book_list1[p4][2]+";"+str(book_list1[p4][3])+";" +str(book_list1[p4][4])+"\n")
        elif (p4+1)>int(book_nr4):
            f.write(str(p4)+";"+book_list1[p4][1]+";"+book_list1[p4][2]+";"+str(book_list1[p4][3])+";" +str(book_list1[p4][4])+"\n")



