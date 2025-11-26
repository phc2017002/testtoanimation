from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import numpy as np

class CircularQueueLinkedList(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))
        
        # Introduction
        self.introduction()
        
        # Explain what is a circular queue
        self.explain_circular_queue_concept()
        
        # Compare array vs linked list implementation
        self.compare_implementations()
        
        # Show node structure
        self.show_node_structure()
        
        # Explain empty queue initialization
        self.explain_initialization()
        
        # Demonstrate enqueue operation
        self.demonstrate_enqueue()
        
        # Demonstrate dequeue operation
        self.demonstrate_dequeue()
        
        # Show complete operation sequence
        self.complete_operation_sequence()
        
        # Explain advantages and disadvantages
        self.advantages_disadvantages()
        
        # Show time complexity analysis
        self.time_complexity_analysis()
        
        # Real-world applications
        self.real_world_applications()
        
        # Conclusion
        self.conclusion()

    def introduction(self):
        with self.voiceover(text="Welcome to this comprehensive explanation of Circular Queue implementation using Linked Lists. A circular queue is a linear data structure that follows the first in first out principle, but with a twist. Unlike a regular queue, the last position is connected back to the first position, making it circular. Today, we will explore how to implement this elegant data structure using linked lists, examining every operation in detail.") as tracker:
            title = Text("Circular Queue Implementation", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            subtitle = Text("Using Linked List", font_size=28, color=GREEN)
            subtitle.next_to(title, DOWN, buff=0.3)
            
            self.play(Write(title))
            self.wait(0.5)
            self.play(Write(subtitle))
            self.wait(1)
        
        with self.voiceover(text="This data structure combines the efficiency of linked lists with the circular nature of ring buffers, making it perfect for scenarios where we need continuous data flow without wasting memory space. Let's dive deep into understanding how it works.") as tracker:
            # Create a simple circular visualization
            circle = Circle(radius=2, color=YELLOW)
            circle.move_to(DOWN * 0.5)
            
            # Add arrows showing circular nature
            arrow1 = CurvedArrow(
                circle.point_at_angle(0),
                circle.point_at_angle(PI/2),
                color=RED,
                angle=PI/2
            )
            arrow2 = CurvedArrow(
                circle.point_at_angle(PI/2),
                circle.point_at_angle(PI),
                color=RED,
                angle=PI/2
            )
            arrow3 = CurvedArrow(
                circle.point_at_angle(PI),
                circle.point_at_angle(3*PI/2),
                color=RED,
                angle=PI/2
            )
            arrow4 = CurvedArrow(
                circle.point_at_angle(3*PI/2),
                circle.point_at_angle(2*PI),
                color=RED,
                angle=PI/2
            )
            
            arrows = VGroup(arrow1, arrow2, arrow3, arrow4)
            
            label = Text("Circular Flow", font_size=24, color=WHITE)
            label.next_to(circle, DOWN, buff=0.5)
            
            self.play(Create(circle))
            self.play(Create(arrows), Write(label))
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def explain_circular_queue_concept(self):
        with self.voiceover(text="Let's start by understanding what makes a queue circular. In a standard linear queue, once we reach the end of the allocated space, we cannot add more elements even if there is space at the beginning. This is inefficient and wasteful.") as tracker:
            title = Text("What is a Circular Queue?", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Show linear queue problem
            linear_label = Text("Linear Queue Problem:", font_size=24, color=YELLOW)
            linear_label.move_to(UP * 1.5)
            
            boxes = VGroup(*[Square(side_length=0.6, color=WHITE) for _ in range(6)])
            boxes.arrange(RIGHT, buff=0.1)
            boxes.move_to(UP * 0.3)
            
            # Fill some boxes
            values = ["X", "X", "", "", "", ""]
            labels = VGroup()
            for i, val in enumerate(values):
                if val:
                    label = Text(val, font_size=20, color=RED)
                    label.move_to(boxes[i].get_center())
                    labels.add(label)
            
            front_arrow = Arrow(UP * 0.8, boxes[2].get_top(), color=GREEN, buff=0.1)
            front_label = Text("Front", font_size=18, color=GREEN).next_to(front_arrow, RIGHT, buff=0.1)
            
            rear_arrow = Arrow(UP * 0.8, boxes[5].get_top(), color=RED, buff=0.1)
            rear_label = Text("Rear", font_size=18, color=RED).next_to(rear_arrow, RIGHT, buff=0.1)
            
            waste_text = Text("Wasted Space!", font_size=20, color=RED)
            waste_text.next_to(boxes, DOWN, buff=0.4)
            
            self.play(Write(linear_label))
            self.play(Create(boxes))
            self.play(Write(labels))
            self.play(Create(front_arrow), Write(front_label))
            self.play(Create(rear_arrow), Write(rear_label))
            self.play(Write(waste_text))
            self.wait(1)
        
        with self.voiceover(text="A circular queue solves this problem by wrapping around. When the rear pointer reaches the end, it circles back to the beginning, utilizing all available space efficiently. This creates a continuous circular flow of data, where the end connects back to the start, eliminating wasted space and allowing continuous operation.") as tracker:
            self.play(FadeOut(*self.mobjects[1:]))  # Keep title
            
            circular_label = Text("Circular Queue Solution:", font_size=24, color=GREEN)
            circular_label.move_to(UP * 1.5)
            
            # Create circular representation
            circle_radius = 1.5
            num_nodes = 6
            nodes = VGroup()
            
            for i in range(num_nodes):
                angle = i * (2 * PI / num_nodes) - PI/2
                x = circle_radius * np.cos(angle)
                y = circle_radius * np.sin(angle) - 0.5
                
                node = Circle(radius=0.3, color=BLUE, fill_opacity=0.3)
                node.move_to([x, y, 0])
                nodes.add(node)
            
            # Add arrows
            circular_arrows = VGroup()
            for i in range(num_nodes):
                start_angle = i * (2 * PI / num_nodes) - PI/2
                end_angle = ((i + 1) % num_nodes) * (2 * PI / num_nodes) - PI/2
                
                start_x = circle_radius * np.cos(start_angle)
                start_y = circle_radius * np.sin(start_angle) - 0.5
                
                end_x = circle_radius * np.cos(end_angle)
                end_y = circle_radius * np.sin(end_angle) - 0.5
                
                arrow = Arrow(
                    [start_x * 0.85, start_y * 0.85, 0],
                    [end_x * 0.85, end_y * 0.85, 0],
                    color=YELLOW,
                    buff=0.3,
                    stroke_width=3
                )
                circular_arrows.add(arrow)
            
            efficient_text = Text("Efficient Space Usage!", font_size=20, color=GREEN)
            efficient_text.move_to(DOWN * 2.5)
            
            self.play(Write(circular_label))
            self.play(Create(nodes))
            self.play(Create(circular_arrows))
            self.play(Write(efficient_text))
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def compare_implementations(self):
        with self.voiceover(text="Now let's compare two ways to implement a circular queue: using arrays versus using linked lists. Array implementation has a fixed size, which means we must decide the maximum capacity in advance. This can lead to either wasted memory if we allocate too much, or overflow if we allocate too little.") as tracker:
            title = Text("Array vs Linked List Implementation", font_size=30, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Array implementation
            array_title = Text("Array-Based", font_size=24, color=YELLOW)
            array_title.move_to(LEFT * 3.5 + UP * 1.8)
            
            array_boxes = VGroup(*[Square(side_length=0.5, color=BLUE) for _ in range(5)])
            array_boxes.arrange(RIGHT, buff=0.05)
            array_boxes.move_to(LEFT * 3.5 + UP * 0.3)
            
            array_pros = Text("Fixed Size", font_size=18, color=RED)
            array_pros.move_to(LEFT * 3.5 + DOWN * 0.8)
            
            array_cons = Text("Memory Waste", font_size=18, color=RED)
            array_cons.move_to(LEFT * 3.5 + DOWN * 1.3)
            
            self.play(Write(array_title))
            self.play(Create(array_boxes))
            self.play(Write(array_pros))
            self.play(Write(array_cons))
            self.wait(0.5)
        
        with self.voiceover(text="On the other hand, linked list implementation offers dynamic size allocation. We can grow or shrink the queue as needed without wasting memory. Each node contains data and a pointer to the next node, and in a circular implementation, the last node points back to the first. This flexibility makes linked lists ideal for situations where the queue size varies significantly during program execution.") as tracker:
            # Linked list implementation
            ll_title = Text("Linked List", font_size=24, color=GREEN)
            ll_title.move_to(RIGHT * 3.5 + UP * 1.8)
            
            # Create linked list nodes
            node1 = self.create_node_visual("A", RIGHT * 2.2 + UP * 0.3)
            node2 = self.create_node_visual("B", RIGHT * 3.5 + UP * 0.3)
            node3 = self.create_node_visual("C", RIGHT * 4.8 + UP * 0.3)
            
            arrow1 = Arrow(node1[0].get_right(), node2[0].get_left(), buff=0.05, color=WHITE, stroke_width=2)
            arrow2 = Arrow(node2[0].get_right(), node3[0].get_left(), buff=0.05, color=WHITE, stroke_width=2)
            arrow3 = CurvedArrow(
                node3[0].get_bottom(),
                node1[0].get_bottom(),
                color=YELLOW,
                angle=-PI/3
            )
            
            ll_pros = Text("Dynamic Size", font_size=18, color=GREEN)
            ll_pros.move_to(RIGHT * 3.5 + DOWN * 0.8)
            
            ll_cons = Text("Efficient Memory", font_size=18, color=GREEN)
            ll_cons.move_to(RIGHT * 3.5 + DOWN * 1.3)
            
            self.play(Write(ll_title))
            self.play(Create(node1), Create(node2), Create(node3))
            self.play(Create(arrow1), Create(arrow2), Create(arrow3))
            self.play(Write(ll_pros))
            self.play(Write(ll_cons))
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def create_node_visual(self, data, position):
        node = Rectangle(width=0.8, height=0.5, color=BLUE, fill_opacity=0.3)
        node.move_to(position)
        
        data_text = Text(data, font_size=20, color=WHITE)
        data_text.move_to(node.get_center())
        
        return VGroup(node, data_text)

    def show_node_structure(self):
        with self.voiceover(text="Let's examine the structure of a node in our circular queue implementation. Each node contains two essential components: the data field, which stores the actual value, and the next pointer, which references the next node in the queue. This simple yet powerful structure is the building block of our circular queue.") as tracker:
            title = Text("Node Structure", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Create detailed node structure
            node_rect = Rectangle(width=4, height=1.5, color=YELLOW)
            node_rect.move_to(UP * 0.5)
            
            divider = Line(node_rect.get_top() + DOWN * 0.75, node_rect.get_bottom() + UP * 0.75, color=WHITE)
            divider.move_to(node_rect.get_center())
            
            data_section = Rectangle(width=1.8, height=1.3, color=GREEN, fill_opacity=0.2)
            data_section.move_to(node_rect.get_center() + LEFT * 1.05)
            
            next_section = Rectangle(width=1.8, height=1.3, color=BLUE, fill_opacity=0.2)
            next_section.move_to(node_rect.get_center() + RIGHT * 1.05)
            
            data_label = Text("Data", font_size=20, color=GREEN)
            data_label.move_to(data_section.get_center())
            
            next_label = Text("Next", font_size=20, color=BLUE)
            next_label.move_to(next_section.get_center())
            
            self.play(Create(node_rect))
            self.play(Create(divider))
            self.play(Create(data_section), Write(data_label))
            self.play(Create(next_section), Write(next_label))
            self.wait(1)
        
        with self.voiceover(text="In code, we define this structure using a class. The node class has two attributes: data, which can hold any value we want to store, and next, which is a reference to another node object. When we create the last node in our circular queue, we set its next pointer to reference the first node, thus completing the circle and creating the circular link that gives this data structure its name.") as tracker:
            # Show code representation
            code = Code(
                code='''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None''',
                language="python",
                font_size=18,
                background="window",
                style="monokai"
            )
            code.move_to(DOWN * 1.2)
            code.scale(0.8)
            
            self.play(Create(code))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def explain_initialization(self):
        with self.voiceover(text="When we initialize an empty circular queue, both the front and rear pointers are set to None. This represents an empty state where no nodes exist yet. The front pointer indicates where we will remove elements from, while the rear pointer shows where we will add new elements. Understanding this initial state is crucial for implementing the operations correctly.") as tracker:
            title = Text("Empty Queue Initialization", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Show empty state
            front_label = Text("Front = None", font_size=26, color=GREEN)
            front_label.move_to(UP * 0.8 + LEFT * 2.5)
            
            rear_label = Text("Rear = None", font_size=26, color=RED)
            rear_label.move_to(UP * 0.8 + RIGHT * 2.5)
            
            empty_box = DashedVMobject(Rectangle(width=5, height=2, color=GRAY))
            empty_box.move_to(DOWN * 0.5)
            
            empty_text = Text("Empty Queue", font_size=24, color=GRAY)
            empty_text.move_to(empty_box.get_center())
            
            self.play(Write(front_label))
            self.play(Write(rear_label))
            self.play(Create(empty_box))
            self.play(Write(empty_text))
            self.wait(1)
        
        with self.voiceover(text="This empty state is important because our enqueue and dequeue operations must handle it specially. When we add the first element, we need to set both front and rear to point to that same node. When we remove the last element, we need to reset both pointers back to None. These edge cases are essential for maintaining the integrity of our circular queue structure.") as tracker:
            conditions = VGroup(
                Text("• Both pointers start as None", font_size=20, color=WHITE),
                Text("• First enqueue sets both pointers", font_size=20, color=WHITE),
                Text("• Last dequeue resets to empty", font_size=20, color=WHITE)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            conditions.move_to(DOWN * 1.8)
            
            self.play(Write(conditions))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def demonstrate_enqueue(self):
        with self.voiceover(text="Now let's see how the enqueue operation works in detail. Enqueue means adding an element to the rear of the queue. When we want to add a new element, we first create a new node with the given data. Then we must consider two scenarios: adding to an empty queue, or adding to a queue that already has elements.") as tracker:
            title = Text("Enqueue Operation", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            step_text = Text("Step 1: Create new node", font_size=24, color=YELLOW)
            step_text.move_to(UP * 1.8)
            self.play(Write(step_text))
            
            new_node = self.create_node_visual("10", ORIGIN + DOWN * 0.3)
            self.play(Create(new_node))
            self.wait(1)
        
        with self.voiceover(text="If the queue is empty, meaning front is None, then this new node becomes both the front and rear of the queue. Critically, we must set the new node's next pointer to point to itself, creating the circular link even with just one element. This maintains the circular property from the very beginning.") as tracker:
            self.play(FadeOut(step_text))
            
            step2 = Text("Step 2: Empty queue case", font_size=24, color=YELLOW)
            step2.move_to(UP * 1.8)
            self.play(Write(step2))
            
            front_pointer = Arrow(UP * 0.5 + LEFT * 2.5, new_node[0].get_top() + LEFT * 0.2, color=GREEN, buff=0.15)
            front_text = Text("Front", font_size=18, color=GREEN).next_to(front_pointer.get_start(), LEFT, buff=0.2)
            
            rear_pointer = Arrow(UP * 0.5 + RIGHT * 2.5, new_node[0].get_top() + RIGHT * 0.2, color=RED, buff=0.15)
            rear_text = Text("Rear", font_size=18, color=RED).next_to(rear_pointer.get_start(), RIGHT, buff=0.2)
            
            self.play(Create(front_pointer), Write(front_text))
            self.play(Create(rear_pointer), Write(rear_text))
            
            # Self loop positioned below to avoid overlap
            self_arrow = CurvedArrow(
                new_node[0].get_right() + DOWN * 0.1,
                new_node[0].get_bottom() + RIGHT * 0.2,
                color=BLUE,
                angle=-PI/2
            )
            self.play(Create(self_arrow))
            self.wait(1)
        
        with self.voiceover(text="For adding to a non-empty queue, the process is different. We set the current rear node's next pointer to the new node, then move the rear pointer to this new node. Finally, we set the new node's next pointer to front, maintaining the circular connection. This ensures that no matter how many elements we add, the last element always points back to the first, preserving our circular structure.") as tracker:
            self.play(FadeOut(step2), FadeOut(self_arrow))
            
            step3 = Text("Step 3: Add second element", font_size=24, color=YELLOW)
            step3.move_to(UP * 1.8)
            self.play(Write(step3))
            
            # Move first node left
            self.play(new_node.animate.shift(LEFT * 1.5))
            self.play(front_pointer.animate.shift(LEFT * 1.5), front_text.animate.shift(LEFT * 1.5))
            
            # Create second node
            node2 = self.create_node_visual("20", ORIGIN + DOWN * 0.3 + RIGHT * 1.5)
            self.play(Create(node2))
            
            # Arrow from first to second
            arrow1 = Arrow(new_node[0].get_right(), node2[0].get_left(), buff=0.05, color=WHITE, stroke_width=3)
            self.play(Create(arrow1))
            
            # Move rear pointer
            self.play(rear_pointer.animate.put_start_and_end_on(
                UP * 0.5 + RIGHT * 2.5, node2[0].get_top() + RIGHT * 0.2
            ))
            self.play(rear_text.animate.shift(RIGHT * 1.5))
            
            # Circular arrow from second to first positioned lower to avoid overlap
            circular = CurvedArrow(
                node2[0].get_bottom() + LEFT * 0.3,
                new_node[0].get_bottom() + RIGHT * 0.3,
                color=YELLOW,
                angle=-PI/3
            )
            self.play(Create(circular))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def demonstrate_dequeue(self):
        with self.voiceover(text="The dequeue operation removes an element from the front of the queue. This operation is fundamental to queue behavior, following the first in first out principle. We must carefully handle several cases to maintain the circular structure and prevent errors when the queue becomes empty.") as tracker:
            title = Text("Dequeue Operation", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Create initial queue with 3 nodes
            node1 = self.create_node_visual("5", LEFT * 2.5 + DOWN * 0.3)
            node2 = self.create_node_visual("10", ORIGIN + DOWN * 0.3)
            node3 = self.create_node_visual("15", RIGHT * 2.5 + DOWN * 0.3)
            
            arrow1 = Arrow(node1[0].get_right(), node2[0].get_left(), buff=0.05, color=WHITE, stroke_width=3)
            arrow2 = Arrow(node2[0].get_right(), node3[0].get_left(), buff=0.05, color=WHITE, stroke_width=3)
            arrow3 = CurvedArrow(
                node3[0].get_bottom() + LEFT * 0.2,
                node1[0].get_bottom() + RIGHT * 0.2,
                color=YELLOW,
                angle=-PI/3
            )
            
            front_pointer = Arrow(UP * 0.8 + LEFT * 4, node1[0].get_top() + LEFT * 0.1, color=GREEN, buff=0.15)
            front_text = Text("Front", font_size=18, color=GREEN).next_to(front_pointer.get_start(), LEFT, buff=0.2)
            
            rear_pointer = Arrow(UP * 0.8 + RIGHT * 4, node3[0].get_top() + RIGHT * 0.1, color=RED, buff=0.15)
            rear_text = Text("Rear", font_size=18, color=RED).next_to(rear_pointer.get_start(), RIGHT, buff=0.2)
            
            self.play(Create(node1), Create(node2), Create(node3))
            self.play(Create(arrow1), Create(arrow2), Create(arrow3))
            self.play(Create(front_pointer), Write(front_text))
            self.play(Create(rear_pointer), Write(rear_text))
            self.wait(1)
        
        with self.voiceover(text="First, we check if the queue is empty by testing if front is None. If empty, we cannot dequeue, so we return an error or None. If not empty, we save the data from the front node to return it later. Then we check if front equals rear, which means we have only one element. In this case, we set both front and rear to None, returning to the empty state.") as tracker:
            step1 = Text("Step 1: Check if empty", font_size=24, color=YELLOW)
            step1.move_to(UP * 1.8)
            self.play(Write(step1))
            self.wait(1)
            
            self.play(FadeOut(step1))
            step2 = Text("Step 2: Save front data", font_size=24, color=YELLOW)
            step2.move_to(UP * 1.8)
            self.play(Write(step2))
            
            saved_data = Text("Data=5", font_size=20, color=GREEN)
            saved_data.move_to(UP * 1.0 + LEFT * 4.5)
            self.play(Write(saved_data))
            self.wait(1)
        
        with self.voiceover(text="If we have more than one element, we move the front pointer to the next node, which is front dot next. Then we update the rear node's next pointer to point to this new front, maintaining the circular link. Finally, we can delete the old front node and return its data. This process efficiently removes the element while preserving the circular structure for all remaining elements.") as tracker:
            self.play(FadeOut(step2))
            step3 = Text("Step 3: Move front pointer", font_size=24, color=YELLOW)
            step3.move_to(UP * 1.8)
            self.play(Write(step3))
            
            # Highlight the node being removed
            remove_rect = SurroundingRectangle(node1, color=RED, buff=0.1)
            self.play(Create(remove_rect))
            
            # Move front pointer
            new_front_pointer = Arrow(UP * 0.8 + LEFT * 1.5, node2[0].get_top() + LEFT * 0.1, color=GREEN, buff=0.15)
            self.play(Transform(front_pointer, new_front_pointer))
            self.play(front_text.animate.shift(RIGHT * 1.5))
            
            # Update circular arrow
            new_circular = CurvedArrow(
                node3[0].get_bottom() + LEFT * 0.2,
                node2[0].get_bottom() + RIGHT * 0.2,
                color=YELLOW,
                angle=-PI/3
            )
            self.play(FadeOut(arrow3), Create(new_circular))
            
            # Remove old node
            self.play(FadeOut(node1), FadeOut(arrow1), FadeOut(remove_rect))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def complete_operation_sequence(self):
        with self.voiceover(text="Let's now observe a complete sequence of operations to see how enqueue and dequeue work together in harmony. We'll start with an empty queue and perform several enqueue operations, followed by some dequeue operations. This will demonstrate how the circular nature maintains efficiency throughout the process.") as tracker:
            title = Text("Complete Operation Sequence", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            operation_text = Text("Starting with empty queue", font_size=24, color=YELLOW)
            operation_text.move_to(UP * 1.8)
            self.play(Write(operation_text))
            
            queue_area = Rectangle(width=10, height=3, color=GRAY)
            queue_area.move_to(DOWN * 0.5)
            self.play(Create(queue_area))
            self.wait(1)
        
        with self.voiceover(text="First, we enqueue the value one. Since the queue is empty, this becomes both front and rear, with its next pointer pointing to itself. Then we enqueue two, which gets added at the rear, and its next points back to one. We continue with three and four, each time maintaining the circular link from the last element back to the first.") as tracker:
            self.play(FadeOut(operation_text))
            
            # Enqueue 1
            op1 = Text("Enqueue(1)", font_size=20, color=GREEN)
            op1.move_to(UP * 1.8 + LEFT * 3)
            self.play(Write(op1))
            
            node1 = self.create_node_visual("1", LEFT * 3 + DOWN * 0.5)
            self.play(Create(node1))
            
            front_ptr = Text("F,R", font_size=16, color=YELLOW).next_to(node1, UP, buff=0.2)
            self.play(Write(front_ptr))
            self.wait(0.5)
            
            # Enqueue 2
            op2 = Text("Enqueue(2)", font_size=20, color=GREEN)
            op2.move_to(UP * 1.8)
            self.play(Write(op2))
            
            node2 = self.create_node_visual("2", LEFT * 1 + DOWN * 0.5)
            arrow1 = Arrow(node1[0].get_right(), node2[0].get_left(), buff=0.05, color=WHITE, stroke_width=2)
            self.play(Create(node2), Create(arrow1))
            
            self.play(FadeOut(front_ptr))
            front_ptr = Text("F", font_size=16, color=GREEN).next_to(node1, UP, buff=0.2)
            rear_ptr = Text("R", font_size=16, color=RED).next_to(node2, UP, buff=0.2)
            self.play(Write(front_ptr), Write(rear_ptr))
            self.wait(0.5)
            
            # Enqueue 3
            op3 = Text("Enqueue(3)", font_size=20, color=GREEN)
            op3.move_to(UP * 1.8 + RIGHT * 3)
            self.play(Write(op3))
            
            node3 = self.create_node_visual("3", RIGHT * 1 + DOWN * 0.5)
            arrow2 = Arrow(node2[0].get_right(), node3[0].get_left(), buff=0.05, color=WHITE, stroke_width=2)
            self.play(Create(node3), Create(arrow2))
            
            self.play(FadeOut(rear_ptr))
            rear_ptr = Text("R", font_size=16, color=RED).next_to(node3, UP, buff=0.2)
            self.play(Write(rear_ptr))
            
            # Circular arrow positioned lower
            circ = CurvedArrow(
                node3[0].get_bottom() + LEFT * 0.3,
                node1[0].get_bottom() + RIGHT * 0.3,
                color=YELLOW,
                angle=-PI/5
            )
            self.play(Create(circ))
            self.wait(1)
        
        with self.voiceover(text="Now let's perform some dequeue operations. We remove the front element, which is one, and update front to point to two. The rear still points to three, and three's next pointer now points to two, maintaining the circular property. We can continue dequeueing, and the structure adapts seamlessly, always maintaining its circular integrity until we're back to an empty state.") as tracker:
            self.play(FadeOut(op1), FadeOut(op2), FadeOut(op3))
            
            deq1 = Text("Dequeue() = 1", font_size=20, color=RED)
            deq1.move_to(UP * 1.8 + LEFT * 2.5)
            self.play(Write(deq1))
            
            remove_box = SurroundingRectangle(node1, color=RED, buff=0.1)
            self.play(Create(remove_box))
            self.play(FadeOut(node1), FadeOut(arrow1), FadeOut(remove_box), FadeOut(front_ptr))
            
            new_front = Text("F", font_size=16, color=GREEN).next_to(node2, UP, buff=0.2)
            self.play(Write(new_front))
            
            # Update circular arrow
            new_circ = CurvedArrow(
                node3[0].get_bottom() + LEFT * 0.2,
                node2[0].get_bottom() + RIGHT * 0.2,
                color=YELLOW,
                angle=-PI/5
            )
            self.play(Transform(circ, new_circ))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def advantages_disadvantages(self):
        with self.voiceover(text="Let's analyze the advantages of using a linked list for circular queue implementation. The primary advantage is dynamic memory allocation. Unlike arrays, we don't need to specify a maximum size upfront. The queue can grow and shrink as needed, using only the memory required for current elements. This makes it highly memory efficient for variable workloads.") as tracker:
            title = Text("Advantages & Disadvantages", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            adv_title = Text("Advantages:", font_size=26, color=GREEN)
            adv_title.move_to(UP * 1.5 + LEFT * 3)
            self.play(Write(adv_title))
            
            advantages = VGroup(
                Text("✓ Dynamic size - no fixed limit", font_size=20, color=WHITE),
                Text("✓ Efficient memory usage", font_size=20, color=WHITE),
                Text("✓ No overflow (if RAM available)", font_size=20, color=WHITE),
                Text("✓ Easy to implement", font_size=20, color=WHITE)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            advantages.move_to(UP * 0.3 + LEFT * 3)
            
            self.play(Write(advantages[0]))
            self.wait(0.5)
            self.play(Write(advantages[1]))
            self.wait(0.5)
            self.play(Write(advantages[2]))
            self.wait(0.5)
            self.play(Write(advantages[3]))
            self.wait(1)
        
        with self.voiceover(text="However, there are some disadvantages to consider. Each node requires extra memory for storing the next pointer, adding overhead compared to arrays. Additionally, we cannot access elements by index in constant time - we must traverse from the front. Memory allocation and deallocation for each operation can be slower than array-based implementations, and the nodes may not be stored contiguously in memory, potentially affecting cache performance.") as tracker:
            disadv_title = Text("Disadvantages:", font_size=26, color=RED)
            disadv_title.move_to(UP * 1.5 + RIGHT * 3.5)
            self.play(Write(disadv_title))
            
            disadvantages = VGroup(
                Text("✗ Extra memory for pointers", font_size=20, color=WHITE),
                Text("✗ No random access", font_size=20, color=WHITE),
                Text("✗ Slower allocation/deallocation", font_size=20, color=WHITE),
                Text("✗ Poor cache locality", font_size=20, color=WHITE)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            disadvantages.move_to(UP * 0.3 + RIGHT * 3.5)
            
            self.play(Write(disadvantages[0]))
            self.wait(0.5)
            self.play(Write(disadvantages[1]))
            self.wait(0.5)
            self.play(Write(disadvantages[2]))
            self.wait(0.5)
            self.play(Write(disadvantages[3]))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def time_complexity_analysis(self):
        with self.voiceover(text="Now let's analyze the time complexity of our circular queue operations. Understanding complexity helps us predict performance and make informed design decisions. For a linked list based circular queue, we'll examine the efficiency of each fundamental operation.") as tracker:
            title = Text("Time Complexity Analysis", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            complexity_table = VGroup()
            
            header = VGroup(
                Text("Operation", font_size=22, color=YELLOW),
                Text("Time", font_size=22, color=YELLOW),
                Text("Reason", font_size=22, color=YELLOW)
            ).arrange(RIGHT, buff=1.2)
            header.move_to(UP * 1.5)
            
            complexity_table.add(header)
            self.play(Write(header))
            self.wait(0.5)
        
        with self.voiceover(text="The enqueue operation runs in constant time, O(1). We simply create a new node and update the rear pointer and one next reference. No matter how many elements are in the queue, this takes the same amount of time. Similarly, dequeue is also O(1) because we only update the front pointer and modify one next reference. We don't need to shift any elements like in an array implementation.") as tracker:
            row1 = VGroup(
                Text("Enqueue", font_size=20, color=WHITE),
                MathTex(r"O(1)", font_size=24, color=GREEN),
                Text("Update pointers only", font_size=18, color=GRAY)
            ).arrange(RIGHT, buff=0.8)
            row1.next_to(header, DOWN, buff=0.4)
            
            row2 = VGroup(
                Text("Dequeue", font_size=20, color=WHITE),
                MathTex(r"O(1)", font_size=24, color=GREEN),
                Text("Update pointers only", font_size=18, color=GRAY)
            ).arrange(RIGHT, buff=0.8)
            row2.next_to(row1, DOWN, buff=0.3)
            
            complexity_table.add(row1, row2)
            self.play(Write(row1))
            self.wait(0.5)
            self.play(Write(row2))
            self.wait(1)
        
        with self.voiceover(text="Checking if the queue is empty is also O(1) - we just check if front is None. Getting the front element without removing it, called peek, is O(1) as we just access front's data. However, if we want to access or search for an arbitrary element, we need O(n) time where n is the number of elements, because we must traverse the linked list from front to rear.") as tracker:
            row3 = VGroup(
                Text("IsEmpty", font_size=20, color=WHITE),
                MathTex(r"O(1)", font_size=24, color=GREEN),
                Text("Check front pointer", font_size=18, color=GRAY)
            ).arrange(RIGHT, buff=0.8)
            row3.next_to(row2, DOWN, buff=0.3)
            
            row4 = VGroup(
                Text("Peek", font_size=20, color=WHITE),
                MathTex(r"O(1)", font_size=24, color=GREEN),
                Text("Access front data", font_size=18, color=GRAY)
            ).arrange(RIGHT, buff=0.75)
            row4.next_to(row3, DOWN, buff=0.3)
            
            row5 = VGroup(
                Text("Search", font_size=20, color=WHITE),
                MathTex(r"O(n)", font_size=24, color=RED),
                Text("Traverse all nodes", font_size=18, color=GRAY)
            ).arrange(RIGHT, buff=0.8)
            row5.next_to(row4, DOWN, buff=0.3)
            
            complexity_table.add(row3, row4, row5)
            self.play(Write(row3))
            self.wait(0.5)
            self.play(Write(row4))
            self.wait(0.5)
            self.play(Write(row5))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def real_world_applications(self):
        with self.voiceover(text="Circular queues implemented with linked lists have numerous real-world applications across computer science and software engineering. Let's explore some of the most important use cases where this data structure provides elegant and efficient solutions.") as tracker:
            title = Text("Real-World Applications", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            app1_title = Text("1. CPU Scheduling", font_size=24, color=YELLOW)
            app1_title.move_to(UP * 1.5 + LEFT * 3.5)
            self.play(Write(app1_title))
            
            # CPU visualization
            cpu = Rectangle(width=1.5, height=1, color=RED, fill_opacity=0.3)
            cpu.move_to(LEFT * 3.5 + UP * 0.2)
            cpu_label = Text("CPU", font_size=18, color=WHITE).move_to(cpu.get_center())
            
            processes = VGroup(
                self.create_node_visual("P1", LEFT * 3.5 + DOWN * 1),
                self.create_node_visual("P2", LEFT * 2.2 + DOWN * 1),
                self.create_node_visual("P3", LEFT * 0.9 + DOWN * 1)
            )
            
            self.play(Create(cpu), Write(cpu_label))
            self.play(Create(processes))
            self.wait(1)
        
        with self.voiceover(text="In operating systems, circular queues manage CPU scheduling using round-robin algorithms. Each process gets a time slice, and after execution, it's moved to the rear of the queue. The circular nature ensures fair distribution of CPU time, with processes continuously cycling through until completion. This prevents starvation and ensures all processes make progress.") as tracker:
            app1_desc = Text("Round-robin scheduling", font_size=18, color=GRAY)
            app1_desc.next_to(processes, DOWN, buff=0.3)
            self.play(Write(app1_desc))
            self.wait(2)
        
        with self.voiceover(text="Another crucial application is in memory management for buffers. Circular queues are perfect for implementing circular buffers used in data streaming, keyboard input buffers, and printer spooling. The producer adds data at the rear while the consumer removes from the front, creating a continuous flow that efficiently handles temporary storage of data in transit.") as tracker:
            self.play(FadeOut(*self.mobjects[1:]))  # Keep title
            
            app2_title = Text("2. Memory Buffers", font_size=24, color=YELLOW)
            app2_title.move_to(UP * 1.5 + RIGHT * 3.5)
            self.play(Write(app2_title))
            
            buffer = Circle(radius=1.2, color=BLUE)
            buffer.move_to(RIGHT * 3.5 + DOWN * 0.3)
            
            producer = Text("Producer", font_size=18, color=GREEN)
            producer.move_to(RIGHT * 2 + UP * 0.5)
            
            consumer = Text("Consumer", font_size=18, color=RED)
            consumer.move_to(RIGHT * 5 + UP * 0.5)
            
            prod_arrow = Arrow(producer.get_bottom(), buffer.get_top() + LEFT * 0.3, color=GREEN, buff=0.1)
            cons_arrow = Arrow(buffer.get_top() + RIGHT * 0.3, consumer.get_bottom(), color=RED, buff=0.1)
            
            self.play(Write(app2_title))
            self.play(Create(buffer))
            self.play(Write(producer), Create(prod_arrow))
            self.play(Write(consumer), Create(cons_arrow))
            
            buffer_desc = Text("Streaming data flow", font_size=18, color=GRAY)
            buffer_desc.move_to(RIGHT * 3.5 + DOWN * 1.8)
            self.play(Write(buffer_desc))
            self.wait(2)
        
        with self.voiceover(text="Additional applications include network packet handling, where routers use circular queues to manage incoming and outgoing packets, and multimedia applications like audio and video players that use circular buffers to ensure smooth playback. The dynamic sizing of linked list implementation makes it particularly suitable for scenarios where the workload varies significantly over time.") as tracker:
            self.play(FadeOut(*self.mobjects[1:]))  # Keep title
            
            other_apps = VGroup(
                Text("• Network Routers - Packet queues", font_size=20, color=WHITE),
                Text("• Media Players - Audio/Video buffering", font_size=20, color=WHITE),
                Text("• Traffic Systems - Vehicle management", font_size=20, color=WHITE),
                Text("• Game Development - Event handling", font_size=20, color=WHITE)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            other_apps.move_to(DOWN * 0.2)
            
            self.play(Write(other_apps))
            self.wait(3)
        
        self.play(FadeOut(*self.mobjects))

    def conclusion(self):
        with self.voiceover(text="We've completed our comprehensive journey through circular queue implementation using linked lists. We've seen how this elegant data structure combines the flexibility of linked lists with the efficiency of circular organization to create a powerful tool for managing sequential data.") as tracker:
            title = Text("Conclusion", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            summary_points = VGroup(
                Text("✓ Dynamic memory allocation", font_size=22, color=GREEN),
                Text("✓ O(1) enqueue and dequeue", font_size=22, color=GREEN),
                Text("✓ Efficient space utilization", font_size=22, color=GREEN),
                Text("✓ Circular structure prevents waste", font_size=22, color=GREEN)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            summary_points.move_to(UP * 0.3)
            
            for point in summary_points:
                self.play(Write(point))
                self.wait(0.5)
        
        with self.voiceover(text="Remember the key operations: enqueue adds at the rear with the new node's next pointing to front, dequeue removes from front while updating the circular link, and both operations run in constant time. The linked list approach gives us flexibility that array-based implementations cannot match, making it ideal for applications with variable or unpredictable workloads.") as tracker:
            key_ops = VGroup(
                Text("Enqueue: Add at rear, maintain circular link", font_size=20, color=YELLOW),
                Text("Dequeue: Remove from front, update pointers", font_size=20, color=YELLOW),
                Text("Both operations: O(1) time complexity", font_size=20, color=YELLOW)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            key_ops.move_to(DOWN * 1.3)
            
            self.play(Write(key_ops))
            self.wait(2)
        
        with self.voiceover(text="Thank you for watching this detailed explanation of circular queues with linked lists. I hope this visualization helped you understand not just how the operations work, but why this data structure is designed the way it is. Practice implementing this yourself, and you'll master one of the fundamental building blocks of computer science. Happy coding!") as tracker:
            self.play(FadeOut(*self.mobjects[1:]))
            
            thank_you = Text("Thank You!", font_size=36, color=GREEN)
            thank_you.move_to(ORIGIN)
            
            final_msg = Text("Keep Learning & Exploring Data Structures!", font_size=24, color=YELLOW)
            final_msg.next_to(thank_you, DOWN, buff=0.6)
            
            self.play(Write(thank_you))
            self.play(Write(final_msg))
            self.wait(3)
        
        self.play(FadeOut(*self.mobjects))