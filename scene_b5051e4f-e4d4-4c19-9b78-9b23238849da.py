from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class BubbleSortExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        # Title Scene
        with self.voiceover(text="Welcome! Today we'll explore the Bubble Sort algorithm, one of the simplest sorting algorithms in computer science.") as tracker:
            title = Text("Bubble Sort Algorithm", font_size=48, color=BLUE)
            self.play(Write(title))
        
        self.play(FadeOut(title))
        self.wait(0.5)

        # Introduction to Bubble Sort
        with self.voiceover(text="Bubble Sort works by repeatedly comparing adjacent elements and swapping them if they are in the wrong order.") as tracker:
            intro_text = Text("How Does It Work?", font_size=36, color=GREEN)
            intro_text.move_to(UP * 2)
            self.play(Write(intro_text))
            
            description = Text("Compare adjacent pairs", font_size=24)
            description.next_to(intro_text, DOWN, buff=1)
            self.play(FadeIn(description))
        
        self.play(FadeOut(intro_text), FadeOut(description))
        self.wait(0.5)

        # Show the algorithm steps
        self.visualize_bubble_sort()

        # Time Complexity
        self.explain_complexity()

        # Conclusion
        with self.voiceover(text="And that's how Bubble Sort works! It's simple but not very efficient for large datasets.") as tracker:
            conclusion = Text("Bubble Sort Complete!", font_size=40, color=GOLD)
            self.play(Write(conclusion))
        
        self.play(FadeOut(conclusion))

    def visualize_bubble_sort(self):
        with self.voiceover(text="Let's visualize Bubble Sort with an example array of numbers.") as tracker:
            # Create the initial array
            array = [5, 3, 8, 4, 2]
            bars, numbers = self.create_bar_chart(array)
            
            # Add title
            sort_title = Text("Sorting: [5, 3, 8, 4, 2]", font_size=28)
            sort_title.to_edge(UP, buff=0.5)
            
            self.play(Write(sort_title))
            self.play(Create(bars), Write(numbers))

        # First Pass
        with self.voiceover(text="In the first pass, we start by comparing 5 and 3. Since 5 is greater than 3, we swap them.") as tracker:
            # Highlight first two elements
            self.play(
                bars[0].animate.set_color(YELLOW),
                bars[1].animate.set_color(YELLOW)
            )
            
            # Swap animation
            self.swap_bars(bars, numbers, 0, 1, array)
        
        with self.voiceover(text="Next, we compare 5 and 8. They're already in order, so no swap is needed.") as tracker:
            # Reset colors and highlight next pair
            self.play(
                bars[0].animate.set_color(BLUE),
                bars[1].animate.set_color(YELLOW),
                bars[2].animate.set_color(YELLOW)
            )
        
        with self.voiceover(text="Now comparing 8 and 4. We swap them since 8 is greater.") as tracker:
            self.play(bars[1].animate.set_color(BLUE))
            self.swap_bars(bars, numbers, 2, 3, array)
        
        with self.voiceover(text="Finally, comparing 8 and 2. Another swap is needed.") as tracker:
            self.play(
                bars[2].animate.set_color(BLUE),
                bars[3].animate.set_color(YELLOW),
                bars[4].animate.set_color(YELLOW)
            )
            self.swap_bars(bars, numbers, 3, 4, array)
        
        with self.voiceover(text="After the first pass, the largest element has bubbled to the end.") as tracker:
            self.play(
                bars[3].animate.set_color(BLUE),
                bars[4].animate.set_color(GREEN)
            )

        # Continue sorting
        with self.voiceover(text="We repeat this process for the remaining unsorted elements until the entire array is sorted.") as tracker:
            # Second pass simplified
            self.play(bars[0].animate.set_color(YELLOW), bars[1].animate.set_color(YELLOW))
            self.swap_bars(bars, numbers, 0, 1, array)
            
            self.play(bars[0].animate.set_color(BLUE), bars[1].animate.set_color(YELLOW), bars[2].animate.set_color(YELLOW))
            self.swap_bars(bars, numbers, 1, 2, array)
            
            self.play(bars[1].animate.set_color(BLUE), bars[2].animate.set_color(YELLOW), bars[3].animate.set_color(YELLOW))
            self.swap_bars(bars, numbers, 2, 3, array)
            
            self.play(bars[2].animate.set_color(BLUE), bars[3].animate.set_color(GREEN))
        
        with self.voiceover(text="Continuing with more passes until everything is sorted.") as tracker:
            # Third pass
            self.play(bars[0].animate.set_color(YELLOW), bars[1].animate.set_color(YELLOW))
            self.swap_bars(bars, numbers, 0, 1, array)
            
            self.play(bars[0].animate.set_color(BLUE), bars[1].animate.set_color(YELLOW), bars[2].animate.set_color(YELLOW))
            # No swap needed
            self.play(bars[1].animate.set_color(BLUE), bars[2].animate.set_color(GREEN))
            
            # Final elements
            self.play(bars[0].animate.set_color(YELLOW), bars[1].animate.set_color(YELLOW))
            # No swap
            self.play(bars[0].animate.set_color(GREEN), bars[1].animate.set_color(GREEN))
        
        with self.voiceover(text="And there we have it! The array is now completely sorted.") as tracker:
            final_title = Text("Sorted: [2, 3, 4, 5, 8]", font_size=28, color=GREEN)
            final_title.to_edge(UP, buff=0.5)
            self.play(Transform(sort_title, final_title))
            self.wait(1)
        
        # Cleanup
        self.play(FadeOut(bars), FadeOut(numbers), FadeOut(sort_title))

    def create_bar_chart(self, array):
        bars = VGroup()
        numbers = VGroup()
        
        bar_width = 1
        max_height = 2.5
        max_val = max(array)
        
        for i, val in enumerate(array):
            # Create bar
            height = (val / max_val) * max_height
            bar = Rectangle(width=bar_width, height=height, color=BLUE, fill_opacity=0.7)
            
            # Create number label
            num = Text(str(val), font_size=28)
            
            bars.add(bar)
            numbers.add(num)
        
        # Arrange bars horizontally
        bars.arrange(RIGHT, buff=0.3)
        bars.move_to(ORIGIN)
        
        # Position numbers on top of bars
        for i, (bar, num) in enumerate(zip(bars, numbers)):
            num.next_to(bar, UP, buff=0.2)
        
        return bars, numbers

    def swap_bars(self, bars, numbers, i, j, array):
        # Swap in array
        array[i], array[j] = array[j], array[i]
        
        # Animate swap
        self.play(
            bars[i].animate.shift(RIGHT * 1.3),
            bars[j].animate.shift(LEFT * 1.3),
            numbers[i].animate.shift(RIGHT * 1.3),
            numbers[j].animate.shift(LEFT * 1.3),
            run_time=0.8
        )
        
        # Update the VGroup order
        bars.submobjects[i], bars.submobjects[j] = bars.submobjects[j], bars.submobjects[i]
        numbers.submobjects[i], numbers.submobjects[j] = numbers.submobjects[j], numbers.submobjects[i]

    def explain_complexity(self):
        with self.voiceover(text="Now let's talk about the time complexity of Bubble Sort.") as tracker:
            complexity_title = Text("Time Complexity", font_size=36, color=PURPLE)
            complexity_title.to_edge(UP, buff=0.5)
            self.play(Write(complexity_title))
        
        with self.voiceover(text="In the worst case, Bubble Sort has a time complexity of O of n squared, where n is the number of elements.") as tracker:
            worst_case = MathTex(r"\text{Worst Case: } O(n^2)", font_size=40, color=RED)
            worst_case.move_to(UP * 1)
            self.play(Write(worst_case))
        
        with self.voiceover(text="The best case occurs when the array is already sorted, giving us O of n.") as tracker:
            best_case = MathTex(r"\text{Best Case: } O(n)", font_size=40, color=GREEN)
            best_case.next_to(worst_case, DOWN, buff=0.8)
            self.play(Write(best_case))
        
        with self.voiceover(text="The space complexity is O of 1, since we only need a constant amount of extra space.") as tracker:
            space_complexity = MathTex(r"\text{Space: } O(1)", font_size=40, color=BLUE)
            space_complexity.next_to(best_case, DOWN, buff=0.8)
            self.play(Write(space_complexity))
        
        # Cleanup
        self.play(FadeOut(complexity_title), FadeOut(worst_case), FadeOut(best_case), FadeOut(space_complexity))


# Instructions to run:
# Save this file as bubble_sort.py
# Run: manim -pql bubble_sort.py BubbleSortExplanation
# For high quality: manim -pqh bubble_sort.py BubbleSortExplanation
