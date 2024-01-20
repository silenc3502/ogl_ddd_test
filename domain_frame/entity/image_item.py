class ImageItem:
    def __init__(self, path, position, size, translation=(0, 0)):
        self.path = path
        self.position = position
        self.size = size
        self.translation = translation

    def translate(self, translation):
        self.translation = translation
