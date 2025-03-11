from msilib.schema import File
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import smtplib, ssl
from email.message import EmailMessage
import imghdr

files = []

def krysa():
    for i in range(1, 1000000, 1):
        message.insert(END, "🐀")

def choose_img():
    global files
    files = filedialog.askopenfilenames(title="Выберите файлы")
    added.configure(text=str(files))
    added.configure(font=("Freestyle Script", 18))

def send():
    toList = email.get().split(", ")
    message_box = message.get("1.0", END)
    Topic = topic.get()

    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "ksenia.pleshakova2001@gmail.com"
    password = "pqlx oudg gpzj gumq"
    context = ssl.create_default_context()
    msg = EmailMessage()
    msg.set_content(message_box)
    msg['Subject'] = Topic
    msg['From'] = sender_email
    msg['To'] = ", ".join(toList)

    for file in files:
        with open(file, 'rb') as fimage:
            image = fimage.read()
        msg.add_attachment(image, maintype='image', subtype=imghdr.what(None, image))

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email, password)
        server.send_message(msg)
        messagebox.showinfo("info", "sent")
    except:
        messagebox.showerror("error")
    finally:
        server.quit()

def clear():
    message.delete("1.0", END)
    files.clear()
    added.configure(text="...") 
    email.delete(0, END)
    topic.delete(0, END)

def add_signature():
    message.insert(END, "\n\nK.P.\nTARgv24")

def preview():
    To = email.get().strip().split()
    Topic = topic.get()
    Message = message.get("1.0", END).strip()
    preview = f"Email: {''.join(To)}\n\nTopic: {''.join(Topic)}\n\nMessage: {''.join(Message)}\n\nAttached files: {''.join(files)}"
    messagebox.showinfo("Preview", preview)

root = Tk()
root.geometry("500x600")
root.resizable(False, False)
root.title("Email")

label1 = Label(root, text="EMAIL:", font=("Blackadder ITC", 20))
label1.place(x=0, y=0)

label2 = Label(root, text="TOPIC:", font=("Blackadder ITC", 20))
label2.place(x=0, y=50)

label3 = Label(root, text="ADD:", font=("Blackadder ITC", 20))
label3.place(x=0, y=100)

label4 = Label(root, text="MESSAGE:", font=("Blackadder ITC", 20))
label4.place(x=0, y=200)

button1 = Button(root, text="ADD IMAGE", font=("Blackadder ITC", 14), command=choose_img)
button1.place(x=250, y=350)

button2 = Button(root, text="SEND", font=("Blackadder ITC", 14), command=send)
button2.place(x=400, y=350)

button3 = Button(root, text="CLEAR", font=("Blackadder ITC", 14), command=clear)
button3.place(x=350, y=450)

button4 = Button(root, text="SIGNATURE", font=("Blackadder ITC", 14), command=add_signature)
button4.place(x=150, y=450)

button4 = Button(root, text="PREVIEW", font=("Blackadder ITC", 14), command=preview)
button4.place(x=50, y=450)

button5 = Button(root, text="🐀", font=("Blackadder ITC", 14), command=krysa)
button5.place(x=50, y=550)

email = Entry(root, font=("Freestyle Script", 25))
email.place(x=190, y=0, width=300, height=50)

topic = Entry(root, font=("Freestyle Script", 25))
topic.place(x=190, y=50, width=300, height=50)

added = Label(root, text="...", font=("Freestyle Script", 25))
added.place(x=190, y=110, width=300, height=20)

message = Text(root, font=("Freestyle Script", 25))
message.place(x=190, y=130, width=300, height=200)

root.mainloop()
