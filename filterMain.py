import stddraw
import sys
import stdaudio
from picture import Picture
from color import Color
from filter import Filter
import simpleaudio
import time


def selected_filter(filtered_image , m):
    match m:
        case 1:
            return filtered_image.grayscale()
        case 2:
            return filtered_image.negative()
        case 3:
            return filtered_image.sepia()
        case 4:
            return filtered_image.blur()
        case 5:
            return filtered_image.posterize()
        case 6:
            return filtered_image.darkshadow()
        case 7:
            return filtered_image.lightshadow()
        case 8:
            return filtered_image.brightness()
        case 9:
            return filtered_image.wavyv()
        case 10:
            return filtered_image.wavyh()
        case _:
            raise ValueError('mammad')


def main():

    image = Picture(sys.argv[1])
    filtered_image = Filter(image)
    while True:
        try:
            menu = int(input("""
pls select your filter by number:
1. grayscale
2. negative
3. sepia
4. blur
5. posterized
6. darkshadow
7. lightshadow
8. brightness
9. wavy (vertical)
10.wavy (horizontal)
"""))
            
            if (menu < 1) or (menu > 10):
                print("pls enter a number between 1 , 10 ")
            
            mix = selected_filter(filtered_image , menu)
            finalimage = mix[0]
            playsound = mix[1]
            break

        except ValueError:
            print('this is not a valid number. pls try again!')
            
    
    stddraw.setCanvasSize(finalimage.width() , finalimage.height())
    stddraw.picture(finalimage)
    stddraw.show()
    playsound.play()
    
if __name__ == "__main__":
    main()