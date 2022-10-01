IMPORTANT: If you have Python3 please modify in the begging at line 2, "from from Tkinter import *" to "from tkinter import *" as it may return an errror if not changed 

My program represents an application with a simple management system for a librarian to use. An esential requirement would be to quit the app and restart it if a withdrawn or return was made in order to update all the new data.

It provides an interface with a menu with 5 options to chose from:

-> Search for book:
    -has a little search engine which can recognize a book title, only by entering a letter (doesn't matter the if it's uppercase or not) that is contained in the title;
    -provides a list with all books in association with the input string ;
    -gives the user the option to withdrawn a book;
    -it is requiered after every display of book search list to exit and restart the application either you withdrawned or not any books.

-> Check for available books:
    -provides a list with all books from database; 
    -gives the user the option to withdrawn a book; 
    -checks from database if the last element from every book is alocated to an student ID and displays 'Not available', otherwise if it's equal to 0 it displays 'Available';
    -checking out a book will automatically set it to 1 day (loan period) in logfile.

-> Return books:
    -allow you to return any book which doesn't have the last element in data base equal to 0 (Available);
    -Different books can be returned without restarting the app.

-> Access loan history:
    -provides a list with all books and their information, and if they were withdrawn for a period longer than 30 days;
    -gives the user the option to delete a book from the list;
    -deleting a book would delete it from both database.txt and logfile.txt.

-> Help:
    -gives the user a few helping indtructions regarding the application.

With the information about reseting the app as I mentioned earlier, please feel free to navigate as I populated the database with a variation of names and availabilities. 

