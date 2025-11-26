from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import numpy as np

class TreeGraphVisualization(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))
        
        # Introduction
        self.show_introduction()
        
        # Basic tree concepts
        self.explain_tree_basics()
        
        # Tree terminology
        self.explain_tree_terminology()
        
        # Binary tree structure
        self.demonstrate_binary_tree()
        
        # Tree traversal methods
        self.explain_tree_traversals()
        
        # Graph introduction
        self.introduce_graphs()
        
        # Graph types
        self.explain_graph_types()
        
        # Graph traversal - BFS
        self.demonstrate_bfs()
        
        # Graph traversal - DFS
        self.demonstrate_dfs()
        
        # Real world applications
        self.show_applications()
        
        # Comparison
        self.compare_trees_and_graphs()
        
        # Conclusion
        self.show_conclusion()

    def show_introduction(self):
        with self.voiceover(text="Welcome to this comprehensive exploration of Trees and Graphs, two of the most fundamental data structures in computer science. These structures are everywhere in the digital world, from file systems on your computer to social networks connecting billions of people. Today, we will dive deep into understanding how they work, how they differ, and why they are so powerful.") as tracker:
            title = Text("Trees and Graphs", font_size=36, color=BLUE, weight=BOLD)
            title.to_edge(UP, buff=1.0)
            
            subtitle = Text("Fundamental Data Structures", font_size=28, color=GRAY)
            subtitle.next_to(title, DOWN, buff=0.4)
            
            self.play(Write(title), run_time=2)
            self.play(FadeIn(subtitle), run_time=1.5)
            
        with self.voiceover(text="Trees and graphs help us represent hierarchical relationships and complex networks. Whether you're organizing data, planning routes on a map, or modeling relationships between entities, understanding these structures is essential for solving real-world problems efficiently.") as tracker:
            # Create simple visual representation
            tree_icon = self.create_simple_tree_icon().scale(0.8)
            tree_icon.move_to(LEFT * 3.5 + DOWN * 0.5)
            tree_label = Text("Trees", font_size=24, color=GREEN)
            tree_label.next_to(tree_icon, DOWN, buff=0.3)
            
            graph_icon = self.create_simple_graph_icon().scale(0.8)
            graph_icon.move_to(RIGHT * 3.5 + DOWN * 0.5)
            graph_label = Text("Graphs", font_size=24, color=ORANGE)
            graph_label.next_to(graph_icon, DOWN, buff=0.3)
            
            self.play(
                Create(tree_icon),
                Write(tree_label),
                Create(graph_icon),
                Write(graph_label),
                run_time=2
            )
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def create_simple_tree_icon(self):
        # Create a simple tree structure
        root = Circle(radius=0.25, color=GREEN, fill_opacity=0.8)
        root.move_to(UP * 1)
        
        child1 = Circle(radius=0.25, color=GREEN, fill_opacity=0.6)
        child1.move_to(LEFT * 0.7 + DOWN * 0.2)
        
        child2 = Circle(radius=0.25, color=GREEN, fill_opacity=0.6)
        child2.move_to(RIGHT * 0.7 + DOWN * 0.2)
        
        leaf1 = Circle(radius=0.25, color=GREEN, fill_opacity=0.4)
        leaf1.move_to(LEFT * 1.2 + DOWN * 1.4)
        
        leaf2 = Circle(radius=0.25, color=GREEN, fill_opacity=0.4)
        leaf2.move_to(LEFT * 0.2 + DOWN * 1.4)
        
        leaf3 = Circle(radius=0.25, color=GREEN, fill_opacity=0.4)
        leaf3.move_to(RIGHT * 0.2 + DOWN * 1.4)
        
        leaf4 = Circle(radius=0.25, color=GREEN, fill_opacity=0.4)
        leaf4.move_to(RIGHT * 1.2 + DOWN * 1.4)
        
        edges = VGroup(
            Line(root.get_center(), child1.get_center(), color=WHITE),
            Line(root.get_center(), child2.get_center(), color=WHITE),
            Line(child1.get_center(), leaf1.get_center(), color=WHITE),
            Line(child1.get_center(), leaf2.get_center(), color=WHITE),
            Line(child2.get_center(), leaf3.get_center(), color=WHITE),
            Line(child2.get_center(), leaf4.get_center(), color=WHITE)
        )
        
        nodes = VGroup(root, child1, child2, leaf1, leaf2, leaf3, leaf4)
        return VGroup(edges, nodes)

    def create_simple_graph_icon(self):
        # Create a simple graph structure
        positions = [
            UP * 1,
            LEFT * 1,
            RIGHT * 1,
            DOWN * 0.5 + LEFT * 0.5,
            DOWN * 0.5 + RIGHT * 0.5
        ]
        
        nodes = VGroup(*[
            Circle(radius=0.25, color=ORANGE, fill_opacity=0.7).move_to(pos)
            for pos in positions
        ])
        
        edges = VGroup(
            Line(positions[0], positions[1], color=WHITE),
            Line(positions[0], positions[2], color=WHITE),
            Line(positions[1], positions[3], color=WHITE),
            Line(positions[2], positions[4], color=WHITE),
            Line(positions[3], positions[4], color=WHITE),
            Line(positions[1], positions[2], color=WHITE)
        )
        
        return VGroup(edges, nodes)

    def explain_tree_basics(self):
        with self.voiceover(text="Let's begin with trees. A tree is a hierarchical data structure consisting of nodes connected by edges. The most important characteristic of a tree is that it has no cycles, meaning you cannot follow the edges and return to a node you've already visited. Every tree has exactly one path between any two nodes.") as tracker:
            title = Text("What is a Tree?", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Create a tree definition
            definition = VGroup(
                Text("A Tree is:", font_size=26, color=WHITE),
                Text("• Connected acyclic graph", font_size=22, color=GRAY),
                Text("• Has N nodes and N-1 edges", font_size=22, color=GRAY),
                Text("• One unique path between nodes", font_size=22, color=GRAY),
                Text("• Hierarchical structure", font_size=22, color=GRAY)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            definition.move_to(LEFT * 3.5 + DOWN * 0.8)
            
            self.play(Write(definition), run_time=3)
            
        with self.voiceover(text="Let me show you a simple tree structure. Notice how we have one node at the top called the root, and all other nodes branch out from it. Each connection represents a parent-child relationship, and no node is connected back to itself or its ancestors, which prevents cycles.") as tracker:
            # Create example tree
            tree = self.create_example_tree()
            tree.move_to(RIGHT * 3 + DOWN * 0.5)
            tree.scale(0.9)
            
            self.play(Create(tree), run_time=2.5)
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def create_example_tree(self):
        # Root node
        root = Circle(radius=0.3, color=YELLOW, fill_opacity=0.8)
        root.move_to(UP * 1.5)
        root_label = Text("A", font_size=20).move_to(root.get_center())
        
        # Level 1 nodes
        node_b = Circle(radius=0.3, color=GREEN, fill_opacity=0.8)
        node_b.move_to(LEFT * 1.2 + UP * 0.2)
        label_b = Text("B", font_size=20).move_to(node_b.get_center())
        
        node_c = Circle(radius=0.3, color=GREEN, fill_opacity=0.8)
        node_c.move_to(RIGHT * 1.2 + UP * 0.2)
        label_c = Text("C", font_size=20).move_to(node_c.get_center())
        
        # Level 2 nodes
        node_d = Circle(radius=0.3, color=BLUE, fill_opacity=0.8)
        node_d.move_to(LEFT * 1.8 + DOWN * 1)
        label_d = Text("D", font_size=20).move_to(node_d.get_center())
        
        node_e = Circle(radius=0.3, color=BLUE, fill_opacity=0.8)
        node_e.move_to(LEFT * 0.6 + DOWN * 1)
        label_e = Text("E", font_size=20).move_to(node_e.get_center())
        
        node_f = Circle(radius=0.3, color=BLUE, fill_opacity=0.8)
        node_f.move_to(RIGHT * 0.6 + DOWN * 1)
        label_f = Text("F", font_size=20).move_to(node_f.get_center())
        
        node_g = Circle(radius=0.3, color=BLUE, fill_opacity=0.8)
        node_g.move_to(RIGHT * 1.8 + DOWN * 1)
        label_g = Text("G", font_size=20).move_to(node_g.get_center())
        
        # Edges
        edges = VGroup(
            Line(root.get_center(), node_b.get_center(), color=WHITE),
            Line(root.get_center(), node_c.get_center(), color=WHITE),
            Line(node_b.get_center(), node_d.get_center(), color=WHITE),
            Line(node_b.get_center(), node_e.get_center(), color=WHITE),
            Line(node_c.get_center(), node_f.get_center(), color=WHITE),
            Line(node_c.get_center(), node_g.get_center(), color=WHITE)
        )
        
        nodes = VGroup(root, node_b, node_c, node_d, node_e, node_f, node_g)
        labels = VGroup(root_label, label_b, label_c, label_d, label_e, label_f, label_g)
        
        return VGroup(edges, nodes, labels)

    def explain_tree_terminology(self):
        with self.voiceover(text="Trees have special terminology that helps us describe their structure precisely. The topmost node is called the root. Nodes with no children are called leaves. The connections between nodes are called edges. The depth of a node is its distance from the root, and the height of the tree is the length of the longest path from root to any leaf.") as tracker:
            title = Text("Tree Terminology", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Create tree
            tree = self.create_labeled_terminology_tree()
            tree.move_to(DOWN * 0.3)
            tree.scale(0.85)
            self.play(Create(tree[0]), Create(tree[1]), run_time=2)
            
        with self.voiceover(text="Let me highlight these important concepts. The yellow node at the top is our root. The blue nodes at the bottom with no children are the leaves. Green nodes in the middle are internal nodes. Each connection is an edge. The parent of a node is the one directly above it, and children are the nodes directly below.") as tracker:
            # Add labels with arrows
            root_arrow = Arrow(start=UP * 2.2 + LEFT * 2.5, end=UP * 1.8 + LEFT * 0.2, color=YELLOW, buff=0.1)
            root_text = Text("Root", font_size=20, color=YELLOW).next_to(root_arrow.get_start(), LEFT, buff=0.1)
            
            leaf_arrow = Arrow(start=DOWN * 2.2 + RIGHT * 2, end=DOWN * 1.5 + RIGHT * 1, color=BLUE, buff=0.1)
            leaf_text = Text("Leaf", font_size=20, color=BLUE).next_to(leaf_arrow.get_start(), RIGHT, buff=0.1)
            
            internal_arrow = Arrow(start=UP * 0.5 + LEFT * 3, end=UP * 0.3 + LEFT * 1.4, color=GREEN, buff=0.1)
            internal_text = Text("Internal", font_size=20, color=GREEN).next_to(internal_arrow.get_start(), LEFT, buff=0.1)
            
            self.play(
                Create(root_arrow), Write(root_text),
                Create(leaf_arrow), Write(leaf_text),
                Create(internal_arrow), Write(internal_text),
                run_time=2.5
            )
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def create_labeled_terminology_tree(self):
        # Root node
        root = Circle(radius=0.35, color=YELLOW, fill_opacity=0.9, stroke_width=3)
        root.move_to(UP * 1.8)
        root_label = Text("1", font_size=22, weight=BOLD).move_to(root.get_center())
        
        # Internal nodes
        node_2 = Circle(radius=0.35, color=GREEN, fill_opacity=0.8, stroke_width=3)
        node_2.move_to(LEFT * 1.5 + UP * 0.5)
        label_2 = Text("2", font_size=22).move_to(node_2.get_center())
        
        node_3 = Circle(radius=0.35, color=GREEN, fill_opacity=0.8, stroke_width=3)
        node_3.move_to(RIGHT * 1.5 + UP * 0.5)
        label_3 = Text("3", font_size=22).move_to(node_3.get_center())
        
        # Leaf nodes
        node_4 = Circle(radius=0.35, color=BLUE, fill_opacity=0.8, stroke_width=3)
        node_4.move_to(LEFT * 2.3 + DOWN * 1)
        label_4 = Text("4", font_size=22).move_to(node_4.get_center())
        
        node_5 = Circle(radius=0.35, color=BLUE, fill_opacity=0.8, stroke_width=3)
        node_5.move_to(LEFT * 0.7 + DOWN * 1)
        label_5 = Text("5", font_size=22).move_to(node_5.get_center())
        
        node_6 = Circle(radius=0.35, color=BLUE, fill_opacity=0.8, stroke_width=3)
        node_6.move_to(RIGHT * 0.7 + DOWN * 1)
        label_6 = Text("6", font_size=22).move_to(node_6.get_center())
        
        node_7 = Circle(radius=0.35, color=BLUE, fill_opacity=0.8, stroke_width=3)
        node_7.move_to(RIGHT * 2.3 + DOWN * 1)
        label_7 = Text("7", font_size=22).move_to(node_7.get_center())
        
        # Edges
        edges = VGroup(
            Line(root.get_center(), node_2.get_center(), color=WHITE, stroke_width=3),
            Line(root.get_center(), node_3.get_center(), color=WHITE, stroke_width=3),
            Line(node_2.get_center(), node_4.get_center(), color=WHITE, stroke_width=3),
            Line(node_2.get_center(), node_5.get_center(), color=WHITE, stroke_width=3),
            Line(node_3.get_center(), node_6.get_center(), color=WHITE, stroke_width=3),
            Line(node_3.get_center(), node_7.get_center(), color=WHITE, stroke_width=3)
        )
        
        nodes = VGroup(root, node_2, node_3, node_4, node_5, node_6, node_7)
        labels = VGroup(root_label, label_2, label_3, label_4, label_5, label_6, label_7)
        
        return VGroup(edges, nodes, labels)

    def demonstrate_binary_tree(self):
        with self.voiceover(text="A special type of tree is the binary tree, where each node has at most two children, conventionally called the left child and the right child. Binary trees are extremely useful in computer science for searching, sorting, and organizing data efficiently. The most famous example is the binary search tree, which keeps data sorted.") as tracker:
            title = Text("Binary Trees", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Show binary tree structure
            binary_tree = self.create_binary_search_tree()
            binary_tree.move_to(DOWN * 0.5)
            self.play(Create(binary_tree), run_time=2.5)
            
        with self.voiceover(text="In a binary search tree, values are organized so that for any node, all values in the left subtree are smaller, and all values in the right subtree are larger. This property makes searching incredibly efficient. Let me show you how we would search for the value fifteen in this tree. We start at the root and compare, going left if our target is smaller, right if larger.") as tracker:
            # Highlight search path for value 15
            search_path = [
                (UP * 1.5, YELLOW),  # 10
                (RIGHT * 1.8 + UP * 0.3, ORANGE),  # 20
                (RIGHT * 1 + DOWN * 1, RED)  # 15
            ]
            
            highlight_circles = VGroup()
            for pos, color in search_path:
                circle = Circle(radius=0.45, color=color, stroke_width=4)
                circle.move_to(pos)
                highlight_circles.add(circle)
                self.play(Create(circle), run_time=0.8)
                self.wait(0.3)
            
            search_text = Text("Search path for 15", font_size=24, color=RED)
            search_text.to_edge(DOWN, buff=0.8)
            self.play(Write(search_text))
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def create_binary_search_tree(self):
        # Values for BST: 10 at root, 5 and 20 as children, etc.
        root_val = 10
        
        root = Circle(radius=0.35, color=YELLOW, fill_opacity=0.8)
        root.move_to(UP * 1.5)
        root_label = Text(str(root_val), font_size=22).move_to(root.get_center())
        
        # Left subtree
        node_5 = Circle(radius=0.35, color=GREEN, fill_opacity=0.8)
        node_5.move_to(LEFT * 1.8 + UP * 0.3)
        label_5 = Text("5", font_size=22).move_to(node_5.get_center())
        
        node_3 = Circle(radius=0.35, color=BLUE, fill_opacity=0.8)
        node_3.move_to(LEFT * 2.6 + DOWN * 1)
        label_3 = Text("3", font_size=22).move_to(node_3.get_center())
        
        node_7 = Circle(radius=0.35, color=BLUE, fill_opacity=0.8)
        node_7.move_to(LEFT * 1 + DOWN * 1)
        label_7 = Text("7", font_size=22).move_to(node_7.get_center())
        
        # Right subtree
        node_20 = Circle(radius=0.35, color=GREEN, fill_opacity=0.8)
        node_20.move_to(RIGHT * 1.8 + UP * 0.3)
        label_20 = Text("20", font_size=22).move_to(node_20.get_center())
        
        node_15 = Circle(radius=0.35, color=BLUE, fill_opacity=0.8)
        node_15.move_to(RIGHT * 1 + DOWN * 1)
        label_15 = Text("15", font_size=22).move_to(node_15.get_center())
        
        node_25 = Circle(radius=0.35, color=BLUE, fill_opacity=0.8)
        node_25.move_to(RIGHT * 2.6 + DOWN * 1)
        label_25 = Text("25", font_size=22).move_to(node_25.get_center())
        
        # Edges
        edges = VGroup(
            Line(root.get_center(), node_5.get_center(), color=WHITE),
            Line(root.get_center(), node_20.get_center(), color=WHITE),
            Line(node_5.get_center(), node_3.get_center(), color=WHITE),
            Line(node_5.get_center(), node_7.get_center(), color=WHITE),
            Line(node_20.get_center(), node_15.get_center(), color=WHITE),
            Line(node_20.get_center(), node_25.get_center(), color=WHITE)
        )
        
        nodes = VGroup(root, node_5, node_20, node_3, node_7, node_15, node_25)
        labels = VGroup(root_label, label_5, label_20, label_3, label_7, label_15, label_25)
        
        return VGroup(edges, nodes, labels)

    def explain_tree_traversals(self):
        with self.voiceover(text="Tree traversal refers to the process of visiting each node in a tree exactly once in a specific order. There are three main types of depth-first traversals: preorder, inorder, and postorder. Each has different applications and produces a different sequence of nodes. Understanding these traversals is crucial for many tree algorithms.") as tracker:
            title = Text("Tree Traversals", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Show the tree we'll traverse
            tree = self.create_traversal_tree()
            tree.move_to(LEFT * 3.5 + DOWN * 0.3)
            tree.scale(0.7)
            self.play(Create(tree), run_time=2)
            
        with self.voiceover(text="Inorder traversal visits the left subtree first, then the current node, then the right subtree. For a binary search tree, this produces values in sorted order. Preorder visits the node first, then left, then right. Postorder visits left, then right, then finally the node itself. Watch as I demonstrate inorder traversal on this tree.") as tracker:
            # Show traversal orders
            traversal_info = VGroup(
                Text("Traversal Types:", font_size=24, color=WHITE),
                Text("Inorder: Left → Node → Right", font_size=18, color=GREEN),
                Text("Preorder: Node → Left → Right", font_size=18, color=YELLOW),
                Text("Postorder: Left → Right → Node", font_size=18, color=ORANGE)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            traversal_info.move_to(RIGHT * 3 + UP * 1)
            
            self.play(Write(traversal_info), run_time=3)
            
            # Demonstrate inorder traversal
            inorder_sequence = Text("Inorder: 3, 5, 7, 10, 15, 20, 25", font_size=20, color=GREEN)
            inorder_sequence.to_edge(DOWN, buff=0.8)
            self.play(Write(inorder_sequence), run_time=2)
            
            # Highlight nodes in inorder sequence
            positions = [
                LEFT * 4.3 + DOWN * 1,  # 3
                LEFT * 3.8 + UP * 0.3,  # 5
                LEFT * 3.2 + DOWN * 1,  # 7
                LEFT * 3.5 + UP * 1.3,  # 10
                LEFT * 2.8 + DOWN * 1,  # 15
                LEFT * 2.3 + UP * 0.3,  # 20
                LEFT * 1.7 + DOWN * 1   # 25
            ]
            
            for pos in positions:
                circle = Circle(radius=0.28, color=GREEN, stroke_width=4)
                circle.move_to(pos)
                self.play(Create(circle), run_time=0.5)
                self.play(FadeOut(circle), run_time=0.3)
            
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def create_traversal_tree(self):
        # Same as BST but smaller
        root = Circle(radius=0.25, color=YELLOW, fill_opacity=0.8)
        root.move_to(UP * 1.5)
        root_label = Text("10", font_size=16).move_to(root.get_center())
        
        node_5 = Circle(radius=0.25, color=GREEN, fill_opacity=0.8)
        node_5.move_to(LEFT * 0.8 + UP * 0.5)
        label_5 = Text("5", font_size=16).move_to(node_5.get_center())
        
        node_20 = Circle(radius=0.25, color=GREEN, fill_opacity=0.8)
        node_20.move_to(RIGHT * 0.8 + UP * 0.5)
        label_20 = Text("20", font_size=16).move_to(node_20.get_center())
        
        node_3 = Circle(radius=0.25, color=BLUE, fill_opacity=0.8)
        node_3.move_to(LEFT * 1.3 + DOWN * 0.5)
        label_3 = Text("3", font_size=16).move_to(node_3.get_center())
        
        node_7 = Circle(radius=0.25, color=BLUE, fill_opacity=0.8)
        node_7.move_to(LEFT * 0.3 + DOWN * 0.5)
        label_7 = Text("7", font_size=16).move_to(node_7.get_center())
        
        node_15 = Circle(radius=0.25, color=BLUE, fill_opacity=0.8)
        node_15.move_to(RIGHT * 0.3 + DOWN * 0.5)
        label_15 = Text("15", font_size=16).move_to(node_15.get_center())
        
        node_25 = Circle(radius=0.25, color=BLUE, fill_opacity=0.8)
        node_25.move_to(RIGHT * 1.3 + DOWN * 0.5)
        label_25 = Text("25", font_size=16).move_to(node_25.get_center())
        
        edges = VGroup(
            Line(root.get_center(), node_5.get_center(), color=WHITE),
            Line(root.get_center(), node_20.get_center(), color=WHITE),
            Line(node_5.get_center(), node_3.get_center(), color=WHITE),
            Line(node_5.get_center(), node_7.get_center(), color=WHITE),
            Line(node_20.get_center(), node_15.get_center(), color=WHITE),
            Line(node_20.get_center(), node_25.get_center(), color=WHITE)
        )
        
        nodes = VGroup(root, node_5, node_20, node_3, node_7, node_15, node_25)
        labels = VGroup(root_label, label_5, label_20, label_3, label_7, label_15, label_25)
        
        return VGroup(edges, nodes, labels)

    def introduce_graphs(self):
        with self.voiceover(text="Now let's move from trees to graphs. While trees are hierarchical and acyclic, graphs are much more general. A graph consists of vertices, also called nodes, and edges that connect them. Unlike trees, graphs can have cycles, multiple paths between nodes, and edges can even have directions and weights. Graphs are perfect for modeling networks and relationships.") as tracker:
            title = Text("Introduction to Graphs", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Show graph definition
            definition = VGroup(
                Text("A Graph consists of:", font_size=26, color=WHITE),
                Text("• Vertices (nodes)", font_size=22, color=GRAY),
                Text("• Edges (connections)", font_size=22, color=GRAY),
                Text("• Can have cycles", font_size=22, color=GRAY),
                Text("• Multiple paths possible", font_size=22, color=GRAY)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            definition.move_to(LEFT * 3.5 + DOWN * 0.6)
            
            self.play(Write(definition), run_time=3)
            
        with self.voiceover(text="Here's a simple undirected graph. Notice how the edges have no direction arrows, meaning the connection works both ways. Also observe the cycle formed by vertices A, B, and C. This is perfectly valid in a graph, though it would never occur in a tree. Graphs can represent social networks, road maps, computer networks, and countless other real-world structures.") as tracker:
            # Create example graph
            graph = self.create_example_graph()
            graph.move_to(RIGHT * 3 + DOWN * 0.3)
            graph.scale(0.85)
            self.play(Create(graph), run_time=2.5)
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def create_example_graph(self):
        # Create vertices
        positions = {
            'A': UP * 1.2,
            'B': LEFT * 1.2 + DOWN * 0.3,
            'C': RIGHT * 1.2 + DOWN * 0.3,
            'D': DOWN * 1.5
        }
        
        vertices = {}
        labels = {}
        
        for name, pos in positions.items():
            vertex = Circle(radius=0.35, color=ORANGE, fill_opacity=0.8)
            vertex.move_to(pos)
            vertices[name] = vertex
            
            label = Text(name, font_size=22, weight=BOLD)
            label.move_to(pos)
            labels[name] = label
        
        # Create edges
        edges = VGroup(
            Line(positions['A'], positions['B'], color=WHITE, stroke_width=3),
            Line(positions['A'], positions['C'], color=WHITE, stroke_width=3),
            Line(positions['B'], positions['C'], color=WHITE, stroke_width=3),
            Line(positions['B'], positions['D'], color=WHITE, stroke_width=3),
            Line(positions['C'], positions['D'], color=WHITE, stroke_width=3)
        )
        
        vertex_group = VGroup(*vertices.values())
        label_group = VGroup(*labels.values())
        
        return VGroup(edges, vertex_group, label_group)

    def explain_graph_types(self):
        with self.voiceover(text="Graphs come in many varieties. An undirected graph has edges with no direction, like friendships on social media where the relationship is mutual. A directed graph, or digraph, has edges with specific directions, like following someone on Twitter where the relationship is one-way. Edges can also have weights representing costs, distances, or capacities.") as tracker:
            title = Text("Types of Graphs", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Undirected graph
            undirected_label = Text("Undirected Graph", font_size=22, color=GREEN)
            undirected_label.move_to(LEFT * 3.5 + UP * 0.8)
            
            undirected = self.create_undirected_graph_example()
            undirected.move_to(LEFT * 3.5 + DOWN * 0.8)
            undirected.scale(0.65)
            
            self.play(Write(undirected_label))
            self.play(Create(undirected), run_time=2)
            
        with self.voiceover(text="On the left, we have an undirected graph where all connections are bidirectional. On the right, see the directed graph with arrows showing the direction of each edge. Directed graphs can model one-way streets, web page links, or task dependencies. Notice how in the directed graph, you can go from A to B, but not necessarily from B back to A unless there's an arrow pointing that way.") as tracker:
            # Directed graph
            directed_label = Text("Directed Graph", font_size=22, color=YELLOW)
            directed_label.move_to(RIGHT * 3.5 + UP * 0.8)
            
            directed = self.create_directed_graph_example()
            directed.move_to(RIGHT * 3.5 + DOWN * 0.8)
            directed.scale(0.65)
            
            self.play(Write(directed_label))
            self.play(Create(directed), run_time=2)
            self.wait(1.5)
        
        self.play(FadeOut(*self.mobjects))

    def create_undirected_graph_example(self):
        pos_a = UP * 1
        pos_b = LEFT * 1 + DOWN * 0.5
        pos_c = RIGHT * 1 + DOWN * 0.5
        
        vertex_a = Circle(radius=0.3, color=GREEN, fill_opacity=0.8)
        vertex_a.move_to(pos_a)
        label_a = Text("A", font_size=18).move_to(pos_a)
        
        vertex_b = Circle(radius=0.3, color=GREEN, fill_opacity=0.8)
        vertex_b.move_to(pos_b)
        label_b = Text("B", font_size=18).move_to(pos_b)
        
        vertex_c = Circle(radius=0.3, color=GREEN, fill_opacity=0.8)
        vertex_c.move_to(pos_c)
        label_c = Text("C", font_size=18).move_to(pos_c)
        
        edges = VGroup(
            Line(pos_a, pos_b, color=WHITE, stroke_width=2),
            Line(pos_a, pos_c, color=WHITE, stroke_width=2),
            Line(pos_b, pos_c, color=WHITE, stroke_width=2)
        )
        
        vertices = VGroup(vertex_a, vertex_b, vertex_c)
        labels = VGroup(label_a, label_b, label_c)
        
        return VGroup(edges, vertices, labels)

    def create_directed_graph_example(self):
        pos_a = UP * 1
        pos_b = LEFT * 1 + DOWN * 0.5
        pos_c = RIGHT * 1 + DOWN * 0.5
        
        vertex_a = Circle(radius=0.3, color=YELLOW, fill_opacity=0.8)
        vertex_a.move_to(pos_a)
        label_a = Text("A", font_size=18).move_to(pos_a)
        
        vertex_b = Circle(radius=0.3, color=YELLOW, fill_opacity=0.8)
        vertex_b.move_to(pos_b)
        label_b = Text("B", font_size=18).move_to(pos_b)
        
        vertex_c = Circle(radius=0.3, color=YELLOW, fill_opacity=0.8)
        vertex_c.move_to(pos_c)
        label_c = Text("C", font_size=18).move_to(pos_c)
        
        edges = VGroup(
            Arrow(pos_a, pos_b, color=WHITE, stroke_width=2, buff=0.3, max_tip_length_to_length_ratio=0.15),
            Arrow(pos_b, pos_c, color=WHITE, stroke_width=2, buff=0.3, max_tip_length_to_length_ratio=0.15),
            Arrow(pos_c, pos_a, color=WHITE, stroke_width=2, buff=0.3, max_tip_length_to_length_ratio=0.15)
        )
        
        vertices = VGroup(vertex_a, vertex_b, vertex_c)
        labels = VGroup(label_a, label_b, label_c)
        
        return VGroup(edges, vertices, labels)

    def demonstrate_bfs(self):
        with self.voiceover(text="Let's explore graph traversal algorithms, starting with Breadth-First Search, or BFS. This algorithm explores the graph level by level, visiting all neighbors of a node before moving to their neighbors. BFS uses a queue data structure and is perfect for finding the shortest path in an unweighted graph. It's widely used in social network analysis to find degrees of separation.") as tracker:
            title = Text("Breadth-First Search (BFS)", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Create graph for BFS
            graph = self.create_bfs_graph()
            graph.move_to(LEFT * 3.5 + DOWN * 0.3)
            graph.scale(0.75)
            self.play(Create(graph), run_time=2)
            
        with self.voiceover(text="Watch carefully as BFS explores this graph starting from node A. First, we visit A and add it to our queue. Then we visit all of A's neighbors, which are B and C. We add them to the queue. Next, we process B, visiting its unvisited neighbor D. Then we process C, and finally D. Notice how we explore level by level, ensuring we find the shortest path.") as tracker:
            # Show BFS algorithm steps
            steps = VGroup(
                Text("BFS Steps:", font_size=24, color=WHITE, weight=BOLD),
                Text("1. Start at source node", font_size=18, color=GRAY),
                Text("2. Visit all neighbors", font_size=18, color=GRAY),
                Text("3. Add to queue", font_size=18, color=GRAY),
                Text("4. Process next in queue", font_size=18, color=GRAY),
                Text("5. Repeat until done", font_size=18, color=GRAY)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            steps.move_to(RIGHT * 3.2 + UP * 0.5)
            self.play(Write(steps), run_time=3)
            
            # Show traversal order
            order_text = Text("Order: A → B → C → D → E", font_size=22, color=GREEN)
            order_text.to_edge(DOWN, buff=0.8)
            self.play(Write(order_text))
            
            # Animate BFS traversal
            bfs_positions = [
                LEFT * 4.25 + UP * 0.8,   # A
                LEFT * 4.8 + DOWN * 0.8,  # B
                LEFT * 3.7 + DOWN * 0.8,  # C
                LEFT * 4.8 + DOWN * 2,    # D
                LEFT * 3.7 + DOWN * 2     # E
            ]
            
            for i, pos in enumerate(bfs_positions):
                circle = Circle(radius=0.32, color=GREEN, stroke_width=4)
                circle.move_to(pos)
                self.play(Create(circle), run_time=0.6)
                self.wait(0.4)
        
        self.play(FadeOut(*self.mobjects))

    def create_bfs_graph(self):
        # Create a simple graph for BFS demonstration
        pos_a = UP * 1.2
        pos_b = LEFT * 0.8 + DOWN * 0.3
        pos_c = RIGHT * 0.8 + DOWN * 0.3
        pos_d = LEFT * 0.8 + DOWN * 1.5
        pos_e = RIGHT * 0.8 + DOWN * 1.5
        
        vertices = {}
        labels = {}
        positions = {'A': pos_a, 'B': pos_b, 'C': pos_c, 'D': pos_d, 'E': pos_e}
        
        for name, pos in positions.items():
            vertex = Circle(radius=0.28, color=ORANGE, fill_opacity=0.8)
            vertex.move_to(pos)
            vertices[name] = vertex
            
            label = Text(name, font_size=18)
            label.move_to(pos)
            labels[name] = label
        
        edges = VGroup(
            Line(pos_a, pos_b, color=WHITE, stroke_width=2),
            Line(pos_a, pos_c, color=WHITE, stroke_width=2),
            Line(pos_b, pos_d, color=WHITE, stroke_width=2),
            Line(pos_c, pos_e, color=WHITE, stroke_width=2),
            Line(pos_d, pos_e, color=WHITE, stroke_width=2)
        )
        
        vertex_group = VGroup(*vertices.values())
        label_group = VGroup(*labels.values())
        
        return VGroup(edges, vertex_group, label_group)

    def demonstrate_dfs(self):
        with self.voiceover(text="Now let's look at Depth-First Search, or DFS, which takes a completely different approach. Instead of exploring level by level, DFS goes as deep as possible along each branch before backtracking. It uses a stack, either explicitly or through recursion. DFS is excellent for detecting cycles, finding connected components, and solving maze problems.") as tracker:
            title = Text("Depth-First Search (DFS)", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Create same graph for DFS
            graph = self.create_bfs_graph()
            graph.move_to(LEFT * 3.5 + DOWN * 0.3)
            graph.scale(0.75)
            self.play(Create(graph), run_time=2)
            
        with self.voiceover(text="Starting from node A with DFS, we immediately go deep. We visit A, then choose one neighbor, say B. From B we go to D. When D has no unvisited neighbors, we backtrack to B, then to A, then explore C, and finally E. Notice the difference: BFS went A, B, C, D, E in layers, but DFS goes A, B, D, then backtracks to explore C and E. The order depends on which neighbor we choose first.") as tracker:
            # Show DFS algorithm steps
            steps = VGroup(
                Text("DFS Steps:", font_size=24, color=WHITE, weight=BOLD),
                Text("1. Start at source node", font_size=18, color=GRAY),
                Text("2. Go deep into one path", font_size=18, color=GRAY),
                Text("3. Use stack/recursion", font_size=18, color=GRAY),
                Text("4. Backtrack when stuck", font_size=18, color=GRAY),
                Text("5. Explore next path", font_size=18, color=GRAY)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            steps.move_to(RIGHT * 3.2 + UP * 0.5)
            self.play(Write(steps), run_time=3)
            
            # Show traversal order
            order_text = Text("Order: A → B → D → C → E", font_size=22, color=PURPLE)
            order_text.to_edge(DOWN, buff=0.8)
            self.play(Write(order_text))
            
            # Animate DFS traversal with different color
            dfs_order = [
                LEFT * 4.25 + UP * 0.8,   # A
                LEFT * 4.8 + DOWN * 0.8,  # B
                LEFT * 4.8 + DOWN * 2,    # D
                LEFT * 3.7 + DOWN * 0.8,  # C
                LEFT * 3.7 + DOWN * 2     # E
            ]
            
            for i, pos in enumerate(dfs_order):
                circle = Circle(radius=0.32, color=PURPLE, stroke_width=4)
                circle.move_to(pos)
                self.play(Create(circle), run_time=0.6)
                self.wait(0.4)
        
        self.play(FadeOut(*self.mobjects))

    def show_applications(self):
        with self.voiceover(text="Trees and graphs have countless real-world applications. Trees are used in file systems where folders contain subfolders in a hierarchy. Database indexing uses B-trees for fast lookups. Decision trees help in machine learning for classification. Abstract syntax trees represent the structure of programming code. Every time you use autocomplete, you're probably querying a tree structure called a trie.") as tracker:
            title = Text("Real-World Applications", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Tree applications
            tree_apps = VGroup(
                Text("Tree Applications:", font_size=26, color=GREEN, weight=BOLD),
                Text("• File systems", font_size=20, color=GRAY),
                Text("• Database indexing", font_size=20, color=GRAY),
                Text("• Decision trees (ML)", font_size=20, color=GRAY),
                Text("• DOM in web browsers", font_size=20, color=GRAY),
                Text("• Expression parsing", font_size=20, color=GRAY)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            tree_apps.move_to(LEFT * 3.5 + DOWN * 0.5)
            
            self.play(Write(tree_apps), run_time=3)
            
        with self.voiceover(text="Graphs are equally powerful. Social networks like Facebook use graphs where people are nodes and friendships are edges. GPS navigation systems use weighted graphs where intersections are nodes, roads are edges, and weights represent distances or travel times. The internet itself is a massive graph of interconnected computers. Google's PageRank algorithm, which revolutionized web search, is fundamentally a graph algorithm analyzing links between web pages.") as tracker:
            # Graph applications
            graph_apps = VGroup(
                Text("Graph Applications:", font_size=26, color=ORANGE, weight=BOLD),
                Text("• Social networks", font_size=20, color=GRAY),
                Text("• GPS and routing", font_size=20, color=GRAY),
                Text("• Network topology", font_size=20, color=GRAY),
                Text("• Recommendation systems", font_size=20, color=GRAY),
                Text("• Circuit design", font_size=20, color=GRAY)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            graph_apps.move_to(RIGHT * 3.5 + DOWN * 0.5)
            
            self.play(Write(graph_apps), run_time=3)
            self.wait(1.5)
        
        self.play(FadeOut(*self.mobjects))

    def compare_trees_and_graphs(self):
        with self.voiceover(text="Let's directly compare trees and graphs to solidify our understanding. A tree is actually a special type of graph with specific constraints. Every tree is a graph, but not every graph is a tree. Trees must be connected, acyclic, and have exactly N minus one edges for N nodes. These restrictions make trees simpler to work with but less flexible than general graphs.") as tracker:
            title = Text("Trees vs Graphs Comparison", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Create comparison table
            tree_col = VGroup(
                Text("TREES", font_size=28, color=GREEN, weight=BOLD),
                Text("Hierarchical", font_size=20, color=GRAY),
                Text("No cycles", font_size=20, color=GRAY),
                Text("One path between nodes", font_size=20, color=GRAY),
                Text("N-1 edges for N nodes", font_size=20, color=GRAY),
                Text("Must be connected", font_size=20, color=GRAY),
                Text("Parent-child relations", font_size=20, color=GRAY)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            tree_col.move_to(LEFT * 3.5 + DOWN * 0.3)
            
            self.play(Write(tree_col), run_time=3)
            
        with self.voiceover(text="Graphs, on the other hand, are much more general and flexible. They can have cycles, allowing you to return to where you started. Multiple paths can exist between any two nodes. Graphs can be disconnected, with separate components that don't connect to each other. The number of edges can vary widely. This flexibility makes graphs suitable for modeling complex, interconnected systems where relationships aren't strictly hierarchical.") as tracker:
            graph_col = VGroup(
                Text("GRAPHS", font_size=28, color=ORANGE, weight=BOLD),
                Text("Network structure", font_size=20, color=GRAY),
                Text("Cycles allowed", font_size=20, color=GRAY),
                Text("Multiple paths possible", font_size=20, color=GRAY),
                Text("Variable edge count", font_size=20, color=GRAY),
                Text("Can be disconnected", font_size=20, color=GRAY),
                Text("Any relationship type", font_size=20, color=GRAY)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            graph_col.move_to(RIGHT * 3.5 + DOWN * 0.3)
            
            self.play(Write(graph_col), run_time=3)
            
            # Add dividing line
            divider = Line(UP * 2.5, DOWN * 2.5, color=WHITE, stroke_width=2)
            divider.move_to(ORIGIN)
            self.play(Create(divider))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def show_conclusion(self):
        with self.voiceover(text="We've covered a tremendous amount of ground today. Trees provide elegant hierarchical organization with their parent-child relationships and guarantee of no cycles. They excel in scenarios requiring fast search, sorted data, and clear hierarchy. Graphs offer ultimate flexibility in modeling any kind of relationship or network, handling cycles and complex interconnections with ease.") as tracker:
            title = Text("Conclusion", font_size=36, color=BLUE, weight=BOLD)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title), run_time=1.5)
            
            # Key takeaways
            takeaways = VGroup(
                Text("Key Takeaways:", font_size=28, color=WHITE, weight=BOLD),
                Text("✓ Trees are hierarchical and acyclic", font_size=22, color=GREEN),
                Text("✓ Graphs are flexible and can have cycles", font_size=22, color=ORANGE),
                Text("✓ BFS explores level by level", font_size=22, color=BLUE),
                Text("✓ DFS explores depth first", font_size=22, color=PURPLE),
                Text("✓ Both are essential in CS", font_size=22, color=YELLOW)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            takeaways.move_to(DOWN * 0.5)
            
            self.play(Write(takeaways), run_time=4)
            self.wait(1.5)
        
        with self.voiceover(text="Understanding these data structures deeply opens doors to solving complex computational problems efficiently. From organizing files to finding the shortest route, from parsing code to analyzing social connections, trees and graphs are the foundation of modern computer science. Thank you for joining me on this journey through trees and graphs. Keep exploring, keep learning!") as tracker:
            self.wait(3)
        
        self.play(FadeOut(*self.mobjects))
        
        # Final thank you
        with self.voiceover(text="Until next time, happy coding!") as tracker:
            thanks = Text("Thank You!", font_size=36, color=BLUE, weight=BOLD)
            thanks.move_to(ORIGIN)
            self.play(Write(thanks), run_time=2)
            self.wait(2)
        
        self.play(FadeOut(thanks))

# Instructions to run:
# Save this file as tree_graph_visualization.py
# Run: manim -pql tree_graph_visualization.py TreeGraphVisualization
# For high quality: manim -pqh tree_graph_visualization.py TreeGraphVisualization