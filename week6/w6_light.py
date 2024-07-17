class LightBulb:
    def __init__(self, room):
        self._room = room       # protected attribute, sub classes can access directly
        self._light = False     # protected attribute, sub classes can access directly

    def show(self):
        if self._light == True:
            status = 'on'
        else:
            status = 'off'
        
        print(f'Light is {status} in {self._room}')
    
    def turn_on(self):
        self._light = True
        print(f'Light is on')
    
    def turn_off(self):
        self._light = False
        print(f'Light is off')

if __name__ == '__main__':
    lb = LightBulb('Living Room')
    lb.show()
    lb.turn_on()
    lb.show()
    lb.turn_off()
    lb.show()