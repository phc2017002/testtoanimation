from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import numpy as np

class HeapSortExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        # Section 1: Introduction
        self.introduction()

        # Section 2: What is a Heap?
        self.what_is_a_heap()

        # Section 3: Max Heap Structure
        self.max_heap_structure()

        # Section 4: Min Heap Structure
        self.min_heap_structure()

        # Section 5: Building a Heap
        self.building_a_heap()

        # Section 6: Heapify Down Procedure
        self.heapify_down_detailed()

        # Section 7: Heapify Up Procedure
        self.heapify_up_detailed()

        # Section 8: Heap Sort Algorithm Overview
        self.heap_sort_overview()

        # Section 9: Step-by-Step Example Part 1
        self.example_part1()

        # Section 10: Step-by-Step Example Part 2
        self.example_part2()

        # Section 11: Time Complexity Analysis
        self.time_complexity_analysis()

        # Section 12: Comparisons and Applications
        self.comparisons_and_applications()

        # Section 13: Summary
        self.summary()

    def introduction(self):
        with self.voiceover(text="""Welcome to this comprehensive explanation of the Heap Sort algorithm. Heap Sort is a powerful comparison-based sorting algorithm that leverages the heap data structure to achieve efficient sorting in O(n log n) time complexity. Unlike quicksort, which can degrade to O(n squared) in worst cases, Heap Sort guarantees optimal performance regardless of input. Over the next several minutes, we'll dive deep into heaps, how to build them, the key heapify operations, the full algorithm, a detailed step-by-step example, complexity analysis, and real-world applications. By the end, you'll fully understand how to implement and visualize Heap Sort.""") as tracker:
            title = Text("Heap Sort Algorithm\nExplained", font_size=36, color=BLUE).to_edge(UP, buff=1.0)
            self.play(Write(title))
            self.wait()

        with self.voiceover(text="""Sorting algorithms are fundamental in computer science, used everywhere from databases to search engines. Heap Sort stands out because it first transforms the array into a heap—a special tree structure—then repeatedly extracts the maximum element to build the sorted array. This in-place sorting makes it memory efficient too. Let's start by understanding what a heap is.""") as tracker:
            sorting_icon = Circle(radius=1, color=YELLOW).next_to(title, DOWN, buff=1.0)
            arrow = Arrow(title.get_bottom(), sorting_icon.get_top(), buff=0.2)
            self.play(Create(sorting_icon), Create(arrow))
            self.wait()

        self.play(FadeOut(title), FadeOut(sorting_icon), FadeOut(arrow))

    def what_is_a_heap(self):
        with self.voiceover(text="""A heap is a complete binary tree that satisfies the heap property. It's 'complete' meaning all levels are fully filled except possibly the last, which is filled left to right. We represent it compactly in an array where for a node at index i, its left child is at 2i+1 and right at 2i+2—assuming 0-based indexing. This array representation avoids pointers, saving space. Heaps are crucial for priority queues and sorting.""") as tracker:
            title = Text("What is a Heap?", font_size=36, color=GREEN).to_edge(UP, buff=1.0)
            self.play(Write(title))

            # Fix: Move array higher (UP * 2.0) to avoid overlap with tree nodes at center/below
            array = MathTex(r"\text{Array: } [", r"4", r", 1", r", 3", r", 2", r"]").scale(0.9).move_to(UP * 2.0)
            
            # Move structure down to provide clearance
            tree_nodes = VGroup(
                Circle().move_to(DOWN * 0.0),
                Circle().move_to(LEFT * 2 + DOWN * 1.5),
                Circle().move_to(RIGHT * 2 + DOWN * 1.5),
                Circle().move_to(LEFT * 4 + DOWN * 3),
                Circle().move_to(RIGHT * 1 + DOWN * 3)
            ).scale(0.6).shift(DOWN * 0.5) # Shift whole tree down
            
            connections = VGroup(
                Line(tree_nodes[0].get_center(), tree_nodes[1].get_center()),
                Line(tree_nodes[0].get_center(), tree_nodes[2].get_center()),
                Line(tree_nodes[1].get_center(), tree_nodes[3].get_center()),
                Line(tree_nodes[1].get_center(), tree_nodes[4].get_center())
            )
            self.play(Write(array))
            self.play(Create(tree_nodes), Create(connections))

        with self.voiceover(text="""Visually, the tree mirrors the array: root at index 0, children derived by doubling indices. This duality allows efficient operations. Next, we'll explore the two types: max heaps and min heaps, defined by their ordering property.""") as tracker:
            labels = VGroup(MathTex(r"0"), MathTex(r"1"), MathTex(r"2"), MathTex(r"3"), MathTex(r"4")).scale(0.8)
            labels.arrange(RIGHT, buff=0.5).next_to(array, DOWN, buff=0.3)
            
            node_labels = VGroup(MathTex("4"), MathTex("1"), MathTex("3"), MathTex("2")).scale(0.8)
            for i, node in enumerate(tree_nodes[:4]):
                node_label = node_labels[i].move_to(node.get_center() + UP * 0.08)
                self.play(Write(node_label))

            self.play(Write(labels))
            self.wait()

        self.play(FadeOut(*self.mobjects))

    def max_heap_structure(self):
        with self.voiceover(text="""A max heap ensures every parent node is greater than or equal to its children. This 'max heap property' bubbles the largest element to the root. In our array view, for every i, array[i] >= array[2i+1] and array[i] >= array[2i+2]. This property is violated during insertions or deletions, requiring heapify to restore it.""") as tracker:
            title = Text("Max Heap Property", font_size=36, color=RED).to_edge(UP, buff=1.0)
            self.play(Write(title))

            eq = MathTex(r"A[i] \geq A[2i+1], \ A[2i+2]", font_size=32).next_to(title, DOWN, buff=0.5)
            self.play(Write(eq))

        with self.voiceover(text="""Here's a valid max heap: [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]. Notice 16 at root, largest. 14 > 8 and 7, 10 > 9 and 3, and so on. The tree view highlights the parent-child inequalities with arrows.""") as tracker:
            # Fix: Move array up to avoid crossing tree area
            array = MathTex(r"[16, 14, 10, 8, 7, 9, 3, 2, 4, 1]", font_size=28).next_to(eq, DOWN, buff=0.5)
            
            # Define tree positions explicitly and scale/shift to fit bottom
            positions = [
                UP * 0, 
                LEFT*2.5+DOWN*1.5, RIGHT*2.5+DOWN*1.5, 
                LEFT*4.5+DOWN*2.8, LEFT*0.5+DOWN*2.8, RIGHT*0.5+DOWN*2.8, RIGHT*4.5+DOWN*2.8, 
                LEFT*6+DOWN*4.0, LEFT*3+DOWN*4.0, RIGHT*3+DOWN*4.0
            ]
            tree_nodes = VGroup(*[Circle(radius=0.25, color=BLUE).move_to(pos) for pos in positions[:10]])
            tree_nodes.scale(0.8).move_to(DOWN * 1.5) # Center group in lower area

            self.play(Write(array), Create(tree_nodes))

            node_vals = [MathTex(str(v), font_size=24) for v in [16,14,10,8,7,9,3,2,4,1]]
            for i, val in enumerate(node_vals):
                val.move_to(tree_nodes[i])
                self.play(Write(val))

            prop_arrows = VGroup(
                Arrow(tree_nodes[0].get_bottom(), tree_nodes[1].get_top(), buff=0.05, color=GREEN),
                Arrow(tree_nodes[1].get_bottom(), tree_nodes[3].get_top(), buff=0.05, color=GREEN),
                Arrow(tree_nodes[1].get_bottom(), tree_nodes[4].get_top(), buff=0.05, color=GREEN)
            )
            self.play(Create(prop_arrows))
            self.wait()

        self.play(FadeOut(*self.mobjects))

    def min_heap_structure(self):
        with self.voiceover(text="""Conversely, a min heap has every parent smaller than or equal to its children. Ideal for extracting minimums, like Dijkstra's algorithm. Property: A[i] <= A[2i+1] and A[i] <= A[2i+2]. Heap Sort typically uses max heaps to sort in ascending order by extracting max repeatedly.""") as tracker:
            title = Text("Min Heap Property", font_size=36, color=ORANGE).to_edge(UP, buff=1.0)
            eq = MathTex(r"A[i] \leq A[2i+1], \ A[2i+2]", font_size=32).next_to(title, DOWN, buff=0.6)
            self.play(Write(title), Write(eq))

        with self.voiceover(text="""Example min heap: [1, 2, 3, 4, 7, 9, 10, 14, 8, 16]. 1 is smallest at root. Children of 2 are 4 and 7, both larger. This structure supports efficient minimum priority queues.""") as tracker:
            # Fix: Move array higher
            array_min = MathTex(r"[1, 2, 3, 4, 7, 9, 10, 14, 8, 16]", font_size=28).next_to(eq, DOWN, buff=0.5)
            
            positions = [
                UP * 0, 
                LEFT*2.5+DOWN*1.5, RIGHT*2.5+DOWN*1.5, 
                LEFT*4.5+DOWN*2.8, LEFT*0.5+DOWN*2.8, RIGHT*0.5+DOWN*2.8, RIGHT*4.5+DOWN*2.8, 
                LEFT*6+DOWN*4.0, LEFT*3+DOWN*4.0, RIGHT*3+DOWN*4.0
            ]
            tree_nodes_min = VGroup(*[Circle(radius=0.25, color=PURPLE).move_to(pos) for pos in positions])
            tree_nodes_min.scale(0.8).move_to(DOWN * 1.5)

            # Fix: Add specific note about spacing to avoid overlap with node '3'
            node_vals_min = [MathTex(str(v), font_size=24) for v in [1,2,3,4,7,9,10,14,8,16]]
            self.play(Write(array_min), Create(tree_nodes_min))
            for i, val in enumerate(node_vals_min):
                val.move_to(tree_nodes_min[i])
                self.play(Write(val))

        self.play(FadeOut(*self.mobjects))

    def building_a_heap(self):
        with self.voiceover(text="""To sort, we first build a max heap from the unsorted array. The naive way—insert one by one—is O(n log n), but we can do better with bottom-up heapify in O(n). Start from the last non-leaf node (floor(n/2)-1) and call heapify-down on each, propagating properties upward.""") as tracker:
            title = Text("Building a Max Heap", font_size=36, color=YELLOW).to_edge(UP, buff=1.0)
            build_eq = MathTex(r"\\text{for } i = \\lfloor n/2 \\rfloor -1 \\text{ to } 0: \\\\ \\text{heapify-down}(A, i)", font_size=28).next_to(title, DOWN, buff=0.6)
            self.play(Write(title), Write(build_eq))

        with self.voiceover(text="""Consider unsorted array [4,1,3,2,16,9,10,14,8,7]. Last non-leaf is index 4 (value 9). Heapify-down on 4 swaps 9 with larger child if needed, then recurse. Repeat backward to root. This linear time build is a key insight by Floyd.""") as tracker:
            # Fix: Added spaces in list
            unsorted = MathTex(r"[4, 1, 3, 2, 16, 9, 10, 14, 8, 7]", font_size=28).move_to(DOWN * 2)
            self.play(Write(unsorted))
            rect = SurroundingRectangle(unsorted, buff=0.2, color=RED)
            self.play(Create(rect))
            self.wait(2)
            self.play(FadeOut(rect))

        self.play(FadeOut(*self.mobjects))

    def heapify_down_detailed(self):
        with self.voiceover(text="""Heapify-down restores max heap property at a subtree rooted at index i. Compare A[i] with its largest child. If parent smaller, swap with largest child and recurse on that child until property holds. Leaves no recursion. Pseudocode: find largest among i, left, right; if not i, swap and heapify(largest).""") as tracker:
            title = Text("Heapify-Down (Max Heap)", font_size=36, color=RED).to_edge(UP, buff=1.0)
            # Fix: Ensure no overlap with title by moving block down
            pseudo = MathTex(
                r"\\text{def heapify-down}(A, i):\\\\",
                r"n = len(A)\\\\",
                r"largest = i\\\\",
                r"l = 2*i + 1; r = 2*i + 2\\\\",
                r"\\text{if } l < n \\text{ and } A[l] > A[largest]: largest = l\\\\",
                r"\\text{if } r < n \\text{ and } A[r] > A[largest]: largest = r\\\\",
                r"\\text{if } largest != i:\\\\",
                r"\\quad \\text{swap}(A,i,largest)\\\\",
                r"\\quad \\text{heapify-down}(A, largest)"
            ).scale(0.7).move_to(LEFT * 3.5 + DOWN * 0.5)
            self.play(Write(title), Write(pseudo))

        with self.voiceover(text="""Animation: suppose at i=1, A=[16,4,10,...], children 8 and 7. 10 largest child, but if 4<10, swap 4 and 10, then check 10's subtree. Bubbles down violations efficiently, O(log n) worst case.""") as tracker:
            nodes = VGroup(Circle().move_to(UP*0.5), Circle().move_to(LEFT*1.5+DOWN*1), Circle().move_to(RIGHT*1.5+DOWN*1), Circle().move_to(LEFT*3+DOWN*2.2)).scale(0.5).shift(RIGHT * 3)
            vals = [MathTex("4",font_size=24), MathTex("8"), MathTex("10"), MathTex("14")]
            for i, v in enumerate(vals):
                v.move_to(nodes[i])
            self.play(Create(nodes), *[Write(v) for v in vals])
            swap_arrow = Arrow(nodes[0].get_center(), nodes[2].get_center(), color=ORANGE, buff=0.1)
            self.play(Create(swap_arrow))
            self.wait()

        self.play(FadeOut(*self.mobjects))

    def heapify_up_detailed(self):
        with self.voiceover(text="""Heapify-up is used after insertion: start from new leaf, swap with smaller parent if larger, until root or property holds. Symmetric to down, used in building bottom-up or inserts. While parent exists and child > parent, swap.""") as tracker:
            title = Text("Heapify-Up (Max Heap)", font_size=36, color=RED).to_edge(UP, buff=1.0)
            # Fix: Move down to avoid title overlap
            pseudo_up = MathTex(
                r"\\text{def heapify-up}(A, i):\\\\",
                r"\\text{while } i > 0:\\\\",
                r"\\quad p = \\text{floor}((i-1)/2)\\\\",
                r"\\quad \\text{if } A[i] > A[p]:\\\\",
                r"\\quad \\quad \\text{swap}(A,i,p)\\\\",
                r"\\quad \\quad i = p\\\\",
                r"\\quad \\text{else: break}"
            ).scale(0.7).move_to(LEFT * 3.5 + DOWN * 0.5)
            self.play(Write(title), Write(pseudo_up))

        with self.voiceover(text="""Example: insert 20 into heap. Append to array end, heapify-up: compare with parent, swap if larger, bubbling up. O(log n) height.""") as tracker:
            insert_array = MathTex(r"[16, 14, 10, 8, 7, 9, 3, 2, 4, 1, 20]", font_size=24).move_to(DOWN * 2 + RIGHT * 2)
            self.play(Write(insert_array))
            bubble_arrow = CurvedArrow(RIGHT * 4 + DOWN * 1.5, RIGHT * 2 + UP * 0.5, angle=TAU/4, color=GREEN)
            self.play(Create(bubble_arrow))
            self.wait()

        self.play(FadeOut(*self.mobjects))

    def heap_sort_overview(self):
        with self.voiceover(text="""Heap Sort: 1. Build max heap from array (O(n)). 2. For i from n-1 to 1: swap root A[0] with A[i], reduce heap size by 1, heapify-down on root. Largest goes to end, repeat. In-place, stable performance.""") as tracker:
            title = Text("Heap Sort Algorithm", font_size=36, color=BLUE).to_edge(UP, buff=1.0)
            # Fix: Use valid multiline TeX to prevent packing overlaps
            steps = MathTex(
                r"1. \\text{build\_max\_heap}(A) \\\\",
                r"2. \\text{for } i = n-1 \\text{ downto } 1: \\\\",
                r"\\quad A[0] \\leftrightarrow A[i] \\\\",
                r"\\quad \\text{heap\_size} -= 1 \\\\",
                r"\\quad \\text{heapify\_down}(A, 0)"
            ).scale(0.9).next_to(title, DOWN, buff=0.8)
            self.play(Write(title), Write(steps))

        with self.voiceover(text="""Visually, after build, largest at root. Swap to end, heapify restores subtree, next largest to root, repeat. Unsorted suffix grows, prefix shrinks.""") as tracker:
            before = MathTex(r"\\text{Max Heap: } [16, 14, 10, ...]", font_size=28).to_edge(LEFT).shift(DOWN * 2)
            after_swap = MathTex(r"\\text{Swap: } [14, 10, 16 | ...]", font_size=28).next_to(before, RIGHT, buff=0.8)
            divider = Line(DOWN*1.2, DOWN*2.8, color=GRAY).next_to(after_swap, RIGHT, buff=0.5)
            self.play(Write(before), Write(after_swap), Create(divider))
            self.wait()

        self.play(FadeOut(*self.mobjects))

    def example_part1(self):
        # Use example: [4,1,3,2,16,9,10,14,8,7]
        with self.voiceover(text="""Let's trace Heap Sort on [4,1,3,2,16,9,10,14,8,7]. First, build max heap. Start heapify-down from i=4 (9). Children 14 and 8, 14>9>8, swap 9 and 14: now [4,1,3,2,14,9,10,9,8,7]. Then heapify on 4 (now 9), no children larger.""") as tracker:
            title = Text("Example: Build Heap (Part 1)", font_size=36, color=GREEN).to_edge(UP, buff=1.0)
            # Fix: Added spaces to comma separated lists
            arr1 = MathTex(r"[4, 1, 3, 2, \\color{red}{16}, \\color{red}{9}, 10, 14, 8, 7]").scale(0.9).move_to(DOWN * 1.8)
            self.play(Write(title), Write(arr1))
            # Fix: Highlight rectangle overlapping text. Increased buff.
            swap_highlight = SurroundingRectangle(arr1, buff=0.15, color=ORANGE) # Simplified to surround whole array or just move it
            # Creating a precise target since arr1 is a VGroup of chars
            # To highlight 16 and 9 specifically without overlap issues, use a wider box manually positioned
            hl_box = SurroundingRectangle(MathTex(r"16, 9").scale(0.9), buff=0.3, color=ORANGE).move_to(arr1.get_center())
            self.play(Create(hl_box))

        with self.voiceover(text="""Next i=3 (2), children 8,7; 8>2, swap 2-8: [4,1,3,8,14,9,10,9,2,7]. Heapify on 8 (now2), leaf ok. Continue similarly until full max heap: [16,14,10,8,7,9,3,2,4,1].""") as tracker:
            # Fix: Added spaces
            arr2 = MathTex(r"[4, 1, 3, \\color{red}{2}, 14, 9, 10, 9, \\color{red}{8}, 7]").scale(0.9).move_to(arr1.get_center())
            self.play(Transform(arr1, arr2), FadeOut(hl_box))
            final_heap = MathTex(r"[16, 14, 10, 8, 7, 9, 3, 2, 4, 1]", font_size=32).move_to(arr2.get_center())
            self.play(Transform(arr2, final_heap))
            self.wait()

        self.play(FadeOut(*self.mobjects))

    def example_part2(self):
        with self.voiceover(text="""Now sorting phase. Heap size=10, swap root 16 with end 1: [1,14,10,8,7,9,3,2,4,16], size=9, heapify-down on 1. Largest child 14 or 10, swap with 14: [14,1,10,8,7,9,3,2,4,16], then on 1 (now1), leaf.""") as tracker:
            title = Text("Example: Sorting Phase (Part 2)", font_size=36, color=GREEN).to_edge(UP, buff=1.0)
            # Fix: Fixed closing bracket overlap with spacing
            swap1 = MathTex(r"[\\color{red}{16}, 14, 10, 8, 7, 9, 3, 2, 4, \\color{red}{1}\\, ] \\to [1, 14, ..., 16]").scale(0.85).move_to(DOWN * 1.5)
            self.play(Write(title), Write(swap1))

        with self.voiceover(text="""Repeat: swap 14 with 4: [4,10,1,8,7,9,3,2,14,16], heapify yields next max at root, continue until [1,2,3,4,7,8,9,10,14,16] sorted! Each extract O(log n), total O(n log n).""") as tracker:
            sorted_final = MathTex(r"[1, 2, 3, 4, 7, 8, 9, 10, 14, 16]", font_size=36, color=GOLD).move_to(DOWN * 0.5)
            self.play(Transform(swap1, sorted_final), run_time=3)
            checkmark = Text("✓ Sorted!", font_size=32, color=GREEN).next_to(sorted_final, DOWN)
            self.play(Write(checkmark))
            self.wait()

        self.play(FadeOut(*self.mobjects))

    def time_complexity_analysis(self):
        with self.voiceover(text="""Time complexity: Build heap O(n), since heapify-down heights sum to O(n). Each of n extracts: swap O(1) + heapify O(log n), total O(n log n). Space O(1) in-place. Worst/average/best all O(n log n), beats merge sort space-wise, stable unlike quicksort worst-case.""") as tracker:
            title = Text("Time Complexity", font_size=36, color=BLUE).to_edge(UP, buff=1.0)
            # Fix: Position relative to title to avoid overlap
            complexity = MathTex(r"O(n \\text{ build}) + O(n \\log n \\text{ extracts}) = O(n \\log n)", font_size=36).next_to(title, DOWN, buff=0.5)
            self.play(Write(title), Write(complexity))

        with self.voiceover(text="""Proof sketch: Height h=log n, nodes at height k contribute O(n / 2^k * k) work, telescopes to O(n). Reliable performance makes it great for embedded systems.""") as tracker:
            graph = Axes(x_range=[0,11,1], y_range=[0,5,1], x_length=7, y_length=4).move_to(DOWN * 1.5)
            line = graph.plot(lambda x: x * np.log2(x) if x>0 else 0, color=RED)
            label = Text("O(n log n)", font_size=24).next_to(graph, RIGHT, buff=0.6)
            self.play(Create(graph), Create(line), Write(label))
            self.wait()

        self.play(FadeOut(*self.mobjects))

    def comparisons_and_applications(self):
        with self.voiceover(text="""Compared to Quicksort: Heap Sort slower constant but guaranteed O(n log n), no pivot issues. Vs Merge Sort: in-place, no extra space. Vs Heapsort strengths: priority queues, median finding, graph algos like Prim/Dijkstra use heap variants.""") as tracker:
            title = Text("Comparisons & Applications", font_size=36, color=PURPLE).to_edge(UP, buff=1.0)

            left_col = VGroup(
                Text("Heap Sort", font_size=24),
                MathTex(r"O(n \\log n)", font_size=24, color=GREEN),
                Text("In-place", font_size=24, color=GREEN)
            ).arrange(DOWN, buff=0.6).move_to(LEFT * 3.2)

            # Fix: Increased buff and spacing in strings to avoid overlaps
            right_col = VGroup(
                Text("Quick Sort", font_size=24),
                MathTex(r"O(n \\log n) \\text{ avg}", font_size=24, color=YELLOW),
                Text("O(n^2) worst", font_size=24, color=RED)
            ).arrange(DOWN, buff=0.6).move_to(RIGHT * 3.2)

            self.play(Write(title), Write(left_col), Write(right_col))

        with self.voiceover(text="""Applications: OS task scheduling (priority), Huffman coding, k-largest elements. Python's heapq module uses min-heap for these. Versatile!""") as tracker:
            apps = VGroup(
                Text("• Priority Queues", font_size=24),
                Text("• Graph Algorithms", font_size=24),
                Text("• Scheduling", font_size=24)
            ).arrange(DOWN, buff=0.5).move_to(DOWN * 0.8)
            self.play(Write(apps))
            self.wait()

        self.play(FadeOut(*self.mobjects))

    def summary(self):
        with self.voiceover(text="""To recap: Heap Sort builds a max heap in O(n), then extracts max n times in O(n log n) total. Key ops: heapify-up/down maintain properties. Reliable, in-place, O(n log n). Implement by transforming arrays to trees visually in mind. Thanks for watching this deep dive—practice with code to master it!""") as tracker:
            summary_title = Text("Summary", font_size=36, color=GOLD).to_edge(UP, buff=1.0)
            key_points = VGroup(
                Text("• Binary Heap Tree", font_size=28),
                Text("• Build O(n)", font_size=28),
                Text("• Sort O(n log n)", font_size=28),
                Text("• In-place!", font_size=28)
            ).arrange(DOWN, buff=0.4).next_to(summary_title, DOWN, buff=0.8)
            self.play(Write(summary_title), Write(key_points))
            thanks = Text("Thank You!", font_size=36, color=BLUE).to_edge(DOWN)
            self.play(Write(thanks))
            self.wait(3)

        self.play(FadeOut(*self.mobjects))

# Instructions to run:
# pip install manim manim-voiceover  (if needed)
# manim -pql this_file.py HeapSortExplanation
if __name__ == "__main__":
    from manim import config
    config.background_color = BLACK  # Optional
    scene = HeapSortExplanation()
    scene.render()