# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 16:57:39 2022

@author: Deepesh
"""

#importing tkinter graphical interface libraries
from tkinter import *


# creating main window widget
root = Tk()
root.configure(background='lavender')


#setting title
root.title("Practical Assignment 0")


#creating Enter text Label and putting it as grid on root widget
P1 = Label(root, text="Enter the text",fg="Red",font = ('Helvetica', 10, 'bold'))
P1.grid(row=0,column=0)


#Input widget as grid on the root window widget
a = Entry(root,width=100,borderwidth=5)
a.grid(row=1,column=0,columnspan=20,padx=10,pady=10)



#encryption algorithm 
def encrypt_text():
    str = a.get() 
    enc_str = ""
    key = 5
    # key = 5 in this demonstration
    for i in range(0,len(str)):
        if (str[i].isspace()) == True :
            enc_str+=" "
            continue
        
        add = ord(str[i]) + key 
        if add > ord('z') :
            shift = add - ord('z') 
            add = ord('a') + shift - 1
        enc_str += chr(add)

    output_label = Label(root,text="Encrypted text: ",font = ('Arial', 10, 'bold'))
    output_label.grid(row=2,column=0)
    output_label = Label(root,text= enc_str,fg="Green",font = ('Arial', 10))
    output_label.grid(row=3,column=0)
    return


#decryption algorithm 
def decrypt_text():
    str = a.get() 
    dec_str = ""
    key = 5
    # key = 5 in this demonstration
    for i in range(0,len(str)):
        if (str[i].isspace()) == True :
            dec_str+=" "
            continue
        
        sub = ord(str[i]) - key
        if sub < ord('a') :
            shift = ord('a') - sub
            sub = ord('z') - shift + 1
        dec_str += chr(sub)
    
    output_label1 = Label(root,text="Decrypted text: ",font = ('Arial', 10, 'bold'))
    output_label1.grid(row=2,column=0)
    output_label2 = Label(root,text= dec_str,fg="Green",font = ('Arial', 10))
    output_label2.grid(row=3,column=0)
    return
    

# adding buttons for encryption and decryption
encrypt = Button(root, text = "Encrypt the text",command=encrypt_text,fg="White",bg="Black",font = ('Helvetica', 10, 'bold'))
decrypt = Button(root, text = "Decrypt the text",command=decrypt_text,fg="Black",bg="White",font = ('Helvetica', 10, 'bold'))


#putting the buttons as grid on the main window root widget
encrypt.grid(row=4,column=0)
decrypt.grid(row=4,column=1)


#main loop
root.mainloop() 

 