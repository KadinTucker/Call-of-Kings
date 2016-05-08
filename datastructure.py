#Test Data Structure for Call of Kings

class tile():
    def __init__(self):
        self.settlement=None
        self.coordinates=(0,0)
        self.terrain=None

class terrain(object):
    def __init__(self):
        self.resources=[]
        self.image=None
        self.type=None

class resource(object):
    def __init__(self):
        self.type=None
        self.name=None

class settlement(object):
    def __init__(self):
        self.size=1
        self.sizelimit=3
        self.inventory=[]
        self.tile=None
        self.image=None
        self.type=None
        
class village(settlement):
    def __init__(self):
        super(village, self).__init__()
        self.workers=[]
        self.productivity=0
        self.link=None
        self.type='village'
        
class castle(settlement):
    def __init__(self):
        super(village, self).__init__()
        self.garrison=0
        self.lord=None
        self.villages=[]
        self.type='castle'
        
class city(settlement):
    def __init__(self):
        super(village, self).__init__()
        self.sizelimit=6
        self.workers=[]
        self.productivity=0
        self.garrison=0
        self.lord=None
        self.villages=[]
        self.type='city'

class worker(object):
    def __init__(self):
        self.settlement=None
        self.product=None
        
class merchant(worker):
    def __init__(self):
        super(merchant, self).__init__()
        self.linkvillage=None
        self.discount=0.05
        

class vassal(object):
    def __init__(self):
        self.morale=0
        self.court=[]
        self.type=None
        
class lord(vassal):
    def __init__(self):
        super(lord, self).__init__()
        self.type='ruler'
        self.feastfood=0
        
class general(vassal):
    def __init__(self):
        super(general, self).__init__()
        self.army=0
        self.supplies=[]
        
            
        




    
