from tkinter import *

window = Tk()


def windowSettings():
    window.title(string='BMI Calculator')
    window.iconbitmap("bmi.ico")


# open right in the middle of the screen
def center_window(rootWindow, width, height):
    screen_width = rootWindow.winfo_screenwidth()
    screen_height = rootWindow.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    rootWindow.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")


windowSettings()
center_window(window, width=250, height=230)


def calculate(weight, height, resultText):
    if weight.isdigit() and height.isdigit():
        weight = int(weight)
        height = int(height)

        if 0 < weight < 250 and 0 < height < 230:
            bmi = weight / (height / 100) ** 2
            if bmi < 18.5:
                return 'Below ideal weight'
            elif 18.5 <= bmi < 24.9:
                return 'Ideal weight'
            elif 24.9 <= bmi < 29.9:
                return 'Above ideal weight'
            elif 29.9 <= bmi < 39.9:
                return 'Above ideal weight (obese)'
            elif bmi > 39.9:
                return 'Above ideal weight (morbidly obese)'
        else:
            resultText.config(text='Please enter a valid weight and height value')
    else:
        resultText.config(text='Please enter a valid weight and height value')


def initWidgets():
    labelWeight = Label(text='Enter your weight (kg)', padx=10, pady=10, font=('Times New Roman', 13, 'normal'))
    labelWeight.pack()

    entryWeight = Entry(width=20)
    entryWeight.pack()

    labelHeight = Label(text='Enter your Height (cm)', padx=10, pady=10, font=('Times New Roman', 13, 'normal'))
    labelHeight.pack()

    entryHeight = Entry(width=20)
    entryHeight.pack()

    resultText = Label()
    resultText.pack(padx=5, pady=5)

    calculateButton = Button(text='Calculate', bg='#eb901a', fg='white',
                             command=lambda: resultText.config(
                                 text=calculate(weight=entryWeight.get(), height=entryHeight.get(),
                                                resultText=resultText)))
    calculateButton.pack(padx=15, pady=15)


initWidgets()

window.mainloop()
