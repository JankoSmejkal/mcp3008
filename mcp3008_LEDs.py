# Import libraries
import Adafruit_MCP3008
import RPi.GPIO as GPIO

#Led pins (BCM)
led_1 = 26
led_2 = 19
led_3 = 13
led_4 = 6
led_5 = 21
led_6 = 20

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_1, GPIO.OUT)
GPIO.setup(led_2, GPIO.OUT)
GPIO.setup(led_3, GPIO.OUT)
GPIO.setup(led_4, GPIO.OUT)
GPIO.setup(led_5, GPIO.OUT)
GPIO.setup(led_6, GPIO.OUT)

# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Main loop
try:
    while True:
        # Read the ADC channel, normalize and round it to two decimal places
        value = round((mcp.read_adc(0) / 1023),2)
        # Uncomment the line below if you want to print out the value
        #print(value)
        if value == 0.0:
            GPIO.output(led_1, False)
            GPIO.output(led_2, False)
            GPIO.output(led_3, False)
            GPIO.output(led_4, False)
            GPIO.output(led_5, False)
            GPIO.output(led_6, False)
        if value > 0 and value < 0.2:
            GPIO.output(led_1, True)
            GPIO.output(led_2, False)
            GPIO.output(led_3, False)
            GPIO.output(led_4, False)
            GPIO.output(led_5, False)
            GPIO.output(led_6, False)
        if value >= 0.2 and value < 0.4:
            GPIO.output(led_2, True)
            GPIO.output(led_3, False)
            GPIO.output(led_4, False)
            GPIO.output(led_5, False)
            GPIO.output(led_6, False)
        if value >= 0.4 and value < 0.6:
            GPIO.output(led_3, True)
            GPIO.output(led_4, False)
            GPIO.output(led_5, False)
            GPIO.output(led_6, False)
        if value >= 0.6 and value < 0.8:
            GPIO.output(led_4, True)
            GPIO.output(led_5, False)
            GPIO.output(led_6, False)
        if value >= 0.8 and value < 1:
            GPIO.output(led_5, True)
            GPIO.output(led_6, False)
        if value == 1:
            GPIO.output(led_6, True)
            
except KeyboardInterrupt:
    GPIO.cleanup()
    

