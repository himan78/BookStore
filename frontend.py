from tkinter import *

# ================================= settings =============================
window = Tk()
window.title("BookStore")
window.geometry("450x300")

# ================================= labels =============================
L_title = Label(window,text="Title")
L_title.grid(row=0 , column=0)
L_author = Label(window,text="Author")
L_author.grid(row=0 , column=2)
L_year = Label(window,text="Year")
L_year.grid(row=1 , column=0)
L_isbn = Label(window,text="Isbn")
L_isbn.grid(row=1 , column=2)

# ================================= Entries =============================
E_title = Entry(window)
E_title.grid(row=0 , column=1)
E_author= Entry(window)
E_author.grid(row=0 , column=3)
E_year= Entry(window)
E_year.grid(row=1 , column=1)
E_isbn= Entry(window)
E_isbn.grid(row=1 , column=3)



window.mainloop()