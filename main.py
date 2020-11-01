from config import *
from tkinter import *


#INTERFATA GRAFICA:

def update(ind):

    frame = frames[ind]
    ind += 3
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    app.after(100, update, ind)


app = Tk()
app.title('Soft Squad - School Assistant')
app.geometry('800x600')
app.resizable(False, False)
app.configure(bg='#000000')
frameCnt = 60
frames = [PhotoImage(master = app, file='Sufletul.gif', format = 'gif -index %i' %(i)) for i in range(frameCnt)]

label = Label(app)
label.pack()
Button(master = app, text="Push to talk!", command = vorbit, width=10, height=1).place(x=350, y=550)
app.after(0, update, 0)



wishMe()
app.mainloop()