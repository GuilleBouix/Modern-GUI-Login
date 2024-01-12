from customtkinter import *
from tkinter import *
from PIL import Image, ImageTk
import os

# Colors
background_color = '#10181c'
entry_color = '#192028'
entry_focus_color = '#4272be'
button_color = '#256bfe'

root = Tk()
root.resizable(False,False)
root.title('Modern TK Login')
root.config(bg=background_color)

logo = Label(root,
             text='Login UI',
             font=('Montserrat Bold',30),
             bg=background_color,
             fg='white')
logo.grid(row=0,padx=200,pady=60)

# EMAIL
email_frame = CTkFrame(root,
                     width=300,
                     fg_color=entry_color,
                     corner_radius=20,
                     border_width=1,
                     border_color=background_color,
                     bg_color=background_color)
email_frame.grid(row=1)

txt_email = CTkEntry(email_frame,
                     width=300,
                     placeholder_text_color='gray',
                     placeholder_text='Enter your Email',
                     border_width=0,
                     bg_color=entry_color,
                     font=('Montserrat',16),
                     fg_color=('white',entry_color))
txt_email.grid(padx=10,pady=20)

# PASSWORD
password_frame = CTkFrame(root,
                     width=300,
                     fg_color=entry_color,
                     corner_radius=20,
                     border_width=1,
                     border_color=background_color,
                     bg_color=background_color)
password_frame.grid(row=2,pady=10)
txt_password = CTkEntry(password_frame,
                     width=300,
                     placeholder_text_color='gray',
                     placeholder_text='Enter your Password',
                     show='•',
                     border_width=0,
                     bg_color=entry_color,
                     font=('Montserrat',16),
                     fg_color=('white',entry_color))
txt_password.grid(padx=10,pady=20)

# FORGOT PASSWORD
btn_forgot_password = Button(root,
                             border=0,
                             relief='flat',
                             bg=background_color,
                             fg='#236cfe',
                             text='Forgot Password?',
                             font=('Montserrat Medium',10),
                             cursor='hand2',
                             activebackground=background_color,
                             activeforeground='white')
btn_forgot_password.grid(row=3)

# LOGIN
btn_login = CTkButton(root,
                     width=300,
                     height=60,
                     corner_radius=20,
                     text='LOGIN',
                     border_width=0,
                     bg_color=background_color,
                     font=('Montserrat Medium',20),
                     fg_color=('white',button_color),
                     hover_color=('black','#257cfe'),
                     cursor='hand2')
btn_login.grid(row=4,pady=10)

# CEATE ACCOUNT
signup_frame = Frame(root,
                    bg=background_color)
signup_frame.grid(row=5)
lbl_signup = Label(signup_frame,
                    border=0,
                    relief='flat',
                    bg=background_color,
                    fg='gray',
                    text='Dont have an account?',
                    font=('Montserrat Medium',10))
lbl_signup.grid(row=0,column=0)
btn_signup = Button(signup_frame,
                    border=0,
                    relief='flat',
                    bg=background_color,
                    fg='#236cfe',
                    text='Sign Up',
                    font=('Montserrat Medium',10),
                    cursor='hand2',
                    activebackground=background_color,
                    activeforeground='white')
btn_signup.grid(row=0,column=1)

# FACEBOOK/GOOGLE
facebook_google_frame = Frame(root,
                              bg=background_color)
facebook_google_frame.grid(row=6,pady=20)

lbl_or = Label(facebook_google_frame,
                border=0,
                relief='flat',
                bg=background_color,
                fg='gray',
                text='OR',
                font=('Montserrat Medium',10))
lbl_or.grid(row=0,columnspan=2,pady=10,sticky=NSEW)

# FACEBOOK
file_path = os.path.dirname(os.path.realpath(__file__))
facebook_logo = CTkImage(Image.open(file_path + 
                                    '/assets/facebook.png'),size=(20,20))

btn_facebook = CTkButton(facebook_google_frame,
                        image=facebook_logo,
                        width=200,
                        height=50,
                        corner_radius=8,
                        text='Facebook',
                        border_width=0,
                        bg_color=background_color,
                        font=('Montserrat',16),
                        fg_color=('white',entry_color),
                        hover_color='#232c37',
                        cursor='hand2')
btn_facebook.grid(row=1,column=0,padx=3)

# GOOGLE
file_path = os.path.dirname(os.path.realpath(__file__))
google_logo = CTkImage(Image.open(file_path + 
                                    '/assets/google.png'),size=(20,20))
btn_google = CTkButton(facebook_google_frame,
                        image=google_logo,
                        width=200,
                        height=50,
                        corner_radius=8,
                        text='Google',
                        border_width=0,
                        bg_color=background_color,
                        font=('Montserrat',16),
                        fg_color=('white',entry_color),
                        hover_color='#232c37',
                        cursor='hand2')
btn_google.grid(row=1,column=1,padx=3)

# EMAIL FUNCTIONS
def active_email_border(event):
    email_frame.configure(border_color=entry_focus_color)

def restore_email_border(event):
    email_frame.configure(border_color=background_color)

txt_email.bind('<FocusIn>', active_email_border)
txt_email.bind('<FocusOut>', restore_email_border)

# PASSWORD FUNCTIONS
def active_password_border(event):
    password_frame.configure(border_color=entry_focus_color)

def restore_password_border(event):
    password_frame.configure(border_color=background_color)

txt_password.bind('<FocusIn>', active_password_border)
txt_password.bind('<FocusOut>', restore_password_border)

# LOST FOCUS FUNCTION
def lost_focus(Event):
    if(Event.widget == root):
        root.focus()

root.bind("<Button-1>", lost_focus)

# CENTER WINDOW
root.update_idletasks()
width = root.winfo_reqwidth()
height = root.winfo_reqheight()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - width) // 2
y = (screen_height - height) // 2

root.geometry(f'{width}x{height}+{x}+{y-30}')

# MAINLOOP
root.mainloop()