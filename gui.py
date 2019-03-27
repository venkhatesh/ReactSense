from tkinter import*
import cv2
import numpy as np
import pyrebase

#from PIL import Image,ImageTk
config = {
  "apiKey": "AIzaSyCN_J0v_7fcjqt0ffpzIDa38v2J10-Qs-M",
  "authDomain": "reactsense-de14d.firebaseapp.com",
  "databaseURL": "https://reactsense-de14d.firebaseio.com/",
  "storageBucket": "reactsense-de14d.appspot.com",
  "serviceAccount": "ReactSense.json"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
top= Tk()
top.title("REACTSENSE")
top.geometry("1300x1300")
title=Label(top,text="REACTSENSE")
title.config(font="Verdana 40 bold")
title.place(relx=0.5,rely=0.4,anchor=CENTER)

def play1():
	cap = cv2.VideoCapture('gems.mp4')
	while(cap.isOpened()):
	#Capture frame-by-frame
		data = {}
		for i in range(5):
			db.child("custid").child("vidid").child(i).update({"1":"Hello World"})
		ret, frame = cap.read()
		if ret==True:
			cv2.imshow('Frame',frame)
 
    	# Press Q on keyboard to  exit
			if cv2.waitKey(25) & 0xFF == ord('q'):
				break
 
  		# Break the loop
		else: 
			break
def play2():
	cap = cv2.VideoCapture('cadbury.mp4')
	while(cap.isOpened()):
	#Capture frame-by-frame
		ret, frame = cap.read()
		if ret==True:
			cv2.imshow('Frame',frame)
 
    	# Press Q on keyboard to  exit
			if cv2.waitKey(25) & 0xFF == ord('q'):
				break
 
  		# Break the loop
		else: 
			break
def play3():
	cap = cv2.VideoCapture('moto.mp4')
	while(cap.isOpened()):
	#Capture frame-by-frame
		ret, frame = cap.read()
		if ret==True:
			cv2.imshow('Frame',frame)
 
    	# Press Q on keyboard to  exit
			if cv2.waitKey(25) & 0xFF == ord('q'):
				break
 
  		# Break the loop
		else: 
			break
def play4():
	cap = cv2.VideoCapture('appleX.mp4')
	while(cap.isOpened()):
	#Capture frame-by-frame
		ret, frame = cap.read()
		if ret==True:
			cv2.imshow('Frame',frame)
 
    	# Press Q on keyboard to  exit
			if cv2.waitKey(25) & 0xFF == ord('q'):
				break
 
  		# Break the loop
		else: 
			break





def openLoginPage():
	top.destroy()
	loginpage = Tk()
	loginpage.title("REACTSENSE")
	loginpage.geometry("1300x1300")
	login_title=Label(loginpage,text="REACTSENSE")
	instruction=Label(loginpage,text="Please enter your credentials")
	instruction.config(font="Verdana 25")
	#instruction.grid(row=1,column=1,sticky=E)
	instruction.place(relx=0.5,rely=0.3,anchor=CENTER)
	user_id= Entry(loginpage, width=20)
	usernameLabel = Label(loginpage,text='Username')
	usernameLabel.config(font="Verdana 20",padx=2)
	#usernameLabel.grid(row=3,column = 5,sticky=W,pady=30)
	usernameLabel.pack()
	usernameLabel.place(relx=0.4,rely=0.4,anchor=CENTER)
	#user_id.grid(row=3,column = 4)
	user_id.pack()
	user_id.place(relx=0.5,rely=0.4,anchor=CENTER)
	#usernameLabel.pack(padx=10,pady=10,expand=True)
	#user_id.pack(padx=10,pady=10,expand=True)

	password= Entry(loginpage,width=20,show = '*')
	passwordLabel = Label(loginpage,text='password')
	passwordLabel.config(font="Verdana 20")
	passwordLabel.pack()
	passwordLabel.place(relx=0.4,rely=0.45,anchor=CENTER)
	#passwordLabel.grid(row=4,column=5,sticky=W)
	#password.grid(row=4,column=4)
	password.pack()
	password.place(relx=0.5,rely=0.45,anchor=CENTER)
	def callvideos():
		loginpage.destroy()
		videos()
	submit_btn=Button(loginpage,text="Submit",width = 20,height=4,command=callvideos)
	#submit_btn.grid(row=5,column=5,pady=10)
	submit_btn.pack()
	submit_btn.place(relx=0.5,rely=0.5,anchor=CENTER)
	loginpage.pack()


	


def videos():
		#loginpage.destroy()
		v = Tk()
		v.title("REACTSENSE")
		#image=Image.open('image.png')
		v.geometry("1300x1300")
		
		
		photo = PhotoImage(file = 'image.png',master = v)
		b1=Button(v,image=photo,command=play1)
		b1.config(width="250",height="200",padx=5,pady=5)
		#b1.grid(row=1,column=1)
		b1.pack()
		b1.place(relx=0.2,rely=0.3,anchor=W)
		b1_label=Label(v,text="Video 1")
		b1_label.config(font="Verdana 20",padx=5,pady=5)
		#b1_label.grid(row=2,column=1)
		b1_label.pack()
		b1_label.place(relx=0.3,rely=0.4,anchor=CENTER)
		b2=Button(v,image=photo,command=play2)
		b2.config(width="250",height="200",padx=5,pady=5)
		#b2.grid(row=1,column=2,padx=30)
		b2.pack()
		b2.place(relx=0.8,rely=0.3,anchor=E)
		b2_label=Label(v,text="Video 2")
		b2_label.config(font="Verdana 20",padx=2,pady=5)
		#b2_label.grid(row=2,column=2)
		b2_label.pack()
		b2_label.place(relx=0.7,rely=0.4,anchor=CENTER)
		b3=Button(v,image=photo,command=play3)
		b3.config(width="250",height="200",padx=5,pady=5)
		#b3.grid(row=3,column=1)
		b3.pack()
		b3.place(relx=0.2,rely=0.6,anchor=W)
		b3_label=Label(v,text="Video 3")
		b3_label.config(font="Verdana 20",padx=5,pady=5)
		#b3_label.grid(row=4,column=1)
		b3_label.pack()
		b3_label.place(relx=0.3,rely=0.7,anchor=CENTER)
		b4=Button(v,image=photo,command=play4)
		b4.config(width="250",height="200",padx=5,pady=5)
		#b4.grid(row=3,column=2,padx=30)
		b4.pack()
		b4.place(relx=0.8,rely=0.6,anchor=E)
		b4_label=Label(v,text="Video 4")
		b4_label.config(font="Verdana 20",padx=2,pady=5)
		#b4_label.grid(row=4,column=2)
		b4_label.pack()
		b4_label.place(relx=0.7,rely=0.7,anchor=CENTER)
		v.pack()

#title.grid(row = 1)	
login_btn = Button(top, text ="Login",command = openLoginPage)
login_btn.config( height ="5", width ="20",padx=2)
signup_btn=Button(top,text="Sign up")
signup_btn.config( height = "5", width = "20",padx=2)
login_btn.place(relx=0.3,rely=0.6,anchor=W)
signup_btn.place(relx=0.7,rely=0.6,anchor=E)
#login_btn.grid(row=2,column = 10,pady = 10,padx = (245,10))
#signup_btn.grid(row=2,column = 11)

top.mainloop()

