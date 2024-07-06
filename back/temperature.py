FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit -32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) -32
    return fahrenheit

def main():
    Temperature = float(input("Enter the temperature to convert:"))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")


    if unit == 'C':
        CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
        converted_temperature = (Temperature * CELSIUS_TO_FAHRENHEIT_FACTOR ) + 32
        print(f"{Temperature}°C is {converted_temperature}°F")

    elif unit == 'F':
        FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
        converted_temperature = (Temperature -32)* FAHRENHEIT_TO_CELSIUS_FACTOR
        print(f"{Temperature}°F if {converted_temperature }°C")

    else:
        print("Invalid Temperature or Unit!")
main()
        

