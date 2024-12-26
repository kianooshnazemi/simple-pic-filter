import math
from picture import Picture
from color import Color
import simpleaudio

class Filter :

    def __init__(self,image):
        self._image = image
        self._width = self._image.width()
        self._height = self._image.height()

    def grayscale(self):
        

        for x in range(self._width):
            for y in range(self._height):
                c = self._image.get(x,y)
                r, g, b = c.getRed() , c.getGreen() , c.getBlue
                luminance = int((0.299 * r) + (0.587 * g) + (0.114 * b))
                grey = Color(luminance,luminance,luminance)
                self._image.set(x , y , grey)
        sound = simpleaudio.WaveObject.from_wave_file('grayscalem.wav')
        playsound = sound.play()    
        return [self._image,playsound]


    def negative(self):
       
        for x in range(self._width):
            for y in range(self._height):
                c = self._image.get(x,y)
                r, g, b = c.getRed() , c.getGreen() , c.getBlue()
                neg = Color(255 - r, 255 - g, 255 - b)
                self._image.set(x, y, neg)
        sound = simpleaudio.WaveObject.from_wave_file('negativem.wav')
        playsound = sound.play()    
        return [self._image,playsound]


    def sepia(self):
      
        for x in range(self._width):
            for y in range(self._height):
                c = self._image.get(x, y)
                r, g, b = c.getRed(), c.getGreen(), c.getBlue()
                tr = int(0.393 * r + 0.769 * g + 0.189 * b)
                tg = int(0.349 * r + 0.686 * g + 0.168 * b)
                tb = int(0.272 * r + 0.534 * g + 0.131 * b)
                r = min(255, tr)
                g = min(255, tg)
                b = min(255, tb)
                sep = Color(r, g, b)
                self._image.set(x, y, sep)
        sound = simpleaudio.WaveObject.from_wave_file('sepiam.wav')
        playsound = sound.play()    
        return [self._image,playsound]


    def blur(self):

        for x in range(1, self._width - 1):
            for y in range(1, self._height - 1):
                r, g, b = 0, 0, 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                         c = self._image.get(x + i, y + j)
                         nr, ng, nb = c.getRed(), c.getGreen(), c.getBlue()
                         r += nr
                         g += ng
                         b += nb
                r //= 9
                g //= 9
                b //= 9
                blured = Color(r, g, b)
                self._image.set(x ,y ,blured)
        sound = simpleaudio.WaveObject.from_wave_file('blurm.wav')
        playsound = sound.play()    
        return [self._image,playsound]
                    
    
    def posterize(self):
        while True:
            try:
                levels = int(input("pls enter your target posterize levels(abs positive integer (preferly 1-10)):"))
                def posterize_value(value, levels):
                    return int(value // (256 / levels) * (256 / levels))
                
                for x in range(self._width):
                    for y in range(self._height):
                        c = self._image.get(x,y)
                        r, g, b = c.getRed() , c.getGreen() , c.getBlue()
                        r = posterize_value(r, levels)
                        g = posterize_value(g, levels)
                        b = posterize_value(b, levels)
                        post = Color(r, g, b)
                        self._image.set(x, y, post)
                sound = simpleaudio.WaveObject.from_wave_file('posterizem.wav')
                playsound = sound.play()    
                return [self._image,playsound]
            except Exception:
                print("pls enter a valid number")
    
    def darkshadow(self):
        while True:
            try:
                level = int(input("pls enter your target shadow level(0-765):"))
                for x in range (self._width):            
                    for y in range (self._height):
                        c = self._image.get(x,y)
                        r , g , b = c.getRed(), c.getGreen(), c.getBlue()
                        
                        if (int(r)+int(g)+int(b)) > level :
                            self._image.set(x,y,Color(255,255,255))
                        
                        else: 
                            self._image.set(x,y,Color(0,0,0))
                sound = simpleaudio.WaveObject.from_wave_file('shadowm.wav')
                playsound = sound.play()    
                return [self._image,playsound]
            except Exception:
                print("pls enter a valid number")

    
    def lightshadow(self):
        while True:
            try:     
                level = int(input("pls enter your target shadow level(variable 0-765):"))        
                for x in range (self._width):            
                    for y in range (self._height):
                        c = self._image.get(x,y)
                        r , g , b = c.getRed(), c.getGreen(), c.getBlue()
                        
                        if (int(r)+int(g)+int(b)) < level :
                            self._image.set(x,y,Color(255,255,255))
                        
                        else: 
                            self._image.set(x,y,Color(0,0,0))                
                sound = simpleaudio.WaveObject.from_wave_file('shadowm.wav')
                playsound = sound.play()    
                return [self._image,playsound]
            except Exception:
                print("pls enter a valid number")


    def brightness(self):
        while True:
            try:
                coe = int(input("pls enter your target brightness level (0=darkest , 255=lightest) :"))
                for x in range (self._width):
                    for y in range (self._height):
                        c = self._image.get(x,y)
                        r , g , b = c.getRed(), c.getGreen(), c.getBlue()
                        r , g , b = float(r) , float(g) , float(b)

                        dn = Color(int(coe * r / 255),int(coe * g / 255),int(coe * b / 255))
                        self._image.set(x,y,dn)
                sound = simpleaudio.WaveObject.from_wave_file('brightnessm.wav')
                playsound = sound.play()    
                return [self._image,playsound]
            except Exception:
                print("pls enter inter a number between 0 and 255!")

    def wavyv(self) :      
        while True:
            try:
                length = int(input("pls enter the length of the waves(a none zero integer number):"))
                newimage = Picture(self._width,self._height)
                for x in range (self._width):
                    for y in range (self._height):
                        c = self._image.get(x,y)
                        length = float(length)
                        newimage.set(x , y + int(20 * math.sin(x / length)) , c)
                sound = simpleaudio.WaveObject.from_wave_file('wavym.wav')
                playsound = sound.play() 
                return [newimage , playsound]
            except  ZeroDivisionError:
                print("length can't be 0")
            except ValueError:
                print("pls enter a number!")

    def wavyh(self) :      
         while True:
            try:
                length = int(input("pls enter the length of the waves(a none zero integer number):"))
                newimage = Picture(self._width,self._height)
                for x in range (self._width):
                    for y in range (self._height):
                        c = self._image.get(x,y)
                        length = float(length)
                        newimage.set(x + int(20 * math.sin(y / length)) , y, c)
                sound = simpleaudio.WaveObject.from_wave_file('wavym.wav')
                playsound = sound.play()         
                return [newimage , playsound]   
            except  ZeroDivisionError:
                print("length can't be 0")
            except ValueError:
                print("pls enter a number!")
