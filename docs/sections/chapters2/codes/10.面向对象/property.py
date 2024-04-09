class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        print("Setting value")
        self._temperature = value


c = Celsius()
c.temperature = 37  # Setting value
print(c.temperature)  # Getting value，然后输出 37
print(c.to_fahrenheit())  # 输出 98.60000000000001
c.temperature = -300  # 抛出 ValueError: Temperature below -273.15 is not possible
