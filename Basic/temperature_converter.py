from temperature import Temperature1


print("For temperature converter please choose on of the following")
print(" 1. For Fahrenheit to Celsius")
print(" 2. For Celsius to Fahrenheit")
print(" 3. For Fahrenheit to Kelvin")
print(" 4. For Celsius to Kelvin")
print(" 5. For Kelvin to Fahrenheit")
print(" 6. For Kelvin to Celsius")

choosen = int(input("Choose one from 1 to 6 for your required conversion: "))
temp_object = Temperature1()

if choosen == 1:
    fahrenheit = float(input("Enter the Fahrenheit you want to convert: "))
    celsius = temp_object.Fahrenheit_to_Celsius(fahrenheit)
    print(f"Your given tempertaure is converted to celsius is {celsius:.2f}°C")

elif choosen == 2:
    celsius = float(input("Enter the Celsius you want to convert: "))
    fahrenheit = temp_object.Celsius_to_Fahrenheit(celsius)
    print(f"Your given temperture is converted to fahrenheit is {fahrenheit:.2f}°F")

elif choosen == 3:
        fahrenheit = float(input("Enter the Fahrenheit you want to convert: "))
        kelvin = temp_object.Fahrenheit_to_Kelvin(fahrenheit)
        print(f"Your given temperture is converted to Kelvin is {kelvin:.2f}°K")

elif choosen == 4:
        celsius = float(input("Enter the Celsius you want to convert: "))
        kelvin = temp_object.Celsius_to_Kelvin(celsius)
        print(f"Your given temperture is converted to Kelvin is {kelvin:.2f}°K")

elif choosen == 5:
        kelvin = float(input("Enter the Kelvin you want to convert: "))
        fahrenheit = temp_object.Kelvin_to_Fahrenheit(kelvin)
        print(f"Your given temperture is converted to Fahrenheit is {fahrenheit:.2f}°F")

elif choosen == 6:
        kelvin = float(input("Enter the Kelvin you want to convert: "))
        celsius = temp_object.Kelvin_to_Celsius(kelvin)
        print(f"Your given temperture is converted to Celcius is {celsius:.2f}°C")

else:
    print("Your choice is invalid, Please choose from 1 to 6 only.")
