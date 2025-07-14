from tkinter import *
window= Tk()
window.title("CALCULATOR")
window.geometry("290x310")
window.iconbitmap(r'Calculations.ico')
window.config(bg='pink')

def click_button(numbers):
    global operator
    operator=operator + str(numbers)
    text_input.set(operator)

def equal_button():
    global operator
    evaluate= str(eval(operator))
    text_input.set(evaluate)
    operator=""
    #print(evaluate)

text_input = StringVar()
operator=""

def clear():
    global operator
    operator=''
    text_input.set('')


def delete_button():
    #typingbox.delete(-1) # deletes from left to right
    #typingbox.delete(-1, END) #  clears the entire box
    typingbox.delete(len(typingbox.get())-1, END) #deleting from right to left

def off_button():
    window.destroy()

typingbox= Entry(window,width=40,borderwidth=0, textvariable=text_input)
typingbox.grid(row=0,column=0,columnspan=10, padx=1, pady=15, ipady=10)

def buttons():

    n1= Button(window, text="9",bg="blue",fg="white", padx=20, pady=15,command=lambda: click_button(9) )
    n1.grid(row=1, column=0)

    n2= Button(window, text="8",bg= 'blue',fg="white", padx=20, pady=15,command=lambda: click_button(8))
    n2.grid(row=1, column=1)

    n3= Button(window, text="7", bg= 'blue',fg="white", padx=20, pady=15,command=lambda: click_button(7))
    n3.grid(row=1, column=2)

    n4= Button(window, text="4",bg="blue",fg="white", padx=20, pady=15,command=lambda: click_button(4))
    n4.grid(row=2, column=0)

    n5= Button(window, text="5", bg="blue",fg="white",padx=20, pady=15,command=lambda: click_button(5))
    n5.grid(row=2, column=1)

    n6= Button(window, text="6",bg="blue",fg="white", padx=20, pady=15,command=lambda: click_button(6))
    n6.grid(row=2, column=2)

    n7= Button(window, text="1", bg="blue",fg="white", padx=20, pady=15,command=lambda: click_button(1))
    n7.grid(row=3, column=0)

    n8= Button(window, text="2", bg="blue",fg="white",  padx=20, pady=15,command=lambda: click_button(2))
    n8.grid(row=3, column=1)

    n9= Button(window, text="3", bg="blue",fg="white", padx=20, pady=15,command=lambda: click_button(3))
    n9.grid(row=3, column=2)

    n0= Button(window, text=0, bg="blue",fg="white",padx=20, pady=15,command=lambda: click_button(0))
    n0.grid(row=4, column=0)

    subtraction_button = Button(window, text="-", bg = "green", padx=20, pady=15, width=2,command=lambda: click_button(" - "))
    subtraction_button.grid(row=1, column=3)

    multiplication_button = Button(window, text="x", bg = "green", padx=20, pady=15, width=2,command=lambda: click_button(" * "))# command=multplication_button)
    multiplication_button.grid(row=2, column=3)

    plus_button = Button(window, text="+", bg = "green", padx=20, pady=15, width=2,command=lambda: click_button(" + "))
    plus_button.grid(row=3, column=3)

    division_button = Button(window, text="÷", bg = "green", padx=20, pady=15, width=2,command=lambda: click_button(" / "))
    division_button.grid(row=4, column=3)

equal_button = Button(window, text="=", bg = "red", padx=20, pady=15, command=equal_button)
equal_button.grid(row=4, column=2)

clear_button = Button(window, text="C", bg = "red", padx=20, pady=15,command=delete_button)
clear_button.grid(row=4, column=1)

OFF_button= Button(window, text="OFF", bg="black", fg="white",activebackground="red",highlightbackground="white",padx=5, pady=5, height=6,command=off_button)
OFF_button.grid(row=3,column=4 ,columnspan=5, rowspan=2)

ON_button= Button(window, text="ON", bg="black", fg="white",activeforeground="black",activebackground="black", padx=5, pady=5, height=6, command=buttons)
ON_button.grid(row=1,column=4 ,columnspan=5, rowspan=2)

window.mainloop()