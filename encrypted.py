from tkinter import *

root= Tk()

root.geometry("600x600")

root.title("Names In Ascii")

root.configure(background="yellow")

textbox=Entry(root)

textbox.place(relx=0.5, rely=0.4, anchor=CENTER)

label=Label(root, text="Name In Ascii : ", bg="green", fg="black")

label2=Label(root, text="Encrypted Name : ", bg="black", fg="white")
label2.place(relx=0.5, rely= 0.7, anchor=CENTER)
label.place(relx=0.5, rely=0.6, anchor=CENTER)

def asciiConverter():
    input_word=textbox.get()
    for letter in input_word:
        label["text"] += str(ord(letter)) + " "
        ascii=int(ord(letter))
        reduced=ascii-1
        label2["text"]+= str(chr(reduced))
button=Button(root, text="Convert", command=asciiConverter, bg="gray", fg="white")
button.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
        