import Fordon

class personbil:

    def __init__ (self,fabrikt,color, bagagevolym):
        self.bagagevolym = bagagevolym
        self.fabrikat = fabrikt
        self.color = color


    def set_bagagevolym(self, bagagevolym):
        self.bagagevolym = bagagevolym

    def get_bagagevolym(self):
        return self.bagagevolym

    def print_Fordon(self):
        print(self.fabrikat +"Färg: "+ self.color + "bagagevolym= "+ str(self.bagagevolym))