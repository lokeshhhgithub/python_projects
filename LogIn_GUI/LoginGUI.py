
from tkinter import Tk , Label, Entry, Button, messagebox
from PIL import ImageTk, Image


def handle_login():
    email = email_input.get()
    password = pass_input.get()

    if email == 'lokeshdhakal2000@gmail.com' or email == '9813130809' and password == '1234':
        messagebox.showinfo('Congrats', 'Login Successful')
    else:
        messagebox.showerror('Error', 'Login Failed')



root = Tk()
root.title('facebook')
root.geometry('400x400')
root.minsize(400,400)
root.config(background= 'blue')

logo = Image.open('logo2.png')
resized_img = logo.resize((70,70))

img = ImageTk.PhotoImage(resized_img)
img_label = Label(root , image = img, fg = 'blue', bg = 'blue')
img_label.pack(pady =(2,3))

text_label = Label(root, text = 'Welcome to Facebook', fg = 'white', bg = 'blue')
text_label.pack(pady=(3,5))
text_label.config(font = ('Times new Roman', 24, 'bold'))

email_label = Label(root, text = 'Enter your Email ', fg = 'white', bg = 'Blue')
email_label.pack(pady = (20,5))
email_label.config(font = ('Times new Roman', 12))

email_input = Entry(root, width= 50) 
email_input.pack(ipady= 5, pady= (1 ,15))


pass_label = Label(root, text = 'Enter your Password ', fg = 'white', bg = 'Blue')
pass_label.pack(pady = (20,5))
pass_label.config(font = ('Times new Roman', 12))

pass_input = Entry(root, width= 50) 
pass_input.pack(ipady= 5, pady= (1 ,15))


login_btn = Button(root, text = 'Log In', fg = 'white', bg = 'blue' , command = handle_login)
login_btn.pack(pady = (10,20))
login_btn.config(font = ('Times new Roman', 10))

root.mainloop()


