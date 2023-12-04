import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Set the GPIO pin number you want to measure
#gpio_pin = 17
gpio_pin = 14
GPIO.setup(gpio_pin, GPIO.IN)

try:
    while True:
        # Read the voltage on the GPIO pin
        voltage = GPIO.input(gpio_pin)
        print(f"Voltage on GPIO pin {gpio_pin}: {voltage}")
        time.sleep(1)

except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    GPIO.cleanup()

