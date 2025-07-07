from manim import *
from manim_slides import Slide


from slides.shared.base_slide import BaseSlide



class Slide1(BaseSlide):
    TITLE = "Hello"

    def create_content(self):
        eq = MathTex(r"E=mc^2", r"\text{not true}" , color=self.FONT_COLOR)
        self.slide.add(eq)
        
        
# to be run as standalone
# i.e. by only `manim slide1.py Slide1Scene`
class Slide1Scene(Slide):  
    def construct(self):
        Slide1(self)
        self.wait()