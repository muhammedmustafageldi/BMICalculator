from tkinter import *

window = Tk()


def windowSettings():
    window.title(string='BMI Calculator')


# open right in the middle of the screen
def center_window(rootWindow, width, height):
    screen_width = rootWindow.winfo_screenwidth()
    screen_height = rootWindow.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    rootWindow.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")


windowSettings()
center_window(window, width=250, height=200)


def calculate(weight, height, resultText):
    resultText.insert(weight, height)


def initWidgets():
    labelWeight = Label(text='Enter your weight (kg)', padx=10, pady=10, font=('Times New Roman', 13, 'normal'))
    labelWeight.pack()

    entryWeight = Entry(width=20)
    entryWeight.pack()

    labelHeight = Label(text='Enter your Height (cm)', padx=10, pady=10, font=('Times New Roman', 13, 'normal'))
    labelHeight.pack()

    entryHeight = Entry(width=20)
    entryHeight.pack()

    resultText = Text(width=5, height=5)
    resultText.pack()

    calculateButton = Button(text='Calculate', bg='#eb901a', fg='white',
                             command=lambda: calculate(weight=entryWeight.get(), height=entryHeight.get(),
                                                       resultText=resultText))
    calculateButton.pack(padx=15, pady=15)


initWidgets()

window.mainloop()
