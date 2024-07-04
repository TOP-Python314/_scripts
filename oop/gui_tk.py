from tkinter import Tk, Frame, Label, StringVar, Button


root = Tk()
root.title('Пример графического интерфейса')

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

mainframe = Frame(
    root,
    background='#24d'
)
mainframe.grid(
    row=0, column=0, 
    padx=20, pady=20,
    # ipadx=20, ipady=20,
    sticky='nswe'
)

mainframe.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=1)

lbl_text = StringVar(value='Hello World!')

lbl = Label(
    mainframe,
    textvariable=lbl_text,
    font=('Hack', 16),
    background='#2d2',
    width=30
)
lbl.grid(
    row=0, column=0,
    padx=20, pady=(20, 10),
    sticky='nswe'
)

Button(
    mainframe,
    text='НАЖМИ МЕНЯ!',
    font=('Courier New', 16),
    command=lambda: lbl_text.set('Реакция на кнопку')
).grid(
    row=1, column=0,
    padx=20, pady=(10, 20),
    sticky='sew'
)

root.mainloop()
