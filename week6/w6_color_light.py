from w6_light import LightBulb

class ColorLightBulb(LightBulb):
    def __init__(self, room):
        # call super class constructor to 
        # init room and light attributes
        super().__init__(room)
        self.__colors = ['white', 'yellow', 'red']
        self.__current = 0

    def show(self):
        # call super class show method
        super().show()
        print(f'Color is {self.__colors[self.__current]}')

    def turn_on(self):
        super().turn_on()
        if self.__current == 2:
            self.__current = 0
        else:
            self.__current += 1
        print(f'Color is {self.__colors[self.__current]}')

if __name__ == '__main__':
    clb = ColorLightBulb('Bedroom')
    clb.show()
    clb.turn_on()
    clb.turn_off()
    clb.turn_on()
    clb.turn_off()
    clb.turn_on()