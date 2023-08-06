# Temper-Windows
Allows you to access the temperature in celsius of a Temper USB device on Windows. 

## Installation
    pip install temper-windows

## Demo
    import temper_windows
    
    temperature = temper_windows.get_temperature()
    print(temperature)

    
    >>> 21.26
    
#### Notes
1. I only have the TemperX to test on so it may not work on others. Pull requests welcome if it doesn't.
2. Tested on Python 3.6 and 2.7 although will most likely work on earlier versions too.