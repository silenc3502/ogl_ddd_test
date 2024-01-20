import tkinter as tk
from pyopengltk import OpenGLFrame
from OpenGL import GL, GLU, GLUT
from PIL import Image
import numpy as np

from domain_frame.entity.circle import Circle
from domain_frame.entity.domain_scene import DomainScene
from domain_frame.entity.image_item import ImageItem
from domain_frame.entity.rectangle import Rectangle
from domain_frame.entity.shape import Shape
from domain_frame.renderer.domain_frame_renderer import DomainFrameRenderer


class DomainWindow(OpenGLFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.domain_scene = DomainScene()

        self.width = self.winfo_reqwidth()
        self.height = self.winfo_reqheight()

        self.bind("<Configure>", self.on_resize)

        self.init_shapes()

        self.domain_scene.add_image(
            ImageItem(
                path="images/card1.png",
                position=(25, 25),
                size=(300, 300),
                translation=(0, 0)))

        equip_image = ImageItem(
                path="images/equip_white.jpg",
                position=(390, 30),
                size=(40, 40),
                translation=(0, 0))
        self.domain_scene.add_image(equip_image)
        equip_image.set_visible(False)

        self.renderer = DomainFrameRenderer(self.domain_scene, self)

    def init_shapes(self):
        equip_card = Rectangle(
            color=(0.6, 0.4, 0.6, 1.0),
            vertices=[(0, 0), (350, 0), (350, 500), (0, 500)],
            translation=(20, 20))
        equip_card.set_draw_gradient(True)
        self.domain_scene.add_shape(equip_card)

        # equip_effect = Rectangle(
        #     color=(1.0, 1.0, 1.0, 1.0),
        #     vertices=[(0, 0), (40, 0), (40, 40), (0, 40)],
        #     translation=(390, 30))
        # equip_effect.set_draw_gradient(True)
        # self.domain_scene.add_shape(equip_effect)

        unit_card = Rectangle(
            color=(0.0, 0.78, 0.34, 1.0),
            vertices=[(0, 0), (350, 0), (350, 500), (0, 500)],
            translation=(0, 0))
        unit_card.set_draw_gradient(True)
        self.domain_scene.add_shape(unit_card)

        circle_radius = 30
        circle_center_coordinates = [(0, 0), (350, 0), (350, 500), (0, 500)]
        for center in circle_center_coordinates:
            circle = Circle(
                    color=(1.0, 0.33, 0.34, 1.0),
                    center=center,
                    radius=circle_radius,
                    translation=(0, 0))
            self.domain_scene.add_shape(circle)

        equip_card.set_visible(False)

    def apply_translation(self, translation):
        for shape in self.domain_scene.shapes:
            print("shape translate")
            shape.translate(translation)

        for image in self.domain_scene.images:
            image.translate(translation)

    def initgl(self):
        GL.glClearColor(1.0, 1.0, 1.0, 0.0)
        GL.glOrtho(0, self.width, self.height, 0, -1, 1)

    def toggle_visibility(self):
        equip_card = self.domain_scene.shapes[0]
        equip_card.set_visible(not equip_card.get_visible())

        equip_image = self.domain_scene.images[1]
        equip_image.set_visible(not equip_image.get_visible())

        self.apply_translation((-50, -50))
        self.redraw()

    def reshape(self, width, height):
        GL.glViewport(0, 0, width, height)
        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GLU.gluOrtho2D(0, width, height, 0)
        GL.glMatrixMode(GL.GL_MODELVIEW)
        GL.glLoadIdentity()

    def on_resize(self, event):
        self.reshape(event.width, event.height)

    def redraw(self):
        self.apply_translation((50, 50))
        self.renderer.render()

