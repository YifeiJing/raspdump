import smbus2
import bme280

port = 1
address = 0x76 # 这里根据第2步中i2cdetect -y 1的结果填写0x77或0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

data = bme280.sample(bus, address, calibration_params) # 通过这一行，可以获取数据

print(data.id)
print(data.timestamp)
print(data.temperature) # 温度
print(data.pressure) # 压力
print(data.humidity) # 湿度