from manim import *
from manim_slides import Slide


from slides.shared.base_slide import BaseSlide
from slides.shared.wrappers import *



class Slide1(BaseSlide):
    TITLE = "Hello"

    def create_content(self):
        slide = self.slide
        
        eq = MathTexWrapper(r"a\land b \land c", r"\limplies s")
        slide.add(eq)
        slide.wait()
        slide.next_slide()
        eq2 = MathTexWrapper(r"a\land b \land c", r"\land d", r"\limplies s")
        
        # transform matching chunks
        slide.play(
            TransformMatchingTex(eq, eq2)
        )
        eq = eq2
        
        # animate scaling up
        slide.next_slide()
        slide.play(
            
            eq.animate.scale(2)
        )
        
        # animate scaling up, show positioning relative to the slide
        slide.next_slide()
        slide.play(
            eq.animate.scale(0.5).to_corner(UR)
        )
        
        slide.next_slide()
        
        # absolute positioning
        slide.play(
            eq.animate.move_to([-1, -1, 0])
        )
        
        # surrouding rectangle
        # get relevant part
        slide.next_slide()
        part_to_surround = eq.get_part_by_tex(r"a\land b \land c")
        rect = SurroundingRectangle(part_to_surround, color=BLUE, buff=0.2)
        slide.play(Create(rect))  
              
        slide.next_slide()
        slide.play(FadeOut(rect))
        
        # add another formula, put if below the first one, then create a group and move the entire group together
        eq3 = MathTexWrapper(r"x\limplies y").next_to(eq, DOWN, aligned_edge=LEFT)
        slide.next_slide()
        slide.play(FadeIn(eq3))
        
        #
        slide.next_slide()
        gr = VGroup(eq3, eq)
        
        slide.play(
            gr.animate.to_edge(RIGHT)
        )

        slide.next_slide()
        
        
        # add rectangle around
        rect2 = SurroundingRectangle(gr, color=GREEN, fill_color=GREEN, fill_opacity=0.1)
        slide.add(rect2)
        slide.play(
            GrowFromEdge(rect2, LEFT)
        )
        
        # add the rectangle to the group
        gr1 = VGroup(gr, rect2)
        
        # transform into something else
        # create many things, add them into a group, position the group where the rectangle is, transform one into the other
        
        slide.next_slide()
        e = MathTexWrapper(r"E=mc^2").move_to(gr1.get_center())
        c = MathTexWrapper(r"C=2\pi r").next_to(e, DOWN, aligned_edge=LEFT)
        p = MathTexWrapper(r"a^2+b^2=c^2").next_to(c, DOWN, aligned_edge=LEFT)
        
        circ = Circle(radius=1.5, color=RED, fill_color=RED, fill_opacity=0.1).move_to(c.get_center())
        
        gr2 = VGroup(e,c,p, circ)
        # slide.bring_to_back(circ)
        
        slide.play(Transform(gr1, gr2))
        
        slide.next_slide()
        slide.play(FadeOut(gr1), FadeOut(gr2))
        
        slide.next_slide()
        
        table = Table(
            [["First", "Second"],
            ["Third","Fourth"]],
            row_labels=[Text("R1", color=BLACK), Text("R2", color=BLACK)],
            col_labels=[Text("C1", color=BLACK), Text("C2", color=BLACK)],
            top_left_entry=Text("TOP"),
            line_config={"stroke_color": BLACK},
            )
        for mob in table.get_entries():
            mob.set_color(BLACK)

        slide.play(Create(table))
        
        slide.next_slide()
    
        cell = table.get_cell((2, 2))
        highlight = SurroundingRectangle(cell, stroke_width=0, buff=0, fill_color=GREEN, fill_opacity=0.5)
        
        slide.play(FadeIn(highlight))

        
        
        
        
        
# to be run as standalone
# i.e. by only `manim slide1.py Slide1Scene`
class Slide1Scene(Slide):  
    def construct(self):
        Slide1(self)
        self.wait()