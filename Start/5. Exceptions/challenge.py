# Example file for Advanced Python by Joe Marini
# Programming challenge for working with Exceptions

# Implement the InvalidTempError exception class here
class InvalidTempError(Exception):
    """Raised when the temperature is too cold or too hot"""
    def __init__(self, temp):
        self.temp = temp
        if temp < 100:
            self.message = f"Oven is not hot enough."
        elif temp > 500:
            self.message = f"Warning! Oven is too hot!"
        super().__init__(self.message)

class DigitalOven:
    def __init__(self):
        self.temp = 0

    def set_temp(self, temp):
        self.temp = temp
        if 0 < temp < 100:
            raise InvalidTempError(temp)
        elif temp > 500:
            raise InvalidTempError(temp)

    def get_temp(self):
        return self.temp

def test_oven(test_temp):
    global oven
    try:
        oven.set_temp(test_temp)
    except InvalidTempError as e:
        print(e)
    finally:
        print(f"Current temp setting is {oven.get_temp()}\n")

# An "InvalidTempError" Exception should be raised if the temperature
# is set below 100 degrees or above 500 degrees
oven = DigitalOven()
test_oven(250)
test_oven(50)
test_oven(0)
test_oven(600)
