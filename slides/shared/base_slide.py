from manim_slides import Slide
from manim import *

class BaseSlide:
    
    # Talk meta
    TALK_TITLE = 'Talk Title: A Sample Manim Talk Template'
    SHORT_TITLE = 'Talk Title: Short Title'
    
    TALK_AUTHORS = '<u>John Doe</u> and Jane Doe'
    SHORT_AUTHORS = '<u>John Doe</u>, Jane Doe'
    
    FOOTER_FONT_SIZE = 20
    BACKGROUND_COLOR = WHITE
    FONT_COLOR = BLACK
    
    
    # Slide specific
    TITLE = None  # Subclasses override
    
    TITLE_FONT_SIZE = 48
    
    def __init__(self, slide: Slide, show_footer=True, slide_no=9, slide_total=99):
        
        self.slide = slide
        slide.camera.background_color = self.BACKGROUND_COLOR  # White bg for all slides
        
        if self.TITLE:
            _title = Text(self.TITLE, color=self.FONT_COLOR, font_size=self.TITLE_FONT_SIZE).to_corner(UL)
            slide.add(_title)
            
        if show_footer:
            _slide_count = Text(f'{slide_no}/{slide_total}', font_size=self.FOOTER_FONT_SIZE, color=self.FONT_COLOR).to_corner(DR)
            _footer_title = MarkupText(self.SHORT_TITLE, font_size=self.FOOTER_FONT_SIZE, color=self.FONT_COLOR).to_edge(DL)
            _authors = MarkupText(self.SHORT_AUTHORS, font_size=self.FOOTER_FONT_SIZE, color=self.FONT_COLOR).to_corner(DOWN)
            slide.add(_slide_count, _authors, _footer_title)
        
        self.create_content()


    def create_content(self):
        pass  # Override per slide

    
    def pause(self):
        self.slide.wait()
        self.slide.next_slide()
        self.slide.clear()

