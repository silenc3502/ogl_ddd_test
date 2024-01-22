import os

from pyopengltk import OpenGLFrame
from OpenGL import GL, GLU

from new_try.entity.battle_field_unit_card_scene import BattleFieldUnitCardScene
from new_try.entity.circle import Circle
from new_try.entity.image_element import ImageElement
from new_try.entity.image_item import ImageItem
from new_try.entity.rectangle import Rectangle
from new_try.entity.unit_card import UnitCard
from new_try.renderer.battle_field_unit_card_frame_renderer import BattleFieldUnitCardFrameRenderer
from new_try.renderer.new_battle_field_unit_card_frame_renderer import NewBattleFieldUnitCardFrameRenderer


class NewBattleFieldUnitCardFrame(OpenGLFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.unit_card_scene_list = []

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        self.width = screen_width
        self.height = screen_height

        self.bind("<Configure>", self.on_resize)

        self.init_shapes()

        current_directory = os.getcwd()
        print("현재 디렉토리:", current_directory)

        self.renderer = NewBattleFieldUnitCardFrameRenderer(self.unit_card_scene_list, self)

    def init_shapes(self):
        first_unit = UnitCard()
        first_unit.init_shapes("images/card1.png")

        second_unit = UnitCard(local_translation=(500, 0))
        second_unit.init_shapes("images/card2.png")

        self.unit_card_scene_list.append(first_unit)
        self.unit_card_scene_list.append(second_unit)

    def apply_global_translation(self, translation):
        for scene in self.unit_card_scene_list:
            for shape in scene.shapes:
                print("apply_global_translation")
                shape.global_translate(translation)


    def initgl(self):
        GL.glClearColor(1.0, 1.0, 1.0, 0.0)
        GL.glOrtho(0, self.width, self.height, 0, -1, 1)

    def toggle_visibility(self):
        for scene in self.unit_card_scene_list:
            attached_tool_card = scene.shapes[0]
            attached_tool_card.set_visible(not attached_tool_card.get_visible())

            equipped_mark = scene.shapes[3]
            equipped_mark.set_visible(not equipped_mark.get_visible())

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
        self.apply_global_translation((50, 50))
        self.renderer.render()

