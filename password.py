import sys
import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip
#This section is the password generator Algorithm
def generate_password():
    
    pass_length = int(entry.get())
    password_characters = string.ascii_letters + string.digits + string.punctuation
  
    generated_password = ''.join(random.choice(password_characters) for _ in range(pass_length))
    result_label.config(text="Generated Password: " + generated_password, bg="black", font=("Arial", 12), fg="white")
    result_label.place(relx=0.3, rely=0.8)

 
   
    

   
   
def clear_password():
    result_label.config(text="")
   
#To copy the generated password
def copy_password():
    generated_password = result_label.cget("text").split(": ")[-1]
    pyperclip.copy(generated_password)
    message = f"Password Copied: /n/{generated_password}"
    messagebox.showinfo('Password Copied ', message)
    
    #Gui part of the program
    
window_x =600
window_y=500

root = tk.Tk()
root.title("Password Generator")
root.geometry(f"{window_x}x{window_y}")
root.configure(bg="#00FFFF")
root.resizable(0,0)
icon = tk.PhotoImage(file='add_the_file_location_for_image')
root.iconphoto(False, icon)
background_image = tk.PhotoImage(file='add_the_file_location_for_image')

background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

def on_closing():
    root.quit()
    root.destroy()



    


length_label = tk.Label(root, text="Enter Password Length",bg="#00FFFF",font=("Arial", 16) )
length_label.place(relx=0.32, rely=0.08)
entry = tk.Entry(root, width=8)
entry.place(relx=0.45,rely=0.16)




on_button_photo = tk.PhotoImage(file='add_the_file_location_for_image')
resize_photo = on_button_photo.subsample(1,1)
generate_button = tk.Button(root, text="Generate Password", image  = resize_photo, command=generate_password, font=("Arial", 12))
generate_button.place(relx=0.34, rely=0.3, anchor=tk.CENTER)







on_button_photo_clear = tk.PhotoImage(file='add_the_file_location_for_image')
resize_photo_clear = on_button_photo_clear.subsample(1,1)
clear_button = tk.Button(root, text ="Clear Password", image= resize_photo_clear, command =clear_password, font=("Arial", 12))
clear_button.place(relx=0.62, rely=0.3, anchor=tk.CENTER)


copy_button = tk.Button(text= "Copy the password", command= copy_password,  font=("Arial", 12))
copy_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)



result_label = tk.Label(root, text="")
result_label.pack()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()

