import Fordon
class lastbil:

    def __init__(self,fabrikt,color, flakvolym):
        self.flakvolym = flakvolym
        self.fabrikat = fabrikt
        self.color = color


    def set_flakvolym(self, flakvolym):
        self.flakvolym = flakvolym

    def get_flakvolym(self):
        return self.flakvolym

    def print_Fordon(self):
        print(self.fabrikat +"Färg: "+ self.color + "flakvolym= "+ str(self.flakvolym))

