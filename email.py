import smtplib
from tkinter import *
from tkinter import messagebox

def send_message():
    address_info = address.get()
    email_body_info = email_body.get()

    sender_email = "your_gmail@gmail.com"
    sender_password = "youre_password"

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        print("Login successful")

        server.sendmail(sender_email, address_info, email_body_info)
        print("Message sent")

        messagebox.showinfo("Success", "Email sent successfully!")
        address_entry.delete(0, END)
        email_body_entry.delete(0, END)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {str(e)}")
app = Tk()
app.geometry("500x300")
app.title("Python Mail Send App")

heading = Label(
    text="Python Email Sending App",
    bg="yellow", fg="black",
    font=("Arial", 14, "bold"),
    width="500", height="2"
)
heading.pack()

address_field = Label(text="Recipient Address:")
email_body_field = Label(text="Message:")

address_field.place(x=15, y=70)
email_body_field.place(x=15, y=120)

address = StringVar()
email_body = StringVar()

address_entry = Entry(textvariable=address, width="40")
email_body_entry = Entry(textvariable=email_body, width="40")

address_entry.place(x=160, y=70)
email_body_entry.place(x=160, y=120)

button = Button(
    app, text="Send Message",
    command=send_message,
    width="30", height="2", bg="grey"
)
button.place(x=150, y=180)

mainloop()
