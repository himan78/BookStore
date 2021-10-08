from tkinter import *

# ================================= settings =============================
window = Tk()
window.title("BookStore")
window.geometry("420x220")

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
E_title = Entry(window)
E_title.grid(row=0, column=1)
E_author = Entry(window)
E_author.grid(row=0, column=3)
E_year = Entry(window)
E_year.grid(row=1, column=1)
E_isbn = Entry(window)
E_isbn.grid(row=1, column=3)

# ================================= listbox =============================
list = Listbox(window,width=40 , height=8)
list.grid(row=2, column=0, rowspan=6, columnspan=2)

sb = Scrollbar(window)
sb.grid(row=2 , column=2 , rowspan=6)

list.configure(yscrollcommand=sb.set)
sb.configure(command=list.yview)

# ================================= button =============================
B_add = Button(window , text="Add" , width=10)
B_add.grid(row=2 , column=3)
B_view = Button(window , text="View All", width=10)
B_view.grid(row=3 , column=3)
B_search = Button(window , text="Search", width=10)
B_search.grid(row=4 , column=3)
B_update = Button(window , text="Update", width=10)
B_update.grid(row=5 , column=3)
B_delete = Button(window , text="Delete", width=10)
B_delete.grid(row=6 , column=3)
B_close = Button(window , text="Close", width=10)
B_close.grid(row=7 , column=3)


window.mainloop()
