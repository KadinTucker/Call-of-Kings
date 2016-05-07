import settlement
import resource
import terrain
import vassal

class worker():
    def __init__(self):
        self.settlement = None
        self.product = None
    def gather(self):
        if self.settlement.type == 'village' and self.product != None:
            for i in range(self.settlement.link.lord.getMorale() + self.settlement.productivity):
                self.settlement.inventory.append(self.product())


        
