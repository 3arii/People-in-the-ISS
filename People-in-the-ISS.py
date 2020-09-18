from selenium.webdriver.common.keys import Keys
import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import tkinter
from tkinter import *
from PIL import Image, ImageTk 

def listTostring(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)



        self.image = Image.open(".\Desktop\EarthFromSpace.jpg")#opens the selected image
        self.img_copy= self.image.copy()#puts the image into another variable for later use


        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)#enabling expand and fill
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self,event):

        new_width = event.width#setting the width and height as same as the event ones
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))#changes the new selected images h and w to the selected ones

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)#configures it to the last selected w and h

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.howmanypeopleareinspacerightnow.com/")#opens the web page

numbers = driver.find_element_by_id("top").text #gets the number of people

names_list = []
names = driver.find_elements_by_class_name("person-name") #gets the name of the astronauts
for name in names:
    names_list.append(name.text)
"""
Turns the list into the .text object and adds it to the
names_list which is printable 
"""

namesprime = [w.replace("\n", " who is the ") for w in names_list]#changes all \n to = to make a clear string
listTostring(namesprime)#turns the list into a str
print(numbers)
print(namesprime)

#if selected == 1:
#    print("There is a single person cooler than you!")
#else:
#    print("There are " + selected + " people cooler than you!")

window = tkinter.Tk()
window.title("Cooler Than You")
window.geometry("600x600")
window.configure(background="black")

label = tkinter.Label(window, text = "There are " + numbers + " People cooler than you!", font =("Helvetica, 50"), fg = "white", bg ="black").pack()
label1 = tkinter.Label(window, text = namesprime, font = ("Helvetica,35"), fg = "white", bg = "black").pack()

e = Example(window)
e.pack(fill = BOTH, expand = YES)

window.mainloop()   



