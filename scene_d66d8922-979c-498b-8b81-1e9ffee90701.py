# NOTE: This code has been automatically post-processed to fix common issues:
# - Indexed SurroundingRectangle calls have been disabled
# - Layout spacing has been adjusted to prevent overlaps
# - Axis labels have been positioned to stay within frame
# - Font sizes have been capped to prevent massive text
# Undefined color constants have been replaced with standard Manim colors.

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import numpy as np

class SelectionSortExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        self.intro()
        self.motivation()
        self.basic_idea()
        self.pseudocode()
        self.small_example()
        self.visual_step_by_step()
        self.larger_example()
        self.time_complexity()
        self.space_complexity()
        self.stability_and_properties()
        self.comparison_with_others()
        self.applications_and_summary()

    def intro(self):
        local_mobjects = VGroup()
        title = Text("The Selection Sort Algorithm", font_size=36, color=BLUE).to_edge(UP, buff=1.0)
        subtitle = Text("A Simple Sorting Algorithm with Visualizations", font_size=28).next_to(title, DOWN, buff=0.5)
        local_mobjects.add(title, subtitle)
        
        with self.voiceover(text="Welcome to this comprehensive 5-minute guide on the Selection Sort algorithm. Sorting is a fundamental operation in computer science, used everywhere from organizing lists to optimizing databases. Selection Sort is one of the simplest algorithms to understand and implement. It works by repeatedly finding the minimum element from the unsorted part of the array and placing it at the beginning of the sorted part. Over the next sections, we'll cover its motivation, pseudocode, step-by-step examples, complexity analysis, comparisons, and real-world applications. By the end, you'll have a deep understanding of how it works visually and why it's useful for small datasets.") as tracker:
            self.play(Write(title), Write(subtitle))
            self.wait()

        with self.voiceover(text="Before diving in, let's recall what sorting means. Given an unsorted list like [5, 2, 8, 1, 9], sorting rearranges it into non-decreasing order: [1, 2, 5, 8, 9]. Selection Sort does this efficiently for beginners by selecting the smallest remaining element each time. It's not the fastest for large data, but its simplicity makes it perfect for learning.") as tracker:
            unsorted = MathTex(r"[5, 2, 8, 1, 9]").scale(1.2).move_to(DOWN * 1)
            sorted_arr = MathTex(r"[1, 2, 5, 8, 9]").scale(1.2).next_to(unsorted, RIGHT, buff=1.5)
            arrow = Arrow(unsorted.get_right(), sorted_arr.get_left(), buff=0.3).next_to(unsorted, RIGHT, buff=0.8)
            local_mobjects.add(unsorted, sorted_arr, arrow)
            self.play(Write(unsorted), Write(arrow), Write(sorted_arr))

        self.play(FadeOut(*local_mobjects))
    
    def motivation(self):
        local_mobjects = VGroup()
        title = Text("Why Selection Sort?", font_size=36, color=GREEN).to_edge(UP, buff=1.0)
        local_mobjects.add(title)
        
        with self.voiceover(text="Selection Sort was invented in the early days of computing when efficiency wasn't always paramount, but simplicity was. It's motivated by the human way of sorting cards: you pick the smallest card and place it first, then the next smallest, and so on. This in-place sorting requires no extra memory, unlike Merge Sort. It's ideal for educational purposes and small arrays where O(n^2) time is acceptable, say up to 100 elements. Historically, it appears in Donald Knuth's 'The Art of Computer Programming' as a baseline algorithm.") as tracker:
            self.play(Write(title))
            history_text = Text("Historical Motivation:\n- Simple like sorting cards\n- In-place (no extra space)\n- Great for learning\n- From Knuth's work", font_size=24).move_to(DOWN * 0.5)
            local_mobjects.add(history_text)
            self.play(Write(history_text))

        with self.voiceover(text="Compared to random selection, Selection Sort guarantees progress by fixing one element per pass. It's stable in some implementations but not inherently. We'll see why it's preferred over Bubble Sort—no unnecessary swaps after finding the min.") as tracker:
            pros = VGroup(
                MathTex(r"O(1) space"), MathTex(r"\\Simple code"), MathTex(r"\\Adaptive?")
            ).arrange(DOWN, buff=0.4).to_edge(LEFT)
            cons = VGroup(
                MathTex(r"O(n^2) time"), MathTex(r"\\Not stable"), MathTex(r"\\Worst-case heavy")
            ).arrange(DOWN, buff=0.4).to_edge(RIGHT)
            local_mobjects.add(pros, cons)
            self.play(Write(pros), Write(cons))

        self.play(FadeOut(*local_mobjects))
    
    def basic_idea(self):
        local_mobjects = VGroup()
        title = Text("Core Idea of Selection Sort", font_size=36, color=BLUE).to_edge(UP, buff=1.0)
        local_mobjects.add(title)
        
        with self.voiceover(text="The basic idea is straightforward: Divide the array into two parts—sorted (left) and unsorted (right). Initially, the sorted part is empty. In each iteration, scan the unsorted part to find the index of the minimum element, then swap it with the first unsorted element. This grows the sorted prefix by one each time. For an array of n elements, you do n-1 passes.") as tracker:
            self.play(Write(title))
            idea_text = Text("1. Sorted | Unsorted\n2. Find min in unsorted\n3. Swap with front\n4. Repeat until done", font_size=28).move_to(ORIGIN)
            local_mobjects.add(idea_text)
            self.play(Write(idea_text))

        with self.voiceover(text="Visualize it: Start with full unsorted. After first pass, smallest is at position 0. Second pass: next smallest at 1, and so on. No backtracking—each pass is independent and linear scan.") as tracker:
            array_ex = MathTex(r"[64, 34, 25, 12, 22, 11, 90]").scale(0.9).move_to(DOWN * 1.5)
            passes = VGroup(
                MathTex(r"Pass 1: min=11 \\ \to swap"), 
                MathTex(r"Pass 2: min=12 \\ \to swap")
            ).arrange(DOWN, buff=0.5).next_to(array_ex, RIGHT, buff=1.0)
            local_mobjects.add(array_ex, passes)
            self.play(Write(array_ex), Write(passes))

        self.play(FadeOut(*local_mobjects))
    
    def pseudocode(self):
        local_mobjects = VGroup()
        title = Text("Pseudocode", font_size=36, color=ORANGE).to_edge(UP, buff=1.0)
        local_mobjects.add(title)
        
        with self.voiceover(text="Here's the pseudocode in detail. We use a for loop from 0 to n-2. For each i, assume i is the minimum index initially. Then nested loop from i+1 to n-1 to find any smaller element. If found, update min_index. After inner loop, swap arr[i] with arr[min_index]. This ensures the i-th position is correctly filled.") as tracker:
            self.play(Write(title))
            code = MathTex(
                r"""for i = 0 to n-2:
    min\_idx = i
    for j = i+1 to n-1:
        if arr[j] < arr[min\_idx]:
            min\_idx = j
    swap(arr[i], arr[min\_idx])""",
                font_size=32
            ).move_to(DOWN * 0.5)
            local_mobjects.add(code)
            self.play(Write(code))

        with self.voiceover(text="Notice the nested loops: outer for positions, inner for scanning minimums. Swaps happen only once per outer iteration, unlike Bubble Sort's many swaps. This makes it efficient in terms of swaps: exactly n-1 swaps worst-case.") as tracker:
            # highlight = SurroundingRectangle(code[1], buff=0.2, color=YELLOW)  # Auto-disabled: indexed SurroundingRectangle
            # self.play(Create(highlight))  # Auto-disabled: uses disabled SurroundingRectangle
            self.wait(2)
            # self.play(FadeOut(highlight))  # Auto-disabled: uses disabled SurroundingRectangle

        self.play(FadeOut(*local_mobjects))
    
    def small_example(self):
        local_mobjects = VGroup()
        title = Text("Small Example: [3, 1, 4, 1, 5]", font_size=36, color=PURPLE).to_edge(UP, buff=1.0)
        local_mobjects.add(title)
        
        with self.voiceover(text="Let's trace a small array: [3, 1, 4, 1, 5]. Pass 1 (i=0): scan 1,4,1,5. Min is 1 at index 1. Swap 3 and 1: [1, 3, 4, 1, 5]. Now position 0 fixed.") as tracker:
            self.play(Write(title))
            arr1 = self.create_array_visual([3,1,4,1,5], DOWN * 1.2)
            local_mobjects.add(arr1)
            self.play(Create(arr1))

        with self.voiceover(text="Pass 2 (i=1): scan from 4,1,5. Min=1 at index 3. Swap 3 and 1: [1, 1, 4, 3, 5]. Pass 3 (i=2): scan 3,5. Min=3 at 3. Swap 4 and 3: [1, 1, 3, 4, 5]. Pass 4: 5 is min. Done.") as tracker:
            self.animate_pass(arr1, 0, 1, 3)  # Simulate swap
            self.animate_pass(arr1, 1, 3, 3)
            self.animate_pass(arr1, 2, 3, 3)

        self.play(FadeOut(*local_mobjects))
    
    def visual_step_by_step(self):
        local_mobjects = VGroup()
        title = Text("Visual Step-by-Step Breakdown", font_size=36, color=TEAL).to_edge(UP, buff=1.0)
        local_mobjects.add(title)
        
        with self.voiceover(text="For deeper visualization, consider [64, 25, 12, 22, 11]. Pass 1: Highlight scanning (yellow), find min 11 (red), swap with 64. Array becomes [11, 25, 12, 22, 64]. The sorted part is marked green, unsorted orange.") as tracker:
            self.play(Write(title))
            arr = self.create_array_visual([64,25,12,22,11], DOWN * 1.5)
            local_mobjects.add(arr)
            self.play(Create(arr))
            self.highlight_scan(arr, 0)

        with self.voiceover(text="Pass 2: Sorted [11 | 25,12,22,64]. Scan unsorted, min=12 at index 2. Swap with 25: [11,12,25,22,64]. Notice how the green sorted region grows. This visual separation helps track progress.") as tracker:
            self.animate_swap(arr, 1, 2)
            self.mark_sorted(arr, 2)

        with self.voiceover(text="Continue similarly: Each pass reduces unsorted size by 1. No overlaps in logic—pure selection.") as tracker:
            self.animate_swap(arr, 2, 4)  # Simplified
            self.animate_swap(arr, 3, 3)

        self.play(FadeOut(*local_mobjects))
    
    def larger_example(self):
        local_mobjects = VGroup()
        title = Text("Larger Example: 1 to 10 Shuffled", font_size=36, color=GOLD).to_edge(UP, buff=1.0)
        local_mobjects.add(title)
        
        shuffled = [7, 2, 9, 5, 1, 6, 10, 3, 8, 4]
        with self.voiceover(text="Now a 10-element array: [7,2,9,5,1,6,10,3,8,4]. Pass 1 finds 1 (index 4), swaps to front. It would take 9 passes total, each scanning decreasing lengths: 10,9,...,2 comparisons.") as tracker:
            self.play(Write(title))
            arr = self.create_array_visual(shuffled, DOWN * 1.5)
            local_mobjects.add(arr)
            self.play(Create(arr))

        with self.voiceover(text="Visualizing all passes: Watch mins bubble to front. Total swaps: 9. This shows scalability issues for large n, but clarity for small.") as tracker:
            # Simulate key swaps
            self.animate_pass(arr, 0, 4, 4)
            self.animate_pass(arr, 1, 8, 8)  # etc., simplified

        self.play(FadeOut(*local_mobjects))
    
    def time_complexity(self):
        local_mobjects = VGroup()
        title = Text("Time Complexity Analysis", font_size=36, color=RED).to_edge(UP, buff=1.0)
        local_mobjects.add(title)
        
        equation = MathTex(r"T(n) = \sum_{i=0}^{n-2} (n - i) = \frac{n(n-1)}{2} = \Theta(n^2)", font_size=36).to_edge(UP, buff=1.0)
        local_mobjects.add(equation)
        
        with self.voiceover(text="Time complexity: Outer loop n-1 times, inner loop averages n/2 comparisons. Exact: sum from 1 to n-1 = n(n-1)/2 comparisons, plus n-1 swaps. Thus O(n^2) time, quadratic growth.") as tracker:
            self.play(Write(title), Write(equation))
        
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 50, 10],
            x_length=7, y_length=4,
            axis_config={"include_tip": True, "font_size": 24}
        ).move_to(DOWN * 1.5)
        x_label = axes.get_x_axis_label(MathTex("n").shift(DOWN * 0.8).scale(1.2)).shift(DOWN * 0.6)
        y_label = axes.get_y_axis_label(MathTex(r"T(n)").scale(1.2), direction=LEFT).shift(LEFT * 0.8).shift(LEFT * 0.8)
        quad = axes.plot(lambda x: (x**2)/2, color=YELLOW)
        local_mobjects.add(axes, x_label, y_label, quad)
        
        with self.voiceover(text="Graph shows quadratic curve. For n=10, ~45 ops; n=100, 5000 ops—slows dramatically.") as tracker:
            self.play(Create(axes), Write(x_label), Write(y_label), Create(quad))

        self.play(FadeOut(*local_mobjects))
    
    def space_complexity(self):
        local_mobjects = VGroup()
        title = Text("Space Complexity & Properties", font_size=36, color=PINK).to_edge(UP, buff=1.0)
        local_mobjects.add(title)
        
        with self.voiceover(text="Space: O(1) extra—only min_idx variable. In-place swaps modify array directly. Not stable: equal elements may swap, changing order. Not adaptive: always full scans even if sorted.") as tracker:
            self.play(Write(title))
            space_eq = MathTex(r"O(1) \\space", font_size=36).scale(1.2).move_to(LEFT * 3)
            props = VGroup(
                Text("Not Stable", font_size=28).move_to(ORIGIN),
                Text("Not Adaptive", font_size=28).next_to(space_eq, RIGHT, buff=2)
            )
            local_mobjects.add(space_eq, props)
            self.play(Write(space_eq), Write(props))

        with self.voiceover(text="Stability example: [2a, 1, 2b]. Sorts to [1, 2a, 2b] but may swap 2a and 2b if positions dictate.") as tracker:
            stability_ex = MathTex(r"[2_a, 1, 2_b] \\ \to [1, 2_b, 2_a]?").move_to(DOWN * 1)
            local_mobjects.add(stability_ex)
            self.play(Write(stability_ex))

        self.play(FadeOut(*local_mobjects))
    
    def stability_and_properties(self):
        local_mobjects = VGroup()
        title = Text("Detailed Properties", font_size=36, color=BLUE).to_edge(UP, buff=1.0)
        local_mobjects.add(title)
        
        with self.voiceover(text="Properties: Exactly n-1 swaps. Prefers small arrays. Online? No, needs full scan. Can be optimized by skipping if arr[i] <= arr[min_idx].") as tracker:
            self.play(Write(title))
            props_list = VGroup(
                MathTex(r"n-1 swaps"), Text("Small arrays", font_size=28),
                Text("Optimizable", font_size=28)
            ).arrange(DOWN, buff=0.4).move_to(DOWN * 0.5)
            local_mobjects.add(props_list)
            self.play(Write(props_list))

        self.play(FadeOut(*local_mobjects))
    
    def comparison_with_others(self):
        local_mobjects = VGroup()
        title = Text("Comparisons with Bubble & Insertion Sort", font_size=36, color=GREEN).to_edge(UP, buff=1.0)
        local_mobjects.add(title)
        
        with self.voiceover(text="Vs Bubble: Selection does one swap per pass, Bubble many. Both O(n^2), but Selection fewer writes. Vs Insertion: Insertion adaptive (O(n) best), shifts elements; Selection always scans fully.") as tracker:
            self.play(Write(title))
            table = VGroup(
                Text("Algorithm", font_size=24).to_edge(LEFT),
                Text("Worst", font_size=24).next_to(Text(" "), RIGHT * 2),
                Text("Swaps", font_size=24).next_to(Text(" "), RIGHT * 4)
            ).arrange(DOWN).move_to(DOWN * 1)
            local_mobjects.add(table)
            # Simplified table
            bubble = Text("Bubble: O(n^2), many swaps").move_to(LEFT * 3.5 + DOWN * 0.5)
            insert = Text("Insertion: Adaptive").move_to(RIGHT * 3.5 + DOWN * 0.5)
            local_mobjects.add(bubble, insert)
            self.play(Write(bubble), Write(insert))

        self.play(FadeOut(*local_mobjects))
    
    def applications_and_summary(self):
        local_mobjects = VGroup()
        title = Text("Applications & Conclusion", font_size=36, color=ORANGE).to_edge(UP, buff=1.0)
        local_mobjects.add(title)
        
        with self.voiceover(text="Applications: Embedded systems, small datasets, teaching. Not for big data—use QuickSort/ TimSort. In Python, use sorted() instead.") as tracker:
            self.play(Write(title))
            apps = Text("Use when:\n- n small (<100)\n- Few swaps matter\n- Simplicity > speed", font_size=28).move_to(DOWN * 1)
            local_mobjects.add(apps)
            self.play(Write(apps))

        with self.voiceover(text="Summary: Selection Sort selects mins sequentially, O(n^2) time, O(1) space. Visual, simple, foundational. Thanks for watching!") as tracker:
            summary = Text("Key Takeaway: Master the basics!", font_size=32, color=YELLOW).move_to(ORIGIN)
            local_mobjects.add(summary)
            self.play(Write(summary))

        self.play(FadeOut(*local_mobjects))

    def create_array_visual(self, arr, pos=ORIGIN):
        elements = VGroup()
        for i, val in enumerate(arr):
            rect = SurroundingRectangle(Rectangle(width=0.8, height=0.6), buff=0.05, color=WHITE)
            num = Text(str(val), font_size=24).move_to(rect.get_center())
            elem = VGroup(rect, num).shift(RIGHT * i * 1.0)
            elements.add(elem)
        elements.move_to(pos)
        return elements

    def highlight_scan(self, arr, start_idx):
        for i in range(start_idx + 1, len(arr)):
            self.play(arr[i].animate.set_color(YELLOW))
        self.wait(1)
        self.play(*[elem.animate.set_color(WHITE) for elem in arr])

    def animate_swap(self, arr, idx1, idx2):
        self.play(
            arr[idx1].animate.move_to(arr[idx2].get_center()),
            arr[idx2].animate.move_to(arr[idx1].get_center())
        )
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]  # Swap in group

    def animate_pass(self, arr, i, min_idx, orig_pos):
        self.highlight_scan(arr, i)
        arr[min_idx].set_color(RED)
        self.wait(1)
        self.animate_swap(arr, i, min_idx)

    def mark_sorted(self, arr, num_sorted):
        for i in range(num_sorted):
            arr[i].set_color(GREEN)

# Instructions to run:
# Save this as selection_sort.py
# Install: pip install manim manim-voiceover
# Render: manim -pql selection_sort.py SelectionSortExplanation
# This will produce a ~5-7 minute video with voiceover.