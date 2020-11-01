from time import sleep
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(270)

def clamp(num, min=0, max=255):
  if num < min:
    num = min
  elif num > max:
    num = max
  return num

def color_from_temp(min, max, temp):
  low_for_humans = 4
  high_for_humans = 35
  
  range = 10

  if min < 0:
    temp -= min
    low_for_humans -= min
    high_for_humans -= min
    
  if temp < low_for_humans:
    red = 0
    green = 255 - ((low_for_humans - temp) * range)
    blue = (low_for_humans - temp) * range
  elif temp > high_for_humans:
    red = (temp - high_for_humans) * range
    green = 255 - ((temp - high_for_humans) * range)
    blue = 0
  else:
    red = 0
    green = 255
    blue = 0
    
  red = clamp(red)
  blue = clamp(blue)
  green = clamp(green)
  
  rgb = (red, green, blue)
  #print(rgb)
  return rgb
  
def set_display(temp):
  c = color_from_temp(-40, 120, temp)
  
  image = []
  pixels = 64
  for i in range(pixels):
    image.append(c)
    
  sense.set_pixels(image)
  
while True:
  set_display(sense.get_temperature())
  sleep(0.1)
  
#test
#for i in range(-40, 120):
#  sleep(0.1)
#  set_display(i)
