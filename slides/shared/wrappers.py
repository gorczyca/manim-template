from manim import *

TEX_TEMPLATE_LOC = 'assets/preamble.tex'


def get_tex_template():
    custom_template = TexTemplate()
    
    with open(TEX_TEMPLATE_LOC) as f:
        preamble = f.read()
        
        print(preamble)
        custom_template.add_to_preamble(preamble)
        
        return custom_template


class MathTexWrapper(MathTex):
    
    FONT_SIZE = 35
    FONT_COLOR = BLACK
    TEX_TEMPLATE = get_tex_template()
    
    def __init__(self, *tex_strings, color=FONT_COLOR, font_size=FONT_SIZE, tex_template=TEX_TEMPLATE):
        super().__init__(*tex_strings, color=color, font_size=font_size, tex_template=tex_template)