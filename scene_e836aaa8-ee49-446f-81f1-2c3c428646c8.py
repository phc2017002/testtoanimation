from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import numpy as np

class MergeSortExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        self.title_intro()
        self.what_is_sorting()
        self.problems_with_simple_sorts()
        self.introduce_mergesort()
        self.divide_and_conquer_paradigm()
        self.mergesort_recursion_tree()
        self.the_merge_function()
        self.small_example_step_by_step()
        self.full_example_large_array()
        self.time_complexity_analysis()
        self.space_complexity_and_optimizations()
        self.comparisons_with_other_sorts()
        self.applications_and_summary()

    def title_intro(self):
        with self.voiceover(text="""Welcome to this comprehensive explanation of the MergeSort algorithm. 
        MergeSort is one of the most efficient and elegant sorting algorithms, using a divide-and-conquer strategy. 
        Over the next several minutes, we'll cover what sorting is, why simple methods fail for large data, 
        how MergeSort works step by step, visualize examples, analyze its complexity, and see real-world applications. 
        By the end, you'll fully understand why MergeSort is a cornerstone of computer science.""") as tracker:
            title = Text("MergeSort Algorithm\nVisualized", font_size=36, color=BLUE).to_edge(UP, buff=1.0)
            subtitle = Text("Divide and Conquer", font_size=28).next_to(title, DOWN, buff=0.3)
            self.play(Write(title), Write(subtitle))
            self.wait(2)

        self.play(FadeOut(title), FadeOut(subtitle))

    def what_is_sorting(self):
        with self.voiceover(text="""Sorting is a fundamental problem in computer science: arranging a collection of items, 
        like numbers in an array, in a specific order, usually ascending or descending. 
        Imagine you have a messy desk with papers by height; sorting organizes them neatly. 
        Efficient sorting is crucial for databases, search engines, and data analysis, 
        where datasets can have millions of elements. Poor sorting can take hours; good ones finish in seconds.""") as tracker:
            unsorted_array = self.create_array([5, 2, 8, 1, 9, 3], colors=[RED]*6)
            unsorted_array.move_to(ORIGIN)
            unsorted_label = Text("Unsorted Array", font_size=24).next_to(unsorted_array, UP, buff=0.6)
            self.play(Create(unsorted_array), Write(unsorted_label))

        with self.voiceover(text="""Here we see an unsorted array of numbers. Our goal is to rearrange them so each element is smaller than or equal to the next. 
        Simple methods like bubble sort compare adjacent pairs and swap if out of order, but they struggle with large inputs.""") as tracker:
            sorted_array = self.create_array([1, 2, 3, 5, 8, 9], colors=[GREEN]*6)
            sorted_array.next_to(unsorted_array, RIGHT, buff=1.5)
            sorted_label = Text("Sorted Array", font_size=24).next_to(sorted_array, UP, buff=0.6)
            arrow = Arrow(unsorted_array.get_right(), sorted_array.get_left(), buff=0.2).shift(DOWN*0.3)
            self.play(Create(sorted_array), Write(sorted_label), Create(arrow))

        self.play(FadeOut(*self.mobjects))

    def problems_with_simple_sorts(self):
        with self.voiceover(text="""Let's examine why naive sorting algorithms like Bubble Sort or Insertion Sort fail for large data. 
        Bubble Sort repeatedly passes through the list, comparing neighbors and bubbling larger elements to the end. 
        In the worst case, it performs about n squared comparisons, where n is the array size. 
        For n equals 1 million, that's a trillion operations—impossibly slow on any computer.""") as tracker:
            title = Text("Problems with Simple Sorts", font_size=32).to_edge(UP, buff=1.0)
            self.play(Write(title))
            bubble_steps = VGroup(
                Text("Bubble Sort: O(n²)", font_size=28).shift(UP*1.5),
                MathTex(r"n^2 = 10^6 \\times 10^6 = 10^{12}").shift(ORIGIN).scale(1.2)
            ).arrange(DOWN, buff=0.8)
            self.play(Write(bubble_steps))

        with self.voiceover(text="""Insertion Sort builds a sorted portion incrementally, inserting each new element. 
        Again, worst-case quadratic time. These algorithms are fine for small lists but explode in time for big data, 
        like sorting web search results or genomic sequences.""") as tracker:
            insertion = Text("Insertion Sort: Also O(n²)", font_size=28).next_to(bubble_steps, DOWN, buff=0.8, aligned_edge=LEFT)
            big_n = Text("n=10^6 → Too Slow!", font_size=28, color=RED).next_to(insertion, RIGHT, buff=1.0)
            self.play(Write(insertion), Write(big_n))

        self.play(FadeOut(title), FadeOut(bubble_steps), FadeOut(insertion), FadeOut(big_n))

    def introduce_mergesort(self):
        with self.voiceover(text="""Enter MergeSort: a divide-and-conquer algorithm invented by John von Neumann in 1945. 
        It guarantees O(n log n) time—much faster than quadratic. For n=1 million, log n is about 20, so only 20 million operations. 
        The key idea: divide the array into halves recursively until single elements, then merge sorted halves efficiently.""") as tracker:
            title = Text("Introducing MergeSort", font_size=32).to_edge(UP, buff=1.0)
            self.play(Write(title))
            eq = MathTex(r"T(n) = 2T(n/2) + O(n)").scale(1.2).next_to(title, DOWN, buff=0.8)
            self.play(Write(eq))
            logn = MathTex(r"O(n \\log n)", color=GREEN).scale(1.5).next_to(eq, RIGHT, buff=1.2)
            self.play(Write(logn))

        with self.voiceover(text="""MergeSort splits the problem size in half each time, solving subproblems independently, 
        then combines results. This recursive strategy scales beautifully for parallel processing too.""") as tracker:
            diagram = self.create_simple_split([64, 32, 16, 8, 4, 2, 1], pos=DOWN*1.0)
            self.play(Create(diagram))

        self.play(FadeOut(*self.mobjects))

    def divide_and_conquer_paradigm(self):
        with self.voiceover(text="""Divide and Conquer is a powerful paradigm: 1. Divide the problem into smaller subproblems. 
        2. Conquer by solving subproblems recursively. 3. Combine solutions efficiently. 
        MergeSort exemplifies this: divide array into two halves, sort each recursively, merge into sorted whole. 
        Base case: single element is already sorted.""") as tracker:
            title = Text("Divide & Conquer Paradigm", font_size=32).to_edge(UP, buff=1.0)
            self.play(Write(title))
            steps = VGroup(
                MathTex(r"1. \\Divide").shift(UP*1.8),
                MathTex(r"2. \\Conquer").shift(UP*0.3),
                MathTex(r"3. \\Combine").shift(DOWN*1.2)
            ).arrange(DOWN, buff=1.0, aligned_edge=LEFT).shift(LEFT*2)
            arrows = VGroup(
                Arrow(steps[0].get_bottom(), steps[1].get_top(), buff=0.1),
                Arrow(steps[1].get_bottom(), steps[2].get_top(), buff=0.1)
            )
            self.play(Write(steps), Create(arrows))

        with self.voiceover(text="""This reduces complexity from exponential to logarithmic depth. 
        Recursion depth is log n levels, each level does O(n) work during merges.""") as tracker:
            array_ex = self.create_array([8,3,7,4], colors=[BLUE]*4).move_to(RIGHT*2.5).shift(DOWN*0.5)
            split_line = Line(array_ex[1].get_right(), array_ex[1].get_right(), color=YELLOW, stroke_width=5).set_length(0.1)
            self.play(Create(array_ex), GrowFromCenter(split_line))

        self.play(FadeOut(*self.mobjects))

    def mergesort_recursion_tree(self):
        with self.voiceover(text="""Visualize MergeSort as a recursion tree. Root is full array of size n. 
        Children are two halves of n/2. Leaves are single elements. 
        Merges happen bottom-up: first merge pairs, then quadruples, up to full array. 
        Tree height is log n, total merge work is O(n log n).""") as tracker:
            title = Text("Recursion Tree", font_size=32).to_edge(UP, buff=1.0)
            self.play(Write(title))
            tree_levels = VGroup(
                Text("n", font_size=36).shift(UP*2),
                VGroup(Text("n/2", font_size=32), Text("n/2", font_size=32)).arrange(RIGHT, buff=2.5).shift(UP*0.8),
                VGroup(*[Text("n/4", font_size=28) for _ in range(4)]).arrange(RIGHT, buff=1.2).shift(DOWN*0.4),
                Text("... leaves (1)", font_size=24).shift(DOWN*1.8)
            )
            self.play(Write(tree_levels))

        with self.voiceover(text="""Each level merges all n elements exactly once. With log n levels, total time O(n log n). 
        Beautiful balance between divide and merge costs.""") as tracker:
            cost = MathTex(r"\\text{Level cost: } O(n) \\\\ \\text{Levels: } \\log n").scale(1.2).move_to(RIGHT*3)
            total = MathTex(r"O(n \\log n)", color=GREEN, font_size=36).next_to(cost, DOWN, buff=0.6)
            self.play(Write(cost), Write(total))

        self.play(FadeOut(*self.mobjects))

    def the_merge_function(self):
        with self.voiceover(text="""The heart of MergeSort is the merge step. Given two sorted halves, merge produces a single sorted array. 
        Use two pointers, one per half. Compare heads, pick smaller, advance that pointer. 
        Repeat until both exhausted. Stable and efficient: exactly n-1 comparisons worst case.""") as tracker:
            title = Text("The Merge Function", font_size=32).to_edge(UP, buff=1.0)
            self.play(Write(title))
            left = self.create_array([1,3,5], colors=[GREEN]*3).shift(LEFT*2.5)
            right = self.create_array([2,4,6], colors=[GREEN]*3).shift(RIGHT*2.5)
            merged_pos = DOWN*1.5
            self.play(Create(left), Create(right))

        with self.voiceover(text="""See: left [1,3,5], right [2,4,6]. Pointers i=0, j=0. 
        1<2, take 1 to output. i advances. Now 3>2, take 2. j advances. Continue till [1,2,3,4,5,6].""") as tracker:
            pointers = VGroup(
                Triangle(color=RED, fill_opacity=1).scale(0.3).move_to(left[0].get_center()),
                Triangle(color=RED, fill_opacity=1).scale(0.3).move_to(right[0].get_center())
            )
            output = self.create_empty_array(6, merged_pos)
            self.play(Create(pointers), FadeIn(output))
            # Simulate quick merge animation
            self.play(
                left[0].animate.shift(DOWN*0.1),  # Simulate take
                pointers[0].animate.next_to(left[1], buff=-0.2),
                FadeOut(left[0])
            )

        self.play(FadeOut(*self.mobjects))

    def small_example_step_by_step(self):
        with self.voiceover(text="""Let's trace MergeSort on [3,1,4,2]. First divide: mid=2, left [3,1], right [4,2]. 
        Recurse left: divide to [3] and [1]. Merge: 1<3 → [1,3]. 
        Right: [4] and [2] → 2<4 → [2,4]. Now top merge: [1,3] and [2,4].""") as tracker:
            title = Text("Small Example: [3,1,4,2]", font_size=32).to_edge(UP, buff=1.0)
            self.play(Write(title))
            initial = self.create_array([3,1,4,2], colors=[YELLOW]*4, label="Original").move_to(ORIGIN)
            self.play(Write(initial))

        with self.voiceover(text="""Step 1: Divide into [3,1] and [4,2]. Recurse: left to [3],[1] → merge to [1,3]. 
        Right to [4],[2] → [2,4]. Final merge: compare 1<2→1, 3>2→2, 3<4→3, then 4 → [1,2,3,4].""") as tracker:
            left_half = self.create_array([3,1], colors=[BLUE]*2).shift(LEFT*2.2)
            right_half = self.create_array([4,2], colors=[ORANGE]*2).shift(RIGHT*2.2)
            self.play(Transform(initial[0:2], left_half), Transform(initial[2:4], right_half))

            sorted_left = self.create_array([1,3], colors=[GREEN]*2).move_to(left_half.get_center())
            sorted_right = self.create_array([2,4], colors=[GREEN]*2).move_to(right_half.get_center())
            self.play(FadeTransform(left_half, sorted_left), FadeTransform(right_half, sorted_right))

            final = self.create_array([1,2,3,4], colors=[GREEN]*4).shift(DOWN*1.2)
            self.play(Transform(VGroup(sorted_left, sorted_right), final))

        self.play(FadeOut(*self.mobjects))

    def full_example_large_array(self):
        with self.voiceover(text="""Now a full trace on 8 elements: [8,3,7,4,1,6,2,5]. 
        Divide to [8,3,7,4] and [1,6,2,5]. Recurse left to [8,3]→[3,8], [7,4]→[4,7], merge→[3,4,7,8]. 
        Right: [1,6]→[1,6], [2,5]→[2,5], merge→[1,2,5,6].""") as tracker:
            title = Text("Full Example: [8,3,7,4,1,6,2,5]", font_size=32).to_edge(UP, buff=1.0)
            self.play(Write(title))
            orig = self.create_array([8,3,7,4,1,6,2,5], colors=[YELLOW]*8, width=0.4).move_to(ORIGIN)
            self.play(Write(orig))

        with self.voiceover(text="""Final merge: left [3,4,7,8], right [1,2,5,6]. Pointers start: 3>1→1, 3>2→2, 3<5→3, 4<5→4, 7>5→5, 7>6→6, 7→7,8→ [1,2,3,4,5,6,7,8]. 
        Notice stability: equal elements retain order.""") as tracker:
            left_final = self.create_array([3,4,7,8], colors=[BLUE]*4).shift(LEFT*1.8, DOWN*0.3)
            right_final = self.create_array([1,2,5,6], colors=[ORANGE]*4).shift(RIGHT*1.8, DOWN*0.3)
            self.play(FadeTransform(orig[:4], left_final), FadeTransform(orig[4:], right_final))

            sorted_final = self.create_array([1,2,3,4,5,6,7,8], colors=[GREEN]*8, width=0.4).shift(DOWN*1.5)
            self.play(Transform(VGroup(left_final, right_final), sorted_final))

        self.play(FadeOut(*self.mobjects))

    def time_complexity_analysis(self):
        with self.voiceover(text="""Time complexity: recurrence T(n) = 2 T(n/2) + Theta(n). 
        Divide: O(1), recurse: 2 T(n/2), merge: O(n). Master theorem solves to O(n log n) for all cases. 
        Best, average, worst all O(n log n)—predictable!""") as tracker:
            title = Text("Time Complexity", font_size=32).to_edge(UP, buff=1.0)
            self.play(Write(title))
            recurrence = MathTex(r"T(n) = 2T(n/2) + \\Theta(n)", font_size=36).to_edge(UP, buff=1.0)
            self.play(Write(recurrence))

        with self.voiceover(text="""Graphically: each level costs O(n), log n levels. Compare to O(n²): for n=1024, MergeSort ~10k ops, quadratic 1M ops.""") as tracker:
            axes = Axes(
                x_range=[0, 10, 2], y_range=[0, 10, 2], x_length=7, y_length=4,
                axis_config={"include_tip": True, "color": BLUE}
            ).move_to(DOWN*1.5)
            x_label = axes.get_x_axis_label("n (log scale).shift(DOWN * 0.8)", font_size=24).shift(DOWN*0.6)
            y_label = axes.get_y_axis_label("Time", direction=LEFT).shift(LEFT * 0.8).shift(LEFT*0.8)
            nlogn = axes.plot(lambda x: x * np.log2(x+1), color=GREEN, x_range=[1,9])
            nsq = axes.plot(lambda x: (x)**2 / 100, color=RED, x_range=[1,9])
            self.play(Create(axes), Write(x_label), Write(y_label))
            self.play(Create(nlogn), Create(nsq))

        self.play(FadeOut(*self.mobjects))

    def space_complexity_and_optimizations(self):
        with self.voiceover(text="""Space: O(n) auxiliary due to temp arrays in merge. Total with input O(n). 
        In-place variants exist but complicate stability. Optimizations: natural merge for partially sorted data, 
        parallel merge for multi-core.""") as tracker:
            title = Text("Space & Optimizations", font_size=32).to_edge(UP, buff=1.0)
            self.play(Write(title))
            space_eq = MathTex(r"O(n) \\text{ auxiliary space}", font_size=36, color=ORANGE).shift(UP*0.5)
            self.play(Write(space_eq))
            opts = VGroup(
                Text("• In-place (less stable)", font_size=28),
                Text("• Parallel Merge", font_size=28),
                Text("• Bottom-up iterative", font_size=28)
            ).arrange(DOWN, buff=0.4).next_to(space_eq, DOWN, buff=1.0, aligned_edge=LEFT)
            self.play(Write(opts))

        self.play(FadeOut(*self.mobjects))

    def comparisons_with_other_sorts(self):
        with self.voiceover(text="""Compare: QuickSort average O(n log n) but worst O(n²), in-place O(log n) space. 
        HeapSort O(n log n), in-place, but higher constant. Bubble/Insertion O(n²). 
        MergeSort shines for stability, guaranteed time, external sorting (disk-based).""") as tracker:
            title = Text("Comparisons", font_size=32).to_edge(UP, buff=1.0)
            self.play(Write(title))
            table = VGroup(
                Text("Algorithm", font_size=24).to_edge(LEFT),
                Text("Time", font_size=24).shift(RIGHT*1.5),
                Text("Space", font_size=24).shift(RIGHT*3),
                Text("Stable?", font_size=24).shift(RIGHT*4.5)
            ).arrange(DOWN).to_edge(UP, buff=1.0).shift(DOWN*1.0)
            rows = VGroup(
                VGroup(Text("MergeSort"), Text("n log n"), Text("O(n)"), Text("Yes")),
                VGroup(Text("QuickSort"), Text("n log n avg"), Text("O(log n)"), Text("No")),
                VGroup(Text("HeapSort"), Text("n log n"), Text("O(1)"), Text("No"))
            )
            for row in rows:
                row.arrange(RIGHT, buff=0.8)
            full_table = VGroup(table, *rows).arrange(DOWN, buff=0.3)
            self.play(Write(full_table))

        self.play(FadeOut(*self.mobjects))

    def applications_and_summary(self):
        with self.voiceover(text="""Applications: Java's Arrays.sort() uses modified MergeSort for stability. 
        External sorting for huge data (merge runs from disk). Databases, big data tools like Hadoop. 
        Summary: MergeSort's divide-conquer-merge is elegant, efficient O(n log n), stable. 
        Master it for interviews and understanding scalable algorithms. Thanks for watching!""") as tracker:
            title = Text("Applications & Summary", font_size=32).to_edge(UP, buff=1.0)
            self.play(Write(title))
            apps = VGroup(
                Text("• Java Arrays.sort()", font_size=28),
                Text("• External Sorting", font_size=28),
                Text("• Databases / Big Data", font_size=28)
            ).arrange(DOWN, buff=0.5).shift(ORIGIN)
            summary = Text("O(n log n) | Stable | Divide & Conquer", font_size=32, color=GREEN).shift(DOWN*1.2)
            self.play(Write(apps), Write(summary))

        self.play(FadeOut(*self.mobjects))

    def create_array(self, values, colors=None, width=0.6, label=None):
        if colors is None:
            colors = [BLUE] * len(values)
        bars = VGroup()
        labels = VGroup()
        for i, (val, color) in enumerate(zip(values, colors)):
            bar = Rectangle(width=width, height=val/10, color=color, fill_opacity=0.7).move_to(i*width*1.2 - (len(values)-1)*width*0.6/2 * RIGHT)
            num = Text(str(val), font_size=24).move_to(bar.get_center())
            group = VGroup(bar, num)
            bars.add(bar)
            labels.add(num)
        array = VGroup(bars, labels)
        if label:
            label_obj = Text(label, font_size=24).next_to(array, UP, buff=0.6)
            return VGroup(array, label_obj)
        return array

    def create_empty_array(self, size, pos):
        slots = VGroup(*[Rectangle(width=0.5, height=0.3, color=WHITE, stroke_width=2) for _ in range(size)])
        slots.arrange(RIGHT, buff=0.4).move_to(pos)
        return slots

    def create_simple_split(self, sizes, pos):
        groups = VGroup()
        current_x = -3.5
        for size in sizes:
            box = Rectangle(width=1, height=0.5).move_to([current_x, pos[1], 0])
            label = Text(str(size), font_size=36).move_to(box)
            group = VGroup(box, label)
            groups.add(group)
            current_x += 1.2
        return groups

if __name__ == "__main__":
    # To render: manim -pql mergesort.py MergeSortExplanation
    # Requires: pip install manim manim-voiceover gtts
    # This generates a ~8-10 minute video due to detailed narrations (each block 20-30s, ~30 blocks)
    config.pixel_height = 1080
    config.pixel_width = 1920
    scene = MergeSortExplanation()
    scene.render()