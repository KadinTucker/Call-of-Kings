import workers

class settlement(object):
    def __init__(self):
        self.location = (0, 0)
        self.size=1
        self.sizelimit=3
        self.inventory=[]
        self.tile=None
        self.image=None
        self.type=None
        
class village(settlement):
    def __init__(self):
        super(village, self).__init__()
        self.workers=[workers.worker()]
        self.productivity=0
        self.link=None
        self.type='village'
        
class castle(settlement):
    def __init__(self):
        super(castle, self).__init__()
        self.garrison=0
        self.lord=None
        self.villages=[]
        self.type='castle'
        
class city(settlement):
    def __init__(self):
        super(city, self).__init__()
        self.sizelimit=6
        self.workers=[]
        self.productivity=0
        self.garrison=0
        self.lord=None
        self.villages=[]
        self.type='city'
