from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class BinarySearchTreeExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))
        
        # Run all sections
        self.introduction()
        self.historical_context()
        self.tree_structure_basics()
        self.bst_property_explanation()
        self.insertion_operation()
        self.search_operation()
        self.deletion_operation()
        self.time_complexity_analysis()
        self.balanced_vs_unbalanced()
        self.real_world_applications()
        self.advantages_and_disadvantages()
        self.conclusion()
    
    def introduction(self):
        with self.voiceover(text="Welcome to this comprehensive explanation of Binary Search Trees, one of the most fundamental data structures in computer science. A Binary Search Tree, commonly abbreviated as BST, is a tree-based data structure that maintains elements in a sorted order, allowing for efficient searching, insertion, and deletion operations.") as tracker:
            title = Text("Binary Search Trees", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            subtitle = Text("A Fundamental Data Structure", font_size=24, color=YELLOW)
            subtitle.next_to(title, DOWN, buff=0.4)
            
            self.play(Write(title), run_time=2)
            self.play(FadeIn(subtitle), run_time=1.5)
        
        with self.voiceover(text="Throughout this video, we will explore how Binary Search Trees work, their properties, operations, time complexities, and practical applications. We'll visualize each concept step by step to build a complete understanding of this essential data structure.") as tracker:
            key_topics = VGroup(
                Text("• Tree Structure & Properties", font_size=22),
                Text("• Insertion, Search & Deletion", font_size=22),
                Text("• Time Complexity Analysis", font_size=22),
                Text("• Real-world Applications", font_size=22)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            key_topics.move_to(ORIGIN)
            
            self.play(FadeIn(key_topics, shift=UP), run_time=2)
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))
    
    def historical_context(self):
        with self.voiceover(text="Before diving into Binary Search Trees, let's understand why they were developed. In the early days of computing, organizing and retrieving data efficiently was a major challenge. Linear search through arrays required examining every element, which was extremely slow for large datasets.") as tracker:
            title = Text("Historical Context", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Show linear array
            array_label = Text("Linear Array Search", font_size=24, color=YELLOW)
            array_label.move_to(UP * 1.5)
            
            array = VGroup(*[Square(side_length=0.6, color=WHITE) for _ in range(8)])
            array.arrange(RIGHT, buff=0.1)
            array.move_to(ORIGIN)
            
            values = [12, 5, 18, 3, 9, 15, 21, 7]
            labels = VGroup(*[Text(str(val), font_size=20).move_to(array[i]) for i, val in enumerate(values)])
            
            self.play(Write(array_label))
            self.play(Create(array), Write(labels))
        
        with self.voiceover(text="Binary Search Trees were developed to overcome this limitation. They combine the efficiency of binary search with the flexibility of linked structures. The key insight is organizing data in a hierarchical tree structure where each decision cuts the search space in half, similar to how binary search works on sorted arrays.") as tracker:
            # Highlight sequential search
            search_arrow = Arrow(start=UP*0.3, end=DOWN*0.3, color=RED)
            search_arrow.next_to(array[0], UP, buff=0.2)
            
            for i in range(8):
                search_arrow.next_to(array[i], UP, buff=0.2)
                self.play(search_arrow.animate.next_to(array[i], UP, buff=0.2), run_time=0.3)
            
            complexity = MathTex(r"O(n)", r"\text{ time complexity}", font_size=28, color=RED)
            complexity.next_to(array, DOWN, buff=0.6)
            self.play(Write(complexity))
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))
    
    def tree_structure_basics(self):
        with self.voiceover(text="Let's begin by understanding the basic structure of a tree. A tree is a hierarchical data structure consisting of nodes connected by edges. The topmost node is called the root. Each node can have child nodes, and nodes without children are called leaf nodes.") as tracker:
            title = Text("Tree Structure Basics", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Create a simple tree structure
            root = Circle(radius=0.35, color=GREEN).shift(UP * 1.2)
            root_label = Text("Root", font_size=18).move_to(root)
            
            left_child = Circle(radius=0.35, color=YELLOW).shift(LEFT * 2 + DOWN * 0.5)
            left_label = Text("Node", font_size=18).move_to(left_child)
            
            right_child = Circle(radius=0.35, color=YELLOW).shift(RIGHT * 2 + DOWN * 0.5)
            right_label = Text("Node", font_size=18).move_to(right_child)
            
            left_leaf = Circle(radius=0.35, color=ORANGE).shift(LEFT * 3 + DOWN * 2.2)
            left_leaf_label = Text("Leaf", font_size=18).move_to(left_leaf)
            
            right_leaf = Circle(radius=0.35, color=ORANGE).shift(RIGHT * 3 + DOWN * 2.2)
            right_leaf_label = Text("Leaf", font_size=18).move_to(right_leaf)
            
            edge1 = Line(root.get_bottom(), left_child.get_top(), color=WHITE)
            edge2 = Line(root.get_bottom(), right_child.get_top(), color=WHITE)
            edge3 = Line(left_child.get_bottom(), left_leaf.get_top(), color=WHITE)
            edge4 = Line(right_child.get_bottom(), right_leaf.get_top(), color=WHITE)
            
            self.play(Create(root), Write(root_label))
            self.play(Create(edge1), Create(edge2))
            self.play(Create(left_child), Write(left_label), Create(right_child), Write(right_label))
            self.play(Create(edge3), Create(edge4))
            self.play(Create(left_leaf), Write(left_leaf_label), Create(right_leaf), Write(right_leaf_label))
        
        with self.voiceover(text="In a binary tree, each node has at most two children, commonly referred to as the left child and the right child. The height of a tree is the longest path from the root to any leaf node. Understanding this structure is crucial before we introduce the special property that makes a Binary Search Tree unique.") as tracker:
            # Add labels for left and right
            left_arrow = Arrow(start=LEFT*1.2+UP*0.5, end=left_child.get_top(), color=BLUE, buff=0.1)
            left_text = Text("Left Child", font_size=20, color=BLUE).next_to(left_arrow, LEFT, buff=0.2)
            
            right_arrow = Arrow(start=RIGHT*1.2+UP*0.5, end=right_child.get_top(), color=BLUE, buff=0.1)
            right_text = Text("Right Child", font_size=20, color=BLUE).next_to(right_arrow, RIGHT, buff=0.2)
            
            self.play(Create(left_arrow), Write(left_text))
            self.play(Create(right_arrow), Write(right_text))
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))
    
    def bst_property_explanation(self):
        with self.voiceover(text="Now let's explore the defining property of a Binary Search Tree. The BST property states that for every node in the tree, all values in its left subtree must be less than the node's value, and all values in its right subtree must be greater than the node's value. This property must hold for every single node in the tree.") as tracker:
            title = Text("The BST Property", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Mathematical definition
            definition = MathTex(
                r"\text{For every node } n:",
                r"\text{ Left}(n) < n < \text{Right}(n)",
                font_size=30
            ).arrange(DOWN, buff=0.3)
            definition.move_to(UP * 1.8)
            
            self.play(Write(definition))
            self.wait(1)
        
        with self.voiceover(text="Let's visualize this with a concrete example. Consider a BST with root value 15. All nodes in the left subtree have values less than 15, such as 10, 5, and 12. All nodes in the right subtree have values greater than 15, such as 20, 18, and 25. This ordering property is what enables efficient searching.") as tracker:
            # Create BST with values
            root_val = 15
            root = Circle(radius=0.4, color=GREEN).shift(UP * 0.8)
            root_label = Text(str(root_val), font_size=22).move_to(root)
            
            left_val = 10
            left = Circle(radius=0.4, color=YELLOW).shift(LEFT * 2.5 + DOWN * 0.8)
            left_label = Text(str(left_val), font_size=22).move_to(left)
            
            right_val = 20
            right = Circle(radius=0.4, color=YELLOW).shift(RIGHT * 2.5 + DOWN * 0.8)
            right_label = Text(str(right_val), font_size=22).move_to(right)
            
            ll_val = 5
            ll = Circle(radius=0.4, color=ORANGE).shift(LEFT * 3.5 + DOWN * 2.4)
            ll_label = Text(str(ll_val), font_size=22).move_to(ll)
            
            lr_val = 12
            lr = Circle(radius=0.4, color=ORANGE).shift(LEFT * 1.5 + DOWN * 2.4)
            lr_label = Text(str(lr_val), font_size=22).move_to(lr)
            
            rl_val = 18
            rl = Circle(radius=0.4, color=ORANGE).shift(RIGHT * 1.5 + DOWN * 2.4)
            rl_label = Text(str(rl_val), font_size=22).move_to(rl)
            
            rr_val = 25
            rr = Circle(radius=0.4, color=ORANGE).shift(RIGHT * 3.5 + DOWN * 2.4)
            rr_label = Text(str(rr_val), font_size=22).move_to(rr)
            
            # Edges
            edges = VGroup(
                Line(root.get_bottom(), left.get_top(), color=WHITE),
                Line(root.get_bottom(), right.get_top(), color=WHITE),
                Line(left.get_bottom(), ll.get_top(), color=WHITE),
                Line(left.get_bottom(), lr.get_top(), color=WHITE),
                Line(right.get_bottom(), rl.get_top(), color=WHITE),
                Line(right.get_bottom(), rr.get_top(), color=WHITE)
            )
            
            self.play(Create(edges))
            self.play(
                Create(root), Write(root_label),
                Create(left), Write(left_label),
                Create(right), Write(right_label)
            )
            self.play(
                Create(ll), Write(ll_label),
                Create(lr), Write(lr_label),
                Create(rl), Write(rl_label),
                Create(rr), Write(rr_label)
            )
            
            # Highlight left subtree
            left_subtree = SurroundingRectangle(VGroup(left, ll, lr), color=BLUE, buff=0.15)
            left_text = Text("All < 15", font_size=20, color=BLUE).next_to(left_subtree, LEFT, buff=0.3)
            self.play(Create(left_subtree), Write(left_text))
            self.wait(0.5)
            
            # Highlight right subtree
            right_subtree = SurroundingRectangle(VGroup(right, rl, rr), color=RED, buff=0.15)
            right_text = Text("All > 15", font_size=20, color=RED).next_to(right_subtree, RIGHT, buff=0.3)
            self.play(Create(right_subtree), Write(right_text))
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))
    
    def insertion_operation(self):
        with self.voiceover(text="Let's examine how we insert a new value into a Binary Search Tree. The insertion algorithm is elegant and recursive. We start at the root and compare our value with the current node. If our value is less, we go left; if greater, we go right. We continue until we find an empty spot where we can place our new node.") as tracker:
            title = Text("Insertion Operation", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Initial BST
            root = Circle(radius=0.35, color=GREEN).shift(UP * 1.0)
            root_label = Text("15", font_size=20).move_to(root)
            
            left = Circle(radius=0.35, color=YELLOW).shift(LEFT * 2 + DOWN * 0.5)
            left_label = Text("10", font_size=20).move_to(left)
            
            right = Circle(radius=0.35, color=YELLOW).shift(RIGHT * 2 + DOWN * 0.5)
            right_label = Text("20", font_size=20).move_to(right)
            
            ll = Circle(radius=0.35, color=ORANGE).shift(LEFT * 3 + DOWN * 2.0)
            ll_label = Text("5", font_size=20).move_to(ll)
            
            edges = VGroup(
                Line(root.get_bottom(), left.get_top(), color=WHITE),
                Line(root.get_bottom(), right.get_top(), color=WHITE),
                Line(left.get_bottom(), ll.get_top(), color=WHITE)
            )
            
            self.play(Create(edges))
            self.play(
                Create(root), Write(root_label),
                Create(left), Write(left_label),
                Create(right), Write(right_label),
                Create(ll), Write(ll_label)
            )
        
        with self.voiceover(text="Let's insert the value 12 into this tree. We start at the root which is 15. Since 12 is less than 15, we move to the left child which is 10. Now 12 is greater than 10, so we move to the right. The right child of 10 is empty, so this is where we place our new node with value 12.") as tracker:
            # Show value to insert
            insert_text = Text("Insert: 12", font_size=24, color=BLUE_C)
            insert_text.to_edge(LEFT, buff=1.0).shift(UP * 2)
            self.play(Write(insert_text))
            
            # Traversal path
            path1 = Arrow(start=insert_text.get_right(), end=root.get_left(), color=BLUE_C, buff=0.1)
            self.play(Create(path1))
            self.play(root.animate.set_color(CYAN), run_time=0.5)
            self.wait(0.3)
            
            compare1 = Text("12 < 15 → go left", font_size=18, color=BLUE_C)
            compare1.next_to(root, RIGHT, buff=0.3)
            self.play(Write(compare1))
            
            self.play(root.animate.set_color(GREEN), left.animate.set_color(CYAN), run_time=0.5)
            self.wait(0.3)
            self.play(FadeOut(compare1))
            
            compare2 = Text("12 > 10 → go right", font_size=18, color=BLUE_C)
            compare2.next_to(left, LEFT, buff=0.3)
            self.play(Write(compare2))
            
            # Create new node
            new_node = Circle(radius=0.35, color=BLUE_C).shift(LEFT * 1 + DOWN * 2.0)
            new_label = Text("12", font_size=20).move_to(new_node)
            new_edge = Line(left.get_bottom(), new_node.get_top(), color=WHITE)
            
            self.play(Create(new_edge), Create(new_node), Write(new_label))
            self.play(left.animate.set_color(YELLOW), new_node.animate.set_color(ORANGE))
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))
    
    def search_operation(self):
        with self.voiceover(text="Searching in a Binary Search Tree is remarkably efficient. To find a value, we start at the root and use the BST property to eliminate half of the remaining tree at each step. If the target is less than the current node, we search left. If greater, we search right. If equal, we've found our target.") as tracker:
            title = Text("Search Operation", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Create BST
            root = Circle(radius=0.35, color=GREEN).shift(UP * 1.0)
            root_label = Text("15", font_size=20).move_to(root)
            
            left = Circle(radius=0.35, color=YELLOW).shift(LEFT * 2 + DOWN * 0.5)
            left_label = Text("10", font_size=20).move_to(left)
            
            right = Circle(radius=0.35, color=YELLOW).shift(RIGHT * 2 + DOWN * 0.5)
            right_label = Text("20", font_size=20).move_to(right)
            
            ll = Circle(radius=0.35, color=ORANGE).shift(LEFT * 3 + DOWN * 2.0)
            ll_label = Text("5", font_size=20).move_to(ll)
            
            lr = Circle(radius=0.35, color=ORANGE).shift(LEFT * 1 + DOWN * 2.0)
            lr_label = Text("12", font_size=20).move_to(lr)
            
            rl = Circle(radius=0.35, color=ORANGE).shift(RIGHT * 1 + DOWN * 2.0)
            rl_label = Text("18", font_size=20).move_to(rl)
            
            rr = Circle(radius=0.35, color=ORANGE).shift(RIGHT * 3 + DOWN * 2.0)
            rr_label = Text("25", font_size=20).move_to(rr)
            
            edges = VGroup(
                Line(root.get_bottom(), left.get_top(), color=WHITE),
                Line(root.get_bottom(), right.get_top(), color=WHITE),
                Line(left.get_bottom(), ll.get_top(), color=WHITE),
                Line(left.get_bottom(), lr.get_top(), color=WHITE),
                Line(right.get_bottom(), rl.get_top(), color=WHITE),
                Line(right.get_bottom(), rr.get_top(), color=WHITE)
            )
            
            self.play(Create(edges))
            self.play(
                Create(root), Write(root_label),
                Create(left), Write(left_label),
                Create(right), Write(right_label),
                Create(ll), Write(ll_label),
                Create(lr), Write(lr_label),
                Create(rl), Write(rl_label),
                Create(rr), Write(rr_label)
            )
        
        with self.voiceover(text="Let's search for the value 18. Starting at root 15, we compare: 18 is greater than 15, so we go right to node 20. Now 18 is less than 20, so we go left to node 18. We found it! This took only 3 comparisons instead of checking all 7 nodes. This logarithmic efficiency is the key advantage of Binary Search Trees.") as tracker:
            search_text = Text("Search: 18", font_size=24, color=PURPLE)
            search_text.to_edge(LEFT, buff=1.0).shift(UP * 2)
            self.play(Write(search_text))
            
            # Step 1
            self.play(root.animate.set_color(PURPLE), run_time=0.5)
            step1 = Text("18 > 15", font_size=18, color=PURPLE).next_to(root, RIGHT, buff=0.3)
            self.play(Write(step1))
            self.wait(0.5)
            
            # Step 2
            self.play(root.animate.set_color(GREEN), right.animate.set_color(PURPLE))
            self.play(FadeOut(step1))
            step2 = Text("18 < 20", font_size=18, color=PURPLE).next_to(right, RIGHT, buff=0.3)
            self.play(Write(step2))
            self.wait(0.5)
            
            # Step 3
            self.play(right.animate.set_color(YELLOW), rl.animate.set_color(PURPLE))
            self.play(FadeOut(step2))
            step3 = Text("Found!", font_size=18, color=PURPLE).next_to(rl, DOWN, buff=0.3)
            self.play(Write(step3))
            
            # Highlight found node
            found_circle = Circle(radius=0.5, color=PURPLE, stroke_width=4).move_to(rl)
            self.play(Create(found_circle))
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))
    
    def deletion_operation(self):
        with self.voiceover(text="Deletion is the most complex operation in a Binary Search Tree. There are three cases to consider. Case one: deleting a leaf node is simple, we just remove it. Case two: deleting a node with one child, we replace it with its child. Case three: deleting a node with two children requires finding either the inorder predecessor or successor.") as tracker:
            title = Text("Deletion Operation", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            case_text = Text("Three Cases of Deletion", font_size=26, color=YELLOW)
            case_text.move_to(UP * 1.8)
            self.play(Write(case_text))
            
            cases = VGroup(
                Text("1. Leaf Node (no children)", font_size=20),
                Text("2. One Child", font_size=20),
                Text("3. Two Children", font_size=20)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            cases.move_to(DOWN * 0.2)
            
            self.play(Write(cases[0]))
            self.wait(0.5)
            self.play(Write(cases[1]))
            self.wait(0.5)
            self.play(Write(cases[2]))
            self.wait(1)
        
        with self.voiceover(text="Let's visualize the most interesting case: deleting a node with two children. Suppose we want to delete node 15 which has both left and right children. We find the inorder successor, which is the smallest value in the right subtree. In this case, it's 18. We replace 15 with 18, then delete the original 18 node, which will be a simpler case.") as tracker:
            self.play(FadeOut(case_text), FadeOut(cases))
            
            # Create BST
            root = Circle(radius=0.35, color=GREEN).shift(UP * 1.0)
            root_label = Text("15", font_size=20).move_to(root)
            
            left = Circle(radius=0.35, color=YELLOW).shift(LEFT * 2 + DOWN * 0.5)
            left_label = Text("10", font_size=20).move_to(left)
            
            right = Circle(radius=0.35, color=YELLOW).shift(RIGHT * 2 + DOWN * 0.5)
            right_label = Text("20", font_size=20).move_to(right)
            
            ll = Circle(radius=0.35, color=ORANGE).shift(LEFT * 3 + DOWN * 2.0)
            ll_label = Text("5", font_size=20).move_to(ll)
            
            lr = Circle(radius=0.35, color=ORANGE).shift(LEFT * 1 + DOWN * 2.0)
            lr_label = Text("12", font_size=20).move_to(lr)
            
            rl = Circle(radius=0.35, color=ORANGE).shift(RIGHT * 1 + DOWN * 2.0)
            rl_label = Text("18", font_size=20).move_to(rl)
            
            rr = Circle(radius=0.35, color=ORANGE).shift(RIGHT * 3 + DOWN * 2.0)
            rr_label = Text("25", font_size=20).move_to(rr)
            
            edges = VGroup(
                Line(root.get_bottom(), left.get_top(), color=WHITE),
                Line(root.get_bottom(), right.get_top(), color=WHITE),
                Line(left.get_bottom(), ll.get_top(), color=WHITE),
                Line(left.get_bottom(), lr.get_top(), color=WHITE),
                Line(right.get_bottom(), rl.get_top(), color=WHITE),
                Line(right.get_bottom(), rr.get_top(), color=WHITE)
            )
            
            self.play(Create(edges))
            self.play(
                Create(root), Write(root_label),
                Create(left), Write(left_label),
                Create(right), Write(right_label),
                Create(ll), Write(ll_label),
                Create(lr), Write(lr_label),
                Create(rl), Write(rl_label),
                Create(rr), Write(rr_label)
            )
            
            # Highlight deletion
            del_text = Text("Delete: 15", font_size=22, color=RED)
            del_text.to_edge(LEFT, buff=1.0).shift(UP * 2.2)
            self.play(Write(del_text))
            self.play(root.animate.set_color(RED))
            
            # Find successor
            successor_text = Text("Find successor: 18", font_size=20, color=GREEN)
            successor_text.next_to(del_text, DOWN, buff=0.3)
            self.play(Write(successor_text))
            self.play(rl.animate.set_color(GREEN))
            
            # Replace
            new_root_label = Text("18", font_size=20).move_to(root)
            self.play(Transform(root_label, new_root_label))
            self.play(root.animate.set_color(GREEN), rl.animate.set_color(RED))
            
            # Remove old successor
            self.play(FadeOut(rl), FadeOut(rl_label), edges[4].animate.set_opacity(0))
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))
    
    def time_complexity_analysis(self):
        with self.voiceover(text="Now let's analyze the time complexity of Binary Search Tree operations. For a balanced BST with n nodes, the height is logarithmic, specifically log base 2 of n. Since operations like search, insertion, and deletion traverse from root to leaf, they all have a time complexity of O of log n in the best case.") as tracker:
            title = Text("Time Complexity Analysis", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Complexity table
            operations = VGroup(
                Text("Operation", font_size=24, color=YELLOW),
                Text("Search", font_size=22),
                Text("Insert", font_size=22),
                Text("Delete", font_size=22)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            operations.shift(LEFT * 3.5 + UP * 0.5)
            
            best_case = VGroup(
                Text("Best Case", font_size=24, color=GREEN),
                MathTex(r"O(\log n)", font_size=22),
                MathTex(r"O(\log n)", font_size=22),
                MathTex(r"O(\log n)", font_size=22)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            best_case.shift(LEFT * 0.5 + UP * 0.5)
            
            worst_case = VGroup(
                Text("Worst Case", font_size=24, color=RED),
                MathTex(r"O(n)", font_size=22),
                MathTex(r"O(n)", font_size=22),
                MathTex(r"O(n)", font_size=22)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            worst_case.shift(RIGHT * 2.5 + UP * 0.5)
            
            self.play(Write(operations))
            self.wait(0.5)
            self.play(Write(best_case))
            self.wait(0.5)
            self.play(Write(worst_case))
        
        with self.voiceover(text="However, the worst case occurs when the tree becomes unbalanced and degenerates into a linked list. In this scenario, the height becomes n, and all operations degrade to O of n time complexity. This is why balanced tree variants like AVL trees and Red-Black trees were developed to guarantee logarithmic height.") as tracker:
            # Height equation
            height_eq = MathTex(
                r"\text{Height } h = ",
                r"\begin{cases} \log_2(n) & \text{balanced} \\ n & \text{unbalanced} \end{cases}",
                font_size=28
            )
            height_eq.move_to(DOWN * 1.8)
            self.play(Write(height_eq))
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))
    
    def balanced_vs_unbalanced(self):
        with self.voiceover(text="Let's visualize the dramatic difference between balanced and unbalanced trees. On the left, we have a balanced Binary Search Tree where the height is logarithmic. Each level doubles the number of nodes we can store efficiently. This structure enables the fast operations we desire.") as tracker:
            title = Text("Balanced vs Unbalanced Trees", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Balanced tree label
            balanced_label = Text("Balanced BST", font_size=22, color=GREEN)
            balanced_label.shift(LEFT * 3.5 + UP * 1.8)
            self.play(Write(balanced_label))
            
            # Create balanced tree
            b_root = Circle(radius=0.25, color=GREEN).shift(LEFT * 3.5 + UP * 0.6)
            b_l = Circle(radius=0.25, color=GREEN).shift(LEFT * 4.3 + UP * 0.0)
            b_r = Circle(radius=0.25, color=GREEN).shift(LEFT * 2.7 + UP * 0.0)
            b_ll = Circle(radius=0.25, color=GREEN).shift(LEFT * 4.7 + DOWN * 0.6)
            b_lr = Circle(radius=0.25, color=GREEN).shift(LEFT * 3.9 + DOWN * 0.6)
            b_rl = Circle(radius=0.25, color=GREEN).shift(LEFT * 3.1 + DOWN * 0.6)
            b_rr = Circle(radius=0.25, color=GREEN).shift(LEFT * 2.3 + DOWN * 0.6)
            
            b_edges = VGroup(
                Line(b_root.get_bottom(), b_l.get_top(), color=WHITE, stroke_width=2),
                Line(b_root.get_bottom(), b_r.get_top(), color=WHITE, stroke_width=2),
                Line(b_l.get_bottom(), b_ll.get_top(), color=WHITE, stroke_width=2),
                Line(b_l.get_bottom(), b_lr.get_top(), color=WHITE, stroke_width=2),
                Line(b_r.get_bottom(), b_rl.get_top(), color=WHITE, stroke_width=2),
                Line(b_r.get_bottom(), b_rr.get_top(), color=WHITE, stroke_width=2)
            )
            
            self.play(Create(b_edges))
            self.play(Create(VGroup(b_root, b_l, b_r, b_ll, b_lr, b_rl, b_rr)))
            
            # Height annotation
            height_balanced = MathTex(r"h = \log_2(7) \approx 3", font_size=20, color=GREEN)
            height_balanced.shift(LEFT * 3.5 + DOWN * 1.5)
            self.play(Write(height_balanced))
        
        with self.voiceover(text="On the right, we see an unbalanced tree where nodes were inserted in sorted order. This creates a degenerate tree that's essentially a linked list. The height equals the number of nodes, destroying the efficiency benefits. Insertions of 1, 2, 3, 4, 5, 6, 7 in order create this worst-case structure.") as tracker:
            # Unbalanced tree label
            unbalanced_label = Text("Unbalanced BST", font_size=22, color=RED)
            unbalanced_label.shift(RIGHT * 3.5 + UP * 1.8)
            self.play(Write(unbalanced_label))
            
            # Create unbalanced tree (linked list)
            u_nodes = []
            u_edges = VGroup()
            for i in range(7):
                node = Circle(radius=0.25, color=RED).shift(RIGHT * 3.5 + UP * (0.8 - i * 0.45))
                u_nodes.append(node)
                if i > 0:
                    edge = Line(u_nodes[i-1].get_bottom(), u_nodes[i].get_top(), color=WHITE, stroke_width=2)
                    u_edges.add(edge)
            
            self.play(Create(u_edges))
            self.play(Create(VGroup(*u_nodes)))
            
            # Height annotation
            height_unbalanced = MathTex(r"h = 7", font_size=20, color=RED)
            height_unbalanced.shift(RIGHT * 3.5 + DOWN * 2.3)
            self.play(Write(height_unbalanced))
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))
    
    def real_world_applications(self):
        with self.voiceover(text="Binary Search Trees have numerous practical applications in computer science and software engineering. They are used in implementing symbol tables in compilers, where identifiers need to be looked up efficiently. Database systems use BST variants for indexing, allowing quick retrieval of records based on key values.") as tracker:
            title = Text("Real-World Applications", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            app1 = VGroup(
                Text("• Database Indexing", font_size=24, color=YELLOW),
                Text("  Fast record retrieval", font_size=18)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            app1.shift(UP * 1.2 + LEFT * 2)
            
            app2 = VGroup(
                Text("• Symbol Tables", font_size=24, color=YELLOW),
                Text("  Compiler variable lookup", font_size=18)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            app2.shift(UP * 0.0 + LEFT * 2)
            
            app3 = VGroup(
                Text("• File Systems", font_size=24, color=YELLOW),
                Text("  Directory organization", font_size=18)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            app3.shift(DOWN * 1.2 + LEFT * 2)
            
            self.play(Write(app1))
            self.wait(0.5)
            self.play(Write(app2))
            self.wait(0.5)
            self.play(Write(app3))
        
        with self.voiceover(text="File systems utilize tree structures to organize directories and files hierarchically. Network routers use BSTs for IP address lookup tables. Programming language libraries often implement sets and maps using balanced BST variants. Auto-complete features in search engines leverage tree structures to suggest completions efficiently as you type.") as tracker:
            app4 = VGroup(
                Text("• Network Routing", font_size=24, color=YELLOW),
                Text("  IP address lookup", font_size=18)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            app4.shift(UP * 1.2 + RIGHT * 2)
            
            app5 = VGroup(
                Text("• Language Libraries", font_size=24, color=YELLOW),
                Text("  Set and Map implementations", font_size=18)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            app5.shift(UP * 0.0 + RIGHT * 2)
            
            app6 = VGroup(
                Text("• Auto-complete", font_size=24, color=YELLOW),
                Text("  Search suggestions", font_size=18)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            app6.shift(DOWN * 1.2 + RIGHT * 2)
            
            self.play(Write(app4))
            self.wait(0.5)
            self.play(Write(app5))
            self.wait(0.5)
            self.play(Write(app6))
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))
    
    def advantages_and_disadvantages(self):
        with self.voiceover(text="Let's summarize the advantages of Binary Search Trees. They provide logarithmic time complexity for search, insertion, and deletion when balanced. They maintain elements in sorted order, making range queries efficient. In-order traversal of a BST visits nodes in ascending order, which is useful for many applications.") as tracker:
            title = Text("Advantages & Disadvantages", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            adv_title = Text("Advantages", font_size=28, color=GREEN)
            adv_title.shift(LEFT * 3.5 + UP * 1.5)
            self.play(Write(adv_title))
            
            advantages = VGroup(
                Text("• O(log n) operations", font_size=20),
                Text("• Sorted order maintained", font_size=20),
                Text("• Efficient range queries", font_size=20),
                Text("• Dynamic size", font_size=20)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            advantages.shift(LEFT * 3.5 + UP * 0.2)
            
            for adv in advantages:
                self.play(Write(adv))
                self.wait(0.3)
        
        with self.voiceover(text="However, BSTs also have disadvantages. The main drawback is that performance degrades to O of n in the worst case when the tree becomes unbalanced. They require extra memory for storing pointers to child nodes. Simple BSTs don't guarantee balance, which is why self-balancing variants were developed. Understanding these trade-offs helps in choosing the right data structure for specific use cases.") as tracker:
            dis_title = Text("Disadvantages", font_size=28, color=RED)
            dis_title.shift(RIGHT * 3.5 + UP * 1.5)
            self.play(Write(dis_title))
            
            disadvantages = VGroup(
                Text("• Can become unbalanced", font_size=20),
                Text("• O(n) worst case", font_size=20),
                Text("• Extra memory for pointers", font_size=20),
                Text("• No balance guarantee", font_size=20)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            disadvantages.shift(RIGHT * 3.5 + UP * 0.2)
            
            for dis in disadvantages:
                self.play(Write(dis))
                self.wait(0.3)
            
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))
    
    def conclusion(self):
        with self.voiceover(text="We've reached the end of our comprehensive exploration of Binary Search Trees. We've covered the fundamental structure, the critical BST property, and all major operations including insertion, search, and deletion. We analyzed time complexity and understood the importance of balance.") as tracker:
            title = Text("Conclusion", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            summary = VGroup(
                Text("Key Takeaways:", font_size=28, color=YELLOW),
                Text("", font_size=18),
                Text("✓ BST Property: Left < Node < Right", font_size=22),
                Text("✓ Efficient O(log n) operations when balanced", font_size=22),
                Text("✓ Three deletion cases to handle", font_size=22),
                Text("✓ Balance is crucial for performance", font_size=22),
                Text("✓ Foundation for advanced trees (AVL, Red-Black)", font_size=22)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            summary.move_to(UP * 0.3)
            
            for item in summary:
                self.play(Write(item))
                self.wait(0.4)
        
        with self.voiceover(text="Binary Search Trees are a fundamental data structure that every computer scientist should master. They serve as the foundation for more advanced balanced tree structures like AVL trees and Red-Black trees. Understanding BSTs deeply will help you tackle complex algorithmic problems and make informed decisions about data structure selection in your projects. Thank you for watching this detailed explanation!") as tracker:
            self.wait(1)
            
            # Clean up for final message
            self.play(FadeOut(*self.mobjects))
            
            thanks = Text("Thank You for Watching!", font_size=36, color=BLUE)
            thanks.move_to(ORIGIN)
            
            subscribe = Text("Master Data Structures!", font_size=24, color=YELLOW)
            subscribe.next_to(thanks, DOWN, buff=0.6)
            
            self.play(Write(thanks))
            self.play(FadeIn(subscribe))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

# To render the animation, use the following command:
# manim -pql binary_search_tree.py BinarySearchTreeExplanation
# For high quality: manim -pqh binary_search_tree.py BinarySearchTreeExplanation