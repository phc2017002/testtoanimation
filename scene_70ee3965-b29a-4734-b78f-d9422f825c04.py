from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class DoublyLinkedListExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))
        
        # Introduction
        self.introduction()
        
        # Historical context
        self.historical_context()
        
        # Structure explanation
        self.structure_explanation()
        
        # Node structure detailed
        self.node_structure_detailed()
        
        # Basic operations - insertion
        self.insertion_operations()
        
        # Basic operations - deletion
        self.deletion_operations()
        
        # Traversal operations
        self.traversal_operations()
        
        # Comparison with singly linked list
        self.comparison_with_singly()
        
        # Time complexity analysis
        self.time_complexity_analysis()
        
        # Real-world applications
        self.real_world_applications()
        
        # Memory representation
        self.memory_representation()
        
        # Conclusion
        self.conclusion()

    def introduction(self):
        with self.voiceover(text="Welcome to this comprehensive explanation of Doubly Linked Lists, one of the most fundamental data structures in computer science. A doubly linked list is a sophisticated linear data structure where each element contains not just data, but also two pointers, allowing bidirectional traversal through the list. This makes it incredibly powerful for many real-world applications.") as tracker:
            title = Text("Doubly Linked Lists", font_size=36, color=BLUE, weight=BOLD)
            title.to_edge(UP, buff=1.0)
            subtitle = Text("A Bidirectional Data Structure", font_size=24, color=YELLOW)
            subtitle.next_to(title, DOWN, buff=0.4)
            
            self.play(Write(title), run_time=2)
            self.play(FadeIn(subtitle), run_time=1.5)
            
        with self.voiceover(text="Unlike arrays which have fixed size and contiguous memory allocation, doubly linked lists provide dynamic memory allocation with the added benefit of traversing in both forward and backward directions. This bidirectional capability makes them superior to singly linked lists for certain operations, though they do require more memory per node.") as tracker:
            features = VGroup(
                Text("✓ Dynamic Size", font_size=24, color=GREEN),
                Text("✓ Bidirectional Traversal", font_size=24, color=GREEN),
                Text("✓ Efficient Insertion/Deletion", font_size=24, color=GREEN),
                Text("✓ Flexible Memory Usage", font_size=24, color=GREEN)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            features.move_to(ORIGIN)
            
            for feature in features:
                self.play(FadeIn(feature), run_time=0.8)
        
        self.play(FadeOut(*self.mobjects))

    def historical_context(self):
        with self.voiceover(text="The concept of linked lists emerged in the nineteen fifties with the development of early programming languages. Doubly linked lists were introduced to overcome the limitation of singly linked lists, which could only be traversed in one direction. This innovation was crucial for implementing complex data structures like deques and certain types of caches.") as tracker:
            timeline_title = Text("Evolution of Linked Lists", font_size=32, color=BLUE)
            timeline_title.to_edge(UP, buff=1.0)
            self.play(Write(timeline_title))
            
            timeline = VGroup(
                Text("1950s: Singly Linked Lists", font_size=22, color=YELLOW),
                Text("1960s: Doubly Linked Lists", font_size=22, color=GREEN),
                Text("1970s: Circular Variants", font_size=22, color=ORANGE),
                Text("Modern: Optimized Implementations", font_size=22, color=RED)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
            timeline.next_to(timeline_title, DOWN, buff=1.2)
            
            for item in timeline:
                self.play(FadeIn(item), run_time=1)
                
        with self.voiceover(text="The doubly linked list became particularly important in operating systems for process scheduling, memory management, and maintaining browser history. The ability to move backward through the list without having to traverse from the beginning revolutionized many algorithms and made certain operations significantly more efficient.") as tracker:
            applications = VGroup(
                Text("→ Operating System Schedulers", font_size=20, color=TEAL),
                Text("→ Browser Navigation History", font_size=20, color=TEAL),
                Text("→ Music Player Playlists", font_size=20, color=TEAL),
                Text("→ Undo/Redo Functionality", font_size=20, color=TEAL)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            applications.next_to(timeline, DOWN, buff=0.8)
            
            self.play(FadeIn(applications), run_time=2)
        
        self.play(FadeOut(*self.mobjects))

    def structure_explanation(self):
        with self.voiceover(text="Let us now visualize the structure of a doubly linked list. Each node in the list contains three main components: the data field which stores the actual value, a previous pointer which points to the previous node in the sequence, and a next pointer which points to the following node. The first node's previous pointer is null, and the last node's next pointer is also null.") as tracker:
            structure_title = Text("Doubly Linked List Structure", font_size=32, color=BLUE)
            structure_title.to_edge(UP, buff=1.0)
            self.play(Write(structure_title))
            
            # Create three nodes
            node1 = self.create_node("10", ORANGE)
            node2 = self.create_node("20", GREEN)
            node3 = self.create_node("30", PURPLE)
            
            nodes = VGroup(node1, node2, node3).arrange(RIGHT, buff=1.5)
            nodes.move_to(ORIGIN)
            
            self.play(FadeIn(node1), run_time=1)
            self.play(FadeIn(node2), run_time=1)
            self.play(FadeIn(node3), run_time=1)
            
        with self.voiceover(text="Notice how the arrows flow in both directions. The forward arrows, shown in blue, point from left to right, allowing us to traverse the list from head to tail. The backward arrows, shown in red, point from right to left, enabling reverse traversal from tail to head. This bidirectional linking is what makes doubly linked lists so versatile and powerful.") as tracker:
            # Add forward arrows
            forward1 = Arrow(node1.get_right() + RIGHT*0.1, node2.get_left() + LEFT*0.1, 
                           color=BLUE, buff=0.1, stroke_width=4)
            forward2 = Arrow(node2.get_right() + RIGHT*0.1, node3.get_left() + LEFT*0.1, 
                           color=BLUE, buff=0.1, stroke_width=4)
            
            self.play(Create(forward1), Create(forward2), run_time=2)
            
            # Add backward arrows
            backward1 = Arrow(node2.get_left() + LEFT*0.1 + DOWN*0.3, 
                            node1.get_right() + RIGHT*0.1 + DOWN*0.3,
                            color=RED, buff=0.1, stroke_width=4)
            backward2 = Arrow(node3.get_left() + LEFT*0.1 + DOWN*0.3, 
                            node2.get_right() + RIGHT*0.1 + DOWN*0.3,
                            color=RED, buff=0.1, stroke_width=4)
            
            self.play(Create(backward1), Create(backward2), run_time=2)
            
            # Add labels
            forward_label = Text("Next pointers", font_size=18, color=BLUE)
            forward_label.next_to(nodes, UP, buff=0.8)
            backward_label = Text("Previous pointers", font_size=18, color=RED)
            backward_label.next_to(nodes, DOWN, buff=1.2)
            
            self.play(Write(forward_label), Write(backward_label))
        
        self.play(FadeOut(*self.mobjects))

    def create_node(self, data, color):
        """Helper function to create a node visualization"""
        box = Rectangle(width=1.5, height=1.0, color=color, stroke_width=3)
        data_text = Text(data, font_size=28, color=WHITE)
        data_text.move_to(box.get_center())
        
        prev_box = Rectangle(width=0.4, height=0.4, color=RED, stroke_width=2)
        prev_box.move_to(box.get_left() + RIGHT*0.25)
        
        next_box = Rectangle(width=0.4, height=0.4, color=BLUE, stroke_width=2)
        next_box.move_to(box.get_right() + LEFT*0.25)
        
        return VGroup(box, data_text, prev_box, next_box)

    def node_structure_detailed(self):
        with self.voiceover(text="Let's examine a single node in greater detail to understand its internal structure. In most programming languages, a node is implemented as a class or structure containing three fields. The data field can hold any type of value, whether it's an integer, string, or even a complex object. The previous pointer stores the memory address of the preceding node, while the next pointer stores the address of the following node.") as tracker:
            detail_title = Text("Node Structure in Detail", font_size=32, color=BLUE)
            detail_title.to_edge(UP, buff=1.0)
            self.play(Write(detail_title))
            
            # Create detailed node diagram
            node_box = Rectangle(width=4, height=2.5, color=YELLOW, stroke_width=3)
            node_box.move_to(ORIGIN)
            
            # Labels for each section
            prev_label = Text("prev", font_size=20, color=RED)
            prev_label.move_to(node_box.get_left() + RIGHT*0.7 + UP*0.8)
            
            data_label = Text("data", font_size=20, color=WHITE)
            data_label.move_to(node_box.get_center() + UP*0.8)
            
            next_label = Text("next", font_size=20, color=BLUE)
            next_label.move_to(node_box.get_right() + LEFT*0.7 + UP*0.8)
            
            # Dividing lines
            line1 = Line(node_box.get_top() + DOWN*0.6, node_box.get_bottom() + UP*0.1, color=WHITE)
            line1.move_to(node_box.get_left() + RIGHT*1.33)
            line2 = Line(node_box.get_top() + DOWN*0.6, node_box.get_bottom() + UP*0.1, color=WHITE)
            line2.move_to(node_box.get_right() + LEFT*1.33)
            
            self.play(Create(node_box), run_time=1.5)
            self.play(Create(line1), Create(line2), run_time=1)
            self.play(Write(prev_label), Write(data_label), Write(next_label), run_time=1.5)
            
        with self.voiceover(text="Here is how we would define this structure in code. We create a Node class with three attributes: previous, which is a reference to another Node object, data which holds our value, and next, which is also a reference to a Node object. When we create a new node, we typically initialize the previous and next pointers to null, indicating that the node is not yet connected to any other nodes in the list.") as tracker:
            code = Code(
                code="""class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None
        
# Creating a new node
new_node = Node(42)""",
                language="python",
                font_size=18,
                background="window",
                style="monokai"
            )
            code.scale(0.7)
            code.next_to(node_box, DOWN, buff=0.6)
            
            self.play(FadeIn(code), run_time=2)
        
        self.play(FadeOut(*self.mobjects))

    def insertion_operations(self):
        with self.voiceover(text="Insertion is one of the fundamental operations in a doubly linked list. There are several types of insertions: at the beginning, at the end, or at a specific position. Let's start with insertion at the beginning, which is one of the most efficient operations. We create a new node, set its next pointer to the current head, update the old head's previous pointer to point to our new node, and finally update the head pointer to our new node.") as tracker:
            insert_title = Text("Insertion Operations", font_size=32, color=BLUE)
            insert_title.to_edge(UP, buff=1.0)
            self.play(Write(insert_title))
            
            # Initial list
            node1 = self.create_node("20", GREEN)
            node2 = self.create_node("30", PURPLE)
            
            nodes = VGroup(node1, node2).arrange(RIGHT, buff=1.5)
            nodes.move_to(DOWN * 0.5)
            
            arrow1 = Arrow(node1.get_right() + RIGHT*0.1, node2.get_left() + LEFT*0.1,
                          color=BLUE, buff=0.1, stroke_width=4)
            arrow2 = Arrow(node2.get_left() + LEFT*0.1 + DOWN*0.3,
                          node1.get_right() + RIGHT*0.1 + DOWN*0.3,
                          color=RED, buff=0.1, stroke_width=4)
            
            head_label = Text("HEAD", font_size=20, color=YELLOW)
            head_label.next_to(node1, UP, buff=0.5)
            head_arrow = Arrow(head_label.get_bottom(), node1.get_top(), color=YELLOW, buff=0.1)
            
            self.play(FadeIn(nodes), Create(arrow1), Create(arrow2))
            self.play(Write(head_label), Create(head_arrow))
            
        with self.voiceover(text="Now we insert a new node with value ten at the beginning. Watch carefully as we create the new node above the current list. We then connect its next pointer to node twenty, update node twenty's previous pointer to point back to our new node ten, and finally move the head pointer to point to this new first node. This operation takes constant time, making it very efficient.") as tracker:
            # New node to insert
            new_node = self.create_node("10", ORANGE)
            new_node.move_to(UP * 1.5 + LEFT * 3)
            
            self.play(FadeIn(new_node), run_time=1.5)
            
            # Step 1: new_node.next = head
            new_arrow = Arrow(new_node.get_right() + RIGHT*0.1 + DOWN*0.5,
                             node1.get_left() + LEFT*0.1 + UP*0.5,
                             color=BLUE, buff=0.1, stroke_width=4)
            step1 = Text("Step 1: new_node.next = head", font_size=18, color=YELLOW)
            step1.to_edge(DOWN, buff=0.8)
            
            self.play(Create(new_arrow), Write(step1), run_time=2)
            self.wait(0.5)
            self.play(FadeOut(step1))
            
            # Step 2: head.prev = new_node
            back_arrow = Arrow(node1.get_left() + LEFT*0.1 + DOWN*0.8,
                              new_node.get_right() + RIGHT*0.1 + DOWN*0.8,
                              color=RED, buff=0.1, stroke_width=4)
            step2 = Text("Step 2: head.prev = new_node", font_size=18, color=YELLOW)
            step2.to_edge(DOWN, buff=0.8)
            
            self.play(Create(back_arrow), Write(step2), run_time=2)
            self.wait(0.5)
            self.play(FadeOut(step2))
            
            # Step 3: head = new_node
            step3 = Text("Step 3: head = new_node", font_size=18, color=YELLOW)
            step3.to_edge(DOWN, buff=0.8)
            
            new_head_arrow = Arrow(head_label.get_bottom(), new_node.get_top(), 
                                  color=YELLOW, buff=0.1)
            
            self.play(
                Transform(head_arrow, new_head_arrow),
                Write(step3),
                run_time=2
            )
        
        self.play(FadeOut(*self.mobjects))

    def deletion_operations(self):
        with self.voiceover(text="Deletion is another critical operation in doubly linked lists. The bidirectional nature of these lists makes deletion particularly elegant compared to singly linked lists. We can delete nodes from the beginning, from the end, or from any specific position. The key advantage is that we can directly access the previous node without traversing the entire list, which makes deletion much more efficient.") as tracker:
            delete_title = Text("Deletion Operations", font_size=32, color=BLUE)
            delete_title.to_edge(UP, buff=1.0)
            self.play(Write(delete_title))
            
            # Create list with three nodes
            node1 = self.create_node("10", ORANGE)
            node2 = self.create_node("20", GREEN)
            node3 = self.create_node("30", PURPLE)
            
            nodes = VGroup(node1, node2, node3).arrange(RIGHT, buff=1.5)
            nodes.move_to(ORIGIN)
            
            # Forward arrows
            f_arrow1 = Arrow(node1.get_right() + RIGHT*0.1, node2.get_left() + LEFT*0.1,
                            color=BLUE, buff=0.1, stroke_width=4)
            f_arrow2 = Arrow(node2.get_right() + RIGHT*0.1, node3.get_left() + LEFT*0.1,
                            color=BLUE, buff=0.1, stroke_width=4)
            
            # Backward arrows
            b_arrow1 = Arrow(node2.get_left() + LEFT*0.1 + DOWN*0.3,
                            node1.get_right() + RIGHT*0.1 + DOWN*0.3,
                            color=RED, buff=0.1, stroke_width=4)
            b_arrow2 = Arrow(node3.get_left() + LEFT*0.1 + DOWN*0.3,
                            node2.get_right() + RIGHT*0.1 + DOWN*0.3,
                            color=RED, buff=0.1, stroke_width=4)
            
            self.play(FadeIn(nodes))
            self.play(Create(f_arrow1), Create(f_arrow2), Create(b_arrow1), Create(b_arrow2))
            
        with self.voiceover(text="Let's delete the middle node containing value twenty. First, we identify the node to delete. Then we update the previous node's next pointer to skip over the node being deleted and point directly to the following node. Similarly, we update the following node's previous pointer to point back to the node before the one being deleted. Finally, we can safely remove the middle node. Notice how the list maintains its integrity with both forward and backward connections intact.") as tracker:
            # Highlight node to delete
            highlight = SurroundingRectangle(node2, color=RED, buff=0.15, stroke_width=4)
            label = Text("Delete this node", font_size=18, color=RED)
            label.next_to(node2, UP, buff=0.6)
            
            self.play(Create(highlight), Write(label), run_time=1.5)
            self.wait(1)
            self.play(FadeOut(label))
            
            # New forward arrow
            new_f_arrow = Arrow(node1.get_right() + RIGHT*0.1 + UP*0.5,
                               node3.get_left() + LEFT*0.1 + UP*0.5,
                               color=GREEN, buff=0.1, stroke_width=5)
            
            # New backward arrow
            new_b_arrow = Arrow(node3.get_left() + LEFT*0.1 + DOWN*0.8,
                               node1.get_right() + RIGHT*0.1 + DOWN*0.8,
                               color=GREEN, buff=0.1, stroke_width=5)
            
            step1 = Text("Reconnecting adjacent nodes", font_size=18, color=YELLOW)
            step1.to_edge(DOWN, buff=0.8)
            
            self.play(
                Create(new_f_arrow),
                Create(new_b_arrow),
                Write(step1),
                run_time=2
            )
            self.wait(1)
            
            # Remove middle node
            step2 = Text("Removing deleted node", font_size=18, color=YELLOW)
            step2.to_edge(DOWN, buff=0.8)
            
            self.play(
                FadeOut(node2),
                FadeOut(f_arrow1),
                FadeOut(f_arrow2),
                FadeOut(b_arrow1),
                FadeOut(b_arrow2),
                FadeOut(highlight),
                Transform(step1, step2),
                run_time=2
            )
        
        self.play(FadeOut(*self.mobjects))

    def traversal_operations(self):
        with self.voiceover(text="One of the most powerful features of doubly linked lists is the ability to traverse in both directions. Forward traversal starts from the head and follows the next pointers until we reach null. Backward traversal starts from the tail and follows the previous pointers. This bidirectional capability is invaluable in many applications, such as implementing browser history where you need to move both forward and backward through visited pages.") as tracker:
            trav_title = Text("Bidirectional Traversal", font_size=32, color=BLUE)
            trav_title.to_edge(UP, buff=1.0)
            self.play(Write(trav_title))
            
            # Create list
            node1 = self.create_node("5", ORANGE)
            node2 = self.create_node("15", GREEN)
            node3 = self.create_node("25", PURPLE)
            node4 = self.create_node("35", TEAL)
            
            nodes = VGroup(node1, node2, node3, node4).arrange(RIGHT, buff=1.2)
            nodes.move_to(DOWN * 0.5)
            
            # Create all arrows
            arrows_forward = VGroup()
            arrows_backward = VGroup()
            
            for i in range(3):
                f_arrow = Arrow(nodes[i].get_right() + RIGHT*0.1,
                               nodes[i+1].get_left() + LEFT*0.1,
                               color=BLUE, buff=0.1, stroke_width=3)
                arrows_forward.add(f_arrow)
                
                b_arrow = Arrow(nodes[i+1].get_left() + LEFT*0.1 + DOWN*0.3,
                               nodes[i].get_right() + RIGHT*0.1 + DOWN*0.3,
                               color=RED, buff=0.1, stroke_width=3)
                arrows_backward.add(b_arrow)
            
            self.play(FadeIn(nodes))
            self.play(Create(arrows_forward), Create(arrows_backward))
            
        with self.voiceover(text="Let's visualize forward traversal. We start at the head node with value five and visit each node in sequence by following the blue next pointers. Watch as we highlight each node as we traverse through the list. This is similar to how you would read a book from beginning to end, moving forward one page at a time.") as tracker:
            forward_label = Text("Forward Traversal →", font_size=22, color=BLUE)
            forward_label.next_to(trav_title, DOWN, buff=0.8)
            self.play(Write(forward_label))
            
            # Animate forward traversal
            for i, node in enumerate(nodes):
                highlight = SurroundingRectangle(node, color=YELLOW, buff=0.12, stroke_width=4)
                visit_text = Text(f"Visit: {5 + i*10}", font_size=18, color=YELLOW)
                visit_text.to_edge(DOWN, buff=0.8)
                
                self.play(Create(highlight), Write(visit_text), run_time=1.2)
                self.wait(0.3)
                if i < len(nodes) - 1:
                    self.play(FadeOut(highlight), FadeOut(visit_text), run_time=0.5)
                else:
                    self.play(FadeOut(highlight), FadeOut(visit_text), FadeOut(forward_label), run_time=0.5)
                    
        with self.voiceover(text="Now let's see backward traversal. Starting from the tail node with value thirty five, we follow the red previous pointers to move backward through the list. This is like using the back button in your browser, moving through your history in reverse order. Notice how we visit the nodes in exactly the opposite sequence compared to forward traversal.") as tracker:
            backward_label = Text("← Backward Traversal", font_size=22, color=RED)
            backward_label.next_to(trav_title, DOWN, buff=0.8)
            self.play(Write(backward_label))
            
            # Animate backward traversal
            for i in range(len(nodes)-1, -1, -1):
                highlight = SurroundingRectangle(nodes[i], color=ORANGE, buff=0.12, stroke_width=4)
                visit_text = Text(f"Visit: {5 + i*10}", font_size=18, color=ORANGE)
                visit_text.to_edge(DOWN, buff=0.8)
                
                self.play(Create(highlight), Write(visit_text), run_time=1.2)
                self.wait(0.3)
                self.play(FadeOut(highlight), FadeOut(visit_text), run_time=0.5)
        
        self.play(FadeOut(*self.mobjects))

    def comparison_with_singly(self):
        with self.voiceover(text="Let's compare doubly linked lists with singly linked lists to understand when to use each structure. A singly linked list has only one pointer per node, pointing to the next node, which makes it more memory efficient. However, it can only be traversed in one direction, and certain operations like deletion require access to the previous node, which means we must traverse from the beginning.") as tracker:
            comp_title = Text("Doubly vs Singly Linked Lists", font_size=32, color=BLUE)
            comp_title.to_edge(UP, buff=1.0)
            self.play(Write(comp_title))
            
            # Left side - Singly Linked List
            singly_label = Text("Singly Linked List", font_size=24, color=YELLOW)
            singly_label.move_to(LEFT * 3.5 + UP * 1.8)
            
            s_node1 = Rectangle(width=1.2, height=0.8, color=GREEN, stroke_width=3)
            s_node1.move_to(LEFT * 4.5 + DOWN * 0.5)
            s_data1 = Text("10", font_size=20).move_to(s_node1)
            
            s_node2 = Rectangle(width=1.2, height=0.8, color=GREEN, stroke_width=3)
            s_node2.move_to(LEFT * 2.5 + DOWN * 0.5)
            s_data2 = Text("20", font_size=20).move_to(s_node2)
            
            s_arrow = Arrow(s_node1.get_right(), s_node2.get_left(), 
                           color=BLUE, buff=0.1, stroke_width=3)
            
            singly_group = VGroup(singly_label, s_node1, s_data1, s_node2, s_data2, s_arrow)
            
            self.play(Write(singly_label))
            self.play(FadeIn(s_node1), FadeIn(s_data1), FadeIn(s_node2), FadeIn(s_data2))
            self.play(Create(s_arrow))
            
        with self.voiceover(text="In contrast, a doubly linked list has two pointers per node, which uses more memory but provides significant advantages. We can traverse in both directions, delete a node in constant time if we have a pointer to it, and efficiently implement certain advanced data structures. The trade-off is the extra memory overhead and slightly more complex insertion and deletion logic.") as tracker:
            # Right side - Doubly Linked List
            doubly_label = Text("Doubly Linked List", font_size=24, color=ORANGE)
            doubly_label.move_to(RIGHT * 3.5 + UP * 1.8)
            
            d_node1 = self.create_node("10", PURPLE)
            d_node1.scale(0.7)
            d_node1.move_to(RIGHT * 2 + DOWN * 0.5)
            
            d_node2 = self.create_node("20", PURPLE)
            d_node2.scale(0.7)
            d_node2.move_to(RIGHT * 5 + DOWN * 0.5)
            
            d_f_arrow = Arrow(d_node1.get_right() + RIGHT*0.05, d_node2.get_left() + LEFT*0.05,
                             color=BLUE, buff=0.05, stroke_width=3)
            d_b_arrow = Arrow(d_node2.get_left() + LEFT*0.05 + DOWN*0.2,
                             d_node1.get_right() + RIGHT*0.05 + DOWN*0.2,
                             color=RED, buff=0.05, stroke_width=3)
            
            self.play(Write(doubly_label))
            self.play(FadeIn(d_node1), FadeIn(d_node2))
            self.play(Create(d_f_arrow), Create(d_b_arrow))
            
        with self.voiceover(text="Here's a summary of the key differences. Memory usage: singly linked lists use less memory per node. Traversal: singly is unidirectional while doubly is bidirectional. Deletion: doubly linked lists can delete in constant time with a node pointer, while singly linked lists need the previous node reference. Implementation complexity: doubly linked lists are slightly more complex but offer more flexibility.") as tracker:
            comparison_table = VGroup(
                Text("Memory: Singly < Doubly", font_size=18, color=WHITE),
                Text("Traversal: Uni vs Bi-directional", font_size=18, color=WHITE),
                Text("Deletion: O(n) vs O(1)", font_size=18, color=WHITE),
                Text("Complexity: Simple vs Flexible", font_size=18, color=WHITE)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            comparison_table.move_to(DOWN * 2.5)
            
            for item in comparison_table:
                self.play(FadeIn(item), run_time=0.8)
        
        self.play(FadeOut(*self.mobjects))

    def time_complexity_analysis(self):
        with self.voiceover(text="Understanding the time complexity of operations is crucial for choosing the right data structure. Let's analyze the computational complexity of common operations on doubly linked lists. Access by index requires traversing from the head or tail, giving us linear time complexity. However, if we already have a pointer to a node, accessing its neighbors is constant time.") as tracker:
            complexity_title = Text("Time Complexity Analysis", font_size=32, color=BLUE)
            complexity_title.to_edge(UP, buff=1.0)
            self.play(Write(complexity_title))
            
            # Create table header
            operations = VGroup(
                Text("Operation", font_size=24, color=YELLOW),
                Text("Time", font_size=24, color=WHITE)
            ).arrange(RIGHT, buff=3.5)
            operations.next_to(complexity_title, DOWN, buff=0.8)
            
            self.play(Write(operations))
            
            # Create table rows
            access = VGroup(
                Text("Access by Index", font_size=20),
                MathTex(r"O(n)", font_size=28, color=RED)
            ).arrange(RIGHT, buff=3.2)
            
            search = VGroup(
                Text("Search", font_size=20),
                MathTex(r"O(n)", font_size=28, color=RED)
            ).arrange(RIGHT, buff=4.8)
            
            insert_begin = VGroup(
                Text("Insert at Beginning", font_size=20),
                MathTex(r"O(1)", font_size=28, color=GREEN)
            ).arrange(RIGHT, buff=2.2)
            
            insert_end = VGroup(
                Text("Insert at End", font_size=20),
                MathTex(r"O(1)", font_size=28, color=GREEN)
            ).arrange(RIGHT, buff=2.8)
            
            delete = VGroup(
                Text("Delete (with pointer)", font_size=20),
                MathTex(r"O(1)", font_size=28, color=GREEN)
            ).arrange(RIGHT, buff=1.5)
            
            table_rows = VGroup(access, search, insert_begin, insert_end, delete)
            table_rows.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            table_rows.next_to(operations, DOWN, buff=0.6)
            
            for row in table_rows:
                self.play(FadeIn(row), run_time=1)
                
        with self.voiceover(text="The real power of doubly linked lists shows in insertion and deletion operations. When we have a pointer to a specific location, we can insert or delete in constant time because we can directly access both the previous and next nodes. This is a significant advantage over singly linked lists, where deletion requires finding the previous node, which takes linear time. Search operations still require linear time as we must potentially examine every node in the worst case.") as tracker:
            explanation = VGroup(
                Text("• O(1) operations use direct pointer access", font_size=18, color=GREEN),
                Text("• O(n) operations require traversal", font_size=18, color=RED),
                Text("• Bidirectional links enable efficient updates", font_size=18, color=YELLOW),
                Text("• Trade-off: Memory for time efficiency", font_size=18, color=ORANGE)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            explanation.to_edge(DOWN, buff=1.2)
            
            for item in explanation:
                self.play(FadeIn(item), run_time=1)
        
        self.play(FadeOut(*self.mobjects))

    def real_world_applications(self):
        with self.voiceover(text="Doubly linked lists are used extensively in real-world applications. Operating systems use them for managing processes in schedulers, where the ability to move forward and backward through the process queue is essential. Text editors rely on doubly linked lists to implement efficient undo and redo functionality, allowing users to navigate through their editing history in both directions.") as tracker:
            app_title = Text("Real-World Applications", font_size=32, color=BLUE)
            app_title.to_edge(UP, buff=1.0)
            self.play(Write(app_title))
            
            # Application 1: Browser History
            browser_title = Text("1. Browser Navigation", font_size=26, color=YELLOW)
            browser_title.move_to(UP * 1.8)
            
            pages = VGroup(
                self.create_simple_node("Page A", BLUE),
                self.create_simple_node("Page B", GREEN),
                self.create_simple_node("Page C", PURPLE),
                self.create_simple_node("Page D", ORANGE)
            ).arrange(RIGHT, buff=0.8)
            pages.move_to(UP * 0.3)
            
            self.play(Write(browser_title))
            self.play(FadeIn(pages), run_time=1.5)
            
            back_arrow = Arrow(pages[2].get_left() + LEFT*0.1 + DOWN*0.4,
                              pages[1].get_right() + RIGHT*0.1 + DOWN*0.4,
                              color=RED, buff=0.1, stroke_width=4)
            forward_arrow = Arrow(pages[1].get_right() + RIGHT*0.1,
                                 pages[2].get_left() + LEFT*0.1,
                                 color=BLUE, buff=0.1, stroke_width=4)
            
            back_label = Text("◄ Back", font_size=16, color=RED)
            back_label.next_to(back_arrow, DOWN, buff=0.2)
            forward_label = Text("Forward ►", font_size=16, color=BLUE)
            forward_label.next_to(pages[2], RIGHT, buff=0.5)
            
            self.play(Create(back_arrow), Create(forward_arrow))
            self.play(Write(back_label), Write(forward_label))
            
        with self.voiceover(text="Music players use doubly linked lists for playlists, enabling users to skip forward to the next song or go back to the previous one seamlessly. The least recently used cache, or LRU cache, which is crucial for optimizing performance in databases and web servers, is implemented using a doubly linked list combined with a hash map. This allows constant time access to any element and efficient removal of the least recently used item.") as tracker:
            # Clear and show Application 2
            self.play(FadeOut(*self.mobjects))
            
            app_title2 = Text("Real-World Applications", font_size=32, color=BLUE)
            app_title2.to_edge(UP, buff=1.0)
            self.play(FadeIn(app_title2))
            
            music_title = Text("2. Music Player Playlist", font_size=26, color=YELLOW)
            music_title.move_to(UP * 1.8)
            
            songs = VGroup(
                self.create_simple_node("Song 1", TEAL),
                self.create_simple_node("Song 2", GOLD),
                self.create_simple_node("Song 3", MAROON)
            ).arrange(RIGHT, buff=1.0)
            songs.move_to(UP * 0.3)
            
            self.play(Write(music_title))
            self.play(FadeIn(songs))
            
            prev_btn = Text("⏮ Prev", font_size=18, color=RED)
            next_btn = Text("Next ⏭", font_size=18, color=BLUE)
            prev_btn.move_to(DOWN * 1.2 + LEFT * 2)
            next_btn.move_to(DOWN * 1.2 + RIGHT * 2)
            
            self.play(Write(prev_btn), Write(next_btn))
            
        with self.voiceover(text="In memory management, operating systems use doubly linked lists to track free memory blocks. The bidirectional linking allows efficient coalescing of adjacent free blocks. Version control systems also leverage doubly linked lists to maintain commit history, allowing developers to navigate through different versions of code in both forward and backward directions efficiently.") as tracker:
            other_apps = VGroup(
                Text("3. LRU Cache Implementation", font_size=20, color=ORANGE),
                Text("4. Memory Management Systems", font_size=20, color=PURPLE),
                Text("5. Undo/Redo in Text Editors", font_size=20, color=GREEN),
                Text("6. Navigation in Image Galleries", font_size=20, color=PINK)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
            other_apps.move_to(DOWN * 1.8)
            
            for app in other_apps:
                self.play(FadeIn(app), run_time=0.8)
        
        self.play(FadeOut(*self.mobjects))

    def create_simple_node(self, text, color):
        """Helper function for simplified node visualization"""
        box = Rectangle(width=1.6, height=0.7, color=color, stroke_width=3)
        label = Text(text, font_size=16, color=WHITE)
        label.move_to(box.get_center())
        return VGroup(box, label)

    def memory_representation(self):
        with self.voiceover(text="Let's examine how doubly linked lists are stored in computer memory. Unlike arrays which occupy contiguous memory locations, linked list nodes can be scattered throughout memory. Each node stores its data along with two memory addresses: one pointing to the previous node and one pointing to the next node. This non-contiguous storage is both an advantage and a challenge.") as tracker:
            mem_title = Text("Memory Representation", font_size=32, color=BLUE)
            mem_title.to_edge(UP, buff=1.0)
            self.play(Write(mem_title))
            
            # Memory blocks
            mem_label = Text("Computer Memory", font_size=22, color=YELLOW)
            mem_label.next_to(mem_title, DOWN, buff=0.5)
            self.play(Write(mem_label))
            
            # Create memory visualization
            mem1 = Rectangle(width=2, height=0.8, color=ORANGE, stroke_width=3)
            mem1.move_to(LEFT * 3.5 + UP * 0.8)
            addr1 = Text("0x1000", font_size=14, color=GRAY)
            addr1.next_to(mem1, LEFT, buff=0.3)
            data1 = Text("Node: 10", font_size=16)
            data1.move_to(mem1.get_center())
            
            mem2 = Rectangle(width=2, height=0.8, color=GREEN, stroke_width=3)
            mem2.move_to(RIGHT * 1.5 + DOWN * 0.5)
            addr2 = Text("0x2050", font_size=14, color=GRAY)
            addr2.next_to(mem2, LEFT, buff=0.3)
            data2 = Text("Node: 20", font_size=16)
            data2.move_to(mem2.get_center())
            
            mem3 = Rectangle(width=2, height=0.8, color=PURPLE, stroke_width=3)
            mem3.move_to(LEFT * 4 + DOWN * 2)
            addr3 = Text("0x3100", font_size=14, color=GRAY)
            addr3.next_to(mem3, LEFT, buff=0.3)
            data3 = Text("Node: 30", font_size=16)
            data3.move_to(mem3.get_center())
            
            self.play(
                FadeIn(mem1), FadeIn(mem2), FadeIn(mem3),
                FadeIn(addr1), FadeIn(addr2), FadeIn(addr3),
                FadeIn(data1), FadeIn(data2), FadeIn(data3),
                run_time=2
            )
            
        with self.voiceover(text="Notice how the nodes are not stored sequentially in memory. Node at address one thousand is followed in the list by the node at address two thousand fifty, which is physically located elsewhere in memory. The pointers create the logical sequence. This scattered arrangement means we cannot use simple arithmetic to access elements like we can with arrays, but it allows for dynamic size changes without moving existing elements.") as tracker:
            # Show pointer connections
            ptr1 = Arrow(mem1.get_right() + RIGHT*0.1, mem2.get_left() + LEFT*0.1 + UP*0.2,
                        color=BLUE, buff=0.1, stroke_width=3)
            ptr2 = Arrow(mem2.get_bottom() + DOWN*0.2 + LEFT*0.2, mem3.get_top() + UP*0.1 + LEFT*0.2,
                        color=BLUE, buff=0.1, stroke_width=3)
            
            ptr1_label = Text("next: 0x2050", font_size=12, color=BLUE)
            ptr1_label.next_to(ptr1, UP, buff=0.2)
            ptr2_label = Text("next: 0x3100", font_size=12, color=BLUE)
            ptr2_label.next_to(ptr2, RIGHT, buff=0.4)
            
            self.play(Create(ptr1), Create(ptr2))
            self.play(Write(ptr1_label), Write(ptr2_label))
            
            # Show backward pointers
            back1 = Arrow(mem2.get_left() + LEFT*0.1 + DOWN*0.2, 
                         mem1.get_right() + RIGHT*0.1 + DOWN*0.2,
                         color=RED, buff=0.1, stroke_width=3)
            back2 = Arrow(mem3.get_top() + UP*0.1 + RIGHT*0.2,
                         mem2.get_bottom() + DOWN*0.2 + RIGHT*0.2,
                         color=RED, buff=0.1, stroke_width=3)
            
            back1_label = Text("prev: 0x1000", font_size=12, color=RED)
            back1_label.next_to(back1, DOWN, buff=0.2)
            back2_label = Text("prev: 0x2050", font_size=12, color=RED)
            back2_label.next_to(back2, LEFT, buff=0.4)
            
            self.play(Create(back1), Create(back2))
            self.play(Write(back1_label), Write(back2_label))
        
        self.play(FadeOut(*self.mobjects))

    def conclusion(self):
        with self.voiceover(text="We've covered the comprehensive structure and behavior of doubly linked lists. This elegant data structure provides bidirectional traversal capabilities, efficient insertion and deletion operations when you have a pointer to a node, and forms the foundation for many advanced data structures and algorithms. While they use more memory than singly linked lists due to the extra pointer, the flexibility they provide makes them invaluable in many scenarios.") as tracker:
            conclusion_title = Text("Summary and Conclusion", font_size=32, color=BLUE)
            conclusion_title.to_edge(UP, buff=1.0)
            self.play(Write(conclusion_title))
            
            key_points = VGroup(
                Text("✓ Bidirectional traversal capability", font_size=22, color=GREEN),
                Text("✓ O(1) insertion and deletion with pointer", font_size=22, color=GREEN),
                Text("✓ Extra memory for backward pointers", font_size=22, color=YELLOW),
                Text("✓ Foundation for LRU cache, deques, etc.", font_size=22, color=ORANGE),
                Text("✓ Wide applications in real systems", font_size=22, color=PURPLE)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.45)
            key_points.move_to(UP * 0.3)
            
            for point in key_points:
                self.play(FadeIn(point), run_time=1)
                
        with self.voiceover(text="When choosing between data structures, consider your specific needs. Use doubly linked lists when you need bidirectional traversal, frequent insertions and deletions in the middle of the list, or when implementing structures like LRU caches. For simple forward-only traversal with minimal memory usage, a singly linked list might suffice. For random access, arrays or dynamic arrays are more appropriate. Understanding these trade-offs will help you write more efficient code.") as tracker:
            recommendations = VGroup(
                Text("When to Use Doubly Linked Lists:", font_size=24, color=YELLOW, weight=BOLD),
                Text("• Need bidirectional navigation", font_size=18, color=WHITE),
                Text("• Frequent middle insertions/deletions", font_size=18, color=WHITE),
                Text("• Implementing advanced structures", font_size=18, color=WHITE),
                Text("• Memory is not severely constrained", font_size=18, color=WHITE)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            recommendations.move_to(DOWN * 1.8)
            
            for rec in recommendations:
                self.play(FadeIn(rec), run_time=0.8)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Thank you for watching this detailed explanation of doubly linked lists. I hope this visualization has helped you understand not just how they work, but also when and why to use them in your own programs. Keep practicing with implementing these structures, and you'll develop a deeper intuition for choosing the right data structure for any problem you encounter.") as tracker:
            thank_you = Text("Thank You for Watching!", font_size=36, color=BLUE, weight=BOLD)
            thank_you.move_to(UP)
            
            contact = VGroup(
                Text("Master Data Structures", font_size=24, color=YELLOW),
                Text("Practice • Visualize • Understand", font_size=20, color=GREEN)
            ).arrange(DOWN, buff=0.4)
            contact.next_to(thank_you, DOWN, buff=1.2)
            
            self.play(Write(thank_you), run_time=2)
            self.play(FadeIn(contact), run_time=1.5)
            self.wait(2)