from pico2d import *
from canvas_size import *

width = 128
height = 128
class Pattern:
    def __init__(self):
        self.x = None
        self.y = None
        self.image = None
        self.name = None

    def draw(self):
        self.image.clip_draw(0, 0, 128, 128,self.x , self.y, width*0.7, height*0.7)

class Width(Pattern):
    def __init__(self):
        super().__init__()
        self.image = load_image('Pattern\\1.png')
        self.name = '가로선'

class Height(Pattern):
    def __init__(self):
        super().__init__()
        self.image = load_image('Pattern\\2.png')
        self.name = '세로선'
class FoxEar(Pattern):
    def __init__(self):
        super().__init__()
        self.image = load_image('Pattern\\3.png')
        self.name = '여우귀'
class Victory(Pattern):
    def __init__(self):
        super().__init__()
        self.image = load_image('Pattern\\4.png')
        self.name = '브이'
class Thunder(Pattern):
    def __init__(self):
        super().__init__()
        self.image = load_image('Pattern\\5.png')
        self.name = '번개'
class Night(Pattern):
    def __init__(self):
        super().__init__()
        self.image = load_image('Pattern\\6.png')
        self.name = 'N'
class Star(Pattern):
    def __init__(self):
        super().__init__()
        self.image = load_image('Pattern\\7.png')
        self.name = '별'
class Zzz(Pattern):
    def __init__(self):
        super().__init__()
        self.image = load_image('Pattern\\8.png')
        self.name = 'Z'
class diamond(Pattern):
    def __init__(self):
        super().__init__()
        self.image = load_image('Pattern\\9.png')
        self.name = '다이아몬드'
class square(Pattern):
    def __init__(self):
        super().__init__()
        self.image = load_image('Pattern\\10.png')
        self.name = '네모'
class triangle(Pattern):
    def __init__(self):
        super().__init__()
        self.image = load_image('Pattern\\11.png')
        self.name = '세모'
class Black1(Pattern):
    def __init__(self):
        super().__init__()
        self.image = load_image('Pattern\\12.png')
        self.name = '검정1'
class Black2(Pattern):
    def __init__(self):
        super().__init__()
        self.image = load_image('Pattern\\13.png')
        self.name = '검정2'
class Black3(Pattern):
    def __init__(self):
        super().__init__()
        self.image = load_image('Pattern\\14.png')
        self.name = '검정3'
class Black4(Pattern):
    def __init__(self):
        super().__init__()
        self.image = load_image('Pattern\\15.png')
        self.name = '검정4'
class Black5(Pattern):
    def __init__(self):
        super().__init__()
        self.image = load_image('Pattern\\16.png')
        self.name = '검정5'

pattern_set = [Width(), Height(), FoxEar(), Victory(), Thunder(), Night(), Star(), Zzz(), diamond(), square(), triangle(), Black1(), Black2(), Black3(), Black4(), Black5()]
