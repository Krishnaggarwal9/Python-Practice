class Temperature1:
    def Fahrenheit_to_Celsius(self,Fahrenheit):
        return 5/9*(Fahrenheit - 32)
    
    def Celsius_to_Fahrenheit(self,Celsius):
        return (9/5 * Celsius)+32

    def Fahrenheit_to_Kelvin(self,Fahrenheit):
        return (5/9*(Fahrenheit - 32))+273.15

    def Celsius_to_Kelvin(self,Celsius):
        return Celsius + 273.15

    def Kelvin_to_Fahrenheit(self,Kelvin):
        return ((Kelvin - 273.15)*9/5)+32

    def Kelvin_to_Celsius(self,Kelvin):
        return Kelvin - 273.15
    