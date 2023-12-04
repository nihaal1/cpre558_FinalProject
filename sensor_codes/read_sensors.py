import RPi.GPIO as GPIO
import time
import board
import adafruit_dht
from threading import Thread

# GPIO Setup for Sound Sensor
sound_channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(sound_channel, GPIO.IN)

# DHT11 Setup
dhtDevice = adafruit_dht.DHT11(board.D4, use_pulseio=False)

def sound_sensor_callback(channel):
    if GPIO.input(channel):
        print("Sound Detected!")

def read_sound_sensor():
    GPIO.add_event_detect(sound_channel, GPIO.BOTH, bouncetime=300)
    GPIO.add_event_callback(sound_channel, sound_sensor_callback)
    while True:
        # This loop will keep running and the callback function will be triggered on sound detection
        time.sleep(1)

def read_dht11_sensor():
    while True:
        try:
            temperature_c = dhtDevice.temperature
            humidity = dhtDevice.humidity
            print(f"Temp: {temperature_c:.1f} C    Humidity: {humidity}% ")
        except RuntimeError as error:
            print(error.args[0])
            time.sleep(2.0)
        except Exception as error:
            dhtDevice.exit()
            raise error
        time.sleep(2.0)

# Run both sensor readings in parallel threads
if __name__ == "__main__":
    Thread(target=read_sound_sensor).start()
    Thread(target=read_dht11_sensor).start()
