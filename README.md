READ ME
 
 How to use?

 This Image Editor is project with pillow module and tkinter.The first step to use this project
 is to import your image using the import button,next you can see some simple options like 
 rotate,resize,crop.You should feed the angle of rotation in the rotate entry box,you can crop 
 the image with the width and height entry box ,you can also follow these steps to resize the 
 image.
	
 Explanation for the code
 
 Importing all the required module
 
 
 from tkinter import* - importing tkinter for  for the app window

 from PIL import Image - importing PIL for editing the image

 from tkinter import filedialog - importing filedialog to open the 
                                  image
 
 
 root=Tk() - configuring window

 root.title('Image Editor') - configuring title of the window

 root.geometry('300x100') - configuring geometry of the window

 root.config(bg="#F4E4F7") - configuring background color of the window

 root.iconbitmap('image editor.ico')configuring icon of the window
 
 def imp(): - creating a function

    imag=filedialog.askopenfilename(initialdir = "/",title = "Select 
                                    file",filetypes = (("jpeg files","*.jpg"),("all files","*.*"))) 
                      
                      -asking python to ask the image to be selected

    im = Image.open(imag) - opening the selected image

    im.show() - showing the opened image

    root.geometry("300x300") - exanding the window

 	def rotate(): - creating a function

        	im.rotate(int(entry1.get())).save('rotate.png') - rotating the 
                                                        image and saving it
        
        	im.rotate(int(entry1.get())).show() - showing the rotated image

 	def resize(): - creating a function 

        	img = Image.open(imag) - opening the selected image


        	new_width=int(entry2.get()) - feeding the new width through the 
                                      entry box

        	new_height=int(entry3.get()) - feeding the new height through the 
                                      entry box 

        	resizedimg = img.resize((new_width, new_height),
                           Image.ANTIALIAS).save('resize.png')
                           - resizeing the image

        	resizedimg = img.resize((new_width, new_height), Image.ANTIALIAS).show()
                           -showing the resized image
 
 	def crop(): - creating a function 

        	img = Image.open(imag) - opening the selected image

        	x1=0 - x axis of the crop box

        	y1=0 - y axis of the crop box

        	x	2=img.width-int(entry4.get())  - subracting x axis of the crop 
                                          box from the width of the image

        	y2=img.height-int(entry5.get())   - subracting y axis of the crop 
                                          box from the width of the image

        	crop=img.crop((x1,y1,x2,y2)).save('cropped.png') - saving cropped 
                                                           image

        	img.crop((x1,y1,x2,y2)).show() - showing cropped image

 	def convt():- creating a function 

        	img = Image.open(imag) - opening the selected image

        	bw_img=img.convert('L').save('bw_img.png') - converting selected 
                                                     image to black and white form
	
        	img.convert('L').show() - saving the converted image



    button1=Button(root,text="rotate",command=rotate,bg="#AAA0DF",fg="black")
    button1.place(x=10,y=70) - creating button and calling the functions


    button2=Button(root,text="resize",command=resize,bg="#AAA0DF",fg="black")
    button2.place(x=160,y=170)- creating button and calling the functions



    button3=Button(root,text="crop",command=crop,bg="#AAA0DF",fg="black")
    button3.place(x=10,y=240)- creating button and calling the functions



    button4=Button(root,text="convert",command=convt,bg="#AAA0DF",fg="black",width=15)
    button4.place(x=160,y=240)- creating button and calling the functions

    button=Button(root,text="import",bg='#AAA0DF',command=imp)
	button.place(x=125,y=0) - creating button and calling the functions


    lbl1=Label(root,text="Width",bg="#F4E4F7",fg="black")
    lbl1.place(x=160,y=40) - labels for diffing the entry box

    lbl2=Label(root,text="Height",bg="#F4E4F7",fg="black")
    lbl2.place(x=160,y=100) - labels for diffing the entry box


    lbl1=Label(root,text="Width",bg="#F4E4F7",fg="black")
    lbl1.place(x=10,y=110) - labels for diffing the entry box

    lbl2=Label(root,text="Height",bg="#F4E4F7",fg="black")
    lbl2.place(x=10,y=180) - labels for diffing the entry box

    lbl2=Label(root,text=" black and white ",bg="#F4E4F7",fg="black")
    lbl2.place(x=160,y=210) - labels for diffing the entry box


    entry1=Entry(root,text='45')
    entry1.place(x=10,y=40) - entry box for feeding the input

    entry2=Entry(root)
    entry2.place(x=160,y=70) - entry box for feeding the input


    entry3=Entry(root)
    entry3.place(x=160,y=130) - entry box for feeding the input



    entry4=Entry(root)
    entry4.place(x=10,y=140) - entry box for feeding the input


    entry5=Entry(root)
    entry5.place(x=10,y=210) - entry box for feeding the input

 root.mainloop() - loop

 Advantages and Disadvantages

 Advantages:

 		* It is a simple project for editingb the image with pillow and python.

 		* This project automatically saves the edited image.

 		* This is the first attempt to make a editting app compleately with python.

 Disadvantages:

 		* It saves the image in the default name only once.

 		* Multiple changes cannot be done


Developer contact: sriramvkumar007@gmail.com
