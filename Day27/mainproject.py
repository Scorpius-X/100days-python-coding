from tkinter import *

# create and bind Tk class to a variable called window
window = Tk()
window.title("Miles to Kilometres converter")
window.config(padx=50, pady= 30, bg= "white")


#def function to convert miles to kilometre

def mileage():
    miles_added = int(input.get())
    km = round(miles_added * 1.609344)
    kilometre_label.config(text= km)

#Create all widgets

input = Entry(width= 10)
input.grid(column= 1, row= 0 )


equals_label = Label(text= "is equal to")
equals_label.grid(column= 0, row= 1 )
equals_label.config(bg= "white")

kilometre_label = Label(text= 0 )
kilometre_label.grid(column= 1, row=1 )
kilometre_label.config(bg= 'white')



calc_button = Button(text= "calculate", command= mileage)
calc_button.grid(column= 1, row= 2)

miles_label = Label(text= "miles")
miles_label.grid(column= 2, row=0)
miles_label.config(bg="white", padx = 5)

km_label = Label(text= "km")
km_label.grid(column= 2, row= 1)
km_label.config(bg="white", padx= 5)








window.mainloop()