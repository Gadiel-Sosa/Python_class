class Color:
    def __init__(self, color):
        self._color = color
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, nuevo_color):
        self._color = nuevo_color
        
        