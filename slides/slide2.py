from manim import *
from manim_slides import Slide

from slides.shared.base_slide import BaseSlide
from slides.shared.wrappers import MathTexWrapper



class Slide2(BaseSlide):
    TITLE = "Slide2"
    def create_content(self):
        eq = MathTexWrapper(r"E=mc^2, \test \text{-- real numbers}")
        self.slide.add(eq)
        
        
# to be run as standalone
# i.e. by only `manim slide2.py Slide2Scene`
class Slide2Scene(Slide):  
    def construct(self):
        Slide2(self)
        self.wait()