from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class BinarySearchTreeExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        # Section 1: Introduction
        self.introduction()
        
        # Section 2: What is a Binary Search Tree
        self.what_is_bst()
        
        # Section 3: BST Properties
        self.bst_properties()
        
        # Section 4: Building a BST Step by Step
        self.building_bst()
        
        # Section 5: Search Operation
        self.search_operation()
        
        # Section 6: Insertion Operation
        self.insertion_operation()
        
        # Section 7: Deletion Operation
        self.deletion_operation()
        
        # Section 8: Time Complexity Analysis
        self.time_complexity()
        
        # Section 9: Traversal Methods
        self.traversal_methods()
        
        # Section 10: Real-World Applications
        self.applications()
        
        # Section 11: Advantages and Disadvantages
        self.pros_and_cons()
        
        # Section 12: Conclusion
        self.conclusion()

    def introduction(self):
        with self.voiceover(text="Welcome to this comprehensive explanation of Binary Search Trees, one of the most fundamental data structures in computer science. A Binary Search Tree, or BST, is a tree-based data structure that maintains sorted data and allows for efficient searching, insertion, and deletion operations.") as tracker:
            title = Text("Binary Search Trees", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            subtitle = Text("A Fundamental Data Structure", font_size=24, color=GRAY)
            subtitle.next_to(title, DOWN, buff=0.4)
            
            self.play(Write(title))
            self.play(FadeIn(subtitle))
            
        with self.voiceover(text="Throughout this animation, we will explore what makes Binary Search Trees special, how they work, and why they are so widely used in software engineering. We will visualize operations step by step, analyze their efficiency, and understand their real-world applications.") as tracker:
            book_icon = Text("📚", font_size=36)
            book_icon.move_to(DOWN * 0.8)
            
            topics = VGroup(
                Text("• BST Structure & Properties", font_size=22),
                Text("• Search, Insert & Delete", font_size=22),
                Text("• Time Complexity Analysis", font_size=22),
                Text("• Traversal Techniques", font_size=22),
                Text("• Real-World Applications", font_size=22)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            topics.next_to(book_icon, DOWN, buff=0.6)
            
            self.play(FadeIn(book_icon))
            self.play(Write(topics), run_time=3)
            
        self.play(FadeOut(*self.mobjects))

    def what_is_bst(self):
        with self.voiceover(text="Let's start by understanding what a Binary Search Tree is. A BST is a tree data structure where each node contains a key and has at most two children, referred to as the left child and the right child.") as tracker:
            title = Text("What is a Binary Search Tree?", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Create a simple BST
            root = Circle(radius=0.4, color=GREEN, fill_opacity=0.3)
            root_val = Text("50", font_size=24).move_to(root.get_center())
            root_group = VGroup(root, root_val)
            root_group.move_to(UP * 1.2)
            
            self.play(Create(root), Write(root_val))
            
        with self.voiceover(text="The defining characteristic of a Binary Search Tree is its ordering property. For every node in the tree, all values in its left subtree are smaller than the node's value, and all values in its right subtree are greater than the node's value. This property makes searching extremely efficient.") as tracker:
            # Add left and right children
            left_node = Circle(radius=0.4, color=YELLOW, fill_opacity=0.3)
            left_val = Text("30", font_size=24)
            left_group = VGroup(left_node, left_val)
            left_group.move_to(LEFT * 2.5 + DOWN * 0.5)
            left_val.move_to(left_node.get_center())
            
            right_node = Circle(radius=0.4, color=YELLOW, fill_opacity=0.3)
            right_val = Text("70", font_size=24)
            right_group = VGroup(right_node, right_val)
            right_group.move_to(RIGHT * 2.5 + DOWN * 0.5)
            right_val.move_to(right_node.get_center())
            
            # Create edges
            left_edge = Line(root.get_bottom(), left_node.get_top(), color=WHITE)
            right_edge = Line(root.get_bottom(), right_node.get_top(), color=WHITE)
            
            self.play(Create(left_edge), Create(right_edge))
            self.play(Create(left_node), Write(left_val))
            self.play(Create(right_node), Write(right_val))
            
            # Add labels
            less_label = Text("< 50", font_size=20, color=RED)
            less_label.next_to(left_group, DOWN, buff=0.3)
            greater_label = Text("> 50", font_size=20, color=RED)
            greater_label.next_to(right_group, DOWN, buff=0.3)
            
            self.play(Write(less_label), Write(greater_label))
            
        self.play(FadeOut(*self.mobjects))

    def bst_properties(self):
        with self.voiceover(text="Binary Search Trees have several important properties that make them powerful. First, the BST property states that for any node, all descendants in the left subtree have smaller values, and all descendants in the right subtree have larger values. This property must hold for every single node in the tree.") as tracker:
            title = Text("BST Properties", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            property_box = Rectangle(height=2.8, width=10, color=YELLOW)
            property_box.move_to(DOWN * 0.3)
            
            properties = VGroup(
                Text("1. Each node has at most 2 children", font_size=24),
                Text("2. Left subtree values < Node value", font_size=24),
                Text("3. Right subtree values > Node value", font_size=24),
                Text("4. Both subtrees are also BSTs", font_size=24)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
            properties.move_to(property_box.get_center())
            
            self.play(Create(property_box))
            self.play(Write(properties), run_time=3)
            
        with self.voiceover(text="Second, the height of a balanced BST with n nodes is logarithmic, specifically log base 2 of n. This is crucial because the height determines the time complexity of most operations. A well-balanced tree ensures optimal performance, while an unbalanced tree can degrade to linear time complexity.") as tracker:
            self.play(FadeOut(property_box), FadeOut(properties))
            
            # Show height formula
            height_formula = MathTex(r"h = \log_2(n)", font_size=36)
            height_formula.move_to(UP * 1.0)
            
            explanation = Text("where h = height, n = number of nodes", font_size=22, color=GRAY)
            explanation.next_to(height_formula, DOWN, buff=0.5)
            
            self.play(Write(height_formula))
            self.play(FadeIn(explanation))
            
            # Visual comparison
            balanced_label = Text("Balanced BST", font_size=20, color=GREEN)
            balanced_label.move_to(LEFT * 3.5 + DOWN * 0.8)
            
            unbalanced_label = Text("Unbalanced BST", font_size=20, color=RED)
            unbalanced_label.move_to(RIGHT * 3.5 + DOWN * 0.8)
            
            self.play(Write(balanced_label), Write(unbalanced_label))
            
            # Simple visual representations
            balanced_height = Text("Height ≈ log(n)", font_size=18, color=GREEN)
            balanced_height.next_to(balanced_label, DOWN, buff=0.3)
            
            unbalanced_height = Text("Height ≈ n", font_size=18, color=RED)
            unbalanced_height.next_to(unbalanced_label, DOWN, buff=0.3)
            
            self.play(Write(balanced_height), Write(unbalanced_height))
            
        self.play(FadeOut(*self.mobjects))

    def building_bst(self):
        with self.voiceover(text="Now let's build a Binary Search Tree from scratch. We'll insert the values 50, 30, 70, 20, 40, 60, and 80 in that order. Watch carefully how each value finds its correct position based on the BST property.") as tracker:
            title = Text("Building a BST: Step by Step", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            insertion_text = Text("Inserting: 50, 30, 70, 20, 40, 60, 80", font_size=24, color=YELLOW)
            insertion_text.next_to(title, DOWN, buff=0.4)
            self.play(Write(insertion_text))
            
        with self.voiceover(text="First, we insert 50 as the root node. Since the tree is empty, 50 becomes the foundation of our tree. Next, we insert 30. Since 30 is less than 50, it becomes the left child of the root.") as tracker:
            # Root node
            root = Circle(radius=0.35, color=GREEN, fill_opacity=0.3)
            root_val = Text("50", font_size=22).move_to(root.get_center())
            root_group = VGroup(root, root_val)
            root_group.move_to(UP * 1.5)
            
            self.play(Create(root), Write(root_val))
            self.wait(0.5)
            
            # Insert 30
            node_30 = Circle(radius=0.35, color=YELLOW, fill_opacity=0.3)
            val_30 = Text("30", font_size=22)
            group_30 = VGroup(node_30, val_30)
            group_30.move_to(LEFT * 2.2 + UP * 0.2)
            val_30.move_to(node_30.get_center())
            
            edge_30 = Line(root.get_bottom(), node_30.get_top(), color=WHITE)
            
            self.play(Create(edge_30))
            self.play(Create(node_30), Write(val_30))
            
        with self.voiceover(text="Now we insert 70. Since 70 is greater than 50, it goes to the right of the root. Then comes 20, which is less than 50 and less than 30, so it becomes the left child of 30. We continue this process for 40, which goes between 30 and 50 as the right child of 30.") as tracker:
            # Insert 70
            node_70 = Circle(radius=0.35, color=YELLOW, fill_opacity=0.3)
            val_70 = Text("70", font_size=22)
            group_70 = VGroup(node_70, val_70)
            group_70.move_to(RIGHT * 2.2 + UP * 0.2)
            val_70.move_to(node_70.get_center())
            
            edge_70 = Line(root.get_bottom(), node_70.get_top(), color=WHITE)
            
            self.play(Create(edge_70))
            self.play(Create(node_70), Write(val_70))
            self.wait(0.3)
            
            # Insert 20
            node_20 = Circle(radius=0.35, color=ORANGE, fill_opacity=0.3)
            val_20 = Text("20", font_size=22)
            group_20 = VGroup(node_20, val_20)
            group_20.move_to(LEFT * 3.3 + DOWN * 1.1)
            val_20.move_to(node_20.get_center())
            
            edge_20 = Line(node_30.get_bottom(), node_20.get_top(), color=WHITE)
            
            self.play(Create(edge_20))
            self.play(Create(node_20), Write(val_20))
            self.wait(0.3)
            
            # Insert 40
            node_40 = Circle(radius=0.35, color=ORANGE, fill_opacity=0.3)
            val_40 = Text("40", font_size=22)
            group_40 = VGroup(node_40, val_40)
            group_40.move_to(LEFT * 1.1 + DOWN * 1.1)
            val_40.move_to(node_40.get_center())
            
            edge_40 = Line(node_30.get_bottom(), node_40.get_top(), color=WHITE)
            
            self.play(Create(edge_40))
            self.play(Create(node_40), Write(val_40))
            
        with self.voiceover(text="Finally, we insert 60 and 80. Sixty is greater than 50 but less than 70, so it becomes the left child of 70. Eighty is greater than both 50 and 70, making it the right child of 70. Our Binary Search Tree is now complete with all seven nodes properly positioned.") as tracker:
            # Insert 60
            node_60 = Circle(radius=0.35, color=ORANGE, fill_opacity=0.3)
            val_60 = Text("60", font_size=22)
            group_60 = VGroup(node_60, val_60)
            group_60.move_to(RIGHT * 1.1 + DOWN * 1.1)
            val_60.move_to(node_60.get_center())
            
            edge_60 = Line(node_70.get_bottom(), node_60.get_top(), color=WHITE)
            
            self.play(Create(edge_60))
            self.play(Create(node_60), Write(val_60))
            self.wait(0.3)
            
            # Insert 80
            node_80 = Circle(radius=0.35, color=ORANGE, fill_opacity=0.3)
            val_80 = Text("80", font_size=22)
            group_80 = VGroup(node_80, val_80)
            group_80.move_to(RIGHT * 3.3 + DOWN * 1.1)
            val_80.move_to(node_80.get_center())
            
            edge_80 = Line(node_70.get_bottom(), node_80.get_top(), color=WHITE)
            
            self.play(Create(edge_80))
            self.play(Create(node_80), Write(val_80))
            
        self.play(FadeOut(*self.mobjects))

    def search_operation(self):
        with self.voiceover(text="The search operation in a Binary Search Tree is remarkably efficient. Let's search for the value 40 in our tree. We start at the root and compare our target value with each node, moving left or right based on the comparison.") as tracker:
            title = Text("Search Operation in BST", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            search_text = Text("Searching for: 40", font_size=26, color=YELLOW)
            search_text.next_to(title, DOWN, buff=0.4)
            self.play(Write(search_text))
            
            # Recreate the tree
            root = Circle(radius=0.35, color=WHITE, fill_opacity=0.1)
            root_val = Text("50", font_size=22).move_to(root.get_center())
            root_group = VGroup(root, root_val)
            root_group.move_to(UP * 1.2)
            
            node_30 = Circle(radius=0.35, color=WHITE, fill_opacity=0.1)
            val_30 = Text("30", font_size=22).move_to(node_30.get_center())
            node_30.move_to(LEFT * 2.2 + UP * 0.0)
            
            node_70 = Circle(radius=0.35, color=WHITE, fill_opacity=0.1)
            val_70 = Text("70", font_size=22).move_to(node_70.get_center())
            node_70.move_to(RIGHT * 2.2 + UP * 0.0)
            
            node_20 = Circle(radius=0.35, color=WHITE, fill_opacity=0.1)
            val_20 = Text("20", font_size=22).move_to(node_20.get_center())
            node_20.move_to(LEFT * 3.3 + DOWN * 1.3)
            
            node_40 = Circle(radius=0.35, color=WHITE, fill_opacity=0.1)
            val_40 = Text("40", font_size=22).move_to(node_40.get_center())
            node_40.move_to(LEFT * 1.1 + DOWN * 1.3)
            
            edge1 = Line(root.get_bottom(), node_30.get_top(), color=WHITE)
            edge2 = Line(root.get_bottom(), node_70.get_top(), color=WHITE)
            edge3 = Line(node_30.get_bottom(), node_20.get_top(), color=WHITE)
            edge4 = Line(node_30.get_bottom(), node_40.get_top(), color=WHITE)
            
            tree = VGroup(edge1, edge2, edge3, edge4, root, root_val, node_30, val_30, 
                         node_70, val_70, node_20, val_20, node_40, val_40)
            
            self.play(Create(tree), run_time=2)
            
        with self.voiceover(text="Step one: We compare 40 with the root value 50. Since 40 is less than 50, we move to the left child. Step two: Now we compare 40 with 30. Since 40 is greater than 30, we move to the right child. Step three: We've found our target! The value 40 matches the current node. The search is successful and complete.") as tracker:
            # Highlight search path
            highlight1 = root.copy().set_color(YELLOW).set_fill(opacity=0.5)
            self.play(Create(highlight1))
            step1 = Text("40 < 50, go LEFT", font_size=20, color=YELLOW)
            step1.move_to(RIGHT * 3.8 + UP * 1.2)
            self.play(Write(step1))
            self.wait(0.8)
            
            highlight2 = node_30.copy().set_color(YELLOW).set_fill(opacity=0.5)
            self.play(ReplacementTransform(highlight1, highlight2))
            step2 = Text("40 > 30, go RIGHT", font_size=20, color=YELLOW)
            step2.move_to(RIGHT * 3.8 + UP * 0.4)
            self.play(Write(step2))
            self.wait(0.8)
            
            highlight3 = node_40.copy().set_color(GREEN).set_fill(opacity=0.5)
            self.play(ReplacementTransform(highlight2, highlight3))
            step3 = Text("Found 40! ✓", font_size=20, color=GREEN)
            step3.move_to(RIGHT * 3.8 + DOWN * 0.4)
            self.play(Write(step3))
            self.wait(0.5)
            
        self.play(FadeOut(*self.mobjects))

    def insertion_operation(self):
        with self.voiceover(text="Insertion in a Binary Search Tree follows a similar path to search. Let's insert the value 35 into our tree. We'll traverse the tree comparing values until we find the appropriate empty spot where 35 should be placed.") as tracker:
            title = Text("Insertion Operation", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            insert_text = Text("Inserting: 35", font_size=26, color=GREEN)
            insert_text.next_to(title, DOWN, buff=0.4)
            self.play(Write(insert_text))
            
            # Recreate simplified tree
            root = Circle(radius=0.35, color=WHITE, fill_opacity=0.1)
            root_val = Text("50", font_size=22).move_to(root.get_center())
            root.move_to(UP * 1.2)
            root_val.move_to(root.get_center())
            
            node_30 = Circle(radius=0.35, color=WHITE, fill_opacity=0.1)
            val_30 = Text("30", font_size=22)
            node_30.move_to(LEFT * 2.2 + UP * 0.0)
            val_30.move_to(node_30.get_center())
            
            node_40 = Circle(radius=0.35, color=WHITE, fill_opacity=0.1)
            val_40 = Text("40", font_size=22)
            node_40.move_to(LEFT * 1.1 + DOWN * 1.3)
            val_40.move_to(node_40.get_center())
            
            edge1 = Line(root.get_bottom(), node_30.get_top(), color=WHITE)
            edge2 = Line(node_30.get_bottom(), node_40.get_top(), color=WHITE)
            
            tree = VGroup(edge1, edge2, root, root_val, node_30, val_30, node_40, val_40)
            self.play(Create(tree), run_time=1.5)
            
        with self.voiceover(text="We start at the root, comparing 35 with 50. Since 35 is less than 50, we go left to node 30. Next, we compare 35 with 30. Since 35 is greater than 30, we attempt to go right. We find that node 40 exists there, so we compare 35 with 40. Since 35 is less than 40, we try to go left from 40, and we find an empty spot. This is where 35 belongs! We create a new node with value 35 and attach it as the left child of 40.") as tracker:
            # Show insertion path
            path1 = root.copy().set_color(YELLOW).set_fill(opacity=0.4)
            self.play(Create(path1))
            self.wait(0.5)
            
            path2 = node_30.copy().set_color(YELLOW).set_fill(opacity=0.4)
            self.play(ReplacementTransform(path1, path2))
            self.wait(0.5)
            
            path3 = node_40.copy().set_color(YELLOW).set_fill(opacity=0.4)
            self.play(ReplacementTransform(path2, path3))
            self.wait(0.5)
            
            # Insert new node
            node_35 = Circle(radius=0.35, color=GREEN, fill_opacity=0.5)
            val_35 = Text("35", font_size=22)
            node_35.move_to(LEFT * 2.2 + DOWN * 2.4)
            val_35.move_to(node_35.get_center())
            
            edge_35 = Line(node_40.get_bottom(), node_35.get_top(), color=GREEN, stroke_width=4)
            
            self.play(Create(edge_35), Create(node_35), Write(val_35))
            self.play(FadeOut(path3))
            
            success = Text("Insertion Complete!", font_size=24, color=GREEN)
            success.move_to(RIGHT * 3.5 + DOWN * 0.5)
            self.play(Write(success))
            
        self.play(FadeOut(*self.mobjects))

    def deletion_operation(self):
        with self.voiceover(text="Deletion is the most complex operation in a Binary Search Tree because we must maintain the BST property after removing a node. There are three cases to consider: deleting a leaf node, deleting a node with one child, and deleting a node with two children.") as tracker:
            title = Text("Deletion Operation", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            cases = VGroup(
                Text("Case 1: Leaf Node (no children)", font_size=24, color=GREEN),
                Text("Case 2: One Child", font_size=24, color=YELLOW),
                Text("Case 3: Two Children", font_size=24, color=RED)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            cases.move_to(DOWN * 0.3)
            
            self.play(Write(cases), run_time=2)
            
        with self.voiceover(text="Case one is the simplest: deleting a leaf node. If a node has no children, we simply remove it from the tree. For example, if we delete node 20, we just remove it and update its parent's pointer to null. The tree structure remains valid.") as tracker:
            self.play(FadeOut(cases))
            
            case1_title = Text("Case 1: Delete Leaf Node (20)", font_size=26, color=GREEN)
            case1_title.next_to(title, DOWN, buff=0.4)
            self.play(Write(case1_title))
            
            # Small tree for demonstration
            root = Circle(radius=0.35, color=WHITE, fill_opacity=0.1)
            root_val = Text("30", font_size=22).move_to(root.get_center())
            root.move_to(UP * 0.8)
            root_val.move_to(root.get_center())
            
            node_20 = Circle(radius=0.35, color=RED, fill_opacity=0.3)
            val_20 = Text("20", font_size=22)
            node_20.move_to(LEFT * 1.8 + DOWN * 0.8)
            val_20.move_to(node_20.get_center())
            
            node_40 = Circle(radius=0.35, color=WHITE, fill_opacity=0.1)
            val_40 = Text("40", font_size=22)
            node_40.move_to(RIGHT * 1.8 + DOWN * 0.8)
            val_40.move_to(node_40.get_center())
            
            edge1 = Line(root.get_bottom(), node_20.get_top(), color=WHITE)
            edge2 = Line(root.get_bottom(), node_40.get_top(), color=WHITE)
            
            self.play(Create(VGroup(edge1, edge2, root, root_val, node_20, val_20, node_40, val_40)))
            
            cross = Cross(node_20, stroke_color=RED, stroke_width=6)
            self.play(Create(cross))
            self.play(FadeOut(node_20), FadeOut(val_20), FadeOut(cross), FadeOut(edge1))
            
            self.wait(0.5)
            self.play(FadeOut(VGroup(root, root_val, node_40, val_40, edge2, case1_title)))
            
        with self.voiceover(text="Case two involves a node with one child. When we delete such a node, we replace it with its only child. The child takes the position of the deleted node, and all the subtree relationships are preserved. This maintains the BST property throughout the tree.") as tracker:
            case2_title = Text("Case 2: Delete Node with One Child", font_size=26, color=YELLOW)
            case2_title.next_to(title, DOWN, buff=0.4)
            self.play(Write(case2_title))
            
            # Demonstrate case 2
            explanation = Text("Node is replaced by its child", font_size=22, color=YELLOW)
            explanation.move_to(DOWN * 1.8)
            self.play(Write(explanation))
            self.wait(1)
            
            self.play(FadeOut(case2_title), FadeOut(explanation))
            
        with self.voiceover(text="Case three is the most interesting: deleting a node with two children. We cannot simply remove it because we need to maintain both subtrees. The solution is to find the in-order successor, which is the smallest node in the right subtree, or the in-order predecessor, which is the largest node in the left subtree. We replace the deleted node's value with the successor's value, then delete the successor node which will be either a leaf or have one child.") as tracker:
            case3_title = Text("Case 3: Delete Node with Two Children", font_size=26, color=RED)
            case3_title.next_to(title, DOWN, buff=0.4)
            self.play(Write(case3_title))
            
            strategy = VGroup(
                Text("Strategy:", font_size=24, color=YELLOW),
                Text("1. Find in-order successor (smallest in right subtree)", font_size=20),
                Text("2. Replace node value with successor value", font_size=20),
                Text("3. Delete the successor node", font_size=20)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
            strategy.move_to(DOWN * 0.5)
            
            self.play(Write(strategy), run_time=3)
            
        self.play(FadeOut(*self.mobjects))

    def time_complexity(self):
        with self.voiceover(text="Let's analyze the time complexity of Binary Search Tree operations. For a balanced BST, the height is logarithmic in the number of nodes. This means search, insertion, and deletion all take O(log n) time in the best and average cases.") as tracker:
            title = Text("Time Complexity Analysis", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            complexity_table = VGroup(
                Text("Operation", font_size=24, color=YELLOW),
                Text("Search", font_size=22),
                Text("Insert", font_size=22),
                Text("Delete", font_size=22)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            complexity_table.move_to(LEFT * 3.5 + DOWN * 0.3)
            
            best_case = VGroup(
                Text("Best/Avg", font_size=24, color=GREEN),
                MathTex(r"O(\log n)", font_size=28),
                MathTex(r"O(\log n)", font_size=28),
                MathTex(r"O(\log n)", font_size=28)
            ).arrange(DOWN, buff=0.4)
            best_case.move_to(RIGHT * 0.0 + DOWN * 0.3)
            
            worst_case = VGroup(
                Text("Worst", font_size=24, color=RED),
                MathTex(r"O(n)", font_size=28),
                MathTex(r"O(n)", font_size=28),
                MathTex(r"O(n)", font_size=28)
            ).arrange(DOWN, buff=0.4)
            worst_case.move_to(RIGHT * 3.5 + DOWN * 0.3)
            
            self.play(Write(complexity_table))
            self.play(Write(best_case))
            self.play(Write(worst_case))
            
        with self.voiceover(text="However, in the worst case, when the tree becomes skewed or unbalanced like a linked list, the height becomes n, and all operations degrade to O(n) time. This happens when we insert already sorted data. For example, inserting 1, 2, 3, 4, 5 in order creates a completely right-skewed tree where each node has only a right child, essentially becoming a linked list.") as tracker:
            self.play(FadeOut(complexity_table), FadeOut(best_case), FadeOut(worst_case))
            
            balanced_text = Text("Balanced BST", font_size=22, color=GREEN)
            balanced_text.move_to(LEFT * 3.5 + UP * 1.2)
            
            skewed_text = Text("Skewed BST (Worst Case)", font_size=22, color=RED)
            skewed_text.move_to(RIGHT * 3.5 + UP * 1.2)
            
            self.play(Write(balanced_text), Write(skewed_text))
            
            # Visual of balanced vs skewed
            bal_height = Text("Height: log(n)", font_size=20, color=GREEN)
            bal_height.move_to(LEFT * 3.5 + DOWN * 1.8)
            
            skew_height = Text("Height: n", font_size=20, color=RED)
            skew_height.move_to(RIGHT * 3.5 + DOWN * 1.8)
            
            self.play(Write(bal_height), Write(skew_height))
            
        self.play(FadeOut(*self.mobjects))

    def traversal_methods(self):
        with self.voiceover(text="Binary Search Trees support three main traversal methods: in-order, pre-order, and post-order. Each traversal visits all nodes but in a different sequence. In-order traversal is particularly special for BSTs because it visits nodes in sorted ascending order.") as tracker:
            title = Text("Tree Traversal Methods", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            methods = VGroup(
                Text("1. In-Order: Left → Root → Right", font_size=24, color=GREEN),
                Text("2. Pre-Order: Root → Left → Right", font_size=24, color=YELLOW),
                Text("3. Post-Order: Left → Right → Root", font_size=24, color=ORANGE)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.45)
            methods.move_to(DOWN * 0.5)
            
            self.play(Write(methods), run_time=2.5)
            
        with self.voiceover(text="Let's visualize in-order traversal on our sample tree. Starting from the root, we recursively visit the left subtree first, then process the current node, and finally visit the right subtree. For our BST with root 50, the in-order traversal would visit nodes in this sequence: 20, 30, 40, 50, 60, 70, 80. Notice how this produces a perfectly sorted list!") as tracker:
            self.play(FadeOut(methods))
            
            inorder_title = Text("In-Order Traversal Example", font_size=26, color=GREEN)
            inorder_title.next_to(title, DOWN, buff=0.4)
            self.play(Write(inorder_title))
            
            # Create small tree
            positions = {
                50: UP * 1.0,
                30: LEFT * 1.8 + UP * 0.0,
                70: RIGHT * 1.8 + UP * 0.0,
                20: LEFT * 2.8 + DOWN * 1.0,
                40: LEFT * 0.8 + DOWN * 1.0,
                60: RIGHT * 0.8 + DOWN * 1.0,
                80: RIGHT * 2.8 + DOWN * 1.0
            }
            
            nodes = {}
            for val, pos in positions.items():
                circle = Circle(radius=0.3, color=WHITE, fill_opacity=0.1)
                circle.move_to(pos)
                text = Text(str(val), font_size=20).move_to(pos)
                nodes[val] = VGroup(circle, text)
            
            # Create edges
            edges = [
                Line(positions[50], positions[30], color=WHITE),
                Line(positions[50], positions[70], color=WHITE),
                Line(positions[30], positions[20], color=WHITE),
                Line(positions[30], positions[40], color=WHITE),
                Line(positions[70], positions[60], color=WHITE),
                Line(positions[70], positions[80], color=WHITE)
            ]
            
            self.play(Create(VGroup(*edges)), *[Create(n) for n in nodes.values()], run_time=2)
            
            # Show traversal order
            order_text = Text("Order: ", font_size=22, color=YELLOW)
            order_text.move_to(LEFT * 5.5 + DOWN * 2.2)
            self.play(Write(order_text))
            
            traversal_order = [20, 30, 40, 50, 60, 70, 80]
            order_display = Text("", font_size=22, color=GREEN)
            order_display.next_to(order_text, RIGHT, buff=0.2)
            
            current_order = ""
            for val in traversal_order:
                highlight = nodes[val][0].copy().set_color(GREEN).set_fill(opacity=0.6)
                self.play(Create(highlight), run_time=0.3)
                current_order += str(val) + ", "
                order_display.become(Text(current_order[:-2], font_size=22, color=GREEN).next_to(order_text, RIGHT, buff=0.2))
                self.play(Write(order_display), run_time=0.3)
                self.play(FadeOut(highlight), run_time=0.2)
            
        self.play(FadeOut(*self.mobjects))

    def applications(self):
        with self.voiceover(text="Binary Search Trees have numerous real-world applications in computer science and software engineering. They are used in databases for indexing, in compilers for symbol tables, in network routing algorithms, and in many other scenarios where we need to maintain sorted data with efficient search capabilities.") as tracker:
            title = Text("Real-World Applications", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            apps = VGroup(
                Text("🗄️  Database Indexing", font_size=26),
                Text("🔍  Auto-complete Systems", font_size=26),
                Text("📊  Priority Queues", font_size=26),
                Text("🌐  Router Tables", font_size=26),
                Text("💾  File Systems", font_size=26),
                Text("🎮  Game AI Decision Trees", font_size=26)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            apps.move_to(DOWN * 0.2)
            
            self.play(Write(apps), run_time=4)
            
        with self.voiceover(text="One common application is implementing a dictionary or map data structure. When you use a tree-based map in programming languages like C++ or Java, it's often implemented using a balanced variant of BST called a Red-Black tree. This provides guaranteed logarithmic time operations while maintaining the simplicity of the BST concept.") as tracker:
            self.play(FadeOut(apps))
            
            use_case = Text("Example: Dictionary/Map Implementation", font_size=28, color=YELLOW)
            use_case.move_to(UP * 1.2)
            self.play(Write(use_case))
            
            code_example = VGroup(
                Text("map.insert('apple', 5)", font_size=22, color=GREEN),
                Text("map.insert('banana', 3)", font_size=22, color=GREEN),
                Text("map.search('apple')  → 5", font_size=22, color=BLUE),
                Text("map.delete('banana')", font_size=22, color=RED)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
            code_example.move_to(DOWN * 0.5)
            
            self.play(Write(code_example), run_time=3)
            
            benefit = Text("All operations in O(log n) time!", font_size=24, color=YELLOW)
            benefit.move_to(DOWN * 2.3)
            self.play(Write(benefit))
            
        self.play(FadeOut(*self.mobjects))

    def pros_and_cons(self):
        with self.voiceover(text="Let's summarize the advantages and disadvantages of Binary Search Trees. The main advantages are efficient search, insertion, and deletion operations in O(log n) time for balanced trees, dynamic size that grows and shrinks as needed, and the ability to traverse data in sorted order easily.") as tracker:
            title = Text("Advantages & Disadvantages", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            pros_title = Text("Advantages ✓", font_size=28, color=GREEN)
            pros_title.move_to(LEFT * 3.5 + UP * 1.4)
            
            cons_title = Text("Disadvantages ✗", font_size=28, color=RED)
            cons_title.move_to(RIGHT * 3.5 + UP * 1.4)
            
            self.play(Write(pros_title), Write(cons_title))
            
            pros = VGroup(
                Text("• Fast search/insert/delete", font_size=20),
                Text("  (O(log n) average)", font_size=18, color=GRAY),
                Text("• Dynamic size", font_size=20),
                Text("• In-order gives sorted", font_size=20),
                Text("• Simple concept", font_size=20)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
            pros.move_to(LEFT * 3.5 + DOWN * 0.3)
            
            cons = VGroup(
                Text("• Can become unbalanced", font_size=20),
                Text("  (O(n) worst case)", font_size=18, color=GRAY),
                Text("• No random access", font_size=20),
                Text("• Extra memory for", font_size=20),
                Text("  pointers", font_size=20)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
            cons.move_to(RIGHT * 3.5 + DOWN * 0.3)
            
            self.play(Write(pros), run_time=2)
            self.play(Write(cons), run_time=2)
            
        with self.voiceover(text="The main disadvantage is that basic BSTs can become unbalanced, leading to degraded performance. This is why balanced variants like AVL trees and Red-Black trees were developed. These self-balancing trees automatically maintain balance during insertions and deletions, guaranteeing O(log n) performance even in the worst case.") as tracker:
            solution = Text("Solution: Self-Balancing BSTs", font_size=24, color=YELLOW)
            solution.move_to(DOWN * 2.2)
            
            examples = Text("(AVL Trees, Red-Black Trees, B-Trees)", font_size=20, color=GRAY)
            examples.next_to(solution, DOWN, buff=0.3)
            
            self.play(Write(solution))
            self.play(Write(examples))
            
        self.play(FadeOut(*self.mobjects))

    def conclusion(self):
        with self.voiceover(text="We've reached the end of our comprehensive exploration of Binary Search Trees. We've learned that BSTs are fundamental data structures that maintain sorted data and provide efficient operations. We've seen how to build them, search through them, insert new values, and delete existing ones.") as tracker:
            title = Text("Conclusion", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            summary_box = Rectangle(height=3.2, width=11, color=YELLOW, stroke_width=3)
            summary_box.move_to(DOWN * 0.2)
            
            summary = VGroup(
                Text("Key Takeaways:", font_size=28, color=YELLOW),
                Text("• BST maintains sorted data with efficient operations", font_size=22),
                Text("• Average time complexity: O(log n)", font_size=22),
                Text("• Three cases for deletion: leaf, one child, two children", font_size=22),
                Text("• In-order traversal produces sorted sequence", font_size=22),
                Text("• Balance is crucial for optimal performance", font_size=22)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.32)
            summary.move_to(summary_box.get_center())
            
            self.play(Create(summary_box))
            self.play(Write(summary), run_time=4)
            
        with self.voiceover(text="Understanding Binary Search Trees is essential for any computer science student or software engineer. They form the foundation for more advanced data structures and algorithms. Whether you're building a database, implementing a compiler, or solving complex algorithmic problems, the concepts you've learned today will serve you well. Thank you for watching this detailed exploration of Binary Search Trees!") as tracker:
            self.play(FadeOut(summary_box), FadeOut(summary))
            
            thank_you = Text("Thank You for Watching!", font_size=36, color=GREEN)
            thank_you.move_to(UP * 0.5)
            
            final_note = Text("Keep practicing and building trees!", font_size=26, color=YELLOW)
            final_note.next_to(thank_you, DOWN, buff=0.6)
            
            emoji = Text("🌳", font_size=36)
            emoji.next_to(final_note, DOWN, buff=0.5)
            
            self.play(Write(thank_you))
            self.play(FadeIn(final_note))
            self.play(FadeIn(emoji, scale=1.5))
            self.wait(2)
            
        self.play(FadeOut(*self.mobjects))

# To render this animation, run:
# manim -pql binary_search_tree.py BinarySearchTreeExplanation
# For high quality: manim -pqh binary_search_tree.py BinarySearchTreeExplanation