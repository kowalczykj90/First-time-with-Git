"""
OOP example
"""

class Car:
    acceleration = 10

    def __init__(self, registration_number):
        self.registration_number = registration_number
        self.in_motion = False
        self.speed = 0

    def drive(self):
        self.in_motion = True

    def accelerate(self):
        self.speed += self.acceleration

    def stop(self):
        self.in_motion = False
        self.speed = 0

if __name__ == "__main__":
    opel_astra = Car('ELC0001')
    print(opel_astra.speed)
    opel_astra.accelerate()
    print(opel_astra.speed)
    print(type(opel_astra))