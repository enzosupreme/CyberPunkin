import neopixel
import time
import board
import adafruit_tcs34725
from digitalio import DigitalInOut, Direction, Pull
from adafruit_debouncer import Debouncer
from colorpallette import colors



numpix = 8
pixpin = board.D11

ORDER = neopixel.GRB

col =[
    colors.CYBER,
    colors.MINT,
    colors.GREEN,
    colors.BLUE,
    colors.NEON,
    colors.MAGENTA
]
pixels = neopixel.NeoPixel(pixpin, numpix, brightness=.3, auto_write=False,pixel_order = ORDER)



i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_tcs34725.TCS34725(i2c)

sensor.integration_time = 20
off = sensor.active
sensor.active = False

while True:
    #if not a.value:

    color = sensor.color
    color_rgb = sensor.color
    print(
            "RGB color as 8 bits per channel int: #{0:02X} or as 3-tuple: {1}".format(
            color, color_rgb
        )
    )

    # Read the color temperature and lux of the sensor too.
    temp = sensor.color_temperature
    lux = sensor.lux

    last_color = color_rgb
    for i in range(0,numpix):
        pixels[i] = last_color
        time.sleep(0.07)
        pixels.show()


    time.sleep(0.005)

