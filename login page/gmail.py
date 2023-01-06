import tkinter
import customtkinter
from PIL import Image,ImageTk
import time

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


def verify_page():
    global server
    global password
    global otp
    global name
    global msg
    global sender
    global receiver_email
    global receiver
    global password2
    try:
        page_2.pack(fill="both",expand=1)
        page_1.forget()
        import random
        import smtplib

        server=smtplib.SMTP('smtp.gmail.com',587)
        # Tls
        server.starttls()
        # gmail
        password='ucbtbksehxgawwrd'
        server.login('siddiquiadnan119@gmail.com',password)
        #OTP using random password function
        otp=''.join([str(random.randint(0,9)) for i in range(4)])
        name = entry_name.get()
        msg='Hello,Mr'+name+'. Your Verification Code is '+str(otp)
        sender='siddiquiadnan119@gmail.com'  #sender email 
        receiver_email=str(entry_email.get())
        receiver=receiver_email #receiver email

        server.sendmail(sender,receiver,msg)
        server.quit()

    except:
        SyntaxError
        if entry_name.get() == "":
            entry_name.configure(placeholder_text="Please enter your name",placeholder_text_color ="#FF5665")
            label_star_name.place(rely=0.40,relx=0.9)
        if entry_email.get() == "":
            entry_email.configure(placeholder_text="Please enter your email",placeholder_text_color ="#FF5665")
            label_star_email.place(rely=0.60,relx=0.9)

def try_again():
    page_1.pack(fill="both",expand=1)
    entry_1_var.set("")
    entry_2_var.set("")
    entry_3_var.set("")
    entry_4_var.set("")
    entry_1.focus()
    page_2.update()
    page_4.forget()
    
    
def verification():
    global server
    global password
    global otp
    global name
    global msg
    global sender
    global receiver_email
    global receiver
    global password2
    password2=str(entry_1.get())+str(entry_2.get())+str(entry_3.get())+str(entry_4.get())
    if password2==str(otp):
        page_2.forget()
        page_3.pack()
        page_3.place(anchor = tkinter.CENTER,rely=0.5,relx=0.5)
        print("login success")
    else:
        page_2.forget()
        page_4.pack(pady=100)
        # page_4.place(anchor = tkinter.CENTER,rely=0.5,relx=0.5)
        print("login failed")

root = customtkinter.CTk()
root.title("OTP Verification")
root.wm_iconbitmap("head1_ico.ico")
root.geometry("433x433")
root.resizable(False,False)
root.eval('tk::PlaceWindow . center')

page_1 = customtkinter.CTkFrame(master=root)

my_image = customtkinter.CTkImage(dark_image=Image.open("head1.png"),size=(70, 70))
label_image = customtkinter.CTkLabel(master=page_1,text="",image=my_image)
label_image.pack()
label_image.place(rely = 0.02,relx=0.45)


label_heading = customtkinter.CTkLabel(master= page_1,text="Sign Up",font=customtkinter.CTkFont("lucida",size=40,weight="bold"),text_color="#149BE6")
label_heading.pack()
label_heading.place(rely=0.2,relx=0.335)

# name = tkinter.StringVar()
# name.set("Enter your name")
entry_name = customtkinter.CTkEntry(master=page_1,placeholder_text="Enter Your Name",font=customtkinter.CTkFont(size=20,weight="bold"),width=340,height=50,corner_radius=15,justify = "center")
entry_name.pack()
entry_name.place(relx = 0.1,rely = 0.4)

entry_email = customtkinter.CTkEntry(master=page_1,placeholder_text="Enter Your Email Id",font=customtkinter.CTkFont(size=20,weight="bold"),width=340,height=50,corner_radius=15,justify = "center")
entry_email.pack()
entry_email.place(relx = 0.1,rely = 0.6)

label_star_email = customtkinter.CTkLabel(master= page_1,text="*",font=customtkinter.CTkFont("lucida",size=20,weight="bold"),text_color="#FF5665",fg_color="transparent",bg_color="transparent")
# label_star_email.pack()
# label_star_email.place(rely=0.60,relx=0.9)

label_star_name = customtkinter.CTkLabel(master= page_1,text="*",font=customtkinter.CTkFont("lucida",size=20,weight="bold"),text_color="#FF5665",fg_color="transparent",bg_color="transparent")
# label_star_name.pack()
# label_star_name.place(rely=0.40,relx=0.9)
#FF5665
b_continue = customtkinter.CTkButton(master=page_1,text="Continue",font=customtkinter.CTkFont(family="lucida",size=20,weight="bold"),height=40,corner_radius=15,command=verify_page)
b_continue.pack()
b_continue.place(anchor=tkinter.CENTER,relx=0.5,rely=0.84)

page_1.pack(fill="both",expand=1)

page_2 = customtkinter.CTkFrame(master=root)

my_image1 = customtkinter.CTkImage(dark_image=Image.open("strength0.png"),size=(70, 70))
label_image1 = customtkinter.CTkLabel(master=page_2,text="",image=my_image1)
label_image1.pack()
label_image1.place(rely = 0.02,relx=0.42)

label_message = customtkinter.CTkLabel(master= page_2,text="Verification Code",font=customtkinter.CTkFont("lucida",size=30,weight="bold"))
label_message.pack()
label_message.place(rely=0.2,relx=0.2)

label_message1 = customtkinter.CTkLabel(master= page_2,text="Please type the verification\ncode sent to your email:",font=customtkinter.CTkFont("lucida",size=20))
label_message1.pack()
label_message1.place(rely=0.3,relx=0.22)

entry_1_var = tkinter.StringVar()
entry_2_var = tkinter.StringVar()
entry_3_var = tkinter.StringVar()
entry_4_var = tkinter.StringVar()

entry_1 = customtkinter.CTkEntry(master=page_2,textvariable=entry_1_var,placeholder_text="",font=customtkinter.CTkFont(size=25,weight="bold"),width=50,height=50,corner_radius=15,justify = "center")
entry_1.pack()
entry_1.place(relx = 0.19,rely = 0.5)

entry_2 = customtkinter.CTkEntry(master=page_2,textvariable=entry_2_var,placeholder_text="",font=customtkinter.CTkFont(size=25,weight="bold"),width=50,height=50,corner_radius=15,justify = "center")
entry_2.pack()
entry_2.place(relx = 0.36,rely = 0.5)

entry_3 = customtkinter.CTkEntry(master=page_2,textvariable=entry_3_var,placeholder_text="",font=customtkinter.CTkFont(size=25,weight="bold"),width=50,height=50,corner_radius=15,justify = "center")
entry_3.pack()
entry_3.place(relx = 0.53,rely = 0.5)

entry_4 = customtkinter.CTkEntry(master=page_2,textvariable=entry_4_var,placeholder_text="",font=customtkinter.CTkFont(size=25,weight="bold"),width=50,height=50,corner_radius=15,justify = "center")
entry_4.pack()
entry_4.place(relx = 0.70,rely = 0.5)

b_verify = customtkinter.CTkButton(master=page_2,text="Verify now",font=customtkinter.CTkFont(family="lucida",size=20,weight="bold"),height=40,corner_radius=15,command=verification)
b_verify.pack()
b_verify.place(anchor=tkinter.CENTER,relx=0.5,rely=0.76)

password=''

otp=''
name=""
msg=""
sender=''  #sender email 
receiver_email=""

page_3 = customtkinter.CTkFrame(master=root,width=300,border_width=5)
my_image2 = customtkinter.CTkImage(dark_image=Image.open("tick-removebg-preview.png"),size=(40, 40))
label_image2 = customtkinter.CTkLabel(master=page_3,text="",image=my_image2)
label_image2.pack()
label_image2.place(rely = 0.09,relx=0.43)

label_message2 = customtkinter.CTkLabel(master= page_3,text="Your email has been verified.",font=customtkinter.CTkFont("lucida",size=17,weight="bold"))
label_message2.pack()
label_message2.place(rely=0.4,relx=0.1)

b_ok = customtkinter.CTkButton(master=page_3,hover_color="#146944",fg_color="#30A572",text="Ok",font=customtkinter.CTkFont(family="lucida",size=20,weight="bold"),height=40,corner_radius=15,command=quit)
b_ok.pack()
b_ok.place(anchor=tkinter.CENTER,relx=0.5,rely=0.84)

page_5 = customtkinter.CTkFrame(master=root)
page_4 = customtkinter.CTkFrame(master=root,width=300,border_width=5)
my_image3 = customtkinter.CTkImage(dark_image=Image.open("cross-removebg-preview.png"),size=(40, 40))
label_image3 = customtkinter.CTkLabel(master=page_4,text="",image=my_image3)
label_image3.pack()
label_image3.place(rely = 0.09,relx=0.43)

label_message3 = customtkinter.CTkLabel(master= page_4,text="Invalid Otp!",font=customtkinter.CTkFont("lucida",size=20,weight="bold"))
label_message3.pack()
label_message3.place(rely=0.4,relx=0.32)

b_try = customtkinter.CTkButton(master=page_4,hover_color="dark red",fg_color="red",text="Try again!",font=customtkinter.CTkFont(family="lucida",size=20,weight="bold"),height=40,corner_radius=15,command=try_again)
b_try.pack()
b_try.place(anchor=tkinter.CENTER,relx=0.5,rely=0.78)


root.mainloop()