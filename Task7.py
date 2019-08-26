class Vehicle:
    name = "Honda"

    def description(self):
        print('Car model is: '+self.name)

    def start(self):
        print('Car is  moving ')

object1 = Vehicle()

object2 = Vehicle()

object1.description()
object2.start()