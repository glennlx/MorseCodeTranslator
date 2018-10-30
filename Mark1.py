# Python program to implement Morse Code Translator

'''
VARIABLE KEY
'cipher' -> 'stores the morse translated form of the english string'
'decipher' -> 'stores the english translated form of the morse string'
'citext' -> 'stores morse code of a single character'
'i' -> 'keeps count of the spaces between morse characters'
'message' -> 'stores the string to be encoded or decoded'
'''
import Tkinter as tk
# Dictionary representing the morse code chart

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':

            # Looks up the dictionary and adds the
            # correspponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '

    return cipher


# Function to decrypt the string
# from morse to english
def decrypt(message):
    # extra space added at the end to access the
    # last morse code
    message += ' '

    decipher = ''
    citext = ''
    for letter in message:

        # checks for space
        if (letter != ' '):

            # counter to keep track of space
            i = 0

            # storing morse code of a single character
            citext += letter

            # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1

            # if i = 2 that indicates a new word
            if i == 2:

                # adding space to separate words
                decipher += ' '
            else:

                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                                                              .values()).index(citext)]
                citext = ''

    return decipher

window = tk.Tk("")
z=tk.IntVar()
window.title("Welcome to Morse Code Translator App by K & G")
window.geometry('350x200')
lbl = tk.Label(window, text="Choose Option : ")
var=tk.IntVar()
v=tk.StringVar()
txt = tk.Entry(window,textvariable=v, width=20)
lb2=tk.Label(window)

def clear():
    v.set("")
    x=var.get()
    if(x==1):
        lb2.configure(text="Enter The English Text to be Encrypted")
    elif(x==2):
        lb2.configure(text="Enter The Morse Code to be Decrypted")

r1=tk.Radiobutton(window,text="English to Morse",value=1,variable=var,command=clear)
r2=tk.Radiobutton(window,text="Morse to English",value=2,variable=var,command=clear)
lbl.grid(column=0, row=0)
r1.grid(row=2)
r2.grid(row=3)
lb2.grid(row=4)
txt.grid(column=0, row=5)

def main(str,var):
    message=str
    if(var==1):
        result = encrypt(message.upper())
        print (result)

    elif(var==2):
        result = decrypt(message)
        print (result)
    z.set(result)


def clicked():
    # lbl.configure(text="Button was clicked !!")
    str=v.get()
    y=var.get()
    main(str,y)


btn = tk.Button(window, text="Click Me",bg="red", command=clicked)
btn.grid(row=6)

lb3=tk.Label(window,textvar=z,text="")
lb3.grid(row=7)
window.mainloop()


# Hard-coded driver function to run the program
# def main(str):
#     message = str
#     result = encrypt(message.upper())
#     print (result)
#
#     message = "-.- . . ..- "
#     result = decrypt(message)
#     print (result)


# # Executes the main function
# if __name__ == '__main__':
#     main()