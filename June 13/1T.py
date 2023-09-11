from random import randint


class Lamp:
    brightness = 0
    durability = 0
    energy_efficiency = 0
    color = ''
    power_source = ''
    type = 'LED'
    batteries = 0

    def __init__(self, energy_efficiency, color, power_source):
        self.brightness = randint(450, 1600)
        self.durability = randint(1000, 10000)
        self.energy_efficiency = energy_efficiency
        self.color = color
        self.power_source = power_source

    def __repr__(self):
        message = "FAQ: Lamp type - %s, durability - %s, color - %s, energy efficiency - %s." % (self.type,
                                                                                                 self.durability,
                                                                                                 self.color,
                                                                                                 self.energy_efficiency)
        return message

    def turn_on(self):
        if self.energy_efficiency >= self.brightness / 75:
            print("Lights ON!")
            return "Lamp type - %s. Your lamp is using %sW and puts out %s lumens of light." % (self.type,
                                                                                                self.energy_efficiency,
                                                                                                self.brightness)
        else:
            return "Not enough energy..."

    def eco_mode(self):
        self.brightness /= 2
        self.energy_efficiency /= 2
        return "Lamp is now on ECO mode!"

    def turn_off(self):
        self.brightness = 0
        return "Lights OFF..."

    def charge(self):
        if self.power_source == 'batteries':
            if self.batteries <= 10:
                self.batteries += randint(0, 100)
                return "Now your lamp charged to - %s%%!" % self.batteries
            else:
                return "Everything is OK."
        else:
            return "Your lamp can not charge!"


my_lamp = Lamp(10, 'white', 'batteries')
print(my_lamp)
print(my_lamp.turn_on())
print(my_lamp.turn_off())
print(my_lamp.eco_mode())
print(my_lamp.charge())
