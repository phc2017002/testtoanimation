from manim import *
import numpy as np
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class MergeSortExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))
        
        self.introduction()
        self.divide_and_conquer_paradigm()
        self.algorithm_overview()
        self.divide_step()
        self.conquer_step()
        self.merge_step()
        self.small_example()
        self.larger_example()
        self.time_complexity()
        self.space_complexity()
        self.comparisons_with_other_sorts()
        self.applications_and_summary()

    def create_array_visual(self, nums, pos=ORIGIN, scale_factor=0.3, color=BLUE, height_scale=1.0):
        """Create a visual array as bars with heights proportional to values."""
        if not nums:
            return VGroup()
        max_val = max(nums)
        bars = VGroup()
        for i, num in enumerate(nums):
            height = 0.2 + (num / max_val) * height_scale
            rect = Rectangle(width=0.7, height=height, color=color, fill_opacity=0.7)
            label = Integer(num, font_size=24).move_to(rect.get_center())
            label.scale_to_fit_height(rect.height * 0.85)
            bar = VGroup(rect, label).shift(RIGHT * i * 0.9)
            bars.add(bar)
        bars.scale(scale_factor)
        bars.move_to(pos)
        return bars

    def introduction(self):
        # Section 1: Introduction
        title = Text("MergeSort Algorithm\nExplained Visually", font_size=36, color=BLUE).to_edge(UP, buff=1.0)
        
        with self.voiceover(text="""Welcome to this comprehensive visual explanation of the MergeSort algorithm. 
        MergeSort is one of the most elegant and efficient sorting algorithms, known for its divide-and-conquer approach. 
        It consistently runs in O(n log n) time, making it ideal for large datasets. 
        Unlike quicker sorts like Quicksort that can degrade to O(n²), MergeSort guarantees optimal performance. 
        We'll break it down step by step, with detailed visualizations, examples, and analysis over the next several minutes.""" ) as tracker:
            self.play(Write(title))
            self.wait(2)
        
        subtitle = Text("Why Study MergeSort?", font_size=32).next_to(title, DOWN, buff=0.6)
        with self.voiceover(text="""MergeSort exemplifies the power of recursion and divide-and-conquer paradigms, 
        concepts fundamental to computer science. It's stable, meaning equal elements retain their relative order, 
        which is crucial for applications like sorting with secondary keys. 
        Invented by John von Neumann around 1945, it laid groundwork for parallel sorting and external memory sorts. 
        Today, it's used in Java's Arrays.sort for object arrays and Python's Timsort hybrid.""" ) as tracker:
            self.play(Write(subtitle))
        
        self.play(FadeOut(title), FadeOut(subtitle))

    def divide_and_conquer_paradigm(self):
        # Section 2: Divide and Conquer Paradigm
        title = Text("Divide and Conquer Paradigm", font_size=36, color=GREEN).to_edge(UP, buff=1.0)
        
        with self.voiceover(text="""At its core, MergeSort follows the divide-and-conquer strategy: 
        Divide the problem into smaller subproblems, conquer them recursively, and combine solutions efficiently. 
        This reduces complexity from brute-force O(n²) to logarithmic. 
        Think of it like sorting a deck of cards: split into two halves, sort each half separately, then merge.""" ) as tracker:
            self.play(Write(title))
            arrow = Arrow(ORIGIN, DOWN * 2).shift(RIGHT * 2)
            divide_label = Text("Divide", font_size=28).next_to(arrow.get_start(), UP)
            conquer_label = Text("Conquer", font_size=28).next_to(arrow.get_end(), DOWN)
            self.play(Create(arrow), Write(divide_label), Write(conquer_label))
        
        with self.voiceover(text="""Visualize a large unsorted array. We recursively halve it until single elements, 
        which are trivially sorted. Then, we merge pairs bottom-up, building larger sorted subarrays. 
        This tree-like recursion ensures balanced division, leading to even work distribution.""" ) as tracker:
            tree = Text("Recursion Tree:\nFull Array → Halves → Quarters → Singles", font_size=24).to_edge(LEFT, buff=1.0).shift(UP * 0.5)
            self.play(Write(tree))
        
        with self.voiceover(text="""The beauty is in the balance: each level processes all n elements during merges, 
        but log n levels mean n log n total work. We'll see this in complexity later.""" ) as tracker:
            self.play(GrowFromCenter(tree))
        
        self.play(FadeOut(*self.mobjects))

    def algorithm_overview(self):
        # Section 3: Algorithm Overview
        title = Text("MergeSort Algorithm Overview", font_size=36, color=BLUE).to_edge(UP, buff=1.0)
        
        with self.voiceover(text="""Pseudocode: def mergesort(arr): if len(arr) <= 1: return arr. 
        mid = len(arr)//2. left = mergesort(arr[:mid]). right = mergesort(arr[mid:]). 
        return merge(left, right). The merge function interleaves two sorted halves into one sorted array.""" ) as tracker:
            self.play(Write(title))
            pseudocode = Text("mergesort(arr):\n  if len(arr) <= 1: return arr\n  mid = len(arr)//2\n  left = mergesort(arr[:mid])\n  right = mergesort(arr[mid:])\n  return merge(left, right)", font_size=24, line_spacing=1.4).next_to(title, DOWN, buff=1.0)
            self.play(Write(pseudocode))
        
        with self.voiceover(text="""Key insight: recursion bottoms out at base case (1 element), then merges upward. 
        No in-place swaps like BubbleSort; it uses extra space for temp arrays during merge.""" ) as tracker:
            base_case = MathTex(r"Base: n \\leq 1 \\to sorted").shift(LEFT * 3.5 + DOWN * 0.8)
            recurse = MathTex(r"T(n) = 2T(n/2) + \\Theta(n)").shift(RIGHT * 3.5 + DOWN * 0.8)
            self.play(Write(base_case), Write(recurse))
        
        self.play(FadeOut(*self.mobjects))

    def divide_step(self):
        # Section 4: Divide Step
        title = Text("The Divide Step: Recursively Halving", font_size=36, color=YELLOW).to_edge(UP, buff=1.0)
        
        with self.voiceover(text="""The divide phase splits the array at midpoint. For [8,3,7,4,1,6,2,5], mid=4, 
        left=[8,3,7,4], right=[1,6,2,5]. Repeat until singles: [8],[3],[7],[4] and [1],[6],[2],[5]. 
        This logarithmic division is efficient.""" ) as tracker:
            self.play(Write(title))
            full_array = self.create_array_visual([8,3,7,4,1,6,2,5], DOWN * 1.0, height_scale=1.5)
            self.play(Create(full_array))
        
        with self.voiceover(text="""Animation: Watch the array split repeatedly. Each split halves size, depth log n. 
        Left and right subarrays move apart visually to show recursion.""" ) as tracker:
            mid_line = Line(full_array[3].get_right(), full_array[4].get_left(), color=RED, stroke_width=5)
            self.play(Create(mid_line))
            left = VGroup(*(full_array[:4])).move_to(LEFT * 2)
            right = VGroup(*(full_array[4:])).move_to(RIGHT * 2)
            self.play(Transform(full_array[:4], left), Transform(full_array[4:], right), FadeOut(mid_line))
        
        with self.voiceover(text="""Singles: Further splits yield [8],[3], etc. Trivial sorts. Now ready for conquer/merge.""" ) as tracker:
            singles_left = VGroup(
                self.create_array_visual([8], LEFT * 3.5 + DOWN * 1.5, 0.2),
                self.create_array_visual([3], LEFT * 2.1 + DOWN * 1.5, 0.2),
                self.create_array_visual([7], LEFT * 0.7 + DOWN * 1.5, 0.2),
                self.create_array_visual([4], LEFT * 0.7 - DOWN * 0.5, 0.2)
            )
            singles_right = VGroup(
                self.create_array_visual([1], RIGHT * 0.7 - DOWN * 0.5, 0.2),
                self.create_array_visual([6], RIGHT * 0.7 + DOWN * 0.5, 0.2),
                self.create_array_visual([2], RIGHT * 2.1 + DOWN * 1.5, 0.2),
                self.create_array_visual([5], RIGHT * 3.5 + DOWN * 1.5, 0.2)
            )
            self.play(FadeIn(singles_left), FadeIn(singles_right))
        
        self.play(FadeOut(*self.mobjects))

    def conquer_step(self):
        # Section 5: Conquer Step (Recursive Sorts)
        title = Text("Conquer: Recursive Sorting of Halves", font_size=36, color=GREEN).to_edge(UP, buff=1.0)
        
        with self.voiceover(text="""Conquer means sorting subarrays recursively. Singles are sorted. 
        Merge pairs: [8] and [3] → [3,8]; [7],[4] → [4,7]; etc. 
        Build up: quarters [3,8,4,7] by merging [3,8] and [4,7].""" ) as tracker:
            self.play(Write(title))
        
        left_quarter = self.create_array_visual([3,8,4,7], LEFT * 2.5, scale_factor=0.3, height_scale=1.2)
        right_quarter = self.create_array_visual([1,6,2,5], RIGHT * 2.5, scale_factor=0.3, height_scale=1.2)
        self.play(Create(left_quarter), Create(right_quarter))
        
        with self.voiceover(text="""Visually, sorted pairs glow green. Merging quarters: left becomes [3,4,7,8], right [1,2,5,6]. 
        Recursion ensures subproblems solved before combining.""" ) as tracker:
            self.play(left_quarter.animate.set_color(GREEN), right_quarter.animate.set_color(GREEN))
        
        self.play(FadeOut(*self.mobjects))

    def merge_step(self):
        # Section 6: The Merge Process
        title = Text("The Merge Step: Combining Sorted Halves", font_size=36, color=RED).to_edge(UP, buff=1.0)
        
        with self.voiceover(text="""Merge takes two sorted arrays, uses two pointers starting at beginnings. 
        Compare heads, pick smaller, advance that pointer, place in result. 
        When one empties, append remainder. O(n) linear time.""" ) as tracker:
            self.play(Write(title))
            left = self.create_array_visual([3,4,7], LEFT * 2, height_scale=1.2, color=GREEN)
            right = self.create_array_visual([1,2,5,6], RIGHT * 2, height_scale=1.2, color=GREEN)
            result = self.create_array_visual([], DOWN * 2, color=WHITE)
            self.play(Create(left), Create(right), Create(result))
        
        # Pointers
        left_ptr = Dot(left[0].get_left(), color=YELLOW, radius=0.1)
        right_ptr = Dot(right[0].get_left(), color=YELLOW, radius=0.1)
        self.play(FadeIn(left_ptr), FadeIn(right_ptr))
        
        with self.voiceover(text="""Step 1: 3 vs 1, pick 1 (right advances). Result: [1]. 
        Step 2: 3 vs 2, pick 2. Result: [1,2]. 
        Step 3: 3 vs 5, pick 3 (left advances). Continue till done.""" ) as tracker:
            # Simulate merge steps
            for i in range(3):
                self.play(left_ptr.animate.next_to(left[i].get_left() if i < len(left) else right[0].get_left(), LEFT),
                          right_ptr.animate.next_to(right[i].get_left() if i < len(right) else left[0].get_left(), LEFT))
                self.wait(0.5)
        
        merged = self.create_array_visual([1,2,3,4,5,6,7], ORIGIN, height_scale=1.5, color=BLUE)
        with self.voiceover(text="""Final merge yields fully sorted array. Pointers exhaust lists linearly.""" ) as tracker:
            self.play(Transform(VGroup(left, right), merged), FadeOut(left_ptr), FadeOut(right_ptr))
        
        self.play(FadeOut(*self.mobjects))

    def small_example(self):
        # Section 7: Small Example
        title = Text("Step-by-Step: Small Example [38, 27, 43, 3]", font_size=36, color=BLUE).to_edge(UP, buff=1.0)
        
        with self.voiceover(text="""Trace [38,27,43,3]. Divide: [38,27] and [43,3]. 
        Subdivide: [38],[27] → merge to [27,38]; [43],[3] → [3,43]. 
        Final merge: [27,38] vs [3,43] → compare 27>3 pick3, 27>43? No pick27, etc. Result [3,27,38,43].""" ) as tracker:
            self.play(Write(title))
            initial = self.create_array_visual([38,27,43,3], DOWN * 1.5)
            self.play(Create(initial))
        
        # Show full recursion tree visually
        tree_top = Text("[38,27,43,3]", font_size=24).move_to(UP * 1.5)
        tree_nodes = VGroup(
            tree_top,
            Text("[38,27]", font_size=24).shift(LEFT * 1.5),
            Text("[43,3]", font_size=24).shift(RIGHT * 1.5),
            Text("[38] [27]", font_size=24).shift(LEFT * 2.5 + DOWN * 0.5),
            Text("[43] [3]", font_size=24).shift(RIGHT * 2.5 + DOWN * 0.5)
        )
        with self.voiceover(text="""Recursion tree shows all merges. Each merge preserves order, builds larger sorted segments.""" ) as tracker:
            self.play(Write(tree_nodes))
        
        final = self.create_array_visual([3,27,38,43], DOWN * 2)
        with self.voiceover(text="""Complete trace confirms sorted output. Stable: equals stay ordered.""" ) as tracker:
            self.play(Transform(initial, final))
        
        self.play(FadeOut(*self.mobjects))

    def larger_example(self):
        # Section 8: Larger Example
        title = Text("Larger Example: 8 Elements Full Trace", font_size=36, color=GREEN).to_edge(UP, buff=1.0)
        
        with self.voiceover(text="""Using earlier [8,3,7,4,1,6,2,5]. After divides: singles. 
        Merge pairs: [3,8],[4,7],[1,6],[2,5]. 
        Merge quarters: [3,4,7,8] from [3,8]+[4,7]; [1,2,5,6] from [1,6]+[2,5]. 
        Final: merge quarters to [1,2,3,4,5,6,7,8].""" ) as tracker:
            self.play(Write(title))
            unsorted = self.create_array_visual([8,3,7,4,1,6,2,5], DOWN * 2)
            self.play(Create(unsorted))
        
        pairs = VGroup(
            self.create_array_visual([3,8], LEFT * 3 + DOWN * 1.5, 0.25),
            self.create_array_visual([4,7], LEFT * 1 + DOWN * 1.5, 0.25),
            self.create_array_visual([1,6], RIGHT * 1 + DOWN * 1.5, 0.25),
            self.create_array_visual([2,5], RIGHT * 3 + DOWN * 1.5, 0.25)
        )
        with self.voiceover(text="""Pairs merged first (green). Note pointers implicitly compare mins.""" ) as tracker:
            self.play(FadeIn(pairs))
            for p in pairs:
                p.set_color(GREEN)
        
        quarters = VGroup(
            self.create_array_visual([3,4,7,8], LEFT * 2, 0.3),
            self.create_array_visual([1,2,5,6], RIGHT * 2, 0.3)
        )
        with self.voiceover(text="""Quarters next. Final merge at top level.""" ) as tracker:
            self.play(FadeIn(quarters))
        
        sorted_full = self.create_array_visual([1,2,3,4,5,6,7,8], ORIGIN)
        self.play(Transform(unsorted, sorted_full), FadeOut(pairs), FadeOut(quarters))
        
        self.play(FadeOut(*self.mobjects))

    def time_complexity(self):
        # Section 9: Time Complexity
        title = Text("Time Complexity Analysis", font_size=36, color=YELLOW).to_edge(UP, buff=1.0)
        equation = MathTex(r"T(n) = 2T(n/2) + \Theta(n)", font_size=36).next_to(title, DOWN, buff=0.5)
        
        with self.voiceover(text="""Recurrence: T(n) = 2 T(n/2) + Θ(n) merge cost. 
        Base T(1)=Θ(1). Unroll: Level 1: n, Level 2: 2*(n/2)=n, ..., log n levels: n log n. 
        Master Theorem: a=2,b=2,f(n)=n = Θ(n^{log_b a}), case 2: T(n)=Θ(n log n).""" ) as tracker:
            self.play(Write(title), Write(equation))
        
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 35, 5],
            x_length=7,
            y_length=4,
            axis_config={"include_tip": False}
        ).move_to(DOWN * 1.5)
        x_label = axes.get_x_axis_label(MathTex("n", font_size=24).shift(DOWN * 0.8)).shift(DOWN * 0.6)
        y_label = axes.get_y_axis_label(MathTex(r"T(n)"), direction=LEFT).shift(LEFT * 2.5)
        
        nlogn = axes.plot(lambda x: x * np.log2(x + 1e-5), color=BLUE, x_range=[1,10])
        n2 = axes.plot(lambda x: x**2 / 10, color=RED, x_range=[0,10])
        
        with self.voiceover(text="""Graph: blue n log n linearithmic growth vs red n² quadratic. 
        MergeSort unbeatable worst-case.""" ) as tracker:
            self.play(Create(axes), Write(x_label), Write(y_label))
            self.play(Create(nlogn), Create(n2))
            legend = VGroup(
                Text("MergeSort: O(n log n)", font_size=24, color=BLUE),
                Text("BubbleSort: O(n²)", font_size=24, color=RED)
            ).arrange(DOWN, buff=0.3).next_to(axes, RIGHT, buff=0.8).to_corner(UR)
            self.play(Write(legend))
        
        self.play(FadeOut(*self.mobjects))

    def space_complexity(self):
        # Section 10: Space Complexity
        title = Text("Space Complexity & Optimizations", font_size=36, color=RED).to_edge(UP, buff=1.0)
        
        with self.voiceover(text="""Space: O(n) for temp array in merge. Recursion depth log n, stack O(log n). 
        Total Θ(n). In-place variants exist but unstable/complex. 
        Bottom-up iterative MergeSort uses O(n) space too, no recursion.""" ) as tracker:
            self.play(Write(title))
            space_eq = MathTex(r"Space = \Theta(n) + O(\log n)", font_size=36).move_to(ORIGIN)
            self.play(Write(space_eq))
        
        temp_array = Rectangle(width=6, height=0.5, color=YELLOW).shift(DOWN * 1.5)
        temp_label = Text("Temporary Merge Array (O(n))", font_size=24).next_to(temp_array, DOWN)
        with self.voiceover(text="""Visual: temp array holds merged result. Can optimize with in-place merge but loses stability.""" ) as tracker:
            self.play(Create(temp_array), Write(temp_label))
        
        self.play(FadeOut(*self.mobjects))

    def comparisons_with_other_sorts(self):
        # Section 11: Comparisons
        title = Text("MergeSort vs Other Sorts", font_size=36, color=BLUE).to_edge(UP, buff=1.0)
        
        left_col = VGroup(
            Text("MergeSort", font_size=28).shift(UP * 1.5),
            Text("Worst: O(n log n)", font_size=24).shift(UP * 0.5),
            Text("Average: O(n log n)", font_size=24).shift(DOWN * 0.5),
            Text("Best: O(n log n)", font_size=24).shift(DOWN * 1.5),
            Text("Stable: Yes", font_size=24).shift(DOWN * 2.3),
            Text("Space: O(n)", font_size=24).shift(DOWN * 3.0)
        ).move_to(LEFT * 3.5)
        
        right_col = VGroup(
            Text("QuickSort", font_size=28).shift(UP * 1.5),
            Text("Worst: O(n²)", font_size=24).shift(UP * 0.5),
            Text("Average: O(n log n)", font_size=24).shift(DOWN * 0.5),
            Text("Best: O(n log n)", font_size=24).shift(DOWN * 1.5),
            Text("Stable: No", font_size=24).shift(DOWN * 2.3),
            Text("Space: O(log n)", font_size=24).shift(DOWN * 3.0)
        ).move_to(RIGHT * 3.5)
        
        with self.voiceover(text="""Column comparison: MergeSort predictable, stable; QuickSort faster average but worst-case risky. 
        Use MergeSort for stability/linked lists.""" ) as tracker:
            self.play(Write(left_col), Write(right_col))
        
        self.play(FadeOut(*self.mobjects))

    def applications_and_summary(self):
        # Section 12: Applications and Summary
        title_parts = VGroup(
            Text("Applications", font_size=36, color=GREEN),
            Text("& Conclusion", font_size=36, color=GREEN)
        ).arrange(RIGHT, buff=0.4).to_edge(UP, buff=1.0)
        
        with self.voiceover(text="""Applications: External sorting (disks), parallel sorts (multicore), 
        Timsort hybrid in Python/Java. Great for big data, stability needed.""" ) as tracker:
            self.play(Write(title_parts))
            apps = VGroup(
                Text("• External Sorting (Databases)", font_size=28),
                Text("• Parallel MergeSort", font_size=28),
                Text("• Stable Sort for Objects", font_size=28)
            ).arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(ORIGIN)
            self.play(Write(apps))
        
        with self.voiceover(text="""Summary: Divide-conquer-merge yields O(n log n) efficient, stable sort. 
        Mastered recursion, visualizations confirm steps. Thanks for watching this detailed exploration!""" ) as tracker:
            summary = Text("Key Takeaway:\nO(n log n) Divide & Conquer Masterpiece", font_size=32, color=BLUE).next_to(apps, DOWN, buff=1.0)
            self.play(Write(summary))
        
        self.play(FadeOut(*self.mobjects))

if __name__ == "__main__":
    from manim import config
    config.quality = "high_quality"
    config.verbosity = "WARNING"