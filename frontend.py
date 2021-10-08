from tkinter import *
import backend

# ================================= settings =============================
window = Tk()
window.title("BookStore")
window.geometry("420x220")


# ================================= function =============================

def clear_list():
    list.delete(0, END)


def selected(event):
    global select_row
    if len(list.curselection()) > 0 :
        index = list.curselection()[0]
        select_row = list.get(index)
        E_title.delete(0 , END)
        E_title.insert(END , select_row[1])
        E_author.delete(0, END)
        E_author.insert(END, select_row[2])
        E_year.delete(0, END)
        E_year.insert(END, select_row[3])
        E_isbn.delete(0, END)
        E_isbn.insert(END, select_row[4])



def view_command():
    clear_list()
    books = backend.view()
    for book in books:
        list.insert(END ,book)


def add_command():
    backend.insert(var_title.get(),var_author.get(),var_year.get(),var_isbn.get())
    view_command()


def search_command():
    clear_list()
    books = backend.search(var_title.get(),var_author.get(),var_year.get(),var_isbn.get())
    for book in books:
        list.insert(END , book)


def update_command():
    backend.update(select_row[0],var_title.get(),var_author.get(),var_year.get(),var_isbn.get())
    view_command()


def delete_command():
    backend.delete(select_row[0])
    view_command()


# ================================= labels =============================
L_title = Label(window, text="Title")
L_title.grid(row=0, column=0)
L_author = Label(window, text="Author")
L_author.grid(row=0, column=2)
L_year = Label(window, text="Year")
L_year.grid(row=1, column=0)
L_isbn = Label(window, text="ISBN")
L_isbn.grid(row=1, column=2)

# ================================= Entries =============================
var_title = StringVar()
E_title = Entry(window, textvariable=var_title)
E_title.grid(row=0, column=1)

var_author = StringVar()
E_author = Entry(window, textvariable=var_author)
E_author.grid(row=0, column=3)

var_year = StringVar()
E_year = Entry(window, textvariable=var_year)
E_year.grid(row=1, column=1)

var_isbn = StringVar()
E_isbn = Entry(window, textvariable=var_isbn)
E_isbn.grid(row=1, column=3)

# ================================= listbox =============================
list = Listbox(window, width=40, height=8)
list.grid(row=2, column=0, rowspan=6, columnspan=2)

list.bind("<<ListboxSelect>>",selected)

sb = Scrollbar(window)
sb.grid(row=2, column=2, rowspan=6)

list.configure(yscrollcommand=sb.set)
sb.configure(command=list.yview)

# ================================= button =============================
B_add = Button(window, text="Add", width=10, command=lambda: add_command())
B_add.grid(row=2, column=3)
B_view = Button(window, text="View All", width=10, command=lambda: view_command())
B_view.grid(row=3, column=3)
B_search = Button(window, text="Search", width=10, command=lambda: search_command())
B_search.grid(row=4, column=3)
B_update = Button(window, text="Update", width=10, command=lambda: update_command())
B_update.grid(row=5, column=3)
B_delete = Button(window, text="Delete", width=10, command=lambda: delete_command())
B_delete.grid(row=6, column=3)
B_close = Button(window, text="Close", width=10, command=lambda: window.destroy())
B_close.grid(row=7, column=3)

window.mainloop()
