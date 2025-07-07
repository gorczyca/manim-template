from manim import *  

# from slides.shared import BaseSlide
from manim_slides import Slide

from slides.slide1 import Slide1 
from slides.slide2 import Slide2 


class SlideDeck(Slide):
    def construct(self):
        
        main_slides = [
            Slide1,
            Slide2,
            
        ]
        
        slides_total = len(main_slides)
        for i, sld in enumerate(main_slides, start=1):
            inst = sld(self)
            inst.pause()
            
            
            
            

            

        
        
