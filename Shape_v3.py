from tkinter import *

# Size of Main Window
window_width = 1100
window_height = 800

# Create Main Window
root = Tk()
root.geometry(str(window_width) + "x" + str(window_height))
root.title("Shape!")
# root.configure(bg="white")

# Size of Canvas
Canvas_width = 1000
Canvas_height = 600
Center_Canvas = [Canvas_width/2,Canvas_height/2]

# Create Canvas
canvas = Canvas(width=Canvas_width, height= Canvas_height, bg='gray')  
canvas.grid(row=1, column=0 , columnspan = 5, padx=5)

# Delete = 0 Rectangle= 1  Oval=2
Figure = 0
r = IntVar()
r.set("0")

# Calcolo dell'area e delle dimensioni (funzione)
def Area_Dim(cordinates,figure):
    Lenght2 = (cordinates[3]- cordinates[1])
    Lenght1 = (cordinates[2]- cordinates[0])

    if Figure == 0:
        Area = (cordinates[3]- cordinates[1]) * (cordinates[2]- cordinates[0])
    elif Figure == 1:
        Area = 3.14 * (cordinates[3]- cordinates[1])/2 * (cordinates[2]- cordinates[0])/2

    area="Dimensioni: " + str(Lenght1) + " x " + str(Lenght2) + " mm"
    dim ="Area: " + str(Area) + " mm^2"
    print(Area)   
    return [area,dim]


# Aumento delle dimensioni lungo x
def click_01():
    global mylabel1
    global mylabel2
    global Size_x
    global Size_y
    global r
    global canvas

    canvas.delete("figure")
    canvas.delete("figure")
    Size_x -= 5

    cordinates = [Center_Canvas[0]-Size_x,Center_Canvas[1]-Size_y,Center_Canvas[0]+Size_x,Center_Canvas[1]+Size_y]
    if Figure == 0:
        a = canvas.create_rectangle(cordinates, width=2, fill='#3CB371', tags="figure")
    elif Figure == 1:
        a = canvas.create_oval(cordinates, width=2, fill='#3CB371', tags="figure")

    mylabel1.destroy()
    mylabel2.destroy()
    
    Dimension = Area_Dim(cordinates,Figure)

    mylabel1 = Label(root, text= Dimension[0])
    mylabel1.grid(row=0, column=0,sticky=W)
    mylabel2 = Label(root, text= Dimension[1])
    mylabel2.grid(row=0, column=1,sticky=W)

    canvas.tag_raise("vertical")
    canvas.tag_raise("horizontal")


# Aumento delle dimensioni lungo x
def click_02():
    global mylabel1
    global mylabel2
    global Size_x
    global Size_y
    global Figure
    global canvas
    canvas.delete("figure")
    canvas.delete("figure")
    Size_x += 5
    cordinates = [Center_Canvas[0]-Size_x,Center_Canvas[1]-Size_y,Center_Canvas[0]+Size_x,Center_Canvas[1]+Size_y]
    if Figure == 0:
        a = canvas.create_rectangle(cordinates, width=2, fill='#3CB371', tags="figure")
    elif Figure == 1:
        a = canvas.create_oval(cordinates, width=2, fill='#3CB371',tags="figure")

    mylabel1.destroy()
    mylabel2.destroy()
    
    Dimension = Area_Dim(cordinates,Figure)

    mylabel1 = Label(root, text= Dimension[0])
    mylabel1.grid(row=0, column=0,sticky=W)
    mylabel2 = Label(root, text= Dimension[1])
    mylabel2.grid(row=0, column=1,sticky=W)
    canvas.tag_raise("vertical")
    canvas.tag_raise("horizontal")

def click_03():
    global mylabel1
    global mylabel2
    global Size_x
    global Size_y
    global Figure
    global canvas
    canvas.delete("figure")
    canvas.delete("figure")
    Size_y -= 5
    cordinates = [Center_Canvas[0]-Size_x,Center_Canvas[1]-Size_y,Center_Canvas[0]+Size_x,Center_Canvas[1]+Size_y]
    
    if Figure == 0:
        a = canvas.create_rectangle(cordinates, width=2, fill='#3CB371', tags="figure")
    elif Figure == 1:
        a = canvas.create_oval(cordinates, width=2, fill='#3CB371', tags="figure")

    mylabel1.destroy()
    mylabel2.destroy()
    
    Dimension = Area_Dim(cordinates,Figure)

    mylabel1 = Label(root, text= Dimension[0])
    mylabel1.grid(row=0, column=0,sticky=W)
    mylabel2 = Label(root, text= Dimension[1])
    mylabel2.grid(row=0, column=1,sticky=W)
    canvas.tag_raise("vertical")
    canvas.tag_raise("horizontal")

def click_04():
    global mylabel1
    global mylabel2
    global Size_x
    global Size_y
    global Figure
    global canvas
    canvas.delete("figure")
    canvas.delete("figure")
    Size_y += 5
    cordinates = [Center_Canvas[0]-Size_x,Center_Canvas[1]-Size_y,Center_Canvas[0]+Size_x,Center_Canvas[1]+Size_y]

    if Figure == 0:
        a = canvas.create_rectangle(cordinates, width=2, fill='#3CB371', tags="figure")
    elif Figure == 1:
        a = canvas.create_oval(cordinates, width=2, fill='#3CB371', tags="figure")

    mylabel1.destroy()
    mylabel2.destroy()
    
    Dimension = Area_Dim(cordinates,Figure)

    mylabel1 = Label(root, text= Dimension[0])
    mylabel1.grid(row=0, column=0,sticky=W)
    mylabel2 = Label(root, text= Dimension[1])
    mylabel2.grid(row=0, column=1,sticky=W)
    
    canvas.tag_raise("vertical")
    canvas.tag_raise("horizontal")



myButton1 = Button(root, text="Diminuisci Larghezza (x-) ", command=click_01, fg ="White", bg="#aaaaaa")
myButton1.grid(row=3, column=0, sticky="WE", padx =10, pady=2)

myButton3 = Button(root, text="Aumenta Larghezza (x+)", command=click_02, fg ="White", bg="#aaaaaa")
myButton3.grid(row=3, column=1, sticky="WE", padx =10)

myButton3 = Button(root, text="Diminuisci Altezza (y-)", command=click_03, fg ="White", bg="#aaaaaa")
myButton3.grid(row=4, column=0, sticky="WE", padx =10)

myButton4 = Button(root, text="Diminuisci Altezza (y+)", command=click_04, fg ="White", bg="#aaaaaa")
myButton4.grid(row=4, column=1, sticky="WE", padx =10)

def clicked1(value):
    global Figure
    global mylabel1
    global mylabel2
    global Size_x
    global Size_y
    global canvas
    myLabel = Label(root,text=value)
    myLabel.grid(row=2, column=3)
    canvas.delete("figure")
    canvas.delete("figure")

    mylabel1.destroy()
    mylabel2.destroy()

    mylabel1 = Label(root, text="Dimensioni: 100x100 mm")
    mylabel1.grid(row=0, column=0 , columnspan = 1,sticky=W)
    mylabel2 = Label(root, text="Area:")
    mylabel2.grid(row=0, column=1 , columnspan = 1,sticky=W)
    Figure = 0
    Size_x = 50
    Size_y = 50
    cordinates = [Center_Canvas[0]-Size_x,Center_Canvas[1]-Size_y,Center_Canvas[0]+Size_x,Center_Canvas[1]+Size_y]
    a = canvas.create_rectangle(cordinates, width=2, fill='#3CB371', tags="figure")
    canvas.tag_raise("vertical")
    canvas.tag_raise("horizontal")
    horizontal.set(50)
    vertical.set(50)

def clicked2(value):
    global Figure
    global mylabel1
    global mylabel2
    global Size_x
    global Size_y
    global canvas

    myLabel = Label(root,text=value)
    myLabel.grid(row=2, column=3)
    canvas.delete("figure")
    canvas.delete("figure")

    mylabel1.destroy()
    mylabel2.destroy()
    mylabel1 = Label(root, text="Dimensioni: 100x100 mm")
    mylabel1.grid(row=0, column=0 , columnspan = 1,sticky=W)
    mylabel2 = Label(root, text="Area:")
    mylabel2.grid(row=0, column=1 , columnspan = 1,sticky=W)
    Figure = 1
    Size_x = 50
    Size_y = 50
    cordinates = [Center_Canvas[0]-Size_x,Center_Canvas[1]-Size_y,Center_Canvas[0]+Size_x,Center_Canvas[1]+Size_y]
    b = canvas.create_oval(cordinates, width=2, fill='#3CB371', tags="figure")
    canvas.tag_raise("vertical")
    canvas.tag_raise("horizontal")
    horizontal.set(50)
    vertical.set(50)


def clicked3(value):
    global canvas
    horizontal.set(50)
    vertical.set(50)
    canvas.delete("figure")


Radiobutton(root, text="Create Rettancle", variable=r, value=1, command=lambda: clicked1(r.get())).grid(row=2, column=0,sticky=W)
Radiobutton(root, text="Create Oval", variable=r, value=2, command=lambda: clicked2(r.get())).grid(row=2, column=1,sticky=W)
Radiobutton(root, text="Delete Figure", variable=r, value=0, command=lambda: clicked3(r.get())).grid(row=2, column=2,sticky=W)


mylabel1 = Label(root, text="Dimensioni")
mylabel1.grid(row=0, column=0 , columnspan = 1,sticky=W)

mylabel2 = Label(root, text="Area")
mylabel2.grid(row=0, column=1 , columnspan = 1,sticky=W)

def slide(event):
    global mylabel1
    global mylabel2
    global Size_x
    global Size_y
    global r
    global canvas

    canvas.delete("figure")
    canvas.delete("figure")
    Size_x = horizontal.get()
    Size_y = vertical.get()

    cordinates = [Center_Canvas[0]-Size_x,Center_Canvas[1]-Size_y,Center_Canvas[0]+Size_x,Center_Canvas[1]+Size_y]
    if r.get() == 1:
        a = canvas.create_rectangle(cordinates, width=2, fill='#3CB371', tags="figure")
    elif r.get() == 2:
        a = canvas.create_oval(cordinates, width=2, fill='#3CB371', tags="figure")

    canvas.tag_raise("vertical")
    canvas.tag_raise("horizontal")
    return

horizontal  = Scale(root,from_=1, to=300, orient=HORIZONTAL, command=slide)
horizontal.set(50)
horizontal.grid(row=2,column=4, columnspan=1, padx=10, sticky=W+E)

vertical  = Scale(root,from_=300, to=1, orient=VERTICAL, command=slide)
vertical.grid(row=1,column=6, columnspan=1 , padx=10, sticky=W+E)
vertical.set(50)


# SET Il Valore della griglia
g = IntVar()
g.set("1")



def grid(value):
    global Canvas_width
    global Canvas_height
    print(value)
    if value==1:
       canvas.delete("vertical") 
       canvas.delete("horizontal") 
    if value==2 or value==4:
        vertical_seg = Canvas_width/100
        for n in range(int(vertical_seg)):
            canvas.create_line(n*100,0,n*100,Canvas_height, tags="vertical")
            print(n)
    if value==3 or value==4:
        horizontal_seg = Canvas_width/100
        for n in range(int(horizontal_seg)):
            canvas.create_line(0,n*100,Canvas_width,n*100,tags="horizontal")
            print(n)
    
    if value == 2:
        canvas.delete("horizontal") 
    if value == 3:
        canvas.delete("vertical") 

  
Grid_01 = Radiobutton(root, text="No Grid", variable=g, value=1, command=lambda: grid(g.get())).grid(row=3,column=3, columnspan=1,sticky=W)
Grid_02 = Radiobutton(root, text="Vertical Grid", variable=g, value=2, command=lambda: grid(g.get())).grid(row=4,column=3, columnspan=1,sticky=W)
Grid_03 = Radiobutton(root, text="Horizontal Grid", variable=g, value=3, command=lambda: grid(g.get())).grid(row=3,column=4, columnspan=1,sticky=W)
Grid_03 = Radiobutton(root, text="Grid", variable=g, value=4, command=lambda: grid(g.get())).grid(row=4,column=4, columnspan=1,sticky=W)


root.mainloop()