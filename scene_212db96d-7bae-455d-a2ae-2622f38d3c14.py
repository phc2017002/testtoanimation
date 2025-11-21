from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class QuickSortExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        # Introduction
        with self.voiceover(text="Welcome! Today we'll explore QuickSort, one of the most efficient sorting algorithms.") as tracker:
            title = Text("QuickSort Algorithm", font_size=48, color=BLUE)
            self.play(Write(title))
            self.wait(0.5)
        
        self.play(FadeOut(title))

        # Overview
        self.show_overview()

        # Visual demonstration
        self.demonstrate_quicksort()

        # Time complexity
        self.explain_complexity()

        # Conclusion
        self.show_conclusion()

    def show_overview(self):
        with self.voiceover(text="QuickSort uses a divide and conquer strategy. It picks a pivot element and partitions the array around it.") as tracker:
            overview_title = Text("How QuickSort Works", font_size=36, color=YELLOW)
            overview_title.to_edge(UP)
            
            steps = VGroup(
                Text("1. Choose a pivot element", font_size=24),
                Text("2. Partition array around pivot", font_size=24),
                Text("3. Recursively sort sub-arrays", font_size=24)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
            steps.next_to(overview_title, DOWN, buff=1)
            
            self.play(Write(overview_title))
            self.play(Write(steps), run_time=2)
        
        self.play(FadeOut(overview_title), FadeOut(steps))

    def demonstrate_quicksort(self):
        with self.voiceover(text="Let's visualize QuickSort with an example array containing the numbers 6, 3, 8, 1, 9, 4, and 2.") as tracker:
            demo_title = Text("QuickSort Visualization", font_size=36, color=GREEN)
            demo_title.to_edge(UP)
            self.play(Write(demo_title))

            # Create initial array
            array_values = [6, 3, 8, 1, 9, 4, 2]
            array_boxes = self.create_array_visualization(array_values, position=UP*1.5)
            
            self.play(Create(array_boxes))
        
        with self.voiceover(text="First, we select the last element, 2, as our pivot. We'll highlight it in red.") as tracker:
            # Highlight pivot
            pivot_index = len(array_values) - 1
            self.play(array_boxes[pivot_index][0].animate.set_fill(RED, opacity=0.5))

        with self.voiceover(text="Now we partition the array. Elements smaller than the pivot go to the left, and larger elements go to the right.") as tracker:
            # Show partitioning process
            pivot_value = array_values[pivot_index]
            
            # Create labels for comparison
            comparison_text = Text(f"Comparing with pivot: {pivot_value}", font_size=24, color=ORANGE)
            comparison_text.next_to(array_boxes, DOWN, buff=0.8)
            self.play(Write(comparison_text))

            # Simulate partition
            left_values = [1]
            right_values = [6, 3, 8, 9, 4]
            pivot = [2]

            # Create new arrangement
            left_array = self.create_array_visualization(left_values, position=UP*1.5 + LEFT*3, color=GREEN)
            pivot_array = self.create_array_visualization(pivot, position=UP*1.5, color=RED)
            right_array = self.create_array_visualization(right_values, position=UP*1.5 + RIGHT*2.5, color=BLUE)

            self.play(
                FadeOut(array_boxes),
                FadeOut(comparison_text),
                Create(left_array),
                Create(pivot_array),
                Create(right_array)
            )

        with self.voiceover(text="The pivot is now in its correct position. We recursively apply the same process to the left and right sub-arrays.") as tracker:
            partition_label = Text("After First Partition", font_size=28, color=YELLOW)
            partition_label.next_to(demo_title, DOWN, buff=0.5)
            self.play(Write(partition_label))
            
            # Add labels
            left_label = Text("< 2", font_size=20).next_to(left_array, DOWN, buff=0.3)
            pivot_label = Text("Pivot", font_size=20).next_to(pivot_array, DOWN, buff=0.3)
            right_label = Text("> 2", font_size=20).next_to(right_array, DOWN, buff=0.3)
            
            self.play(Write(left_label), Write(pivot_label), Write(right_label))

        self.play(
            FadeOut(demo_title),
            FadeOut(partition_label),
            FadeOut(left_array), 
            FadeOut(pivot_array), 
            FadeOut(right_array),
            FadeOut(left_label),
            FadeOut(pivot_label),
            FadeOut(right_label)
        )

        with self.voiceover(text="After recursively sorting all partitions, we get the final sorted array: 1, 2, 3, 4, 6, 8, and 9.") as tracker:
            final_title = Text("Sorted Array", font_size=36, color=GREEN)
            final_title.to_edge(UP)
            
            sorted_values = [1, 2, 3, 4, 6, 8, 9]
            sorted_array = self.create_array_visualization(sorted_values, position=ORIGIN, color=GREEN)
            
            self.play(Write(final_title))
            self.play(Create(sorted_array))
            self.wait(0.5)
        
        self.play(FadeOut(final_title), FadeOut(sorted_array))

    def create_array_visualization(self, values, position=ORIGIN, color=BLUE):
        """Create a visual representation of an array with boxes and numbers."""
        boxes = VGroup()
        box_size = 0.7
        
        for i, value in enumerate(values):
            square = Square(side_length=box_size, color=color, stroke_width=3)
            number = Text(str(value), font_size=28, color=WHITE)
            number.move_to(square.get_center())
            
            box_group = VGroup(square, number)
            boxes.add(box_group)
        
        boxes.arrange(RIGHT, buff=0.1)
        boxes.move_to(position)
        return boxes

    def explain_complexity(self):
        with self.voiceover(text="Let's examine QuickSort's time complexity. In the average case, it operates in O of n log n time.") as tracker:
            complexity_title = Text("Time Complexity Analysis", font_size=36, color=PURPLE)
            complexity_title.to_edge(UP)
            self.play(Write(complexity_title))

            # Create complexity equations
            avg_case = MathTex(r"\text{Average Case: } O(n \log n)", font_size=36, color=GREEN)
            avg_case.move_to(UP*1)
            
            worst_case = MathTex(r"\text{Worst Case: } O(n^2)", font_size=36, color=RED)
            worst_case.move_to(ORIGIN)
            
            best_case = MathTex(r"\text{Best Case: } O(n \log n)", font_size=36, color=BLUE)
            best_case.move_to(DOWN*1)

            self.play(Write(avg_case))
            self.wait(0.3)

        with self.voiceover(text="However, in the worst case, when the pivot is always the smallest or largest element, it degrades to O of n squared.") as tracker:
            self.play(Write(worst_case))
            self.wait(0.3)

        with self.voiceover(text="The best case also achieves O of n log n when partitions are balanced.") as tracker:
            self.play(Write(best_case))
            self.wait(0.3)

        self.play(
            FadeOut(complexity_title),
            FadeOut(avg_case),
            FadeOut(worst_case),
            FadeOut(best_case)
        )

    def show_conclusion(self):
        with self.voiceover(text="QuickSort is widely used due to its efficiency and in-place sorting capability. Thank you for watching!") as tracker:
            conclusion_title = Text("Why Use QuickSort?", font_size=36, color=GOLD)
            conclusion_title.to_edge(UP)
            
            advantages = VGroup(
                Text("✓ Fast average performance", font_size=28, color=GREEN),
                Text("✓ In-place sorting", font_size=28, color=GREEN),
                Text("✓ Cache-efficient", font_size=28, color=GREEN)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            advantages.next_to(conclusion_title, DOWN, buff=1)
            
            self.play(Write(conclusion_title))
            self.play(Write(advantages), run_time=2)
            self.wait(1)

        # Final cleanup
        self.play(FadeOut(*self.mobjects))

# Run the animation
if __name__ == "__main__":
    scene = QuickSortExplanation()
    scene.render()
