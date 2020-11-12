from tkinter import *
import math
def leftClickButton(event):
    print(float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    labelResult.configure(text=round(float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)))
    labelResultText.configure(text=result())
def result():
    tester = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    if tester > 30:
        return "อ้วนมาก"
    elif tester >= 25:
        return "อ้วน"
    elif tester >= 23:
        return "น้ำหนักเกิน"
    elif tester >= 18.6:
        return "น้ำหนักปกติ"
    elif tester < 18.5:
        return "ผอมเกินไป"

MainWindow = Tk()
labelHeight = Label(MainWindow,text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeight = Label(MainWindow,text="น้ำหนัก (Kg.)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวณ")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)
labelResultText = Label(MainWindow,text="ค่าที่ได้")
labelResultText.grid(row=3,column=1)
MainWindow.mainloop()