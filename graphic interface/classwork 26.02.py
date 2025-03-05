from msilib.schema import File
from tkinter import *
from turtle import color
from tkinter import filedialog
import smtplib, ssl
from email.message import *
import imghdr 



def choose_img():
    global file
    file=filedialog.askopenfilename()
    added.configure(text = file)
    added.configure(font=("Freestyle Script", 18))
    
    return file

def send():
    to=email.get()
    message_box=message.get()
    Topic=topic.get()


    smtp_server="smtp.gmail.com"
    port=587
    sender_email="ksenia.pleshakova2001@gmail.com"
    password="pqlx oudg gpzj gumq"
    context=ssl.create_default_context()
    msg=EmailMessage()
    msg.set_content(message_box)
    msg['Subject']=Topic
    msg['From']="aaa"
    msg['To']=to

    with open(file, 'rb') as fimage:
        image = fimage.read()
    msg.add_attachment(image, maintype='image', subtype=imghdr.what(None, image))
    try:
        server=smtplib.SMTP(smtp_server,port)
        server.starttls(context=context)
        server.login(sender_email,password)
        server.send_message(msg)
        message_box.showinfo("info", "sent")
    except:
        message_box.showerror("error")
    finally:
        server.quit()



root=Tk()
root.geometry("500x400")
root.resizable(False,False)
root.title("Email")


label1=Label(root, text = "EMAIL:", font=("Blackadder ITC", 20))
label1.place(x=0,y=0)

label2=Label(root, text = "TOPIC:", font=("Blackadder ITC", 20))
label2.place(x=0,y=50)

label3=Label(root, text = "ADD:", font=("Blackadder ITC", 20))
label3.place(x=0,y=100)

label4=Label(root, text = "MESSAGE:", font=("Blackadder ITC", 20))
label4.place(x=0,y=200)

button1=Button(root, text = "ADD IMAGE", font=("Blackadder ITC", 14), command=choose_img)
button1.place(x=250,y=350)

button2=Button(root, text = "SEND", font=("Blackadder ITC", 14), command=send)
button2.place(x=400,y=350)

email=Entry(root, font=("Freestyle Script", 25))
email.place(x=190, y =0, width= 300, height=50)

topic=Entry(root, font=("Freestyle Script", 25))
topic.place(x=190, y =50, width= 300, height=50)

added=Label(root, text="...", font=("Freestyle Script", 25))
added.place(x=190, y =110, width= 300, height=20)

message=Entry(root, font=("Freestyle Script", 25))
message.place(x=190, y =130, width= 300, height=200)

root.mainloop()
