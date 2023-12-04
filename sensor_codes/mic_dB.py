import time
import board
import busio
import digitalio
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import RPi.GPIO as GPIO

def voltage_to_decibel(voltage, sensitivity):
    reference_voltage = 3.3  # The reference voltage of your ADC
    db = 20 * (1 / reference_voltage) * voltage / sensitivity
    return db

# GPIO SETUP
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def sound_callback(channel):
    if GPIO.input(channel):
        print("Sound Detected!")
        # Now, you can read and print decibel levels, or perform any other desired actions.

# Setup MCP3008 ADC
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D17)  # Change to pin 17
mcp = MCP.MCP3008(spi, cs)
chan = AnalogIn(mcp, MCP.P0)  # Change to the appropriate channel

# You need to determine the sensitivity of your microphone for accurate readings
microphone_sensitivity = 1.0  # Adjust this based on your microphone's specifications

# Set up GPIO event detection
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, sound_callback)

try:
    while True:
        # Read the ADC value when a sound is detected
        if GPIO.event_detected(channel):
            voltage = chan.voltage
            decibel_level = voltage_to_decibel(voltage, microphone_sensitivity)
            print("Raw Value: {}, Voltage: {:.2f} V, Decibel Level: {:.2f} dB".format(chan.value, voltage, decibel_level))
        time.sleep(1)

except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    # Cleanup GPIO resources
    GPIO.cleanup()

