class vassal(object):
    def __init__(self):
        self.base_morale = 30
        self.morale = 0
        self.type = None
    def getMorale(self):
        return self.morale + self.base_morale
        
class lord(vassal):
    def __init__(self):
        super(lord, self).__init__()
        self.type = 'lord'
        self.court = []
        self.feastfood=0
        
class general(vassal):
    def __init__(self):
        super(general, self).__init__()
        self.army = 0
        self.type = 'general'
        self.supplies=[]
