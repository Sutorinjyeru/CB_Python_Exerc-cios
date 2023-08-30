# Defina uma classe TemperatureConverter com métodos para converter de Celsius para
# Fahrenheit e vice-versa. Mantenha os atributos e métodos privados.

class TemperatureConverter:
    def __init__(self,celcius,farenheit):
        self.__celsius = celcius
        self.__farenheit = farenheit

    def convert_farenheit(self):
        # celcius para farenheit
        return ((self.__celsius * (9/5)) + 32)
    
    def convert_celsius(self): 
        #Farenheit para celsius
        return ((self.__farenheit - 32) * (5 / 9))

objeto = TemperatureConverter(40,40)
print(objeto.convert_celsius())
