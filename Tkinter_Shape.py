from tkinter import *
import time

root = Tk()
root.geometry("600x500")
root.title("Shape!")

def update(a):
    canvas.delete('all')
    a = canvas.create_rectangle(cordinates, width=2, fill='red')

def click_01():
    mylabel1.destroy()
    mylabel2.destroy()
    canvas.delete('all')
    cordinates[2] -= 10 
    a = canvas.create_rectangle(cordinates, width=2, fill='#3CB371')

def click_02():
    mylabel1.destroy()
    canvas.delete('all')
    cordinates[3] -= 10 
    a = canvas.create_rectangle(cordinates, width=2, fill='#3CB371')

def click_03():
    mylabel1.destroy()
    canvas.delete('all')
    cordinates[2] += 10 
    a = canvas.create_rectangle(cordinates, width=2, fill='#3CB371')

def click_04():
    mylabel1.destroy()
    canvas.delete('all')
    cordinates[3] += 10 
    a = canvas.create_rectangle(cordinates, width=2, fill='#3CB371')

def click_05(cordinates):
    Area = (cordinates[3]- cordinates[1]) * (cordinates[2]- cordinates[0])
    mylabel = Label(root, text="Area: " + str(Area) + " mm^2")
    mylabel.grid(row=0, column=1)
    print(Area)

def click_06(cordinates):
    Lenght2 = (cordinates[3]- cordinates[1])

    Lenght1 = (cordinates[2]- cordinates[0])
    mylabel = Label(root, text="Dim: " + str(Lenght1) + " x " + str(Lenght2) + " mm")
    mylabel.grid(row=0, column=3)
    print(Area)  


def click_07(Create):
   b = canvas.create_oval(cordinates, width=2, fill='white')


myButton1 = Button(root, text="Diminuisci Larghezza (x-) ", command=click_01, fg ="White", bg="#aaaaaa")
myButton1.grid(row=2, column=0, sticky="WE", padx =10, pady=2)

myButton2 = Button(root, text="Diminuisci Altezza (y-)", command=click_02, fg ="White", bg="#aaaaaa")
myButton2.grid(row=3, column=0, sticky="WE", padx =10)

myButton3 = Button(root, text="Aumenta Larghezza (x+)", command=click_03, fg ="White", bg="#aaaaaa")
myButton3.grid(row=2, column=1, sticky="WE", padx =10)

myButton4 = Button(root, text="Diminuisci Altezza (y+)", command=click_04, fg ="White", bg="#aaaaaa")
myButton4.grid(row=3, column=1, sticky="WE", padx =10)

myButton5 = Button(root, text="Area", command=lambda: click_05(cordinates))
myButton5.grid(row=0, column=0)

myButton6 = Button(root, text="Dimensioni", command=lambda: click_06(cordinates))
myButton6.grid(row=0, column=2)

myButton7 = Button(root, text="Crea Ovale", command=lambda: click_07(1), state=DISABLED)
myButton7.grid(row=3, column=3)


canvas = Canvas(width=500, height=400, bg='white')  
canvas.grid(row=1, column=0 , columnspan = 5)


cordinates = [10,10,290,290]
a = canvas.create_rectangle(cordinates, width=2, fill='#3CB371')


def Area():
    Area = (cordinates[3]- cordinates[1]) * (cordinates[2]- cordinates[0])
    mylabel = Label(root, text="Area:" + str(Area))


Area = (cordinates[3]- cordinates[1]) * (cordinates[2]- cordinates[0])


mylabel1 = Label(root, text="")
mylabel1.grid(row=0, column=3 , columnspan = 1)

mylabel2 = Label(root, text="")
mylabel2.grid(row=0, column=1 , columnspan = 1)


n = int(input("insert input"))

if n ==1:
    for n in range(10):
        print(n)
        update(a)
        time.sleep(0.2)

root.mainloop()