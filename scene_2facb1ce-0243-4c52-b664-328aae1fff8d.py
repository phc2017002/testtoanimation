from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class QueueLinkedListExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        # Introduction
        self.introduction()
        
        # What is a Queue
        self.what_is_queue()
        
        # Queue Operations Overview
        self.queue_operations_overview()
        
        # Linked List Basics
        self.linked_list_basics()
        
        # Why Linked List for Queue
        self.why_linked_list()
        
        # Node Structure
        self.node_structure()
        
        # Enqueue Operation - Detailed
        self.enqueue_operation()
        
        # Dequeue Operation - Detailed
        self.dequeue_operation()
        
        # Complete Example with Multiple Operations
        self.complete_example()
        
        # Time Complexity Analysis
        self.time_complexity_analysis()
        
        # Comparison with Array Implementation
        self.array_vs_linked_list()
        
        # Real World Applications
        self.real_world_applications()
        
        # Conclusion
        self.conclusion()

    def introduction(self):
        with self.voiceover(text="Welcome to this comprehensive tutorial on Queue Implementation using Linked Lists. A queue is one of the most fundamental data structures in computer science, and understanding how to implement it efficiently is crucial for any programmer.") as tracker:
            title = Text("Queue Implementation", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            
            subtitle = Text("Using Linked List", font_size=32, color=GREEN)
            subtitle.next_to(title, DOWN, buff=0.4)
            
            self.play(Write(title))
            self.play(Write(subtitle))
            self.wait(2)
        
        with self.voiceover(text="In this tutorial, we will explore what queues are, why linked lists are an excellent choice for implementing them, and we will visualize every operation step by step. By the end, you will have a complete understanding of queue implementation.") as tracker:
            description = Text(
                "A Deep Dive into Data Structures",
                font_size=24,
                color=YELLOW
            ).next_to(subtitle, DOWN, buff=0.8)
            
            self.play(Write(description))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def what_is_queue(self):
        with self.voiceover(text="Let's begin by understanding what a queue is. A queue is a linear data structure that follows the First In First Out principle, commonly known as FIFO. This means that the first element added to the queue will be the first one to be removed.") as tracker:
            title = Text("What is a Queue?", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            fifo_text = Text("FIFO: First In, First Out", font_size=28, color=GREEN)
            fifo_text.move_to(UP * 1.5)
            self.play(Write(fifo_text))
        
        with self.voiceover(text="Think of a queue like a line of people waiting at a ticket counter. The person who arrives first gets served first, and new people join at the back of the line. This is exactly how a queue data structure works in computer science.") as tracker:
            # Visual representation of people in line
            person1 = Circle(radius=0.3, color=BLUE, fill_opacity=0.5)
            person2 = Circle(radius=0.3, color=BLUE, fill_opacity=0.5)
            person3 = Circle(radius=0.3, color=BLUE, fill_opacity=0.5)
            person4 = Circle(radius=0.3, color=BLUE, fill_opacity=0.5)
            
            label1 = Text("1st", font_size=18).move_to(person1)
            label2 = Text("2nd", font_size=18).move_to(person2)
            label3 = Text("3rd", font_size=18).move_to(person3)
            label4 = Text("4th", font_size=18).move_to(person4)
            
            people = VGroup(
                VGroup(person1, label1),
                VGroup(person2, label2),
                VGroup(person3, label3),
                VGroup(person4, label4)
            ).arrange(RIGHT, buff=0.6)
            people.move_to(DOWN * 0.5)
            
            front_arrow = Arrow(
                start=people[0].get_bottom() + DOWN * 0.5,
                end=people[0].get_bottom(),
                color=RED,
                buff=0.1
            )
            front_label = Text("Front\n(Dequeue)", font_size=20, color=RED)
            front_label.next_to(front_arrow, DOWN, buff=0.2)
            
            rear_arrow = Arrow(
                start=people[3].get_bottom() + DOWN * 0.5,
                end=people[3].get_bottom(),
                color=GREEN,
                buff=0.1
            )
            rear_label = Text("Rear\n(Enqueue)", font_size=20, color=GREEN)
            rear_label.next_to(rear_arrow, DOWN, buff=0.2)
            
            self.play(Create(people))
            self.play(
                Create(front_arrow), Write(front_label),
                Create(rear_arrow), Write(rear_label)
            )
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def queue_operations_overview(self):
        with self.voiceover(text="A queue supports several fundamental operations. The two most important are Enqueue and Dequeue. Enqueue adds an element to the rear of the queue, while Dequeue removes an element from the front. These are the core operations that make a queue useful.") as tracker:
            title = Text("Queue Operations", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            ops_title = Text("Primary Operations:", font_size=28, color=YELLOW)
            ops_title.move_to(UP * 1.8)
            self.play(Write(ops_title))
            
            enqueue = Text("• Enqueue(x): Add element to rear", font_size=24, color=GREEN)
            enqueue.move_to(UP * 0.8)
            
            dequeue = Text("• Dequeue(): Remove element from front", font_size=24, color=RED)
            dequeue.next_to(enqueue, DOWN, buff=0.4, aligned_edge=LEFT)
            
            self.play(Write(enqueue))
            self.play(Write(dequeue))
        
        with self.voiceover(text="Besides these primary operations, queues also support auxiliary operations like Peek, which returns the front element without removing it, isEmpty to check if the queue is empty, and Size to get the number of elements. These helper methods make working with queues much more convenient.") as tracker:
            peek = Text("• Peek(): View front element", font_size=24, color=BLUE)
            peek.next_to(dequeue, DOWN, buff=0.4, aligned_edge=LEFT)
            
            is_empty = Text("• isEmpty(): Check if empty", font_size=24, color=ORANGE)
            is_empty.next_to(peek, DOWN, buff=0.4, aligned_edge=LEFT)
            
            size = Text("• Size(): Get number of elements", font_size=24, color=PURPLE)
            size.next_to(is_empty, DOWN, buff=0.4, aligned_edge=LEFT)
            
            self.play(Write(peek))
            self.play(Write(is_empty))
            self.play(Write(size))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def linked_list_basics(self):
        with self.voiceover(text="Before we implement a queue using a linked list, let's review what a linked list is. A linked list is a dynamic data structure where each element, called a node, contains data and a reference or pointer to the next node in the sequence.") as tracker:
            title = Text("Linked List Basics", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            description = Text(
                "A chain of connected nodes",
                font_size=26,
                color=YELLOW
            ).move_to(UP * 2.0)
            self.play(Write(description))
        
        with self.voiceover(text="Each node in a linked list has two parts: the data field which stores the actual value, and the next field which points to the next node. The last node's next field points to null, indicating the end of the list. This structure allows for efficient insertion and deletion operations.") as tracker:
            # Create three nodes
            node1_rect = Rectangle(width=1.5, height=0.8, color=GREEN)
            node1_data = Text("10", font_size=22).move_to(node1_rect.get_left() + RIGHT * 0.4)
            node1_next = Square(side_length=0.4, color=WHITE).move_to(node1_rect.get_right() + LEFT * 0.3)
            node1 = VGroup(node1_rect, node1_data, node1_next)
            
            node2_rect = Rectangle(width=1.5, height=0.8, color=GREEN)
            node2_data = Text("20", font_size=22).move_to(node2_rect.get_left() + RIGHT * 0.4)
            node2_next = Square(side_length=0.4, color=WHITE).move_to(node2_rect.get_right() + LEFT * 0.3)
            node2 = VGroup(node2_rect, node2_data, node2_next)
            
            node3_rect = Rectangle(width=1.5, height=0.8, color=GREEN)
            node3_data = Text("30", font_size=22).move_to(node3_rect.get_left() + RIGHT * 0.4)
            node3_next = Square(side_length=0.4, color=WHITE).move_to(node3_rect.get_right() + LEFT * 0.3)
            node3 = VGroup(node3_rect, node3_data, node3_next)
            
            # Arrange nodes
            nodes = VGroup(node1, node2, node3).arrange(RIGHT, buff=0.8)
            nodes.move_to(DOWN * 0.3)
            
            # Arrows between nodes
            arrow1 = Arrow(
                start=node1_next.get_right(),
                end=node2_rect.get_left(),
                color=YELLOW,
                buff=0.1
            )
            arrow2 = Arrow(
                start=node2_next.get_right(),
                end=node3_rect.get_left(),
                color=YELLOW,
                buff=0.1
            )
            
            # Null indicator with increased buffer to prevent overlap
            null_text = Text("NULL", font_size=20, color=RED)
            null_text.next_to(node3_next, RIGHT, buff=1.2)
            
            # Labels
            data_label = Text("Data", font_size=18, color=BLUE).next_to(node1_data, DOWN, buff=0.5)
            next_label = Text("Next", font_size=18, color=BLUE).next_to(node1_next, DOWN, buff=0.5)
            
            self.play(Create(nodes))
            self.play(Create(arrow1), Create(arrow2))
            self.play(Write(null_text))
            self.play(Write(data_label), Write(next_label))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def why_linked_list(self):
        with self.voiceover(text="You might wonder why we use a linked list to implement a queue instead of an array. There are several compelling reasons. First, linked lists provide dynamic size, meaning the queue can grow or shrink as needed without pre-allocating memory like arrays require.") as tracker:
            title = Text("Why Linked List for Queue?", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            advantage1 = Text("✓ Dynamic Size - No Fixed Capacity", font_size=24, color=GREEN)
            advantage1.move_to(UP * 1.5)
            self.play(Write(advantage1))
        
        with self.voiceover(text="Second, both enqueue and dequeue operations have constant time complexity, O of one, when using a linked list. We simply update pointers at the front or rear. With arrays, dequeue would require shifting all elements, making it O of n, which is much slower for large queues.") as tracker:
            advantage2 = Text("✓ O(1) Enqueue and Dequeue", font_size=24, color=GREEN)
            advantage2.next_to(advantage1, DOWN, buff=0.5, aligned_edge=LEFT)
            self.play(Write(advantage2))
            
            complexity = MathTex(r"\text{Enqueue: } O(1), \quad \text{Dequeue: } O(1)")
            complexity.scale(0.8)
            complexity.next_to(advantage2, DOWN, buff=0.4)
            self.play(Write(complexity))
        
        with self.voiceover(text="Third, linked lists make efficient use of memory. Each node only allocates memory when created, and we can free memory immediately when nodes are removed. Arrays often waste space with unused capacity, or require expensive resizing operations when they fill up.") as tracker:
            advantage3 = Text("✓ Efficient Memory Usage", font_size=24, color=GREEN)
            advantage3.next_to(complexity, DOWN, buff=0.6, aligned_edge=LEFT)
            self.play(Write(advantage3))
            
            advantage4 = Text("✓ No Wasted Space", font_size=24, color=GREEN)
            advantage4.next_to(advantage3, DOWN, buff=0.4, aligned_edge=LEFT)
            self.play(Write(advantage4))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def node_structure(self):
        with self.voiceover(text="Now let's examine the structure of a node in detail. Each node is a simple object or structure that contains two fields. The data field stores the actual element value, which can be of any data type such as integer, string, or even a complex object.") as tracker:
            title = Text("Node Structure", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            subtitle = Text("Building Block of Linked List Queue", font_size=26, color=YELLOW)
            subtitle.next_to(title, DOWN, buff=0.3)
            self.play(Write(subtitle))
        
        with self.voiceover(text="The second field is the next pointer, which holds the memory address of the next node in the queue. For the last node, this next pointer is set to null, indicating there are no more nodes after it. Let's visualize this structure with code.") as tracker:
            # Code representation
            code = Code(
                code="""class Node:
    def __init__(self, data):
        self.data = data
        self.next = None""",
                language="python",
                font_size=20,
                background="window",
                insert_line_no=False
            )
            code.scale(0.9)
            code.move_to(DOWN * 0.2)
            
            self.play(Create(code))
            self.wait(2)
        
        with self.voiceover(text="Here's the visual representation. The rectangular box on the left represents the data field, and the small square on the right represents the next pointer. When we create a new node, we initialize the data with the provided value, and set next to null by default.") as tracker:
            # Visual node
            node_rect = Rectangle(width=1.8, height=1.0, color=GREEN)
            node_rect.move_to(UP * 1.2)
            
            data_section = Rectangle(width=1.0, height=1.0, color=BLUE)
            data_section.move_to(node_rect.get_left() + RIGHT * 0.5)
            
            next_section = Square(side_length=0.6, color=YELLOW)
            next_section.move_to(node_rect.get_right() + LEFT * 0.4)
            
            data_text = Text("data", font_size=20, color=WHITE).move_to(data_section)
            next_text = Text("next", font_size=18, color=WHITE).move_to(next_section)
            
            data_label = Text("Data Field", font_size=18, color=BLUE)
            data_label.next_to(data_section, DOWN, buff=0.3)
            
            next_label = Text("Next Pointer", font_size=18, color=YELLOW)
            next_label.next_to(next_section, DOWN, buff=0.3)
            
            visual_node = VGroup(node_rect, data_section, next_section, data_text, next_text)
            
            self.play(FadeOut(code))
            self.play(Create(visual_node))
            self.play(Write(data_label), Write(next_label))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def enqueue_operation(self):
        with self.voiceover(text="Let's now explore the enqueue operation in detail. Enqueue adds a new element to the rear of the queue. This is one of the two fundamental operations. We'll visualize this step by step to understand exactly what happens during an enqueue.") as tracker:
            title = Text("Enqueue Operation", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            definition = Text("Adding element to the rear", font_size=26, color=GREEN)
            definition.next_to(title, DOWN, buff=0.3)
            self.play(Write(definition))
        
        with self.voiceover(text="The algorithm for enqueue is straightforward. First, we create a new node with the data. Second, if the queue is empty, meaning both front and rear are null, we set both front and rear to point to this new node. This handles the special case of the first element.") as tracker:
            steps = VGroup(
                Text("1. Create new node with data", font_size=22, color=YELLOW),
                Text("2. If queue is empty:", font_size=22, color=YELLOW),
                Text("   • Set front = new node", font_size=20, color=WHITE),
                Text("   • Set rear = new node", font_size=20, color=WHITE),
                Text("3. Else:", font_size=22, color=YELLOW),
                Text("   • Set rear.next = new node", font_size=20, color=WHITE),
                Text("   • Set rear = new node", font_size=20, color=WHITE)
            )
            steps.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            steps.move_to(DOWN * 0.5)
            
            for step in steps:
                self.play(Write(step), run_time=0.8)
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Now let's visualize this with an example. We'll start with an empty queue and enqueue the values ten, twenty, and thirty. Watch carefully how the front and rear pointers are updated at each step.") as tracker:
            title = Text("Enqueue Visualization", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Empty queue
            front_label = Text("Front: NULL", font_size=24, color=RED)
            front_label.move_to(LEFT * 4 + UP * 1.5)
            rear_label = Text("Rear: NULL", font_size=24, color=GREEN)
            rear_label.move_to(RIGHT * 4 + UP * 1.5)
            
            self.play(Write(front_label), Write(rear_label))
            self.wait(1)
            
            # Enqueue 10
            status = Text("Enqueue(10)", font_size=28, color=YELLOW)
            status.move_to(UP * 0.5)
            self.play(Write(status))
            
            node1_rect = Rectangle(width=1.5, height=0.8, color=GREEN)
            node1_data = Text("10", font_size=22).move_to(node1_rect.get_left() + RIGHT * 0.4)
            node1_next = Square(side_length=0.4, color=WHITE).move_to(node1_rect.get_right() + LEFT * 0.3)
            node1 = VGroup(node1_rect, node1_data, node1_next)
            node1.move_to(DOWN * 1.0)
            
            null1 = Text("NULL", font_size=18, color=RED)
            null1.next_to(node1_next, RIGHT, buff=0.2)
            
            self.play(Create(node1), Write(null1))
            
            new_front = Text("Front: 10", font_size=24, color=RED)
            new_front.move_to(front_label.get_center())
            new_rear = Text("Rear: 10", font_size=24, color=GREEN)
            new_rear.move_to(rear_label.get_center())
            
            self.play(Transform(front_label, new_front), Transform(rear_label, new_rear))
            self.wait(2)
        
        with self.voiceover(text="Now let's enqueue twenty. Since the queue is not empty, we link the current rear node's next pointer to the new node, then update rear to point to the new node. The front pointer remains unchanged because we're adding to the rear.") as tracker:
            new_status = Text("Enqueue(20)", font_size=28, color=YELLOW)
            new_status.move_to(status.get_center())
            self.play(Transform(status, new_status))
            
            node2_rect = Rectangle(width=1.5, height=0.8, color=GREEN)
            node2_data = Text("20", font_size=22).move_to(node2_rect.get_left() + RIGHT * 0.4)
            node2_next = Square(side_length=0.4, color=WHITE).move_to(node2_rect.get_right() + LEFT * 0.3)
            node2 = VGroup(node2_rect, node2_data, node2_next)
            node2.next_to(node1, RIGHT, buff=1.2)
            
            null2 = Text("NULL", font_size=18, color=RED)
            null2.next_to(node2_next, RIGHT, buff=0.2)
            
            arrow1 = Arrow(
                start=node1_next.get_right(),
                end=node2_rect.get_left(),
                color=YELLOW,
                buff=0.1
            )
            
            self.play(FadeOut(null1))
            self.play(Create(node2), Write(null2), Create(arrow1))
            
            newest_rear = Text("Rear: 20", font_size=24, color=GREEN)
            newest_rear.move_to(rear_label.get_center())
            self.play(Transform(rear_label, newest_rear))
            self.wait(2)
        
        with self.voiceover(text="Finally, let's enqueue thirty using the same process. We update the current rear's next pointer, then move the rear pointer to the new node. Notice how the queue grows dynamically, and all operations are constant time.") as tracker:
            final_status = Text("Enqueue(30)", font_size=28, color=YELLOW)
            final_status.move_to(status.get_center())
            self.play(Transform(status, final_status))
            
            node3_rect = Rectangle(width=1.5, height=0.8, color=GREEN)
            node3_data = Text("30", font_size=22).move_to(node3_rect.get_left() + RIGHT * 0.4)
            node3_next = Square(side_length=0.4, color=WHITE).move_to(node3_rect.get_right() + LEFT * 0.3)
            node3 = VGroup(node3_rect, node3_data, node3_next)
            node3.next_to(node2, RIGHT, buff=1.2)
            
            null3 = Text("NULL", font_size=18, color=RED)
            null3.next_to(node3_next, RIGHT, buff=1.2)
            
            arrow2 = Arrow(
                start=node2_next.get_right(),
                end=node3_rect.get_left(),
                color=YELLOW,
                buff=0.1
            )
            
            self.play(FadeOut(null2))
            self.play(Create(node3), Write(null3), Create(arrow2))
            
            final_rear = Text("Rear: 30", font_size=24, color=GREEN)
            final_rear.move_to(rear_label.get_center())
            self.play(Transform(rear_label, final_rear))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def dequeue_operation(self):
        with self.voiceover(text="Now let's examine the dequeue operation, which removes and returns the element at the front of the queue. This operation is crucial for maintaining the FIFO property. We need to be careful to handle edge cases like an empty queue.") as tracker:
            title = Text("Dequeue Operation", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            definition = Text("Removing element from the front", font_size=26, color=RED)
            definition.next_to(title, DOWN, buff=0.3)
            self.play(Write(definition))
        
        with self.voiceover(text="The dequeue algorithm has several steps. First, we check if the queue is empty by verifying if front is null. If it is, we return an error or null. Otherwise, we store the data from the front node, move the front pointer to the next node, and if the queue becomes empty, we also set rear to null.") as tracker:
            steps = VGroup(
                Text("1. Check if queue is empty", font_size=22, color=YELLOW),
                Text("   • If yes, return error", font_size=20, color=WHITE),
                Text("2. Store data from front node", font_size=22, color=YELLOW),
                Text("3. Move front = front.next", font_size=22, color=YELLOW),
                Text("4. If front becomes NULL:", font_size=22, color=YELLOW),
                Text("   • Set rear = NULL", font_size=20, color=WHITE),
                Text("5. Return stored data", font_size=22, color=YELLOW)
            )
            steps.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            steps.move_to(DOWN * 0.3)
            
            for step in steps:
                self.play(Write(step), run_time=0.8)
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Let's visualize dequeue with our existing queue containing ten, twenty, and thirty. Watch how the front pointer moves and how we maintain the integrity of the queue structure during removal.") as tracker:
            title = Text("Dequeue Visualization", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Recreate the queue with 10, 20, 30
            front_label = Text("Front: 10", font_size=24, color=RED)
            front_label.move_to(LEFT * 4 + UP * 1.5)
            rear_label = Text("Rear: 30", font_size=24, color=GREEN)
            rear_label.move_to(RIGHT * 4 + UP * 1.5)
            
            node1_rect = Rectangle(width=1.5, height=0.8, color=GREEN)
            node1_data = Text("10", font_size=22).move_to(node1_rect.get_left() + RIGHT * 0.4)
            node1_next = Square(side_length=0.4, color=WHITE).move_to(node1_rect.get_right() + LEFT * 0.3)
            node1 = VGroup(node1_rect, node1_data, node1_next)
            
            node2_rect = Rectangle(width=1.5, height=0.8, color=GREEN)
            node2_data = Text("20", font_size=22).move_to(node2_rect.get_left() + RIGHT * 0.4)
            node2_next = Square(side_length=0.4, color=WHITE).move_to(node2_rect.get_right() + LEFT * 0.3)
            node2 = VGroup(node2_rect, node2_data, node2_next)
            
            node3_rect = Rectangle(width=1.5, height=0.8, color=GREEN)
            node3_data = Text("30", font_size=22).move_to(node3_rect.get_left() + RIGHT * 0.4)
            node3_next = Square(side_length=0.4, color=WHITE).move_to(node3_rect.get_right() + LEFT * 0.3)
            node3 = VGroup(node3_rect, node3_data, node3_next)
            
            nodes = VGroup(node1, node2, node3).arrange(RIGHT, buff=1.2)
            nodes.move_to(DOWN * 1.0)
            
            arrow1 = Arrow(start=node1_next.get_right(), end=node2_rect.get_left(), color=YELLOW, buff=0.1)
            arrow2 = Arrow(start=node2_next.get_right(), end=node3_rect.get_left(), color=YELLOW, buff=0.1)
            null_text = Text("NULL", font_size=18, color=RED).next_to(node3_next, RIGHT, buff=1.2)
            
            self.play(Write(front_label), Write(rear_label))
            self.play(Create(nodes), Create(arrow1), Create(arrow2), Write(null_text))
            self.wait(1)
            
            status_text = Text("Dequeue() ", font_size=28, color=YELLOW)
            status_arrow = MathTex(r"\rightarrow", font_size=28)
            status_returns = Text(" Returns ", font_size=28, color=YELLOW)
            status_value = Text("10", font_size=28, color=WHITE)
            
            status = VGroup(status_text, status_arrow, status_returns, status_value).arrange(RIGHT, buff=0.15)
            status.move_to(UP * 0.5)
            self.play(Write(status))
            self.wait(1)
        
        with self.voiceover(text="When we dequeue, we remove the front node containing ten. The front pointer now moves to point to the node with twenty. The removed node is freed from memory. Notice that the rear pointer stays unchanged because we only modified the front.") as tracker:
            # Highlight node being removed
            highlight = SurroundingRectangle(node1, color=RED, buff=0.1)
            self.play(Create(highlight))
            self.wait(1)
            
            # Remove first node and arrow
            self.play(FadeOut(node1), FadeOut(arrow1), FadeOut(highlight))
            
            # Update front label
            new_front = Text("Front: 20", font_size=24, color=RED)
            new_front.move_to(front_label.get_center())
            self.play(Transform(front_label, new_front))
            self.wait(2)
        
        with self.voiceover(text="Let's dequeue again to remove twenty. The same process occurs: we remove the front node, update the front pointer to the next node, and the queue now only contains thirty. The rear pointer still points to the last node correctly.") as tracker:
            new_status_text = Text("Dequeue() ", font_size=28, color=YELLOW)
            new_status_arrow = MathTex(r"\rightarrow", font_size=28)
            new_status_returns = Text(" Returns ", font_size=28, color=YELLOW)
            new_status_value = Text("20", font_size=28, color=WHITE)
            
            new_status = VGroup(new_status_text, new_status_arrow, new_status_returns, new_status_value).arrange(RIGHT, buff=0.15)
            new_status.move_to(status.get_center())
            self.play(Transform(status, new_status))
            
            highlight2 = SurroundingRectangle(node2, color=RED, buff=0.1)
            self.play(Create(highlight2))
            self.wait(1)
            
            self.play(FadeOut(node2), FadeOut(arrow2), FadeOut(highlight2))
            
            newest_front = Text("Front: 30", font_size=24, color=RED)
            newest_front.move_to(front_label.get_center())
            self.play(Transform(front_label, newest_front))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def complete_example(self):
        with self.voiceover(text="Let's now walk through a complete example with multiple enqueue and dequeue operations. This will demonstrate how the queue behaves in a realistic scenario and reinforce your understanding of both operations working together.") as tracker:
            title = Text("Complete Example", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            subtitle = Text("Multiple Operations", font_size=28, color=YELLOW)
            subtitle.next_to(title, DOWN, buff=0.3)
            self.play(Write(subtitle))
        
        with self.voiceover(text="We'll start with an empty queue and perform the following sequence: Enqueue five, Enqueue fifteen, Dequeue, Enqueue twenty-five, Enqueue thirty-five, Dequeue, and finally Dequeue again. This sequence shows how elements flow through the queue.") as tracker:
            operations = VGroup(
                Text("Operations Sequence:", font_size=24, color=GREEN),
                Text("1. Enqueue(5)", font_size=22, color=WHITE),
                Text("2. Enqueue(15)", font_size=22, color=WHITE),
                Text("3. Dequeue() → 5", font_size=22, color=RED),
                Text("4. Enqueue(25)", font_size=22, color=WHITE),
                Text("5. Enqueue(35)", font_size=22, color=WHITE),
                Text("6. Dequeue() → 15", font_size=22, color=RED),
                Text("7. Dequeue() → 25", font_size=22, color=RED)
            )
            operations.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            operations.move_to(DOWN * 0.3)
            
            for op in operations:
                self.play(Write(op), run_time=0.6)
            self.wait(3)
        
        self.play(FadeOut(*self.mobjects))
        
        # Now animate the sequence
        with self.voiceover(text="Let's execute this step by step. Starting with an empty queue, we enqueue five as the first element. Both front and rear point to this node.") as tracker:
            title = Text("Step-by-Step Execution", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            current_op = Text("Enqueue(5)", font_size=26, color=YELLOW)
            current_op.move_to(UP * 1.8)
            self.play(Write(current_op))
            
            front_label = Text("F", font_size=20, color=RED)
            front_label.move_to(LEFT * 5.5 + DOWN * 0.5)
            rear_label = Text("R", font_size=20, color=GREEN)
            rear_label.move_to(LEFT * 5.5 + DOWN * 1.2)
            
            node1 = self.create_queue_node("5")
            node1.move_to(LEFT * 3 + DOWN * 0.8)
            
            front_arrow = Arrow(front_label.get_right(), node1.get_left(), color=RED, buff=0.1, stroke_width=3)
            rear_arrow = Arrow(rear_label.get_right(), node1.get_left(), color=GREEN, buff=0.1, stroke_width=3)
            
            self.play(Write(front_label), Write(rear_label))
            self.play(Create(node1))
            self.play(Create(front_arrow), Create(rear_arrow))
            self.wait(1)
        
        with self.voiceover(text="Next, we enqueue fifteen. The rear pointer updates to point to the new node, while front remains at five.") as tracker:
            op2 = Text("Enqueue(15)", font_size=26, color=YELLOW)
            op2.move_to(current_op.get_center())
            self.play(Transform(current_op, op2))
            
            node2 = self.create_queue_node("15")
            node2.next_to(node1, RIGHT, buff=1.0)
            
            link1 = Arrow(node1[2].get_right(), node2[0].get_left(), color=YELLOW, buff=0.1)
            
            self.play(Create(node2), Create(link1))
            
            # Update rear arrow
            new_rear_arrow = Arrow(rear_label.get_right(), node2.get_left(), color=GREEN, buff=0.1, stroke_width=3)
            self.play(Transform(rear_arrow, new_rear_arrow))
            self.wait(1)
        
        with self.voiceover(text="Now we dequeue, removing five from the front. The front pointer moves to fifteen.") as tracker:
            op3 = Text("Dequeue() → 5", font_size=26, color=RED)
            op3.move_to(current_op.get_center())
            self.play(Transform(current_op, op3))
            
            self.play(
                FadeOut(node1),
                FadeOut(link1),
                FadeOut(front_arrow)
            )
            
            new_front_arrow = Arrow(front_label.get_right(), node2.get_left(), color=RED, buff=0.1, stroke_width=3)
            self.play(Create(new_front_arrow))
            front_arrow = new_front_arrow
            self.wait(1)
        
        with self.voiceover(text="We continue by enqueueing twenty-five and then thirty-five, extending the queue at the rear.") as tracker:
            op4 = Text("Enqueue(25)", font_size=26, color=YELLOW)
            op4.move_to(current_op.get_center())
            self.play(Transform(current_op, op4))
            
            node3 = self.create_queue_node("25")
            node3.next_to(node2, RIGHT, buff=1.0)
            link2 = Arrow(node2[2].get_right(), node3[0].get_left(), color=YELLOW, buff=0.1)
            
            self.play(Create(node3), Create(link2))
            
            new_rear_arrow2 = Arrow(rear_label.get_right(), node3.get_left(), color=GREEN, buff=0.1, stroke_width=3)
            self.play(Transform(rear_arrow, new_rear_arrow2))
            self.wait(1)
            
            op5 = Text("Enqueue(35)", font_size=26, color=YELLOW)
            op5.move_to(current_op.get_center())
            self.play(Transform(current_op, op5))
            
            node4 = self.create_queue_node("35")
            node4.next_to(node3, RIGHT, buff=1.0)
            link3 = Arrow(node3[2].get_right(), node4[0].get_left(), color=YELLOW, buff=0.1)
            
            self.play(Create(node4), Create(link3))
            
            new_rear_arrow3 = Arrow(rear_label.get_right(), node4.get_left(), color=GREEN, buff=0.1, stroke_width=3)
            self.play(Transform(rear_arrow, new_rear_arrow3))
            self.wait(1)
        
        with self.voiceover(text="Finally, we perform two consecutive dequeue operations, removing fifteen and then twenty-five. The queue now contains only thirty-five, with both front and rear pointing to this single node.") as tracker:
            op6 = Text("Dequeue() → 15", font_size=26, color=RED)
            op6.move_to(current_op.get_center())
            self.play(Transform(current_op, op6))
            
            self.play(FadeOut(node2), FadeOut(link2), FadeOut(front_arrow))
            new_front_arrow2 = Arrow(front_label.get_right(), node3.get_left(), color=RED, buff=0.1, stroke_width=3)
            self.play(Create(new_front_arrow2))
            front_arrow = new_front_arrow2
            self.wait(1)
            
            op7 = Text("Dequeue() → 25", font_size=26, color=RED)
            op7.move_to(current_op.get_center())
            self.play(Transform(current_op, op7))
            
            self.play(FadeOut(node3), FadeOut(link3), FadeOut(front_arrow))
            final_front_arrow = Arrow(front_label.get_right(), node4.get_left(), color=RED, buff=0.1, stroke_width=3)
            self.play(Create(final_front_arrow))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def create_queue_node(self, value):
        """Helper method to create a queue node with value"""
        node_rect = Rectangle(width=1.2, height=0.7, color=GREEN)
        node_data = Text(value, font_size=20).move_to(node_rect.get_left() + RIGHT * 0.35)
        node_next = Square(side_length=0.35, color=WHITE).move_to(node_rect.get_right() + LEFT * 0.25)
        return VGroup(node_rect, node_data, node_next)

    def time_complexity_analysis(self):
        with self.voiceover(text="Let's analyze the time complexity of our queue operations. Understanding complexity is crucial for evaluating the efficiency of our implementation and comparing it with other approaches.") as tracker:
            title = Text("Time Complexity Analysis", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
        
        with self.voiceover(text="The enqueue operation has a time complexity of O of one, meaning it takes constant time regardless of queue size. We simply create a node and update the rear pointer. No iteration or searching is required, making it extremely efficient.") as tracker:
            enqueue_title = Text("Enqueue Operation", font_size=28, color=GREEN)
            enqueue_title.move_to(UP * 1.8)
            self.play(Write(enqueue_title))
            
            enqueue_complexity = MathTex(r"\text{Time Complexity: } O(1)")
            enqueue_complexity.scale(0.9)
            enqueue_complexity.next_to(enqueue_title, DOWN, buff=0.4)
            self.play(Write(enqueue_complexity))
            
            enqueue_steps = Text("• Create node: O(1)\n• Update rear pointer: O(1)", font_size=22)
            enqueue_steps.next_to(enqueue_complexity, DOWN, buff=0.4)
            self.play(Write(enqueue_steps))
            self.wait(2)
        
        with self.voiceover(text="Similarly, the dequeue operation also has O of one time complexity. We simply access the front node, update the front pointer to the next node, and return the data. Again, no iteration is needed, just direct pointer manipulation.") as tracker:
            self.play(FadeOut(enqueue_title), FadeOut(enqueue_complexity), FadeOut(enqueue_steps))
            
            dequeue_title = Text("Dequeue Operation", font_size=28, color=RED)
            dequeue_title.move_to(UP * 1.8)
            self.play(Write(dequeue_title))
            
            dequeue_complexity = MathTex(r"\text{Time Complexity: } O(1)")
            dequeue_complexity.scale(0.9)
            dequeue_complexity.next_to(dequeue_title, DOWN, buff=0.4)
            self.play(Write(dequeue_complexity))
            
            dequeue_steps = Text("• Access front: O(1)\n• Update front pointer: O(1)\n• Return data: O(1)", font_size=22)
            dequeue_steps.next_to(dequeue_complexity, DOWN, buff=0.4)
            self.play(Write(dequeue_steps))
            self.wait(2)
        
        with self.voiceover(text="Other operations like peek, isEmpty, and size are also O of one. Peek just returns front's data, isEmpty checks if front is null, and if we maintain a size variable, getting the size is also constant time. This makes linked list queues highly efficient.") as tracker:
            self.play(FadeOut(dequeue_title), FadeOut(dequeue_complexity), FadeOut(dequeue_steps))
            
            other_ops = VGroup(
                Text("Other Operations:", font_size=26, color=YELLOW),
                MathTex(r"\text{Peek(): } O(1)"),
                MathTex(r"\text{isEmpty(): } O(1)"),
                MathTex(r"\text{Size(): } O(1)")
            )
            other_ops.arrange(DOWN, buff=0.4)
            other_ops.move_to(DOWN * 0.2)
            
            for item in other_ops:
                self.play(Write(item), run_time=0.8)
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def array_vs_linked_list(self):
        with self.voiceover(text="Now let's compare queue implementation using arrays versus linked lists. This comparison will help you understand when to choose each approach based on your specific requirements and constraints.") as tracker:
            title = Text("Array vs Linked List Implementation", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
        
        with self.voiceover(text="Array-based queues have a fixed size, requiring pre-allocation of memory. This can lead to wasted space if the queue is not full, or overflow errors if it fills up. Linked list queues, however, grow and shrink dynamically, using exactly the memory needed at any time.") as tracker:
            array_label = Text("Array Queue", font_size=26, color=RED)
            array_label.move_to(LEFT * 3.5 + UP * 2.2)
            
            linked_label = Text("Linked List Queue", font_size=26, color=GREEN)
            linked_label.move_to(RIGHT * 3.5 + UP * 2.2)
            
            self.play(Write(array_label), Write(linked_label))
            
            # Size comparison
            array_size = Text("✗ Fixed Size", font_size=22, color=RED)
            array_size.move_to(LEFT * 3.5 + UP * 1.3)
            
            linked_size = Text("✓ Dynamic Size", font_size=22, color=GREEN)
            linked_size.move_to(RIGHT * 3.5 + UP * 1.3)
            
            self.play(Write(array_size), Write(linked_size))
            self.wait(2)
        
        with self.voiceover(text="For dequeue operations, arrays require shifting all remaining elements forward, giving O of n time complexity. Linked lists simply update a pointer, achieving O of one. This makes a huge difference for large queues with frequent dequeue operations.") as tracker:
            # Dequeue comparison
            array_dequeue = Text("✗ Dequeue: O(n)", font_size=22, color=RED)
            array_dequeue.move_to(LEFT * 3.5 + UP * 0.5)
            
            linked_dequeue = Text("✓ Dequeue: O(1)", font_size=22, color=GREEN)
            linked_dequeue.move_to(RIGHT * 3.5 + UP * 0.5)
            
            array_note = Text("(needs shifting)", font_size=18, color=ORANGE)
            array_note.next_to(array_dequeue, DOWN, buff=0.2)
            
            self.play(Write(array_dequeue), Write(linked_dequeue), Write(array_note))
            self.wait(2)
        
        with self.voiceover(text="Arrays do have advantages though. They offer better cache locality because elements are stored contiguously in memory, leading to faster access in practice. Arrays also have no pointer overhead, while linked lists need extra memory for the next pointer in each node.") as tracker:
            # Memory comparison
            array_memory = Text("✓ Cache Friendly", font_size=22, color=GREEN)
            array_memory.move_to(LEFT * 3.5 + DOWN * 0.5)
            
            linked_memory = Text("✗ Pointer Overhead", font_size=22, color=RED)
            linked_memory.move_to(RIGHT * 3.5 + DOWN * 0.5)
            
            array_overhead = Text("✓ No Overhead", font_size=22, color=GREEN)
            array_overhead.move_to(LEFT * 3.5 + DOWN * 1.3)
            
            linked_flexible = Text("✓ No Wasted Space", font_size=22, color=GREEN)
            linked_flexible.move_to(RIGHT * 3.5 + DOWN * 1.3)
            
            self.play(
                Write(array_memory), Write(linked_memory),
                Write(array_overhead), Write(linked_flexible)
            )
            self.wait(2)
        
        with self.voiceover(text="In summary, use linked lists when you need dynamic sizing and efficient dequeue operations. Use arrays when you know the maximum size, need cache-friendly access patterns, or want to minimize memory overhead. The choice depends on your specific use case.") as tracker:
            conclusion = Text("Choose based on your needs!", font_size=24, color=YELLOW)
            conclusion.move_to(DOWN * 2.3)
            self.play(Write(conclusion))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def real_world_applications(self):
        with self.voiceover(text="Queues are everywhere in computer science and real-world applications. Let's explore some practical scenarios where queue data structures are essential for solving problems efficiently.") as tracker:
            title = Text("Real-World Applications", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
        
        with self.voiceover(text="One major application is in operating systems for process scheduling. When multiple processes need CPU time, they are placed in a queue. The CPU scheduler removes processes from the front of the queue in a fair, first-come-first-served manner, ensuring all processes get their turn.") as tracker:
            app1_title = Text("1. Process Scheduling", font_size=28, color=GREEN)
            app1_title.move_to(UP * 2.0)
            self.play(Write(app1_title))
            
            app1_desc = Text("OS manages CPU time for processes", font_size=22)
            app1_desc.next_to(app1_title, DOWN, buff=0.3)
            self.play(Write(app1_desc))
            
            # Visual representation
            process_queue = VGroup(
                Text("P1", font_size=18, color=BLUE),
                Text("P2", font_size=18, color=BLUE),
                Text("P3", font_size=18, color=BLUE),
                Text("P4", font_size=18, color=BLUE)
            ).arrange(RIGHT, buff=0.5)
            process_queue.move_to(UP * 0.8)
            
            cpu_label = Text("CPU", font_size=20, color=RED)
            cpu_label.next_to(process_queue[0], LEFT, buff=0.8)
            
            self.play(Create(process_queue), Write(cpu_label))
            self.wait(2)
            self.play(FadeOut(process_queue), FadeOut(cpu_label), FadeOut(app1_desc))
        
        with self.voiceover(text="Another important application is in printer spooling. When multiple print jobs are sent to a printer, they are queued. The printer processes them one by one in the order they were received, preventing chaos and ensuring fairness.") as tracker:
            app2_title = Text("2. Printer Queue", font_size=28, color=GREEN)
            app2_title.move_to(UP * 2.0)
            self.play(Transform(app1_title, app2_title))
            
            app2_desc = Text("Print jobs processed in order", font_size=22)
            app2_desc.move_to(UP * 1.3)
            self.play(Write(app2_desc))
            
            print_jobs = VGroup(
                Text("Doc1", font_size=18, color=PURPLE),
                Text("Doc2", font_size=18, color=PURPLE),
                Text("Doc3", font_size=18, color=PURPLE)
            ).arrange(RIGHT, buff=0.6)
            print_jobs.move_to(UP * 0.5)
            
            self.play(Create(print_jobs))
            self.wait(2)
            self.play(FadeOut(print_jobs), FadeOut(app2_desc))
        
        with self.voiceover(text="Queues are also fundamental in networking. Data packets are queued in routers and switches before being transmitted. This ensures orderly data flow and helps manage network congestion. Breadth-first search algorithms in graphs also rely heavily on queues to explore nodes level by level.") as tracker:
            app3_title = Text("3. Network Packet Routing", font_size=28, color=GREEN)
            app3_title.move_to(UP * 2.0)
            self.play(Transform(app1_title, app3_title))
            
            app3_desc = Text("Manages data transmission order", font_size=22)
            app3_desc.move_to(UP * 1.3)
            self.play(Write(app3_desc))
            
            app4_title = Text("4. Breadth-First Search (BFS)", font_size=28, color=GREEN)
            app4_title.move_to(UP * 0.3)
            app4_desc2 = Text("Graph traversal algorithm", font_size=22)
            app4_desc2.next_to(app4_title, DOWN, buff=0.3)
            
            self.play(Write(app4_title), Write(app4_desc2))
            self.wait(2)
            self.play(FadeOut(app3_desc), FadeOut(app4_desc2))
        
        with self.voiceover(text="Other applications include handling asynchronous data transfer, managing requests in web servers, implementing undo mechanisms in software, and task scheduling in distributed systems. Queues are truly a versatile and indispensable data structure.") as tracker:
            more_apps = VGroup(
                Text("5. Web Server Request Handling", font_size=22, color=YELLOW),
                Text("6. Asynchronous Data Buffers", font_size=22, color=YELLOW),
                Text("7. Task Scheduling Systems", font_size=22, color=YELLOW),
                Text("8. Call Center Management", font_size=22, color=YELLOW)
            )
            more_apps.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
            more_apps.move_to(DOWN * 0.5)
            
            for app in more_apps:
                self.play(Write(app), run_time=0.7)
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def conclusion(self):
        with self.voiceover(text="We have reached the end of our comprehensive tutorial on queue implementation using linked lists. Let's recap what we've learned and reinforce the key concepts.") as tracker:
            title = Text("Conclusion", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
        
        with self.voiceover(text="We explored what queues are and their FIFO principle. We understood why linked lists are excellent for queue implementation, offering dynamic sizing and constant time operations. We visualized enqueue and dequeue operations in detail, seeing exactly how nodes are added and removed.") as tracker:
            summary_points = VGroup(
                Text("✓ Queue follows FIFO principle", font_size=24, color=GREEN),
                Text("✓ Linked lists offer dynamic sizing", font_size=24, color=GREEN),
                Text("✓ Enqueue and Dequeue are O(1)", font_size=24, color=GREEN),
                Text("✓ Efficient memory utilization", font_size=24, color=GREEN),
                Text("✓ No fixed capacity limitations", font_size=24, color=GREEN)
            )
            summary_points.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            summary_points.move_to(DOWN * 0.3)
            
            for point in summary_points:
                self.play(Write(point), run_time=0.8)
            self.wait(2)
        
        with self.voiceover(text="We analyzed time complexity, compared array versus linked list implementations, and explored real-world applications from operating systems to networking. You now have a solid foundation for implementing and using queues in your own projects.") as tracker:
            self.play(FadeOut(summary_points))
            
            final_message = Text(
                "Master queues, master data structures!",
                font_size=28,
                color=YELLOW
            )
            final_message.move_to(UP * 0.5)
            self.play(Write(final_message))
            self.wait(2)
        
        with self.voiceover(text="Thank you for watching this tutorial. I hope you found it informative and engaging. Keep practicing, keep coding, and continue exploring the fascinating world of data structures and algorithms. Good luck with your programming journey!") as tracker:
            self.play(FadeOut(final_message))
            
            thanks = Text("Thank You!", font_size=36, color=BLUE)
            thanks.move_to(ORIGIN)
            
            keep_learning = Text("Keep Learning & Coding!", font_size=28, color=GREEN)
            keep_learning.next_to(thanks, DOWN, buff=0.6)
            
            self.play(Write(thanks))
            self.play(Write(keep_learning))
            self.wait(3)
        
        self.play(FadeOut(*self.mobjects))