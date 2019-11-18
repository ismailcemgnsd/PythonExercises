temperature = eval(input("Enter the temperature in Fahrenheit between -58 and 41: "))
windSpeed = eval(input("Enter the wind speed in miles per hour: "))

t = 35.74 + 0.6215 * temperature - 35.75 * windSpeed ** 0.16 + 0.4275 * temperature * windSpeed ** 0.16
if windSpeed >= 2 and -58 < temperature < 41:
    print("The wind chill index is", t)
else:
    print("The temperature and/or wind speed is invalid.")