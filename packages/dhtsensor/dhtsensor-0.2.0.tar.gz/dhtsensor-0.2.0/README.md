# dhtsensor
Simplifies reading temperature and humidity data from a DHT11/22 sensor using pigpio

## Requirements
- [pigpio daemon](http://abyz.me.uk/rpi/pigpio/pigpiod.html)
- [pigpio Python package](http://abyz.me.uk/rpi/pigpio/python.html)  
```
pip install pigpio
```

## Install
```
pip install dhtsensor
```

## Quickstart
```python
# Create a new Sensor object for a DHT22 temperature and humidity sensor
# GPIO to read from: 21
# GPIO that powers the sensor: 20
from dhtsensor.sensor import Sensor
s = Sensor(pi, 21, powered_by=20)

# Turn on power to the sensor
s.activate()

# Get temperature and humidity measurement from the sensor
# Do not call read_once repeatedly! Use .read instead
reading = s.read_once()

# Temperature and humidity as separate variables
temp, rh = s.read_once()

# Read from the sensor 10 times, with a 5-second interval between reads
# Outputs a list of 10 Reading objects
reading = s.read(10, interval=5)

```

## Acknowledgment
[pigpio Python examples](http://abyz.me.uk/rpi/pigpio/examples.html#Python%20code)

## Contact
kentkawashima@gmail.com


License: MIT License  
