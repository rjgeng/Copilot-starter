from enum import Enum, auto, unique
import copy 

class Tortoise:
    """ An object to represent a block of squares. """
    class Types(Enum):
        I = auto()
        O = auto()
        L = auto()
        S = auto()
        T = auto()
        J = auto()
        Z = auto()

    def __init__(self, tortoise_type, color,  index=-1):
        assert isinstance(tortoise_type, Tortoise.Types)
        assert type(color) == tuple
        self.type = tortoise_type
        self.color = color        
        self.placed = False
        if index < 0:
            index = tortoise_dict[tortoise_type]
        self.index = index

    def get_index(self):
        return self.index

    def get_unique_rows(self):
        s = set()
        for pos in self.blocks_pos:
            s.add(pos[1])
        return list(s)

    def place_at(self, coordinate):
        if not self.placed:
            validated_apply(self, lambda pos: add_pos(pos, coordinate), False)
            self.placed = True

    def is_placed(self):
        return self.placed

    def get_blocks_pos(self):        
        return self.blocks_pos[:]

    def get_color(self):        
        return self.color

    def get_type(self):
        return self.type

    def __repr__(self):
        return f"<Tortoise {self.type}, {self.color}>"

@unique
class Color(Enum):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    CYAN = (43, 172, 226)
    YELLOW = (253, 225, 2)
    ORANGE = (247, 150, 34)
    GREEN = (77, 184, 72)
    PURPLE = (146, 44, 140)
    BLUE = (0, 90, 156)
    RED = (238, 40, 51)

tortoise_dict = {
    Tortoise.Types.I: [Color.CYAN.value, 1], 
    Tortoise.Types.O: [Color.YELLOW.value, 2], 
    Tortoise.Types.L: [Color.ORANGE.value, 3], 
    Tortoise.Types.S: [Color.GREEN.value, 4], 
    Tortoise.Types.T: [Color.PURPLE.value, 5], 
    Tortoise.Types.J: [Color.BLUE.value, 6], 
    Tortoise.Types.Z: [Color.RED.value, 7]
    }

def tortoise_factory(tortoise_type):
    arg_lst = tortoise_dict.get(tortoise_type, None)
    if arg_lst is not None:
        color, index = arg_lst
        return Tortoise(tortoise_type, color, index)
    else:
        raise ValueError(f'Unknown block type: {tortoise_type}')
