import itertools

book_list =[]

#Function that add books from database.txt to the book_list
def add_books(book_nr,book_title,book_autor,id_user):
    book_list.append([book_nr,book_title,book_autor,id_user])
    return book_list
f = open('database.txt','r')
for line in f:
    line = line.strip()
    line = line.split(';')
    add_books(int(line[0]), line[1], line[2], int(line[3]))
f.close()


book_list2 =[]

#Function that add books from database.txt to the book_list2
def add_books2(book_nr,book_title,book_autor,id_user):
    book_list2.append([book_nr,book_title,book_autor,id_user])
    return book_list2

#Function that search with any lowercase or uppercase from a string into another 
def find_str(word,words):
    word_l=word.lower()
    words_l=words.lower()
    result=words_l.find(word_l)
    return result

#Function read all the information in database.txt in order to find an assotiation with the input searched 
def book_search(x):
    f = open('database.txt','r')
    for line in f:
        line = line.strip()
        line = line.split(';')
        if find_str(str(x),str(line[1]))>=0 :
            add_books2(int(line[0]), line[1], line[2], int(line[3]))
    f.close()
    return book_list2
