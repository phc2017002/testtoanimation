from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import numpy as np

class BubbleSortExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        # Introduction
        self.introduction()
        
        # Algorithm explanation
        self.algorithm_overview()
        
        # Visual demonstration
        self.visual_demonstration()
        
        # Complexity analysis
        self.complexity_analysis()
        
        # Conclusion
        self.conclusion()

    def introduction(self):
        with self.voiceover(text="Welcome! Today we will explore the Bubble Sort algorithm, one of the simplest sorting algorithms in computer science.") as tracker:
            title = Text("Bubble Sort Algorithm", font_size=48, color=BLUE, weight=BOLD)
            title.move_to(ORIGIN)
            self.play(Write(title))
            self.wait(0.5)
        
        self.play(FadeOut(title))

    def algorithm_overview(self):
        with self.voiceover(text="Bubble Sort works by repeatedly stepping through the list, comparing adjacent elements, and swapping them if they are in the wrong order.") as tracker:
            overview_title = Text("How It Works", font_size=40, color=YELLOW)
            overview_title.to_edge(UP)
            self.play(Write(overview_title))
            
            steps = VGroup(
                Text("1. Compare adjacent elements", font_size=24),
                Text("2. Swap if in wrong order", font_size=24),
                Text("3. Repeat until sorted", font_size=24)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
            steps.move_to(ORIGIN)
            
            self.play(Write(steps[0]))
            self.wait(0.3)
            self.play(Write(steps[1]))
            self.wait(0.3)
            self.play(Write(steps[2]))
        
        self.play(FadeOut(overview_title), FadeOut(steps))

    def visual_demonstration(self):
        with self.voiceover(text="Let's visualize this with an example. Here we have an unsorted array of numbers.") as tracker:
            demo_title = Text("Visual Demonstration", font_size=40, color=GREEN)
            demo_title.to_edge(UP)
            self.play(Write(demo_title))
            
            # Create array
            array_values = [5, 2, 8, 1, 9]
            bars = self.create_bars(array_values)
            bars.move_to(ORIGIN).shift(DOWN * 0.5)
            self.play(Create(bars))
        
        with self.voiceover(text="We start by comparing the first two elements. Five is greater than two, so we swap them.") as tracker:
            # First pass - compare 5 and 2
            self.highlight_comparison(bars, 0, 1)
            self.swap_bars(bars, 0, 1, array_values)
        
        with self.voiceover(text="Now we compare five and eight. They are already in order, so no swap is needed.") as tracker:
            # Compare 5 and 8
            self.highlight_comparison(bars, 1, 2)
            self.wait(0.5)
        
        with self.voiceover(text="Next, eight and one. Eight is larger, so we swap them.") as tracker:
            # Compare 8 and 1
            self.highlight_comparison(bars, 2, 3)
            self.swap_bars(bars, 2, 3, array_values)
        
        with self.voiceover(text="Finally, eight and nine are in order. The largest element has bubbled to the end.") as tracker:
            # Compare 8 and 9
            self.highlight_comparison(bars, 3, 4)
            self.wait(0.5)
            
            # Mark last element as sorted
            bars[4].set_color(GREEN)
        
        with self.voiceover(text="We repeat this process, each time the next largest element bubbles to its correct position.") as tracker:
            # Continue sorting
            self.continue_sorting(bars, array_values)
        
        self.play(FadeOut(demo_title), FadeOut(bars))

    def create_bars(self, values):
        bars = VGroup()
        colors = [BLUE, BLUE, BLUE, BLUE, BLUE]
        max_val = max(values)
        
        for i, val in enumerate(values):
            height = (val / max_val) * 2
            bar = Rectangle(width=0.8, height=height, fill_opacity=0.8, color=colors[i])
            label = Text(str(val), font_size=24, color=WHITE)
            label.move_to(bar.get_center())
            bar_group = VGroup(bar, label)
            bars.add(bar_group)
        
        bars.arrange(RIGHT, buff=0.3)
        return bars

    def highlight_comparison(self, bars, i, j):
        bars[i][0].set_color(YELLOW)
        bars[j][0].set_color(YELLOW)
        self.wait(0.3)

    def swap_bars(self, bars, i, j, array_values):
        # Swap in array
        array_values[i], array_values[j] = array_values[j], array_values[i]
        
        # Animate swap
        pos_i = bars[i].get_center()
        pos_j = bars[j].get_center()
        
        self.play(
            bars[i].animate.move_to(pos_j),
            bars[j].animate.move_to(pos_i),
            run_time=0.5
        )
        
        # Swap in VGroup
        bars.submobjects[i], bars.submobjects[j] = bars.submobjects[j], bars.submobjects[i]
        
        # Reset colors
        bars[i][0].set_color(BLUE)
        bars[j][0].set_color(BLUE)

    def continue_sorting(self, bars, array_values):
        n = len(array_values)
        
        for i in range(1, n - 1):
            for j in range(0, n - i - 1):
                self.highlight_comparison(bars, j, j + 1)
                
                if array_values[j] > array_values[j + 1]:
                    self.swap_bars(bars, j, j + 1, array_values)
                else:
                    bars[j][0].set_color(BLUE)
                    bars[j + 1][0].set_color(BLUE)
                    self.wait(0.2)
            
            # Mark as sorted
            bars[n - i - 1][0].set_color(GREEN)
        
        # Mark first element as sorted
        bars[0][0].set_color(GREEN)
        self.wait(0.5)

    def complexity_analysis(self):
        with self.voiceover(text="Now let's analyze the time complexity. Bubble sort has a worst-case and average time complexity of O of n squared.") as tracker:
            complexity_title = Text("Time Complexity", font_size=40, color=ORANGE)
            complexity_title.to_edge(UP)
            self.play(Write(complexity_title))
            
            # Show complexity equations
            worst_case = MathTex(r"\text{Worst Case: } O(n^2)", font_size=36, color=RED)
            worst_case.move_to(UP * 1)
            
            average_case = MathTex(r"\text{Average Case: } O(n^2)", font_size=36, color=YELLOW)
            average_case.next_to(worst_case, DOWN, buff=0.5)
            
            best_case = MathTex(r"\text{Best Case: } O(n)", font_size=36, color=GREEN)
            best_case.next_to(average_case, DOWN, buff=0.5)
            
            self.play(Write(worst_case))
            self.wait(0.3)
            self.play(Write(average_case))
        
        with self.voiceover(text="However, in the best case, when the array is already sorted, it only takes O of n time.") as tracker:
            self.play(Write(best_case))
        
        with self.voiceover(text="The space complexity is O of 1, as it only requires a constant amount of additional memory.") as tracker:
            space_complexity = MathTex(r"\text{Space Complexity: } O(1)", font_size=36, color=BLUE)
            space_complexity.next_to(best_case, DOWN, buff=0.8)
            self.play(Write(space_complexity))
        
        self.play(FadeOut(complexity_title), FadeOut(worst_case), 
                  FadeOut(average_case), FadeOut(best_case), FadeOut(space_complexity))

    def conclusion(self):
        with self.voiceover(text="In conclusion, while Bubble Sort is simple to understand and implement, it is not efficient for large datasets. Thank you for watching!") as tracker:
            conclusion_title = Text("Summary", font_size=40, color=PURPLE)
            conclusion_title.to_edge(UP)
            self.play(Write(conclusion_title))
            
            pros = Text("✓ Simple to understand", font_size=28, color=GREEN)
            pros.move_to(UP * 1)
            
            cons = Text("✗ Inefficient for large data", font_size=28, color=RED)
            cons.next_to(pros, DOWN, buff=0.8)
            
            self.play(Write(pros))
            self.wait(0.3)
            self.play(Write(cons))
            
            self.wait(0.5)
            
            thanks = Text("Thank You!", font_size=48, color=GOLD, weight=BOLD)
            thanks.move_to(DOWN * 1.5)
            self.play(Write(thanks))
        
        self.play(FadeOut(*self.mobjects))

# Render instructions
if __name__ == "__main__":
    scene = BubbleSortExplanation()
    scene.render()
