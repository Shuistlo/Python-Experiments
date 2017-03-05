'''
class Converter converts a temperature to either Celsius or Farenheit 
'''
class Converter():
    def __init__(self):
        '''
        initializes the temperature as zero
        '''
        self.temp = 0
        
    def convertCels(self, temp):
        '''
        converts a temperature into celsius
        '''
        self.temp = temp
        self.temp = (5/9)*(self.temp-32)
        return self.temp
        
    def convertFaren(self, temp):
        '''
        converts a temperature into farenheit
        '''
        self.temp = temp
        self.temp = ((9/5)*self.temp)+32
        return self.temp

    def __str__(self):
        '''
        returns a string interpretation of the temperature
        '''
        return str(self.temp)
