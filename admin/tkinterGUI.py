import tkinter as tk 
from tkinter import * 
import tkinter.font as font


def comman():
    pass 


root = tk.Tk()
root.geometry("500x500")

bg = PhotoImage(file='Images/camera.png')
label1 = Label( root, image = bg)
label1.place(x = 0 ,y = 0 ) 



# this removes the maximize button
root.resizable(0, 0)
root_height = 600
root_width = 1000

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width / 2) - (root_width / 2))
y_cordinate = int((screen_height / 2) - (root_height / 2))

root.geometry("{}x{}+{}+{}".format(root_width, root_height, x_cordinate, y_cordinate))
root.configure(background='#000000')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

header = tk.Label(root, text="Monitoring Registration", width=80, height=2, fg="white", bg="#FF5733",
                          font=('times', 18 , 'bold', 'underline'))
header.place(x=0 , y=0)

# client ID section 
clientID = tk.Label(root, text="Client ID", width=10, height=2, fg="white", bg="#0000FF", font=('times', 15))
clientID.place(x=80, y=80)

displayVariable = StringVar()
clientIDTxt = tk.Entry(root, width=20, text=displayVariable, bg="#00FFFF", fg="black",
                        font=('times', 15, 'bold'))
clientIDTxt.place(x=205, y=80)

# emp id section 

empID = tk.Label(root, text="EmpID", width=10, fg="white", bg="#0000FF", height=2, font=('times', 15))
empID.place(x=450, y=80)


empIDTxt = tk.Entry(root, width=20, bg="white", fg="black", font=('times', 15, ' bold '))
empIDTxt.place(x=575, y=80)

#emp name section 
empName = tk.Label(root, text="Emp Name", width=10, fg="white", bg="#0000FF", height=2, font=('times', 15))
empName.place(x=80, y=140)

empNameTxt = tk.Entry(root, width=20, bg="white", fg="black", font=('times', 15, ' bold '))
empNameTxt.place(x=205, y=140)

# emp email id section 
emailId = tk.Label(root, text="Email ID :", width=10, fg="white", bg="#0000FF", height=2, font=('times', 15))
emailId.place(x=450, y=140)

emailIDTxt = tk.Entry(root, width=20, bg="#FFA07A", fg="black", font=('times', 15, ' bold '))
emailIDTxt.place(x=575, y=140)


# emp contact number section 
mobileNo = tk.Label(root, text="Mobile No :", width=10, fg="white", bg="#0000FF", height=2,
                    font=('times', 15))
mobileNo.place(x=450, y=140)

mobileNoTxt = tk.Entry(root, width=20, bg="white", fg="black", font=('times', 15, ' bold '))
mobileNoTxt.place(x=575, y=140)

# Notification section 
lbl3 = tk.Label(root, text="Notification : ", width=15, fg="white", bg="#0000FF", height=2,
                font=('times', 15))
message = tk.Label(root, text="", bg="#CCCCFF", fg="black", width=30, height=1,
                      activebackground="#e47911", font=('times', 15))
message.place(x=220, y=220)
lbl3.place(x=80, y=260)

message = tk.Label(root, text="", bg="#0000FF", fg="black", width=58, height=2, activebackground="#bbc7d4",
                    font=('times', 15))
message.place(x=205, y=260)

# Image taken section 
takeImg = tk.Button(root, text="Take Images", command=comman(), fg="white", bg="#363e75", width=15,
                    height=2,
                    activebackground="#118ce1", font=('times', 15, ' bold '))
takeImg.place(x=80, y=350)


trainImg = tk.Button(root, text="Train Images", command=comman(), fg="white", bg="#363e75", width=15,
                        height=2,
                        activebackground="#118ce1", font=('times', 15, ' bold '))
trainImg.place(x=350, y=350)

predictImg = tk.Button(root, text="Predict", command=comman(), fg="white", bg="#363e75",
                        width=15,
                        height=2,
                        activebackground="#118ce1", font=('times', 15, ' bold '))
predictImg.place(x=600, y=350)

quitWindow = tk.Button(root, text="Quit", command=comman(), fg="white", bg="#FF0000", width=10, height=2,
                        activebackground="#118ce1", font=('times', 15, 'bold'))
quitWindow.place(x=650, y=510)

link2 = tk.Label(root, text="Copyright©2020,Shubham", fg="#FF0000" )
link2.place(x=690, y=580)
link2.bind("<Button-1>", lambda e : callback("shubhamchau7@gmail.comS"))
label = tk.Label(root)





root.mainloop()



