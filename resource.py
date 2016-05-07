#The resources in the game.
from datastructure import resource

class silk(resource):
    def __init__(self):
        super(silk, self).__init__()
        self.type = 'raw'
        self.name  = 'silk'

class dye(resource):
    def __init__(self):
        super(dye, self).__init__()
        self.type = 'raw'
        self.name  = 'dye'

class flax(resource):
    def __init__(self):
        super(flax, self).__init__()
        self.type = 'raw'
        self.name  = 'flax'

class wool(resource):
    def __init__(self):
        super(wool, self).__init__()
        self.type = 'raw'
        self.name  = 'wool'

class hide(resource):
    def __init__(self):
        super(hide, self).__init__()
        self.type = 'raw'
        self.name  = 'hide'

class fur(resource):
    def __init__(self):
        super(fur, self).__init__()
        self.type = 'raw'
        self.name  = 'fur'

class clay(resource):
    def __init__(self):
        super(clay, self).__init__()
        self.type = 'raw'
        self.name  = 'clay'

class water(resource):
    def __init__(self):
        super(water, self).__init__()
        self.type = 'raw'
        self.name  = 'water'

class metal(resource):
    def __init__(self):
        super(metal, self).__init__()
        self.type = 'raw'
        self.name  = 'metal'
        
class grapes(resource):
    def __init__(self):
        super(grapes, self).__init__()
        self.type = 'raw'
        self.name  = 'grapes'

class hay(resource):
    def __init__(self):
        super(hay, self).__init__()
        self.type = 'raw'
        self.name  = 'hay'

class olives(resource):
    def __init__(self):
        super(olives, self).__init__()
        self.type = 'raw'
        self.name  = 'olives'

class salt(resource):
    def __init__(self):
        super(salt, self).__init__()
        self.type = 'raw'
        self.name  = 'salt'

class wood(resource):
    def __init__(self):
        super(wood, self).__init__()
        self.type = 'raw'
        self.name  = 'wood'

class herbs(resource):
    def __init__(self):
        super(herbs, self).__init__()
        self.type = 'raw'
        self.name  = 'herbs'

class grain(resource):
    def __init__(self):
        super(grain, self).__init__()
        self.type = 'rawfood'
        self.name  = 'grain'

class meat(resource):
    def __init__(self):
        super(meat, self).__init__()
        self.type = 'rawfood'
        self.name  = 'meat'

class vegetable(resource):
    def __init__(self):
        super(vegetable, self).__init__()
        self.type = 'rawfood'
        self.name  = 'vegetable'

class velvet(resource):
    def __init__(self):
        super(velvet, self).__init__()
        self.type = 'manufactured'
        self.name  = 'velvet'
        self.reagents = [silk(), dye()]

class cloth(resource):
    def __init__(self):
        super(cloth, self).__init__()
        self.type = 'manufactured'
        self.name  = 'cloth'
        self.reagents = [flax(), wool()]

class leather(resource):
    def __init__(self):
        super(leather, self).__init__()
        self.type = 'manufactured'
        self.name  = 'leather'
        self.reagents = [hide(), fur()]

class pottery(resource):
    def __init__(self):
        super(pottery, self).__init__()
        self.type = 'tool'
        self.name  = 'cloth'
        self.reagents = [clay(), water()]

class tools(resource):
    def __init__(self):
        super(tools, self).__init__()
        self.type = 'tool'
        self.name  = 'tools'
        self.reagents = [metal(), clay()]

class weapons(resource):
    def __init__(self):
        super(weapons, self).__init__()
        self.type = 'tool'
        self.name  = 'weapons'
        self.reagents = [metal(), water()]

class wine(resource):
    def __init__(self):
        super(cloth, self).__init__()
        self.type = 'manufactured'
        self.name  = 'cloth'
        self.reagents = [grapes(), grapes(), grapes()]

class thatching(resource):
    def __init__(self):
        super(thatching, self).__init__()
        self.type = 'manufactured'
        self.name  = 'thatching'
        self.reagents = [hay(), hay(), hay()]

class oil(resource):
    def __init__(self):
        super(oil, self).__init__()
        self.type = 'manufactured'
        self.name  = 'oil'
        self.reagents = [olives(), olives(), olives()]

class jerky(resource):
    def __init__(self):
        super(jerky, self).__init__()
        self.type = 'manufood'
        self.name  = 'jerky'
        self.reagents = [salt(), meat()]

class bread(resource):
    def __init__(self):
        super(bread, self).__init__()
        self.type = 'manufood'
        self.name  = 'bread'
        self.reagents = [wood(), grain()]

class stew(resource):
    def __init__(self):
        super(stew, self).__init__()
        self.type = 'manufood'
        self.name  = 'stew'
        self.reagents = [herbs(), vegetable()]




