from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class BinaryTreeExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))
        
        # Section 1: Introduction
        self.introduction()
        
        # Section 2: What is a Tree?
        self.what_is_tree()
        
        # Section 3: Binary Tree Definition
        self.binary_tree_definition()
        
        # Section 4: Types of Binary Trees
        self.types_of_binary_trees()
        
        # Section 5: Tree Traversal - Inorder
        self.inorder_traversal()
        
        # Section 6: Tree Traversal - Preorder
        self.preorder_traversal()
        
        # Section 7: Tree Traversal - Postorder
        self.postorder_traversal()
        
        # Section 8: Binary Search Tree
        self.binary_search_tree()
        
        # Section 9: BST Operations - Insertion
        self.bst_insertion()
        
        # Section 10: BST Operations - Search
        self.bst_search()
        
        # Section 11: Real World Applications
        self.real_world_applications()
        
        # Section 12: Conclusion
        self.conclusion()

    def introduction(self):
        with self.voiceover(text="Welcome to this comprehensive guide on Binary Trees! Binary trees are one of the most fundamental data structures in computer science, forming the backbone of countless algorithms and applications. Today, we will explore what binary trees are, how they work, and why they are so important in programming and software development.") as tracker:
            title = Text("Binary Trees", font_size=36, color=BLUE)
            subtitle = Text("A Complete Visual Guide", font_size=28, color=WHITE)
            subtitle.next_to(title, DOWN, buff=0.5)
            
            self.play(Write(title))
            self.wait(0.5)
            self.play(FadeIn(subtitle))
            self.wait(1)
        
        self.play(FadeOut(title), FadeOut(subtitle))

    def what_is_tree(self):
        with self.voiceover(text="Before we dive into binary trees, let's understand what a tree data structure is. A tree is a hierarchical data structure that consists of nodes connected by edges. It starts with a root node at the top and branches out into child nodes, much like an upside-down tree in nature.") as tracker:
            section_title = Text("What is a Tree?", font_size=36, color=YELLOW)
            section_title.to_edge(UP, buff=1.0)
            self.play(Write(section_title))
            
            # Create a simple tree
            root = Circle(radius=0.4, color=GREEN).shift(UP * 1.5)
            root_label = Text("Root", font_size=20).move_to(root.get_center())
            
            child1 = Circle(radius=0.4, color=BLUE).shift(LEFT * 2 + DOWN * 0.5)
            child1_label = Text("Node", font_size=20).move_to(child1.get_center())
            
            child2 = Circle(radius=0.4, color=BLUE).shift(RIGHT * 2 + DOWN * 0.5)
            child2_label = Text("Node", font_size=20).move_to(child2.get_center())
            
            edge1 = Line(root.get_bottom(), child1.get_top(), color=WHITE)
            edge2 = Line(root.get_bottom(), child2.get_top(), color=WHITE)
            
            self.play(Create(root), Write(root_label))
            self.wait(0.3)
            self.play(Create(edge1), Create(edge2))
            self.play(Create(child1), Write(child1_label), Create(child2), Write(child2_label))
        
        with self.voiceover(text="Each connection between nodes is called an edge, and each node can have multiple children. The nodes at the bottom with no children are called leaf nodes. This hierarchical structure allows us to organize data efficiently and perform operations quickly.") as tracker:
            # Add more children to show leaf nodes
            leaf1 = Circle(radius=0.4, color=RED).shift(LEFT * 3 + DOWN * 2.5)
            leaf1_label = Text("Leaf", font_size=18).move_to(leaf1.get_center())
            
            leaf2 = Circle(radius=0.4, color=RED).shift(LEFT * 1 + DOWN * 2.5)
            leaf2_label = Text("Leaf", font_size=18).move_to(leaf2.get_center())
            
            edge3 = Line(child1.get_bottom(), leaf1.get_top(), color=WHITE)
            edge4 = Line(child1.get_bottom(), leaf2.get_top(), color=WHITE)
            
            self.play(Create(edge3), Create(edge4))
            self.play(Create(leaf1), Write(leaf1_label), Create(leaf2), Write(leaf2_label))
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def binary_tree_definition(self):
        with self.voiceover(text="Now let's focus on binary trees specifically. A binary tree is a special type of tree where each node can have at most two children, commonly referred to as the left child and the right child. This constraint of having maximum two children makes binary trees particularly useful for searching and sorting operations.") as tracker:
            section_title = Text("Binary Tree Definition", font_size=36, color=YELLOW)
            section_title.to_edge(UP, buff=1.0)
            self.play(Write(section_title))
            
            # Definition box
            definition = VGroup(
                Text("Binary Tree Properties:", font_size=28, color=BLUE),
                Text("• Each node has at most 2 children", font_size=24),
                Text("• Left child and Right child", font_size=24),
                Text("• Hierarchical structure", font_size=24)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            definition.move_to(LEFT * 3 + UP * 0.5)
            
            self.play(Write(definition[0]))
            self.wait(0.3)
            self.play(Write(definition[1]))
            self.play(Write(definition[2]))
            self.play(Write(definition[3]))
        
        with self.voiceover(text="Let's visualize a binary tree. Here we have a root node with value 10. It has a left child with value 5 and a right child with value 15. Each of these children can also have their own left and right children, forming a tree structure. Notice how each node follows the rule of having at most two children.") as tracker:
            # Create a binary tree visualization
            node_10 = self.create_tree_node("10", RIGHT * 2.5 + UP * 1)
            node_5 = self.create_tree_node("5", RIGHT * 0.5 + DOWN * 0.8)
            node_15 = self.create_tree_node("15", RIGHT * 4.5 + DOWN * 0.8)
            
            edge_10_5 = Line(node_10.get_bottom(), node_5.get_top(), color=WHITE)
            edge_10_15 = Line(node_10.get_bottom(), node_15.get_top(), color=WHITE)
            
            self.play(Create(node_10))
            self.wait(0.3)
            self.play(Create(edge_10_5), Create(edge_10_15))
            self.play(Create(node_5), Create(node_15))
            
            # Add more nodes
            node_3 = self.create_tree_node("3", LEFT * 0.5 + DOWN * 2.6)
            node_7 = self.create_tree_node("7", RIGHT * 1.5 + DOWN * 2.6)
            node_12 = self.create_tree_node("12", RIGHT * 3.5 + DOWN * 2.6)
            node_17 = self.create_tree_node("17", RIGHT * 5.5 + DOWN * 2.6)
            
            edge_5_3 = Line(node_5.get_bottom(), node_3.get_top(), color=WHITE)
            edge_5_7 = Line(node_5.get_bottom(), node_7.get_top(), color=WHITE)
            edge_15_12 = Line(node_15.get_bottom(), node_12.get_top(), color=WHITE)
            edge_15_17 = Line(node_15.get_bottom(), node_17.get_top(), color=WHITE)
            
            self.play(
                Create(edge_5_3), Create(edge_5_7),
                Create(edge_15_12), Create(edge_15_17)
            )
            self.play(
                Create(node_3), Create(node_7),
                Create(node_12), Create(node_17)
            )
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def create_tree_node(self, value, position, color=BLUE):
        circle = Circle(radius=0.4, color=color)
        label = Text(value, font_size=24)
        node = VGroup(circle, label)
        node.move_to(position)
        return node

    def types_of_binary_trees(self):
        with self.voiceover(text="There are several types of binary trees, each with unique properties. A full binary tree has every node with either zero or two children, never just one. A complete binary tree has all levels completely filled except possibly the last level, which is filled from left to right. A perfect binary tree has all internal nodes with two children and all leaf nodes at the same level.") as tracker:
            section_title = Text("Types of Binary Trees", font_size=36, color=YELLOW)
            section_title.to_edge(UP, buff=1.0)
            self.play(Write(section_title))
            
            # Full Binary Tree
            full_title = Text("Full Binary Tree", font_size=24, color=GREEN)
            full_title.move_to(LEFT * 4 + UP * 1.5)
            self.play(Write(full_title))
            
            # Create full binary tree
            full_root = self.create_tree_node("1", LEFT * 4 + UP * 0.3, GREEN)
            full_l = self.create_tree_node("2", LEFT * 5 + DOWN * 1, GREEN)
            full_r = self.create_tree_node("3", LEFT * 3 + DOWN * 1, GREEN)
            full_ll = self.create_tree_node("4", LEFT * 5.5 + DOWN * 2.3, GREEN)
            full_lr = self.create_tree_node("5", LEFT * 4.5 + DOWN * 2.3, GREEN)
            
            full_edges = VGroup(
                Line(full_root.get_bottom(), full_l.get_top(), color=WHITE),
                Line(full_root.get_bottom(), full_r.get_top(), color=WHITE),
                Line(full_l.get_bottom(), full_ll.get_top(), color=WHITE),
                Line(full_l.get_bottom(), full_lr.get_top(), color=WHITE)
            )
            
            self.play(Create(full_edges))
            self.play(Create(full_root), Create(full_l), Create(full_r), Create(full_ll), Create(full_lr))
        
        with self.voiceover(text="On the right, we have a complete binary tree where all levels are filled from left to right. This type is commonly used in heap data structures. Notice how the nodes are arranged systematically, making it easy to represent using arrays in memory.") as tracker:
            # Complete Binary Tree
            complete_title = Text("Complete Binary Tree", font_size=24, color=ORANGE)
            complete_title.move_to(RIGHT * 3 + UP * 1.5)
            self.play(Write(complete_title))
            
            comp_root = self.create_tree_node("1", RIGHT * 3 + UP * 0.3, ORANGE)
            comp_l = self.create_tree_node("2", RIGHT * 2 + DOWN * 1, ORANGE)
            comp_r = self.create_tree_node("3", RIGHT * 4 + DOWN * 1, ORANGE)
            comp_ll = self.create_tree_node("4", RIGHT * 1.5 + DOWN * 2.3, ORANGE)
            comp_lr = self.create_tree_node("5", RIGHT * 2.5 + DOWN * 2.3, ORANGE)
            comp_rl = self.create_tree_node("6", RIGHT * 3.5 + DOWN * 2.3, ORANGE)
            
            comp_edges = VGroup(
                Line(comp_root.get_bottom(), comp_l.get_top(), color=WHITE),
                Line(comp_root.get_bottom(), comp_r.get_top(), color=WHITE),
                Line(comp_l.get_bottom(), comp_ll.get_top(), color=WHITE),
                Line(comp_l.get_bottom(), comp_lr.get_top(), color=WHITE),
                Line(comp_r.get_bottom(), comp_rl.get_top(), color=WHITE)
            )
            
            self.play(Create(comp_edges))
            self.play(Create(comp_root), Create(comp_l), Create(comp_r), 
                     Create(comp_ll), Create(comp_lr), Create(comp_rl))
            self.wait(1.5)
        
        self.play(FadeOut(*self.mobjects))

    def inorder_traversal(self):
        with self.voiceover(text="Tree traversal is the process of visiting each node in the tree exactly once in a specific order. Let's start with inorder traversal. In inorder traversal, we visit the left subtree first, then the current node, and finally the right subtree. This is commonly written as: Left, Root, Right.") as tracker:
            section_title = Text("Tree Traversal: Inorder", font_size=36, color=YELLOW)
            section_title.to_edge(UP, buff=1.0)
            self.play(Write(section_title))
            
            # Show formula
            formula = MathTex(r"\text{Inorder: Left} \rightarrow \text{Root} \rightarrow \text{Right}", font_size=32)
            formula.move_to(UP * 2)
            self.play(Write(formula))
            
            # Create tree
            root = self.create_tree_node("4", ORIGIN + UP * 0.5, BLUE)
            left = self.create_tree_node("2", LEFT * 2 + DOWN * 1, BLUE)
            right = self.create_tree_node("6", RIGHT * 2 + DOWN * 1, BLUE)
            ll = self.create_tree_node("1", LEFT * 3 + DOWN * 2.5, BLUE)
            lr = self.create_tree_node("3", LEFT * 1 + DOWN * 2.5, BLUE)
            rl = self.create_tree_node("5", RIGHT * 1 + DOWN * 2.5, BLUE)
            rr = self.create_tree_node("7", RIGHT * 3 + DOWN * 2.5, BLUE)
            
            edges = VGroup(
                Line(root.get_bottom(), left.get_top(), color=WHITE),
                Line(root.get_bottom(), right.get_top(), color=WHITE),
                Line(left.get_bottom(), ll.get_top(), color=WHITE),
                Line(left.get_bottom(), lr.get_top(), color=WHITE),
                Line(right.get_bottom(), rl.get_top(), color=WHITE),
                Line(right.get_bottom(), rr.get_top(), color=WHITE)
            )
            
            self.play(Create(edges))
            self.play(Create(root), Create(left), Create(right), Create(ll), Create(lr), Create(rl), Create(rr))
        
        with self.voiceover(text="Let's trace through the inorder traversal step by step. We start at the root, but we don't visit it yet. We go to the left subtree. Again, we go left until we reach node 1, which has no left child. We visit 1, then go back to 2, visit it, then visit 3. Now we visit the root 4. Then we traverse the right subtree: visit 5, then 6, then 7. The final inorder sequence is: 1, 2, 3, 4, 5, 6, 7.") as tracker:
            # Highlight nodes in inorder sequence
            result = Text("Inorder Result: ", font_size=24, color=GREEN)
            result.move_to(DOWN * 3.2 + LEFT * 3)
            self.play(Write(result))
            
            sequence = []
            nodes_to_highlight = [ll, left, lr, root, rl, right, rr]
            values = ["1", "2", "3", "4", "5", "6", "7"]
            
            for i, (node, val) in enumerate(zip(nodes_to_highlight, values)):
                self.play(node[0].animate.set_color(GREEN), run_time=0.4)
                num_text = Text(val, font_size=24, color=GREEN)
                if i == 0:
                    num_text.next_to(result, RIGHT, buff=0.2)
                else:
                    num_text.next_to(sequence[-1], RIGHT, buff=0.3)
                sequence.append(num_text)
                self.play(Write(num_text), run_time=0.3)
                self.play(node[0].animate.set_color(BLUE), run_time=0.3)
            
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def preorder_traversal(self):
        with self.voiceover(text="Next, we have preorder traversal. In preorder, we visit the root node first, then traverse the left subtree, and finally the right subtree. The order is: Root, Left, Right. This traversal is useful for creating a copy of the tree or getting prefix expressions.") as tracker:
            section_title = Text("Tree Traversal: Preorder", font_size=36, color=YELLOW)
            section_title.to_edge(UP, buff=1.0)
            self.play(Write(section_title))
            
            formula = MathTex(r"\text{Preorder: Root} \rightarrow \text{Left} \rightarrow \text{Right}", font_size=32)
            formula.move_to(UP * 2)
            self.play(Write(formula))
            
            # Create tree
            root = self.create_tree_node("4", ORIGIN + UP * 0.5, PURPLE)
            left = self.create_tree_node("2", LEFT * 2 + DOWN * 1, PURPLE)
            right = self.create_tree_node("6", RIGHT * 2 + DOWN * 1, PURPLE)
            ll = self.create_tree_node("1", LEFT * 3 + DOWN * 2.5, PURPLE)
            lr = self.create_tree_node("3", LEFT * 1 + DOWN * 2.5, PURPLE)
            rl = self.create_tree_node("5", RIGHT * 1 + DOWN * 2.5, PURPLE)
            rr = self.create_tree_node("7", RIGHT * 3 + DOWN * 2.5, PURPLE)
            
            edges = VGroup(
                Line(root.get_bottom(), left.get_top(), color=WHITE),
                Line(root.get_bottom(), right.get_top(), color=WHITE),
                Line(left.get_bottom(), ll.get_top(), color=WHITE),
                Line(left.get_bottom(), lr.get_top(), color=WHITE),
                Line(right.get_bottom(), rl.get_top(), color=WHITE),
                Line(right.get_bottom(), rr.get_top(), color=WHITE)
            )
            
            self.play(Create(edges))
            self.play(Create(root), Create(left), Create(right), Create(ll), Create(lr), Create(rl), Create(rr))
        
        with self.voiceover(text="Let's trace the preorder traversal. We start by visiting the root node 4 immediately. Then we go to the left subtree, visit 2, then go to its left subtree and visit 1, then visit 3. After completing the left subtree, we move to the right subtree: visit 6, then 5, then 7. The preorder sequence is: 4, 2, 1, 3, 6, 5, 7.") as tracker:
            result = Text("Preorder Result: ", font_size=24, color=GREEN)
            result.move_to(DOWN * 3.2 + LEFT * 3)
            self.play(Write(result))
            
            sequence = []
            nodes_to_highlight = [root, left, ll, lr, right, rl, rr]
            values = ["4", "2", "1", "3", "6", "5", "7"]
            
            for i, (node, val) in enumerate(zip(nodes_to_highlight, values)):
                self.play(node[0].animate.set_color(GREEN), run_time=0.4)
                num_text = Text(val, font_size=24, color=GREEN)
                if i == 0:
                    num_text.next_to(result, RIGHT, buff=0.2)
                else:
                    num_text.next_to(sequence[-1], RIGHT, buff=0.3)
                sequence.append(num_text)
                self.play(Write(num_text), run_time=0.3)
                self.play(node[0].animate.set_color(PURPLE), run_time=0.3)
            
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def postorder_traversal(self):
        with self.voiceover(text="Finally, let's explore postorder traversal. In postorder, we traverse the left subtree first, then the right subtree, and visit the root node last. The order is: Left, Right, Root. This traversal is particularly useful for deleting trees or evaluating postfix expressions.") as tracker:
            section_title = Text("Tree Traversal: Postorder", font_size=36, color=YELLOW)
            section_title.to_edge(UP, buff=1.0)
            self.play(Write(section_title))
            
            formula = MathTex(r"\text{Postorder: Left} \rightarrow \text{Right} \rightarrow \text{Root}", font_size=32)
            formula.move_to(UP * 2)
            self.play(Write(formula))
            
            # Create tree
            root = self.create_tree_node("4", ORIGIN + UP * 0.5, RED)
            left = self.create_tree_node("2", LEFT * 2 + DOWN * 1, RED)
            right = self.create_tree_node("6", RIGHT * 2 + DOWN * 1, RED)
            ll = self.create_tree_node("1", LEFT * 3 + DOWN * 2.5, RED)
            lr = self.create_tree_node("3", LEFT * 1 + DOWN * 2.5, RED)
            rl = self.create_tree_node("5", RIGHT * 1 + DOWN * 2.5, RED)
            rr = self.create_tree_node("7", RIGHT * 3 + DOWN * 2.5, RED)
            
            edges = VGroup(
                Line(root.get_bottom(), left.get_top(), color=WHITE),
                Line(root.get_bottom(), right.get_top(), color=WHITE),
                Line(left.get_bottom(), ll.get_top(), color=WHITE),
                Line(left.get_bottom(), lr.get_top(), color=WHITE),
                Line(right.get_bottom(), rl.get_top(), color=WHITE),
                Line(right.get_bottom(), rr.get_top(), color=WHITE)
            )
            
            self.play(Create(edges))
            self.play(Create(root), Create(left), Create(right), Create(ll), Create(lr), Create(rl), Create(rr))
        
        with self.voiceover(text="Let's trace postorder traversal carefully. We start at the root but don't visit it. We go left to node 2, again we don't visit it. We go to node 1, which has no children, so we visit it. Then we visit 3, then we can finally visit 2. Now we move to the right subtree: visit 5, then 7, then 6. Finally, we visit the root 4. The postorder sequence is: 1, 3, 2, 5, 7, 6, 4.") as tracker:
            result = Text("Postorder Result: ", font_size=24, color=GREEN)
            result.move_to(DOWN * 3.2 + LEFT * 3)
            self.play(Write(result))
            
            sequence = []
            nodes_to_highlight = [ll, lr, left, rl, rr, right, root]
            values = ["1", "3", "2", "5", "7", "6", "4"]
            
            for i, (node, val) in enumerate(zip(nodes_to_highlight, values)):
                self.play(node[0].animate.set_color(GREEN), run_time=0.4)
                num_text = Text(val, font_size=24, color=GREEN)
                if i == 0:
                    num_text.next_to(result, RIGHT, buff=0.2)
                else:
                    num_text.next_to(sequence[-1], RIGHT, buff=0.3)
                sequence.append(num_text)
                self.play(Write(num_text), run_time=0.3)
                self.play(node[0].animate.set_color(RED), run_time=0.3)
            
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def binary_search_tree(self):
        with self.voiceover(text="A Binary Search Tree, or BST, is a special type of binary tree with an important property: for every node, all values in the left subtree are smaller than the node's value, and all values in the right subtree are greater. This property makes searching extremely efficient, with an average time complexity of O log n.") as tracker:
            section_title = Text("Binary Search Tree (BST)", font_size=36, color=YELLOW)
            section_title.to_edge(UP, buff=1.0)
            self.play(Write(section_title))
            
            # BST property
            property_text = VGroup(
                Text("BST Property:", font_size=28, color=BLUE),
                Text("Left subtree < Node < Right subtree", font_size=24)
            ).arrange(DOWN, buff=0.3)
            property_text.move_to(UP * 2)
            self.play(Write(property_text))
        
        with self.voiceover(text="Let's visualize a binary search tree. Here we have the root node with value 50. Notice that 30 is less than 50, so it's in the left subtree. 70 is greater than 50, so it's in the right subtree. This pattern continues at every level: 20 and 40 are both less than 30, while 60 and 80 are compared with 70. This organization allows for efficient searching.") as tracker:
            # Create BST
            root = self.create_tree_node("50", ORIGIN + DOWN * 0.2, GOLD)
            left = self.create_tree_node("30", LEFT * 2.5 + DOWN * 1.5, GOLD)
            right = self.create_tree_node("70", RIGHT * 2.5 + DOWN * 1.5, GOLD)
            ll = self.create_tree_node("20", LEFT * 3.5 + DOWN * 2.8, GOLD)
            lr = self.create_tree_node("40", LEFT * 1.5 + DOWN * 2.8, GOLD)
            rl = self.create_tree_node("60", RIGHT * 1.5 + DOWN * 2.8, GOLD)
            rr = self.create_tree_node("80", RIGHT * 3.5 + DOWN * 2.8, GOLD)
            
            edges = VGroup(
                Line(root.get_bottom(), left.get_top(), color=WHITE),
                Line(root.get_bottom(), right.get_top(), color=WHITE),
                Line(left.get_bottom(), ll.get_top(), color=WHITE),
                Line(left.get_bottom(), lr.get_top(), color=WHITE),
                Line(right.get_bottom(), rl.get_top(), color=WHITE),
                Line(right.get_bottom(), rr.get_top(), color=WHITE)
            )
            
            self.play(Create(edges))
            self.play(Create(root))
            self.wait(0.3)
            self.play(Create(left), Create(right))
            self.wait(0.3)
            self.play(Create(ll), Create(lr), Create(rl), Create(rr))
            
            # Highlight the BST property
            left_arrow = Arrow(left.get_right(), root.get_left(), color=GREEN, buff=0.1)
            left_text = Text("<", font_size=28, color=GREEN).next_to(left_arrow, RIGHT, buff=0.1)
            right_arrow = Arrow(root.get_right(), right.get_left(), color=RED, buff=0.1)
            right_text = Text(">", font_size=28, color=RED).next_to(right_arrow, RIGHT, buff=0.1)
            
            self.play(Create(left_arrow), Write(left_text))
            self.play(Create(right_arrow), Write(right_text))
            self.wait(1.5)
        
        self.play(FadeOut(*self.mobjects))

    def bst_insertion(self):
        with self.voiceover(text="Let's see how to insert a new node into a Binary Search Tree. The insertion algorithm follows these steps: Start at the root. If the value to insert is less than the current node, go left; if greater, go right. Repeat this process until you find an empty spot, then insert the new node there. Let's insert the value 45 into our BST.") as tracker:
            section_title = Text("BST Insertion", font_size=36, color=YELLOW)
            section_title.to_edge(UP, buff=1.0)
            self.play(Write(section_title))
            
            # Create initial BST
            root = self.create_tree_node("50", ORIGIN + UP * 0.8, BLUE)
            left = self.create_tree_node("30", LEFT * 2.5 + DOWN * 0.5, BLUE)
            right = self.create_tree_node("70", RIGHT * 2.5 + DOWN * 0.5, BLUE)
            ll = self.create_tree_node("20", LEFT * 3.5 + DOWN * 1.8, BLUE)
            lr = self.create_tree_node("40", LEFT * 1.5 + DOWN * 1.8, BLUE)
            
            edges = VGroup(
                Line(root.get_bottom(), left.get_top(), color=WHITE),
                Line(root.get_bottom(), right.get_top(), color=WHITE),
                Line(left.get_bottom(), ll.get_top(), color=WHITE),
                Line(left.get_bottom(), lr.get_top(), color=WHITE)
            )
            
            self.play(Create(edges))
            self.play(Create(root), Create(left), Create(right), Create(ll), Create(lr))
            
            insert_text = Text("Inserting: 45", font_size=28, color=GREEN)
            insert_text.move_to(RIGHT * 3.5 + UP * 1.5)
            self.play(Write(insert_text))
        
        with self.voiceover(text="We start at 50. Since 45 is less than 50, we go left to 30. Now 45 is greater than 30, so we go right to 40. Since 45 is greater than 40 and there's no right child, we insert 45 as the right child of 40. The tree maintains its BST property after insertion.") as tracker:
            # Trace the path
            self.play(root[0].animate.set_color(YELLOW), run_time=0.5)
            step1 = Text("45 < 50, go left", font_size=22, color=WHITE)
            step1.move_to(RIGHT * 3.5 + UP * 0.5)
            self.play(Write(step1))
            self.play(root[0].animate.set_color(BLUE), run_time=0.3)
            
            self.play(left[0].animate.set_color(YELLOW), run_time=0.5)
            step2 = Text("45 > 30, go right", font_size=22, color=WHITE)
            step2.move_to(RIGHT * 3.5 + UP * 0)
            self.play(Write(step2))
            self.play(left[0].animate.set_color(BLUE), run_time=0.3)
            
            self.play(lr[0].animate.set_color(YELLOW), run_time=0.5)
            step3 = Text("45 > 40, insert right", font_size=22, color=WHITE)
            step3.move_to(RIGHT * 3.5 + DOWN * 0.5)
            self.play(Write(step3))
            
            # Insert new node
            new_node = self.create_tree_node("45", LEFT * 0.5 + DOWN * 3.1, GREEN)
            new_edge = Line(lr.get_bottom(), new_node.get_top(), color=WHITE)
            
            self.play(Create(new_edge))
            self.play(Create(new_node))
            self.play(lr[0].animate.set_color(BLUE), run_time=0.3)
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def bst_search(self):
        with self.voiceover(text="Searching in a Binary Search Tree is very efficient thanks to its ordered structure. To search for a value, we start at the root and compare our target with the current node. If the target is smaller, we search the left subtree. If larger, we search the right subtree. If equal, we've found it! Let's search for the value 40 in our tree.") as tracker:
            section_title = Text("BST Search Operation", font_size=36, color=YELLOW)
            section_title.to_edge(UP, buff=1.0)
            self.play(Write(section_title))
            
            # Create BST
            root = self.create_tree_node("50", ORIGIN + UP * 0.8, PURPLE)
            left = self.create_tree_node("30", LEFT * 2.5 + DOWN * 0.5, PURPLE)
            right = self.create_tree_node("70", RIGHT * 2.5 + DOWN * 0.5, PURPLE)
            ll = self.create_tree_node("20", LEFT * 3.5 + DOWN * 1.8, PURPLE)
            lr = self.create_tree_node("40", LEFT * 1.5 + DOWN * 1.8, PURPLE)
            rl = self.create_tree_node("60", RIGHT * 1.5 + DOWN * 1.8, PURPLE)
            rr = self.create_tree_node("80", RIGHT * 3.5 + DOWN * 1.8, PURPLE)
            
            edges = VGroup(
                Line(root.get_bottom(), left.get_top(), color=WHITE),
                Line(root.get_bottom(), right.get_top(), color=WHITE),
                Line(left.get_bottom(), ll.get_top(), color=WHITE),
                Line(left.get_bottom(), lr.get_top(), color=WHITE),
                Line(right.get_bottom(), rl.get_top(), color=WHITE),
                Line(right.get_bottom(), rr.get_top(), color=WHITE)
            )
            
            self.play(Create(edges))
            self.play(Create(root), Create(left), Create(right), Create(ll), Create(lr), Create(rl), Create(rr))
            
            search_text = Text("Searching for: 40", font_size=28, color=GREEN)
            search_text.move_to(RIGHT * 3.5 + UP * 1.8)
            self.play(Write(search_text))
        
        with self.voiceover(text="We start at the root, 50. Since 40 is less than 50, we move to the left child, which is 30. Now, 40 is greater than 30, so we move to the right child of 30. We've found 40! Notice we only visited 3 nodes out of 7, demonstrating the efficiency of binary search trees. The time complexity is O log n, much better than linear search.") as tracker:
            # Trace search path
            self.play(root[0].animate.set_color(YELLOW), run_time=0.6)
            comparison1 = Text("40 < 50? Yes, go left", font_size=22, color=WHITE)
            comparison1.move_to(RIGHT * 3.5 + UP * 1)
            self.play(Write(comparison1))
            self.wait(0.4)
            self.play(root[0].animate.set_color(PURPLE), run_time=0.3)
            
            self.play(left[0].animate.set_color(YELLOW), run_time=0.6)
            comparison2 = Text("40 > 30? Yes, go right", font_size=22, color=WHITE)
            comparison2.move_to(RIGHT * 3.5 + UP * 0.3)
            self.play(Write(comparison2))
            self.wait(0.4)
            self.play(left[0].animate.set_color(PURPLE), run_time=0.3)
            
            self.play(lr[0].animate.set_color(GREEN), run_time=0.6)
            found = Text("Found 40! ✓", font_size=28, color=GREEN, weight=BOLD)
            found.move_to(RIGHT * 3.5 + DOWN * 0.5)
            self.play(Write(found))
            
            # Show complexity
            complexity = MathTex(r"\text{Time Complexity: } O(\log n)", font_size=28, color=BLUE)
            complexity.move_to(RIGHT * 3.5 + DOWN * 1.5)
            self.play(Write(complexity))
            self.wait(1.5)
        
        self.play(FadeOut(*self.mobjects))

    def real_world_applications(self):
        with self.voiceover(text="Binary trees and especially binary search trees have numerous real-world applications. They are used in databases for indexing, making data retrieval extremely fast. File systems use tree structures to organize directories and files. Compilers use expression trees to parse and evaluate mathematical expressions.") as tracker:
            section_title = Text("Real-World Applications", font_size=36, color=YELLOW)
            section_title.to_edge(UP, buff=1.0)
            self.play(Write(section_title))
            
            # Application 1: Databases
            app1_title = Text("Database Indexing", font_size=28, color=BLUE)
            app1_title.move_to(LEFT * 3.5 + UP * 1.5)
            app1_desc = Text("Fast data retrieval", font_size=20)
            app1_desc.next_to(app1_title, DOWN, buff=0.3)
            
            self.play(Write(app1_title))
            self.play(Write(app1_desc))
            
            # Small BST illustration
            db_tree = VGroup(
                self.create_tree_node("DB", LEFT * 3.5 + UP * 0, BLUE),
                self.create_tree_node("A-M", LEFT * 4.5 + DOWN * 0.8, BLUE),
                self.create_tree_node("N-Z", LEFT * 2.5 + DOWN * 0.8, BLUE)
            )
            db_edges = VGroup(
                Line(db_tree[0].get_bottom(), db_tree[1].get_top(), color=WHITE),
                Line(db_tree[0].get_bottom(), db_tree[2].get_top(), color=WHITE)
            )
            self.play(Create(db_edges), Create(db_tree))
        
        with self.voiceover(text="Binary trees are also used in network routing algorithms to find the shortest path between nodes. Huffman coding, which is used for data compression, builds a binary tree to create optimal prefix codes. Auto-complete features in search engines use tree structures called tries, which are specialized trees for storing strings efficiently.") as tracker:
            # Application 2: File Systems
            app2_title = Text("File Systems", font_size=28, color=GREEN)
            app2_title.move_to(RIGHT * 0 + UP * 1.5)
            app2_desc = Text("Directory structure", font_size=20)
            app2_desc.next_to(app2_title, DOWN, buff=0.3)
            
            self.play(Write(app2_title))
            self.play(Write(app2_desc))
            
            # File tree illustration
            file_tree = VGroup(
                self.create_tree_node("Root", RIGHT * 0 + UP * 0, GREEN),
                self.create_tree_node("Docs", LEFT * 1 + DOWN * 0.8, GREEN),
                self.create_tree_node("Pics", RIGHT * 1 + DOWN * 0.8, GREEN)
            )
            file_edges = VGroup(
                Line(file_tree[0].get_bottom(), file_tree[1].get_top(), color=WHITE),
                Line(file_tree[0].get_bottom(), file_tree[2].get_top(), color=WHITE)
            )
            self.play(Create(file_edges), Create(file_tree))
            
            # Application 3: Expression Evaluation
            app3_title = Text("Expression Trees", font_size=28, color=ORANGE)
            app3_title.move_to(RIGHT * 3.5 + UP * 1.5)
            app3_desc = Text("Math expressions", font_size=20)
            app3_desc.next_to(app3_title, DOWN, buff=0.3)
            
            self.play(Write(app3_title))
            self.play(Write(app3_desc))
            
            # Expression tree
            expr_tree = VGroup(
                self.create_tree_node("+", RIGHT * 3.5 + UP * 0, ORANGE),
                self.create_tree_node("3", RIGHT * 2.5 + DOWN * 0.8, ORANGE),
                self.create_tree_node("×", RIGHT * 4.5 + DOWN * 0.8, ORANGE)
            )
            expr_edges = VGroup(
                Line(expr_tree[0].get_bottom(), expr_tree[1].get_top(), color=WHITE),
                Line(expr_tree[0].get_bottom(), expr_tree[2].get_top(), color=WHITE)
            )
            self.play(Create(expr_edges), Create(expr_tree))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def conclusion(self):
        with self.voiceover(text="We've covered a lot about binary trees today! We learned what binary trees are, how they differ from general trees, and explored the different types of binary trees. We examined three important traversal methods: inorder, preorder, and postorder. We dove deep into binary search trees and saw how their special property enables efficient searching and insertion.") as tracker:
            section_title = Text("Summary & Conclusion", font_size=36, color=YELLOW)
            section_title.to_edge(UP, buff=1.0)
            self.play(Write(section_title))
            
            # Summary points
            summary = VGroup(
                Text("✓ Binary Tree Structure", font_size=26, color=GREEN),
                Text("✓ Tree Traversals (In/Pre/Post)", font_size=26, color=GREEN),
                Text("✓ Binary Search Trees", font_size=26, color=GREEN),
                Text("✓ BST Operations", font_size=26, color=GREEN),
                Text("✓ Real-World Applications", font_size=26, color=GREEN)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            summary.move_to(UP * 0.3)
            
            for point in summary:
                self.play(Write(point), run_time=0.6)
                self.wait(0.3)
        
        with self.voiceover(text="Binary trees are fundamental data structures that you'll encounter throughout your programming journey. Whether you're optimizing database queries, building compilers, or implementing efficient search algorithms, understanding binary trees is essential. Keep practicing these concepts, and you'll master this powerful data structure. Thank you for watching!") as tracker:
            self.wait(1)
            
            # Final message
            thanks = Text("Thank You for Watching!", font_size=36, color=BLUE)
            thanks.move_to(DOWN * 2)
            self.play(Write(thanks))
            
            # Add a small decorative tree
            final_tree = VGroup(
                self.create_tree_node("🌳", ORIGIN + DOWN * 1, GOLD)
            )
            self.play(FadeIn(final_tree), run_time=0.8)
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))


# Run the animation
if __name__ == "__main__":
    scene = BinaryTreeExplanation()
    scene.render()