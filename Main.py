# pip install cryptography
# pip install pyperclip
# pip install tkinter
# pip install tk

import os
import tkinter
import pyperclip
import tkinter.filedialog
import logging
from cryptography.fernet import Fernet

# Create a log file
logging.basicConfig(filename='logs.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='[%m/%d/%Y %I:%M:%S %p]')

#Create a GUI window
root= tkinter.Tk()
root.title("Secure File Encryption/Decryption")

#Generate a key
def gen_key():
    """Generate a key using the Fernet class from the cryptography module"""
    key= Fernet.generate_key()
    key_entry.delete(0, tkinter.END)
    key_entry.insert(0, key)
    pyperclip.copy(key.decode())
    return None

#Function for encryption
def encrypt():
    """Generate a key using the Fernet class from the cryptography module"""
    input_file= input_entry.get()
    output_file= output_entry.get()
    file_key= key_entry.get()

    #Check if all inputs are provided
    if(input_file == "" or output_file == "" or file_key == ""):
        #Prompt for input
        tkinter.messagebox.showinfo("Error", "Please select all inputs")
        return None
    
    f = Fernet(file_key)
    with open(input_file, 'rb') as in_file:
        file_data= in_file.read()
    encrypted_data= f.encrypt(file_data)
    with open(output_file, 'wb') as out_file:
        out_file.write(encrypted_data)
    input_entry.delete(0, tkinter.END)
    output_entry.delete(0, tkinter.END)
    key_entry.delete(0, tkinter.END)
    logging.info("Encryption: Success | Input File: {} | Output File: {} | Key: {} ".format(input_file, output_file, file_key))
    tkinter.messagebox.showinfo("Success!", "File Encrypted successfully")
    return None

#Function for decryption
def decrypt():
    """Decrypt the file using Fernet from the cryptography module"""
    input_file= input_entry.get()
    output_file= output_entry.get()
    file_key= key_entry.get()

    #Check if all inputs are provided
    if(input_file == "" or output_file == "" or file_key == ""):
        #Prompt for input
        tkinter.messagebox.showinfo("Error", "Please select all inputs")
        return None
    
    f = Fernet(file_key)
    with open(input_file, 'rb') as in_file:
        file_data= in_file.read()
    decrypted_data= f.decrypt(file_data)
    with open(output_file, 'wb') as out_file:
        out_file.write(decrypted_data)
    input_entry.delete(0, tkinter.END)
    output_entry.delete(0, tkinter.END)
    key_entry.delete(0, tkinter.END)
    logging.info("Decryption: Success | Input File: {} | Output File: {} | Key: {}".format(input_file, output_file, file_key))
    tkinter.messagebox.showinfo("Success!", "File Decrypted successfully")
    return None

#Function to select input file
def select_input_file():
    """Prompts the user to select an input file"""
    filename = tkinter.filedialog.askopenfilename(title="Select Input File")
    input_entry.delete(0, tkinter.END)
    input_entry.insert(0, filename)

#Function to select output file
def select_output_file():
    """Prompts the user to select an output file"""
    filename = tkinter.filedialog.asksaveasfilename(title="Select Output File")
    output_entry.delete(0, tkinter.END)
    output_entry.insert(0, filename)

#Function to show logs
def show_logs():
    """Show the logs"""
    os.system('notepad logs.log')

#Function to delete logs
def delete_logs():
    """Delete the logs"""
    log_file = open('logs.log', 'w')
    log_file.write('')
    log_file.close()
    tkinter.messagebox.showinfo("Success", "Logs deleted successfully")

#Function to exit
def exit():
    """Close the window"""
    root.destroy()

#Create a menu bar
input_label= tkinter.Label(root, text="Input File", font="bold")
input_label.grid(row=0, column=0, padx=20, pady=10)

output_label= tkinter.Label(root, text="Output File", font="bold")
output_label.grid(row=1, column=0, padx=20, pady=10)

key_label= tkinter.Label(root, text="Key", font="bold")
key_label.grid(row=2, column=0, padx=20, pady=10)

#Entries
input_entry= tkinter.Entry(root, foreground="black", font=("Helvetica", 12))
input_entry.grid(row=0, column=1, padx=20, pady=10)

output_entry= tkinter.Entry(root, foreground="black", font=("Helvetica", 12))
output_entry.grid(row=1, column=1, padx=20, pady=10)

key_entry= tkinter.Entry(root, foreground="black", font=("Helvetica", 12))
key_entry.grid(row=2, column=1, padx=20, pady=10)

#Buttons
encrypt_button= tkinter.Button(root, text="Encrypt", command=encrypt, font=("Helvetica", 12), bg="green")
encrypt_button.grid(row=3, column=0, padx=20, pady=5)

decrypt_button= tkinter.Button(root, text="Decrypt", command=decrypt, font=("Helvetica", 12), bg="gray")
decrypt_button.grid(row=3, column=1, padx=20, pady=5)

logs_button= tkinter.Button(root, text="Show Logs", command=show_logs, font=("Helvetica", 12))
logs_button.grid(row=3, column=2, padx=20, pady=5)

delete_logs_button= tkinter.Button(root, text="Delete Logs", command=delete_logs, font=("Helvetica", 12))
delete_logs_button.grid(row=3, column=3, padx=20, pady=5)

generate_key_button= tkinter.Button(root, text="Generate Key", command=gen_key, font=("Helvetica", 12), bg="powder blue")
generate_key_button.grid(row=2, column=2, padx=20, pady=10)

input_file_button= tkinter.Button(root, text="Select Input File", command=select_input_file, font=("Helvetica", 12))
input_file_button.grid(row=0, column=2, padx=20, pady=10)

output_file_button= tkinter.Button(root, text="Select Output File", command=select_output_file, font=("Helvetica", 12))
output_file_button.grid(row=1, column=2, padx=20, pady=10)

exit_button= tkinter.Button(root, text="Exit", command=exit, font=("Helvetica", 12), bg="red")
exit_button.grid(row=2, column=3, padx=20, pady=10)

#Message
message= tkinter.Label(root, text="", font=("Helvetica", 12))
message.grid(row=4, column=1, padx=20, pady=10)

#run the main loop
root.mainloop()