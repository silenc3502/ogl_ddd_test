import abc


class Shape(abc.ABC):
    def __init__(self, color, vertices, translation=(0, 0)):
        self.color = color
        self.vertices = vertices
        self.translation = translation

    def translate(self, translation):
        self.translation = translation

    @abc.abstractmethod
    def draw(self):
        pass
