import tkinter
import controller

"""
sets up a gui that accepts a number temperature and converts it to either
Celsius or Farenheit when
a button is pressed
"""

class MyFrame(tkinter.Frame):
    def __init__(self, controller):
        tkinter.Frame.__init__(self)
        self.pack()
        self.Controller = controller 

        self.tempEntry = tkinter.Entry()
        self.tempEntry.insert(0, "enter a temperature")
        self.tempEntry.pack({"side": "left"})
       
        self.quitButton = tkinter.Button(self)
        self.quitButton["text"] = "Quit"
        self.quitButton["command"] =  self.quit
        self.quitButton.pack({"side": "left"})

        self.celsButton = tkinter.Button(self)
        self.celsButton["text"] = "convert to Fahrenheit",
        self.celsButton["command"] = self.Controller.farenPressed
        self.celsButton.pack({"side": "left"})

        self.farenButton = tkinter.Button(self)
        self.farenButton["text"] = "convert to Celsius",
        self.farenButton["command"] = self.Controller.celsPressed
        self.farenButton.pack({"side": "left"})

        self.resultTemp = tkinter.Label(self)
        self.resultTemp.pack({"side": "left"})
        self.resultTemp["text"] = 0
