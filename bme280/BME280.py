import smbus2
import bme280
import time
import csv
import os
import datetime

def write_log(data, head=False):
    with open("log.csv", "a+", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        if head:
            writer.writerow(["Time", "Temperature", "Pressure", "Humidity"])
        else:
            writer.writerow(data)
port = 1
address = 0x76
bus = smbus2.SMBus(port)

if os.path.exists("log.txt"):
    pass
else:
    write_log("", head=True)

calibration_params = bme280.load_calibration_params(bus, address)

while True:
    data = bme280.sample(bus, address, calibration_params)
    now = datetime.datetime.now()
    time_string = now.strftime("%Y/%m/%d %H:%M:%S")
    temperature = "{:.2f}".format(data.temperature)
    pressure = "{:.2f}".format(data.pressure)
    humidity = "{:.2f}".format(data.humidity)
    print("Time:", time_string)
    print("Temperature:", temperature, "°C")
    print("Pressure:", pressure, "hPa")
    print("Humidity:", humidity, "% rH")
    string_data = [time_string, temperature, pressure, humidity]
    write_log(string_data)
    print("-"*60)
    time.sleep(60)