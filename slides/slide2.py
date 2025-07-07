from manim import *
from manim_slides import Slide

from shared import BaseSlide



class Slide2(BaseSlide):
    TITLE = "Slide2"
    def create_content(self):
        eq = MathTex(r"E=mc^2", color=self.FONT_COLOR)
        self.slide.add(eq)
        
        
# to be run as standalone
# i.e. by only `manim slide2.py Slide2Scene`
class Slide2Scene(Slide):  
    def construct(self):
        Slide2(self)
        self.wait()