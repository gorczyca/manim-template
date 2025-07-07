from manim import *

from shared import BaseSlide



class Slide1(BaseSlide):
    TITLE = "Hello"

    def create_content(self):
        eq = MathTex(r"E=mc^2", r"\text{not true}" , color=self.FONT_COLOR)
        self.slide.add(eq)