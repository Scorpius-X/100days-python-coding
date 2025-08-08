from tkinter import *

window = Tk()

window.title("My first Gui program")
window.minsize(width= 500, height= 300)

#each widget.config(padx=,pady=) to add padding or space between the widgets

#label

my_label = Label(text= "I am a Label", font= ("arial", 24, "bold"))
my_label.grid(column= 0,row= 0)


#button
def button_clicked():
    new_text = input.get()
    my_label.config(text = new_text )

button = Button(text="click me", command= button_clicked)
button.grid(column= 1, row= 1)

new_button = Button(text = "new button")
new_button.grid(column=2, row= 0)
#Entry
 
input= Entry(width= 10)
input.grid(column= 3, row= 3)


window.mainloop()