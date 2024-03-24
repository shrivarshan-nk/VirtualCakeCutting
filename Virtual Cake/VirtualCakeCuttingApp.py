import tkinter
from PIL import ImageTk,Image
from pygame import mixer

mixer.init()

root2=tkinter.Tk()
root2.title("GetName")
root2.geometry("1400x900")
canva=tkinter.Canvas(root2,width=900,height=800)
canva.pack()

Bg=Image.open("images/Bg.jpg")
bgr=Bg.resize((798,860),Image.ANTIALIAS)
Bgr=ImageTk.PhotoImage(bgr)
canva.create_image(450,350,image=Bgr)


Input=tkinter.Entry(root2,width=20,font=("Helvetica","14"))
Input.place(x=600,y=440)
Input.get()

label=tkinter.Label(root2,text="Created By:",font=("Helvetica","20","bold","italic")).place(x=0,y=540)

Canvas11=tkinter.Canvas(root2,width=200,height=400)
Canvas11.place(x=0,y=580)

creditf=Image.open("images/creditn.jpg")
creditr=creditf.resize((180,45),Image.ANTIALIAS)
credit=ImageTk.PhotoImage(creditr)
Canvas11.create_image(90,30,image=credit)

a=""
def click():
    global a
    a=Input.get()
    root2.destroy()
    
bott=tkinter.Button(root2,text="Go",command=click)  
bott.place(x=675,y=470)  
root2.mainloop()
if a!="":
    root=tkinter.Tk()
    root.title("Virtual Cake")
    root.geometry("1400x900")
    w=800
    h=800
    
    img = 'images/CakeFull.jpg'
    imgr=Image.open('images/Knife.jpg') 
    resize=imgr.resize((180,30),Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(file=img)
    
    
    
    
    bgr=Image.open('images/BackGround.jpg') 
    resr=bgr.resize((800,750),Image.ANTIALIAS)
    
    img2=ImageTk.PhotoImage(resize)
    
    can=tkinter.Canvas(root,width=w,height=h,bg="white")
    
    can.pack()
    Canvas1=tkinter.Canvas(root,width=200,height=400)
    Canvas1.place(x=0,y=580)
    
    creditf=Image.open("images/creditn.jpg")
    creditr=creditf.resize((180,45),Image.ANTIALIAS)
    credit=ImageTk.PhotoImage(creditr)
    Canvas1.create_image(90,30,image=credit)
    label=tkinter.Label(root,text="Created By:",font=("Helvetica","20","bold","italic")).place(x=0,y=540)
    can.create_image(400,550,image=img1)
    knife=can.create_image(500,400,image=img2)
    if len(a)<=5:
        name1=tkinter.Label(root,text=a,font=("Helvetica","18"),bg="white").place(x=640,y=500)
    elif len(a)>7:
        name1=tkinter.Label(root,text=a,font=("Helvetica","12"),bg="white").place(x=640,y=500)
    else:
        name1=tkinter.Label(root,text=a,font=("Helvetica","14"),bg="white").place(x=640,y=500)
    
    xcor=500
    ycor=400
    xcor1=515
    ycor1=555
    
    img3=ImageTk.PhotoImage(file='images/CakeCut.jpg')
    
    img4=ImageTk.PhotoImage(file='images/Slice.jpg')
    
    bg=ImageTk.PhotoImage(resr)
    name=tkinter.Label(root,text=a,font=("Helvetica","24"),bg="black")
    
    #Functions
    
    def msgbox():
        msg=tkinter.messagebox.askquestion("Exit App","Are You Sure You Want to Quit")
        if msg=="yes":
            mixer.music.stop()
            root.destroy()
        else:
            pass
        
    def move(e):
        global img2,xcor,ycor,img1,img3,img4 ,bg,xcor1,ycor1,name
       
        x1=int(xcor)-90
        x2=int(xcor)+90
        y1=int(ycor)-10
        y2=int(ycor)+10
     
        if e.x in range(x1,x2)and e.y in range (y1,y2):
            img2 = ImageTk.PhotoImage(resize)
            can.create_image(e.x,e.y,image=img2)
            xcor=e.x
            ycor=e.y
          
        if xcor in range(510,520)and ycor in range(430,670):
            img1= ImageTk.PhotoImage(file=img )
            can.create_image(9000,1,image=img1)
            
            bg=ImageTk.PhotoImage(resr)
            can.create_image(400,300,image=bg)
            
            img3=ImageTk.PhotoImage(file='images/CakeCut.jpg')
            can.create_image(400,550,image=img3)
            
            img2 = ImageTk.PhotoImage(resize)
            can.create_image(e.x,e.y,image=img2)        
            
            img4=ImageTk.PhotoImage(file='images/Slice.jpg')
            can.create_image(515,555,image=img4)
          
            name=tkinter.Label(root,text=a,fg="white",font=("Helvetica","30","italic"),bg="black").place(x=650,y=370)
           
            mixer.music.load("Music/Birthday.mp3")
            mixer.music.play(-1)
        
            x11=int(xcor1)-40
            x12=int(xcor1)+40
            y11=int(ycor1)-15
            y12=int(ycor1)+15   
            
            if e.x in range(x11,x12)and e.y in range(y11,y12):
                img4=ImageTk.PhotoImage(file='images/Slice.jpg')
                can.create_image(e.x,e.y,image=img4)
                xcor1=e.x
                ycor1=e.y
                x11=int(xcor1)-40
                x12=int(xcor1)+40
                y11=int(ycor1)-15
                y12=int(ycor1)+15 
    
     
    root.bind('<B1-Motion>',move)
    
    
    button_quit=tkinter.Button(root, text="Exit Program", command=msgbox).place(x=1000,y=0)
    
    root.mainloop()
