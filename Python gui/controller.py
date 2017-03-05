import tkinter
import myFrame    # the VIEW
import converter

class Controller:
    def __init__(self):
        '''
        starts TK framework
        instantiates model (converter)
        instantiates view (MyFrame)
        starts event loop
        '''
        root = tkinter.Tk()
        self.model = converter.Converter()
        self.view = myFrame.MyFrame(self)
        self.view.mainloop()
        root.destroy()

    def farenPressed(self):
        '''
        method called when convert to farenheit button pressed
        '''
        stringTemp = self.view.tempEntry.get()
        temp = float(stringTemp)
        temp = self.model.convertFaren(temp)
        stringTemp = str(temp)+ " F"
        self.view.resultTemp["text"] = stringTemp  
        
    def celsPressed(self):
        '''
        method called when convert to celsius button pressed
        '''
        stringTemp = self.view.tempEntry.get()
        temp = float(stringTemp)
        temp = self.model.convertCels(temp)
        stringTemp = str(temp) + " C"
        self.view.resultTemp["text"] = stringTemp  
        
if __name__ == "__main__":
   c = Controller() 

