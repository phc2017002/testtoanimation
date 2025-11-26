from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class BinarySearchTreeOperations(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))
        
        # Introduction
        self.show_introduction()
        
        # What is a BST
        self.explain_bst_definition()
        
        # BST Properties
        self.explain_bst_properties()
        
        # Search Operation
        self.demonstrate_search_operation()
        
        # Insertion Operation
        self.demonstrate_insertion_operation()
        
        # Deletion Operation - Simple Cases
        self.demonstrate_deletion_simple()
        
        # Deletion Operation - Complex Case
        self.demonstrate_deletion_complex()
        
        # Traversal Methods
        self.demonstrate_traversals()
        
        # Time Complexity Analysis
        self.analyze_time_complexity()
        
        # Real World Applications
        self.show_applications()
        
        # Balanced vs Unbalanced
        self.explain_balance()
        
        # Conclusion
        self.show_conclusion()
    
    def show_introduction(self):
        with self.voiceover(text="Welcome to this comprehensive explanation of Binary Search Tree Operations. A Binary Search Tree, or BST, is one of the most fundamental data structures in computer science.") as tracker:
            title = Text("Binary Search Tree", font_size=36, color=BLUE)
            title.move_to(UP * 2.5)
            subtitle = Text("Operations and Visualization", font_size=32, color=WHITE)
            subtitle.next_to(title, DOWN, buff=0.5)
            
            self.play(Write(title))
            self.play(FadeIn(subtitle))
        
        with self.voiceover(text="In this video, we will explore how Binary Search Trees work, understand their fundamental operations including search, insertion, and deletion, and analyze their time complexity. We will also see how these structures are used in real-world applications.") as tracker:
            features = VGroup(
                Text("• Search Operation", font_size=24),
                Text("• Insert Operation", font_size=24),
                Text("• Delete Operation", font_size=24),
                Text("• Traversal Methods", font_size=24),
                Text("• Time Complexity", font_size=24)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            features.move_to(ORIGIN)
            
            self.play(FadeIn(features, shift=UP))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
    
    def explain_bst_definition(self):
        with self.voiceover(text="Let's start by understanding what a Binary Search Tree is. A Binary Search Tree is a tree data structure where each node has at most two children, referred to as the left child and the right child.") as tracker:
            title = Text("What is a BST?", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Create a simple BST
            root = self.create_node("50", ORIGIN)
            left = self.create_node("30", LEFT * 2.5 + DOWN * 1.5)
            right = self.create_node("70", RIGHT * 2.5 + DOWN * 1.5)
            
            line_left = Line(root.get_bottom(), left.get_top(), color=WHITE)
            line_right = Line(root.get_bottom(), right.get_top(), color=WHITE)
            
            self.play(Create(root))
            self.play(Create(line_left), Create(left))
            self.play(Create(line_right), Create(right))
        
        with self.voiceover(text="The key property that makes it a search tree is the ordering constraint. For every node in the tree, all values in its left subtree must be smaller than the node's value, and all values in its right subtree must be greater than the node's value.") as tracker:
            # Add more nodes to show the structure
            left_left = self.create_node("20", LEFT * 4 + DOWN * 3)
            left_right = self.create_node("40", LEFT * 1 + DOWN * 3)
            right_left = self.create_node("60", RIGHT * 1 + DOWN * 3)
            right_right = self.create_node("80", RIGHT * 4 + DOWN * 3)
            
            ll_line = Line(left.get_bottom(), left_left.get_top(), color=WHITE)
            lr_line = Line(left.get_bottom(), left_right.get_top(), color=WHITE)
            rl_line = Line(right.get_bottom(), right_left.get_top(), color=WHITE)
            rr_line = Line(right.get_bottom(), right_right.get_top(), color=WHITE)
            
            self.play(
                Create(ll_line), Create(left_left),
                Create(lr_line), Create(left_right)
            )
            self.play(
                Create(rl_line), Create(right_left),
                Create(rr_line), Create(right_right)
            )
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
    
    def explain_bst_properties(self):
        with self.voiceover(text="The Binary Search Tree property is what makes this data structure so powerful and efficient. Let's examine this property more closely with a specific example.") as tracker:
            title = Text("BST Property", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            property_text = VGroup(
                Text("For any node N:", font_size=28, color=YELLOW),
                Text("Left subtree values < N", font_size=24),
                Text("Right subtree values > N", font_size=24)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            property_text.move_to(UP * 1)
            
            self.play(FadeIn(property_text, shift=RIGHT))
        
        with self.voiceover(text="Let's visualize this with a concrete example. Consider a node with value fifty. All nodes in its left subtree, including twenty, thirty, and forty, are less than fifty. All nodes in its right subtree, including sixty, seventy, and eighty, are greater than fifty.") as tracker:
            # Create example tree
            root = self.create_node("50", DOWN * 0.5)
            left = self.create_node("30", LEFT * 2 + DOWN * 2)
            right = self.create_node("70", RIGHT * 2 + DOWN * 2)
            ll = self.create_node("20", LEFT * 3.2 + DOWN * 3.5)
            lr = self.create_node("40", LEFT * 0.8 + DOWN * 3.5)
            rl = self.create_node("60", RIGHT * 0.8 + DOWN * 3.5)
            rr = self.create_node("80", RIGHT * 3.2 + DOWN * 3.5)
            
            lines = VGroup(
                Line(root.get_bottom(), left.get_top(), color=WHITE),
                Line(root.get_bottom(), right.get_top(), color=WHITE),
                Line(left.get_bottom(), ll.get_top(), color=WHITE),
                Line(left.get_bottom(), lr.get_top(), color=WHITE),
                Line(right.get_bottom(), rl.get_top(), color=WHITE),
                Line(right.get_bottom(), rr.get_top(), color=WHITE)
            )
            
            tree = VGroup(root, left, right, ll, lr, rl, rr, lines)
            
            self.play(Create(tree))
            
            # Highlight left subtree
            left_highlight = SurroundingRectangle(VGroup(left, ll, lr), color=GREEN, buff=0.2)
            self.play(Create(left_highlight))
            self.wait(1)
            self.play(FadeOut(left_highlight))
            
            # Highlight right subtree
            right_highlight = SurroundingRectangle(VGroup(right, rl, rr), color=RED, buff=0.2)
            self.play(Create(right_highlight))
            self.wait(1)
            self.play(FadeOut(right_highlight))
        
        self.play(FadeOut(*self.mobjects))
    
    def demonstrate_search_operation(self):
        with self.voiceover(text="Now let's understand the search operation in a Binary Search Tree. The search operation takes advantage of the BST property to efficiently find a value. We start at the root and compare the target value with the current node.") as tracker:
            title = Text("Search Operation", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Create the tree
            root = self.create_node("50", LEFT * 3 + UP * 0.5)
            left = self.create_node("30", LEFT * 4.5 + DOWN * 1.2)
            right = self.create_node("70", LEFT * 1.5 + DOWN * 1.2)
            ll = self.create_node("20", LEFT * 5.5 + DOWN * 2.9)
            lr = self.create_node("40", LEFT * 3.5 + DOWN * 2.9)
            rl = self.create_node("60", LEFT * 2.5 + DOWN * 2.9)
            rr = self.create_node("80", LEFT * 0.5 + DOWN * 2.9)
            
            lines = VGroup(
                Line(root.get_bottom(), left.get_top(), color=WHITE),
                Line(root.get_bottom(), right.get_top(), color=WHITE),
                Line(left.get_bottom(), ll.get_top(), color=WHITE),
                Line(left.get_bottom(), lr.get_top(), color=WHITE),
                Line(right.get_bottom(), rl.get_top(), color=WHITE),
                Line(right.get_bottom(), rr.get_top(), color=WHITE)
            )
            
            tree = VGroup(root, left, right, ll, lr, rl, rr, lines)
            self.play(Create(tree))
            
            # Algorithm steps on the right
            algo = VGroup(
                Text("Search for: 60", font_size=26, color=YELLOW),
                Text("1. Start at root", font_size=22),
                Text("2. Compare with target", font_size=22),
                Text("3. Go left if smaller", font_size=22),
                Text("4. Go right if larger", font_size=22),
                Text("5. Repeat until found", font_size=22)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            algo.move_to(RIGHT * 3.5 + UP * 0.5)
            self.play(FadeIn(algo, shift=LEFT))
        
        with self.voiceover(text="Let's search for the value sixty. We start at the root which has value fifty. Since sixty is greater than fifty, we move to the right child. The right child has value seventy. Since sixty is less than seventy, we move to the left child of seventy. We found sixty! The search is complete.") as tracker:
            # Highlight search path
            highlight1 = root[0].copy().set_fill(YELLOW, opacity=0.5)
            self.play(FadeIn(highlight1))
            self.wait(1)
            
            arrow1 = Arrow(root.get_right(), right.get_left(), color=YELLOW, buff=0.1)
            self.play(Create(arrow1))
            self.play(FadeOut(highlight1))
            
            highlight2 = right[0].copy().set_fill(YELLOW, opacity=0.5)
            self.play(FadeIn(highlight2))
            self.wait(1)
            
            arrow2 = Arrow(right.get_bottom(), rl.get_top(), color=YELLOW, buff=0.1)
            self.play(Create(arrow2))
            self.play(FadeOut(highlight2))
            
            highlight3 = rl[0].copy().set_fill(GREEN, opacity=0.7)
            self.play(FadeIn(highlight3))
            
            found_text = Text("Found!", font_size=28, color=GREEN)
            found_text.next_to(rl, RIGHT, buff=0.5)
            self.play(Write(found_text))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
    
    def demonstrate_insertion_operation(self):
        with self.voiceover(text="The insertion operation in a Binary Search Tree follows a similar logic to search. We start at the root and traverse the tree following the BST property until we find an empty spot where the new value should be placed.") as tracker:
            title = Text("Insert Operation", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Initial tree
            root = self.create_node("50", LEFT * 3 + UP * 0.5)
            left = self.create_node("30", LEFT * 4.5 + DOWN * 1.2)
            right = self.create_node("70", LEFT * 1.5 + DOWN * 1.2)
            ll = self.create_node("20", LEFT * 5.5 + DOWN * 2.9)
            lr = self.create_node("40", LEFT * 3.5 + DOWN * 2.9)
            
            lines = VGroup(
                Line(root.get_bottom(), left.get_top(), color=WHITE),
                Line(root.get_bottom(), right.get_top(), color=WHITE),
                Line(left.get_bottom(), ll.get_top(), color=WHITE),
                Line(left.get_bottom(), lr.get_top(), color=WHITE)
            )
            
            tree = VGroup(root, left, right, ll, lr, lines)
            self.play(Create(tree))
            
            insert_text = Text("Insert: 35", font_size=28, color=YELLOW)
            insert_text.move_to(RIGHT * 3.5 + UP * 1.5)
            self.play(Write(insert_text))
        
        with self.voiceover(text="Let's insert the value thirty-five into our tree. We start at fifty. Since thirty-five is less than fifty, we go left to thirty. Since thirty-five is greater than thirty, we go right to forty. Since thirty-five is less than forty, we would go left, but there is no left child. So we insert thirty-five as the left child of forty.") as tracker:
            steps = VGroup(
                Text("Step 1: 35 < 50, go left", font_size=20),
                Text("Step 2: 35 > 30, go right", font_size=20),
                Text("Step 3: 35 < 40, go left", font_size=20),
                Text("Step 4: Empty spot! Insert", font_size=20)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            steps.move_to(RIGHT * 3.5 + DOWN * 0.5)
            
            # Animate path
            h1 = root[0].copy().set_fill(YELLOW, opacity=0.5)
            self.play(FadeIn(h1), Write(steps[0]))
            self.wait(0.8)
            self.play(FadeOut(h1))
            
            h2 = left[0].copy().set_fill(YELLOW, opacity=0.5)
            self.play(FadeIn(h2), Write(steps[1]))
            self.wait(0.8)
            self.play(FadeOut(h2))
            
            h3 = lr[0].copy().set_fill(YELLOW, opacity=0.5)
            self.play(FadeIn(h3), Write(steps[2]))
            self.wait(0.8)
            self.play(FadeOut(h3))
            
            # Insert new node
            new_node = self.create_node("35", LEFT * 4.3 + DOWN * 4)
            new_line = Line(lr.get_bottom(), new_node.get_top(), color=GREEN, stroke_width=3)
            
            self.play(Write(steps[3]))
            self.play(Create(new_line), Create(new_node))
            
            success = Text("Inserted!", font_size=24, color=GREEN)
            success.next_to(new_node, DOWN, buff=0.3)
            self.play(Write(success))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
    
    def demonstrate_deletion_simple(self):
        with self.voiceover(text="Deletion in a Binary Search Tree is more complex than search or insertion. There are three cases to consider. Case one: deleting a leaf node with no children. Case two: deleting a node with one child. Case three: deleting a node with two children.") as tracker:
            title = Text("Delete Operation - Simple Cases", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            cases = VGroup(
                Text("Case 1: No children (leaf)", font_size=24, color=YELLOW),
                Text("Case 2: One child", font_size=24, color=ORANGE),
                Text("Case 3: Two children", font_size=24, color=RED)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            cases.move_to(DOWN * 1.5)
            self.play(FadeIn(cases, shift=UP))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Let's start with Case one, deleting a leaf node. Consider deleting the value twenty from our tree. Since twenty is a leaf node with no children, we simply remove it and update the parent's pointer to null. This is the simplest case.") as tracker:
            subtitle = Text("Case 1: Delete Leaf Node (20)", font_size=32, color=YELLOW)
            subtitle.to_edge(UP, buff=1.0)
            self.play(Write(subtitle))
            
            # Create tree
            root = self.create_node("50", LEFT * 3 + UP * 0.5)
            left = self.create_node("30", LEFT * 4.5 + DOWN * 1.2)
            right = self.create_node("70", LEFT * 1.5 + DOWN * 1.2)
            ll = self.create_node("20", LEFT * 5.5 + DOWN * 2.9)
            lr = self.create_node("40", LEFT * 3.5 + DOWN * 2.9)
            
            lines = VGroup(
                Line(root.get_bottom(), left.get_top(), color=WHITE),
                Line(root.get_bottom(), right.get_top(), color=WHITE),
                Line(left.get_bottom(), ll.get_top(), color=WHITE),
                Line(left.get_bottom(), lr.get_top(), color=WHITE)
            )
            
            self.play(Create(VGroup(root, left, right, ll, lr, lines)))
            
            # Highlight node to delete
            highlight = ll[0].copy().set_fill(RED, opacity=0.6)
            self.play(FadeIn(highlight))
            self.wait(1)
            
            # Remove it
            self.play(FadeOut(ll), FadeOut(lines[2]), FadeOut(highlight))
            
            success = Text("Node removed!", font_size=26, color=GREEN)
            success.move_to(RIGHT * 3.5)
            self.play(Write(success))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Now let's look at Case two, deleting a node with one child. Suppose we want to delete thirty, which has two children. Actually, let's delete seventy which has no children in our example. For a proper case two example, imagine seventy has only one child at sixty. We would replace seventy with sixty, connecting sixty directly to fifty.") as tracker:
            subtitle = Text("Case 2: Delete Node with One Child", font_size=32, color=ORANGE)
            subtitle.to_edge(UP, buff=1.0)
            self.play(Write(subtitle))
            
            # Create modified tree
            root = self.create_node("50", LEFT * 3 + UP * 0.5)
            left = self.create_node("30", LEFT * 4.5 + DOWN * 1.2)
            right = self.create_node("70", LEFT * 1.5 + DOWN * 1.2)
            rl = self.create_node("60", LEFT * 2.5 + DOWN * 2.9)
            
            lines = VGroup(
                Line(root.get_bottom(), left.get_top(), color=WHITE),
                Line(root.get_bottom(), right.get_top(), color=WHITE),
                Line(right.get_bottom(), rl.get_top(), color=WHITE)
            )
            
            self.play(Create(VGroup(root, left, right, rl, lines)))
            
            delete_label = Text("Delete 70", font_size=24, color=RED)
            delete_label.next_to(right, RIGHT, buff=0.5)
            self.play(Write(delete_label))
            
            # Highlight
            h = right[0].copy().set_fill(RED, opacity=0.6)
            self.play(FadeIn(h))
            self.wait(1)
            
            # Show replacement
            self.play(FadeOut(right), FadeOut(h), FadeOut(lines[2]), FadeOut(delete_label))
            
            new_line = Line(root.get_bottom(), rl.get_top(), color=GREEN, stroke_width=3)
            self.play(Create(new_line))
            
            explanation = Text("60 replaces 70", font_size=24, color=GREEN)
            explanation.move_to(RIGHT * 3.5)
            self.play(Write(explanation))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
    
    def demonstrate_deletion_complex(self):
        with self.voiceover(text="The most complex deletion case is when a node has two children. We cannot simply remove the node because we need to maintain the BST property. The solution is to find either the inorder successor or inorder predecessor.") as tracker:
            title = Text("Case 3: Delete Node with Two Children", font_size=34, color=RED)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            explanation = VGroup(
                Text("Strategy:", font_size=26, color=YELLOW),
                Text("1. Find inorder successor", font_size=22),
                Text("   (smallest in right subtree)", font_size=20),
                Text("2. Replace node with successor", font_size=22),
                Text("3. Delete the successor", font_size=22)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            explanation.move_to(RIGHT * 3.5 + UP * 0.5)
            self.play(FadeIn(explanation, shift=LEFT))
        
        with self.voiceover(text="Let's delete the value fifty from our tree. Fifty has two children, so we need to find its inorder successor. The inorder successor is the smallest value in the right subtree. We go right to seventy, then go left as far as possible. The smallest value is sixty. We replace fifty with sixty, then delete the original sixty node.") as tracker:
            # Create full tree
            root = self.create_node("50", LEFT * 3 + UP * 0.3)
            left = self.create_node("30", LEFT * 4.5 + DOWN * 1.4)
            right = self.create_node("70", LEFT * 1.5 + DOWN * 1.4)
            ll = self.create_node("20", LEFT * 5.5 + DOWN * 3.1)
            lr = self.create_node("40", LEFT * 3.5 + DOWN * 3.1)
            rl = self.create_node("60", LEFT * 2.5 + DOWN * 3.1)
            rr = self.create_node("80", LEFT * 0.5 + DOWN * 3.1)
            
            lines = VGroup(
                Line(root.get_bottom(), left.get_top(), color=WHITE),
                Line(root.get_bottom(), right.get_top(), color=WHITE),
                Line(left.get_bottom(), ll.get_top(), color=WHITE),
                Line(left.get_bottom(), lr.get_top(), color=WHITE),
                Line(right.get_bottom(), rl.get_top(), color=WHITE),
                Line(right.get_bottom(), rr.get_top(), color=WHITE)
            )
            
            tree = VGroup(root, left, right, ll, lr, rl, rr, lines)
            self.play(Create(tree))
            
            # Highlight node to delete
            h_root = root[0].copy().set_fill(RED, opacity=0.6)
            self.play(FadeIn(h_root))
            self.wait(1)
            
            # Show path to successor
            arrow1 = Arrow(root.get_right(), right.get_left(), color=YELLOW, buff=0.1)
            self.play(Create(arrow1))
            
            arrow2 = Arrow(right.get_bottom(), rl.get_top(), color=YELLOW, buff=0.1)
            self.play(Create(arrow2))
            
            h_succ = rl[0].copy().set_fill(GREEN, opacity=0.6)
            succ_label = Text("Successor!", font_size=22, color=GREEN)
            succ_label.next_to(rl, DOWN, buff=0.3)
            self.play(FadeIn(h_succ), Write(succ_label))
            self.wait(1)
            
            # Replace
            new_root = self.create_node("60", root.get_center())
            self.play(
                FadeOut(h_root), 
                FadeOut(root),
                FadeOut(rl),
                FadeOut(h_succ),
                FadeOut(arrow1),
                FadeOut(arrow2),
                FadeOut(succ_label)
            )
            self.play(FadeIn(new_root))
            
            result = Text("50 replaced with 60!", font_size=24, color=GREEN)
            result.move_to(RIGHT * 3.5 + DOWN * 2)
            self.play(Write(result))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
    
    def demonstrate_traversals(self):
        with self.voiceover(text="Binary Search Trees support three main traversal methods: inorder, preorder, and postorder. Each traversal visits nodes in a different sequence and is useful for different purposes.") as tracker:
            title = Text("Tree Traversal Methods", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            traversals = VGroup(
                Text("Inorder: Left → Root → Right", font_size=24, color=GREEN),
                Text("Preorder: Root → Left → Right", font_size=24, color=YELLOW),
                Text("Postorder: Left → Right → Root", font_size=24, color=ORANGE)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
            traversals.move_to(UP * 0.5)
            self.play(FadeIn(traversals, shift=UP))
        
        with self.voiceover(text="The inorder traversal is particularly important for Binary Search Trees because it visits nodes in sorted order. Let's see this in action with our example tree. We visit the left subtree first, then the root, then the right subtree. The result is: twenty, thirty, forty, fifty, sixty, seventy, eighty - a perfectly sorted sequence!") as tracker:
            # Create tree
            root = self.create_node("50", DOWN * 0.2, scale=0.7)
            left = self.create_node("30", LEFT * 2 + DOWN * 1.5, scale=0.7)
            right = self.create_node("70", RIGHT * 2 + DOWN * 1.5, scale=0.7)
            ll = self.create_node("20", LEFT * 3.2 + DOWN * 2.8, scale=0.7)
            lr = self.create_node("40", LEFT * 0.8 + DOWN * 2.8, scale=0.7)
            rl = self.create_node("60", RIGHT * 0.8 + DOWN * 2.8, scale=0.7)
            rr = self.create_node("80", RIGHT * 3.2 + DOWN * 2.8, scale=0.7)
            
            lines = VGroup(
                Line(root.get_bottom(), left.get_top(), color=WHITE),
                Line(root.get_bottom(), right.get_top(), color=WHITE),
                Line(left.get_bottom(), ll.get_top(), color=WHITE),
                Line(left.get_bottom(), lr.get_top(), color=WHITE),
                Line(right.get_bottom(), rl.get_top(), color=WHITE),
                Line(right.get_bottom(), rr.get_top(), color=WHITE)
            )
            
            tree = VGroup(root, left, right, ll, lr, rl, rr, lines)
            tree.shift(LEFT * 2.5)
            self.play(Create(tree))
            
            # Show inorder sequence
            sequence_label = Text("Inorder Result:", font_size=24, color=GREEN)
            sequence_label.move_to(RIGHT * 2.5 + UP * 1.5)
            self.play(Write(sequence_label))
            
            nodes_order = [ll, left, lr, root, rl, right, rr]
            values = ["20", "30", "40", "50", "60", "70", "80"]
            result = VGroup()
            
            for i, (node, val) in enumerate(zip(nodes_order, values)):
                h = node[0].copy().set_fill(GREEN, opacity=0.7)
                self.play(FadeIn(h), run_time=0.4)
                
                num = Text(val, font_size=22, color=WHITE)
                if i == 0:
                    num.next_to(sequence_label, DOWN, buff=0.4, aligned_edge=LEFT)
                else:
                    num.next_to(result[-1], RIGHT, buff=0.3)
                result.add(num)
                self.play(Write(num), run_time=0.3)
                self.play(FadeOut(h), run_time=0.2)
            
            sorted_label = Text("Sorted Order! ✓", font_size=26, color=GREEN)
            sorted_label.next_to(result, DOWN, buff=0.5)
            self.play(Write(sorted_label))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
    
    def analyze_time_complexity(self):
        with self.voiceover(text="Now let's analyze the time complexity of Binary Search Tree operations. The efficiency of BST operations depends heavily on the height of the tree. In the best case, when the tree is balanced, the height is logarithmic in the number of nodes.") as tracker:
            title = Text("Time Complexity Analysis", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            complexity_table = VGroup(
                Text("Operation", font_size=26, color=YELLOW),
                Text("Average Case", font_size=26, color=GREEN),
                Text("Worst Case", font_size=26, color=RED)
            ).arrange(RIGHT, buff=1.2)
            complexity_table.move_to(UP * 1.8)
            self.play(Write(complexity_table))
            
            # Draw table lines
            line1 = Line(LEFT * 5 + UP * 1.5, RIGHT * 5 + UP * 1.5, color=WHITE)
            self.play(Create(line1))
        
        with self.voiceover(text="For search, insertion, and deletion operations, the average case time complexity is O of log n when the tree is balanced. This is because we eliminate half of the remaining nodes at each step, similar to binary search on an array. However, in the worst case, when the tree becomes skewed like a linked list, the time complexity degrades to O of n.") as tracker:
            ops = VGroup(
                VGroup(
                    Text("Search", font_size=22),
                    Text("O(log n)", font_size=22, color=GREEN),
                    Text("O(n)", font_size=22, color=RED)
                ).arrange(RIGHT, buff=1.5),
                VGroup(
                    Text("Insert", font_size=22),
                    Text("O(log n)", font_size=22, color=GREEN),
                    Text("O(n)", font_size=22, color=RED)
                ).arrange(RIGHT, buff=1.5),
                VGroup(
                    Text("Delete", font_size=22),
                    Text("O(log n)", font_size=22, color=GREEN),
                    Text("O(n)", font_size=22, color=RED)
                ).arrange(RIGHT, buff=1.5)
            ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
            ops.move_to(UP * 0.3)
            
            for op in ops:
                self.play(FadeIn(op, shift=UP), run_time=0.6)
            
            self.wait(1)
            
            # Show visualization of balanced vs skewed
            balanced_label = Text("Balanced: h = log n", font_size=22, color=GREEN)
            balanced_label.move_to(LEFT * 3 + DOWN * 1.8)
            
            skewed_label = Text("Skewed: h = n", font_size=22, color=RED)
            skewed_label.move_to(RIGHT * 3 + DOWN * 1.8)
            
            self.play(Write(balanced_label), Write(skewed_label))
            
            # Simple balanced tree
            b1 = Circle(radius=0.15, color=GREEN, fill_opacity=1).move_to(LEFT * 3 + DOWN * 2.5)
            b2 = Circle(radius=0.15, color=GREEN, fill_opacity=1).move_to(LEFT * 3.5 + DOWN * 3)
            b3 = Circle(radius=0.15, color=GREEN, fill_opacity=1).move_to(LEFT * 2.5 + DOWN * 3)
            bl1 = Line(b1.get_bottom(), b2.get_top(), color=GREEN)
            bl2 = Line(b1.get_bottom(), b3.get_top(), color=GREEN)
            balanced_tree = VGroup(b1, b2, b3, bl1, bl2)
            
            # Skewed tree
            s1 = Circle(radius=0.15, color=RED, fill_opacity=1).move_to(RIGHT * 3 + DOWN * 2.2)
            s2 = Circle(radius=0.15, color=RED, fill_opacity=1).move_to(RIGHT * 3 + DOWN * 2.7)
            s3 = Circle(radius=0.15, color=RED, fill_opacity=1).move_to(RIGHT * 3 + DOWN * 3.2)
            sl1 = Line(s1.get_bottom(), s2.get_top(), color=RED)
            sl2 = Line(s2.get_bottom(), s3.get_top(), color=RED)
            skewed_tree = VGroup(s1, s2, s3, sl1, sl2)
            
            self.play(Create(balanced_tree), Create(skewed_tree))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
    
    def show_applications(self):
        with self.voiceover(text="Binary Search Trees have numerous real-world applications. They are used in databases for indexing, in compilers for symbol tables, in file systems for directory structures, and in many other scenarios where we need efficient searching and dynamic ordering.") as tracker:
            title = Text("Real-World Applications", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            applications = VGroup(
                VGroup(
                    Text("🗄️ Database Indexing", font_size=26, color=YELLOW),
                    Text("Fast lookup and range queries", font_size=20)
                ).arrange(DOWN, buff=0.2),
                VGroup(
                    Text("📁 File Systems", font_size=26, color=GREEN),
                    Text("Directory structure organization", font_size=20)
                ).arrange(DOWN, buff=0.2),
                VGroup(
                    Text("⚙️ Compilers", font_size=26, color=ORANGE),
                    Text("Symbol tables and syntax trees", font_size=20)
                ).arrange(DOWN, buff=0.2),
                VGroup(
                    Text("🎮 Game Development", font_size=26, color=PURPLE),
                    Text("Spatial partitioning and AI", font_size=20)
                ).arrange(DOWN, buff=0.2)
            ).arrange(DOWN, buff=0.6, aligned_edge=LEFT)
            applications.move_to(ORIGIN)
            
            for app in applications:
                self.play(FadeIn(app, shift=RIGHT), run_time=0.8)
                self.wait(0.5)
        
        with self.voiceover(text="One common application is in database systems where BSTs, or more specifically B-trees which are variants of BSTs, are used to index data for fast retrieval. Another important use is in implementing sets and maps in programming languages, where we need to maintain sorted collections with efficient operations.") as tracker:
            self.wait(3)
            
            example = VGroup(
                Text("Example: Dictionary Implementation", font_size=28, color=CYAN),
                Text("• Insert word: O(log n)", font_size=22),
                Text("• Search word: O(log n)", font_size=22),
                Text("• Sorted iteration: O(n)", font_size=22)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            example.move_to(DOWN * 2)
            self.play(FadeIn(example, shift=UP))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
    
    def explain_balance(self):
        with self.voiceover(text="An important consideration when using Binary Search Trees is maintaining balance. An unbalanced tree can degrade to linear time complexity, defeating the purpose of using a tree structure. This is where self-balancing trees come into play.") as tracker:
            title = Text("Balanced vs Unbalanced BSTs", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Show balanced tree on left
            balanced_title = Text("Balanced Tree", font_size=26, color=GREEN)
            balanced_title.move_to(LEFT * 3.5 + UP * 1.5)
            self.play(Write(balanced_title))
            
            # Create balanced tree
            b_root = self.create_node("50", LEFT * 3.5 + UP * 0.3, scale=0.6)
            b_left = self.create_node("30", LEFT * 4.8 + DOWN * 0.8, scale=0.6)
            b_right = self.create_node("70", LEFT * 2.2 + DOWN * 0.8, scale=0.6)
            b_ll = self.create_node("20", LEFT * 5.5 + DOWN * 2, scale=0.6)
            b_lr = self.create_node("40", LEFT * 4 + DOWN * 2, scale=0.6)
            b_rl = self.create_node("60", LEFT * 2.9 + DOWN * 2, scale=0.6)
            b_rr = self.create_node("80", LEFT * 1.4 + DOWN * 2, scale=0.6)
            
            b_lines = VGroup(
                Line(b_root.get_bottom(), b_left.get_top(), color=GREEN),
                Line(b_root.get_bottom(), b_right.get_top(), color=GREEN),
                Line(b_left.get_bottom(), b_ll.get_top(), color=GREEN),
                Line(b_left.get_bottom(), b_lr.get_top(), color=GREEN),
                Line(b_right.get_bottom(), b_rl.get_top(), color=GREEN),
                Line(b_right.get_bottom(), b_rr.get_top(), color=GREEN)
            )
            
            balanced = VGroup(b_root, b_left, b_right, b_ll, b_lr, b_rl, b_rr, b_lines)
            self.play(Create(balanced))
            
            b_height = Text("Height: 3", font_size=22, color=GREEN)
            b_height.move_to(LEFT * 3.5 + DOWN * 3)
            self.play(Write(b_height))
        
        with self.voiceover(text="On the left, we have a balanced tree with height three. On the right, let's show an unbalanced tree with the same values inserted in sorted order. Notice how it degenerates into a linked list structure with height seven. This is why insertion order matters, and why self-balancing trees like AVL trees and Red-Black trees were invented.") as tracker:
            # Show unbalanced tree on right
            unbalanced_title = Text("Unbalanced Tree", font_size=26, color=RED)
            unbalanced_title.move_to(RIGHT * 3.5 + UP * 1.5)
            self.play(Write(unbalanced_title))
            
            # Create skewed tree
            positions = [UP * 0.3, DOWN * 0.2, DOWN * 0.7, DOWN * 1.2, DOWN * 1.7, DOWN * 2.2, DOWN * 2.7]
            nodes = []
            lines = VGroup()
            
            for i, (val, pos) in enumerate(zip(["20", "30", "40", "50", "60", "70", "80"], positions)):
                node = self.create_node(val, RIGHT * 3.5 + pos, scale=0.6)
                nodes.append(node)
                if i > 0:
                    line = Line(nodes[i-1].get_bottom(), node.get_top(), color=RED)
                    lines.add(line)
                    self.play(Create(line), Create(node), run_time=0.4)
                else:
                    self.play(Create(node), run_time=0.4)
            
            u_height = Text("Height: 7", font_size=22, color=RED)
            u_height.move_to(RIGHT * 3.5 + DOWN * 3.2)
            self.play(Write(u_height))
            
            comparison = VGroup(
                Text("Performance Impact:", font_size=24, color=YELLOW),
                Text("Balanced: O(log n) = O(log 7) ≈ 3", font_size=20, color=GREEN),
                Text("Skewed: O(n) = O(7) = 7", font_size=20, color=RED)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            comparison.move_to(DOWN * 2.5)
            self.play(FadeIn(comparison, shift=UP))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
    
    def show_conclusion(self):
        with self.voiceover(text="We have explored Binary Search Trees in depth, understanding their structure, properties, and core operations. We've seen how search, insertion, and deletion work, examined different traversal methods, and analyzed time complexity.") as tracker:
            title = Text("Summary", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1)
            self.play(Write(title))
            
            key_points = VGroup(
                Text("✓ BST Property: Left < Root < Right", font_size=24),
                Text("✓ Search: O(log n) average", font_size=24),
                Text("✓ Insert: O(log n) average", font_size=24),
                Text("✓ Delete: Three cases to handle", font_size=24),
                Text("✓ Inorder traversal gives sorted order", font_size=24),
                Text("✓ Balance is crucial for efficiency", font_size=24)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            key_points.move_to(UP * 0.2)
            
            for point in key_points:
                self.play(FadeIn(point, shift=RIGHT), run_time=0.6)
                self.wait(0.3)
        
        with self.voiceover(text="Remember that while basic Binary Search Trees are powerful, maintaining balance is essential for optimal performance. In practice, self-balancing variants like AVL trees and Red-Black trees are often preferred. Thank you for watching this explanation of Binary Search Tree operations!") as tracker:
            self.wait(2)
            
            final = VGroup(
                Text("Next Steps:", font_size=28, color=YELLOW),
                Text("• Study AVL Trees", font_size=22),
                Text("• Explore Red-Black Trees", font_size=22),
                Text("• Practice implementations", font_size=22)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            final.move_to(DOWN * 2.2)
            self.play(FadeIn(final, shift=UP))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Thank you for watching!") as tracker:
            thank_you = Text("Thank You!", font_size=36, color=BLUE)
            self.play(Write(thank_you))
            self.wait(2)
    
    def create_node(self, value, position, scale=1.0):
        """Helper function to create a tree node"""
        circle = Circle(radius=0.4 * scale, color=BLUE, fill_opacity=0.8, fill_color=DARK_BLUE)
        text = Text(value, font_size=int(24 * scale), color=WHITE)
        node = VGroup(circle, text)
        node.move_to(position)
        return node


# Run the animation
if __name__ == "__main__":
    scene = BinarySearchTreeOperations()
    scene.render()