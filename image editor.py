#importing required module

from tkinter import*
from PIL import Image
from tkinter import filedialog

#configurating window

root=Tk()
root.title('Image Editor')
root.geometry('300x100')
root.config(bg="#F4E4F7")
root.iconbitmap('icon.ico')

#Defining functions for importing

def imp():
    imag=filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    im = Image.open(imag)
    im.show()
    root.geometry("300x300")
   
   
    def rotate():#Defining functions for rotating image
        im.rotate(int(entry1.get())).save('rotate.png')
        im.rotate(int(entry1.get())).show()

    def resize():#Defining functions for resizeing image
        img = Image.open(imag) # image extension *.png,*.jpg
        new_width=int(entry2.get()) 
        new_height=int(entry3.get())
        rimg = img.resize((new_width, new_height), Image.ANTIALIAS).save('resize.png')
        rimg = img.resize((new_width, new_height), Image.ANTIALIAS).show()
               
    def crop():#Defining functions for croping image
        img = Image.open(imag)
        x1=0
        y1=0
        x2=img.width-int(entry4.get())
        y2=img.height-int(entry5.get())
        crop=img.crop((x1,y1,x2,y2)).save('cropped.png')
        img.crop((x1,y1,x2,y2)).show()

    def convt():#Defining functions for converting image to black and white
        img = Image.open(imag)
        bw_img=img.convert('L').save('bw_img.png')
        img.convert('L').show()

    #buttons and calling functions

    button1=Button(root,text="rotate",command=rotate,bg="#AAA0DF",fg="black")
    button1.place(x=10,y=70)


    button2=Button(root,text="resize",command=resize,bg="#AAA0DF",fg="black")
    button2.place(x=160,y=170)

    button3=Button(root,text="crop",command=crop,bg="#AAA0DF",fg="black")
    button3.place(x=10,y=240)

    button4=Button(root,text="convert ",command=convt,bg="#AAA0DF",fg="black",width=15)
    button4.place(x=160,y=240)
#entry box for feeding input

    entry1=Entry(root,text='45')
    entry1.place(x=10,y=40)

    entry2=Entry(root)
    entry2.place(x=160,y=70)

    entry3=Entry(root)
    entry3.place(x=160,y=130)


    entry4=Entry(root)
    entry4.place(x=10,y=140)

    entry5=Entry(root)
    entry5.place(x=10,y=210)

#labels

    lbl1=Label(root,text="Width",bg="#F4E4F7",fg="black")
    lbl1.place(x=160,y=40)

    lbl2=Label(root,text="Height",bg="#F4E4F7",fg="black")
    lbl2.place(x=160,y=100)


    lbl1=Label(root,text="Width",bg="#F4E4F7",fg="black")
    lbl1.place(x=10,y=110)

    lbl2=Label(root,text="Height",bg="#F4E4F7",fg="black")
    lbl2.place(x=10,y=180)

    lbl2=Label(root,text=" black and white ",bg="#F4E4F7",fg="black")
    lbl2.place(x=160,y=210)




    

button=Button(root,text="import",bg='#AAA0DF',command=imp)
button.place(x=125,y=0)
#loop
root.mainloop()

#detailed explanation in read me file
#Developer contact : sriramvkumar007@gmail.com