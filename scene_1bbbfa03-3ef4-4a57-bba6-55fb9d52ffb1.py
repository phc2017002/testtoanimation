from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class StackUsingQueueExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        # Introduction
        self.introduction()
        
        # Explain Stack basics
        self.explain_stack_basics()
        
        # Explain Queue basics
        self.explain_queue_basics()
        
        # Explain the challenge
        self.explain_challenge()
        
        # Approach 1: Two Queues Method
        self.two_queues_approach()
        
        # Push operation with two queues
        self.push_operation_two_queues()
        
        # Pop operation with two queues
        self.pop_operation_two_queues()
        
        # Approach 2: Single Queue Method
        self.single_queue_approach()
        
        # Push operation with single queue
        self.push_operation_single_queue()
        
        # Complete example walkthrough
        self.complete_example()
        
        # Time complexity analysis
        self.complexity_analysis()
        
        # Conclusion
        self.conclusion()

    def introduction(self):
        with self.voiceover(text="Welcome to this comprehensive tutorial on implementing a stack data structure using queues. This is a classic problem in computer science that demonstrates how we can use one data structure to simulate another.") as tracker:
            title = Text("Stack Implementation\nUsing Queue", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            self.wait(1)
            
        with self.voiceover(text="Today we will explore two different approaches to solve this problem. We'll visualize each operation step by step, analyze the time complexity, and understand the trade-offs between different implementations.") as tracker:
            subtitle = Text("A Visual Guide", font_size=28, color=YELLOW)
            subtitle.next_to(title, DOWN, buff=0.5)
            self.play(FadeIn(subtitle))
            self.wait(1)
        
        self.play(FadeOut(title), FadeOut(subtitle))

    def explain_stack_basics(self):
        with self.voiceover(text="Let's start by reviewing what a stack is. A stack is a linear data structure that follows the Last In First Out principle, commonly abbreviated as LIFO.") as tracker:
            title = Text("Stack: LIFO Structure", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Create stack visualization
            stack_container = Rectangle(width=2, height=4, color=WHITE)
            stack_container.move_to(LEFT * 3.5 + DOWN * 0.5)
            stack_label = Text("Stack", font_size=24).next_to(stack_container, DOWN, buff=0.3)
            
            self.play(Create(stack_container), Write(stack_label))
            
        with self.voiceover(text="The stack supports two main operations. Push adds an element to the top of the stack, and pop removes the element from the top. Let me demonstrate this with a visual example.") as tracker:
            # Push elements
            elements = []
            values = [10, 20, 30]
            y_positions = [-1.5, -0.5, 0.5]
            
            for i, (val, y_pos) in enumerate(zip(values, y_positions)):
                element = Rectangle(width=1.8, height=0.8, color=GREEN, fill_opacity=0.7)
                element.move_to(LEFT * 3.5 + UP * y_pos)
                text = Text(str(val), font_size=24, color=WHITE)
                text.move_to(element.get_center())
                group = VGroup(element, text)
                elements.append(group)
                
                arrow = Arrow(start=RIGHT * 0.5 + UP * y_pos, end=LEFT * 2.3 + UP * y_pos, color=YELLOW, buff=0.1)
                push_label = Text(f"Push({val})", font_size=20, color=YELLOW)
                push_label.next_to(arrow, RIGHT, buff=0.1)
                
                self.play(Create(arrow), Write(push_label))
                self.play(FadeIn(group))
                self.play(FadeOut(arrow), FadeOut(push_label))
                self.wait(0.3)
        
        with self.voiceover(text="Notice how the last element pushed, which is thirty, is at the top. When we pop, we remove this top element first. This is the essence of Last In First Out behavior.") as tracker:
            # Pop demonstration
            arrow = Arrow(start=LEFT * 2.3 + UP * 0.5, end=RIGHT * 0.5 + UP * 0.5, color=RED, buff=0.1)
            pop_label = Text("Pop() → 30", font_size=20, color=RED)
            pop_label.next_to(arrow, RIGHT, buff=0.1)
            
            self.play(Create(arrow), Write(pop_label))
            self.play(FadeOut(elements[-1]))
            self.wait(0.5)
        
        self.play(FadeOut(*self.mobjects))

    def explain_queue_basics(self):
        with self.voiceover(text="Now let's review the queue data structure. A queue follows the First In First Out principle, or FIFO. This is exactly opposite to how a stack behaves.") as tracker:
            title = Text("Queue: FIFO Structure", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Create queue visualization
            queue_container = Rectangle(width=6, height=1.5, color=WHITE)
            queue_container.move_to(DOWN * 0.5)
            
            front_label = Text("Front", font_size=20, color=YELLOW).next_to(queue_container, LEFT, buff=0.3)
            rear_label = Text("Rear", font_size=20, color=YELLOW).next_to(queue_container, RIGHT, buff=0.3)
            
            self.play(Create(queue_container), Write(front_label), Write(rear_label))
            
        with self.voiceover(text="A queue has two main operations. Enqueue adds an element at the rear, and dequeue removes an element from the front. Think of it like a line at a ticket counter, where the first person in line is served first.") as tracker:
            # Enqueue elements
            elements = []
            values = [5, 15, 25]
            x_positions = [-2, 0, 2]
            
            for i, (val, x_pos) in enumerate(zip(values, x_positions)):
                element = Rectangle(width=1.5, height=1.2, color=PURPLE, fill_opacity=0.7)
                element.move_to(RIGHT * x_pos + DOWN * 0.5)
                text = Text(str(val), font_size=24, color=WHITE)
                text.move_to(element.get_center())
                group = VGroup(element, text)
                elements.append(group)
                
                arrow = Arrow(start=RIGHT * x_pos + DOWN * 2.2, end=RIGHT * x_pos + DOWN * 1.3, color=GREEN, buff=0.1)
                enqueue_label = Text(f"Enqueue({val})", font_size=18, color=GREEN)
                enqueue_label.next_to(arrow, DOWN, buff=0.1)
                
                self.play(Create(arrow), Write(enqueue_label))
                self.play(FadeIn(group))
                self.play(FadeOut(arrow), FadeOut(enqueue_label))
                self.wait(0.3)
        
        with self.voiceover(text="When we dequeue, we remove the element from the front, which is the first element that was added. So element five leaves first, demonstrating the First In First Out principle.") as tracker:
            # Dequeue demonstration
            arrow = Arrow(start=LEFT * 2 + DOWN * 0.5, end=LEFT * 2 + UP * 1.2, color=RED, buff=0.1)
            dequeue_label = Text("Dequeue() → 5", font_size=18, color=RED)
            dequeue_label.next_to(arrow, LEFT, buff=0.1)
            
            self.play(Create(arrow), Write(dequeue_label))
            self.play(FadeOut(elements[0]))
            self.wait(0.5)
        
        self.play(FadeOut(*self.mobjects))

    def explain_challenge(self):
        with self.voiceover(text="Now comes the interesting challenge. How can we implement a stack, which is Last In First Out, using a queue, which is First In First Out? These are opposite behaviors!") as tracker:
            title = Text("The Challenge", font_size=32, color=RED)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Show the conflict
            stack_text = Text("Stack: LIFO", font_size=28, color=BLUE)
            stack_text.move_to(LEFT * 3.5 + UP * 0.5)
            
            queue_text = Text("Queue: FIFO", font_size=28, color=PURPLE)
            queue_text.move_to(RIGHT * 3.5 + UP * 0.5)
            
            vs_text = Text("VS", font_size=32, color=YELLOW)
            vs_text.move_to(ORIGIN + UP * 0.5)
            
            self.play(Write(stack_text), Write(vs_text), Write(queue_text))
            
        with self.voiceover(text="The key insight is that we need to reverse the order of elements somehow. We can achieve this using either two queues or a single queue with clever manipulation. Let's explore both approaches in detail.") as tracker:
            question = Text("How to reverse the order?", font_size=26, color=YELLOW)
            question.move_to(DOWN * 1.2)
            self.play(Write(question))
            
            arrow1 = Arrow(start=LEFT * 3.5, end=ORIGIN + DOWN * 0.3, color=ORANGE)
            arrow2 = Arrow(start=RIGHT * 3.5, end=ORIGIN + DOWN * 0.3, color=ORANGE)
            
            self.play(Create(arrow1), Create(arrow2))
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def two_queues_approach(self):
        with self.voiceover(text="The first approach uses two queues, which we'll call queue one and queue two. The main idea is to always keep our stack elements in queue one, with the most recent element at the front.") as tracker:
            title = Text("Approach 1: Two Queues", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Create two queues
            q1_container = Rectangle(width=5, height=1.2, color=GREEN)
            q1_container.move_to(UP * 1.2)
            q1_label = Text("Queue 1 (Main)", font_size=22, color=GREEN)
            q1_label.next_to(q1_container, LEFT, buff=0.3)
            
            q2_container = Rectangle(width=5, height=1.2, color=ORANGE)
            q2_container.move_to(DOWN * 0.5)
            q2_label = Text("Queue 2 (Helper)", font_size=22, color=ORANGE)
            q2_label.next_to(q2_container, LEFT, buff=0.3)
            
            self.play(Create(q1_container), Write(q1_label))
            self.play(Create(q2_container), Write(q2_label))
            
        with self.voiceover(text="Queue two serves as a helper queue. When we push a new element, we'll use queue two to help us maintain the correct order, ensuring the newest element is always at the front of queue one.") as tracker:
            # Add explanation
            explanation = Text("New element always at front of Q1", font_size=22, color=YELLOW)
            explanation.move_to(DOWN * 2.2)
            self.play(Write(explanation))
            
            # Show initial state
            note = Text("Q1 holds stack elements", font_size=18, color=WHITE)
            note.next_to(q1_container, RIGHT, buff=0.3)
            self.play(FadeIn(note))
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def push_operation_two_queues(self):
        with self.voiceover(text="Let's visualize the push operation with two queues in detail. Suppose we want to push elements ten, twenty, and thirty onto our stack.") as tracker:
            title = Text("Push Operation: Two Queues", font_size=30, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Setup queues
            q1_rect = Rectangle(width=6, height=1, color=GREEN)
            q1_rect.move_to(UP * 1.5)
            q1_label = Text("Q1", font_size=20, color=GREEN).next_to(q1_rect, LEFT, buff=0.2)
            
            q2_rect = Rectangle(width=6, height=1, color=ORANGE)
            q2_rect.move_to(DOWN * 0.2)
            q2_label = Text("Q2", font_size=20, color=ORANGE).next_to(q2_rect, LEFT, buff=0.2)
            
            self.play(Create(q1_rect), Write(q1_label), Create(q2_rect), Write(q2_label))
            
        with self.voiceover(text="Step one: Push ten. Since queue one is empty, we simply enqueue ten into queue one. The operation is straightforward for the first element.") as tracker:
            # Push 10
            step1 = Text("Step 1: Push(10)", font_size=24, color=YELLOW)
            step1.move_to(DOWN * 2)
            self.play(Write(step1))
            
            elem1 = Rectangle(width=1, height=0.8, color=BLUE, fill_opacity=0.7)
            elem1.move_to(q1_rect.get_center())
            text1 = Text("10", font_size=20, color=WHITE)
            text1.move_to(elem1.get_center())
            group1 = VGroup(elem1, text1)
            
            self.play(FadeIn(group1))
            self.wait(1)
            self.play(FadeOut(step1))
            
        with self.voiceover(text="Step two: Push twenty. Here's where it gets interesting. First, we enqueue twenty into queue two. Then we transfer all elements from queue one to queue two. Finally, we swap the names of the queues.") as tracker:
            # Push 20
            step2 = Text("Step 2: Push(20)", font_size=24, color=YELLOW)
            step2.move_to(DOWN * 2)
            self.play(Write(step2))
            
            # Enqueue 20 to Q2
            elem2 = Rectangle(width=1, height=0.8, color=BLUE, fill_opacity=0.7)
            elem2.move_to(q2_rect.get_center() + LEFT * 1.5)
            text2 = Text("20", font_size=20, color=WHITE)
            text2.move_to(elem2.get_center())
            group2 = VGroup(elem2, text2)
            
            arrow_down = Arrow(start=UP * 0.5, end=DOWN * 0.2 + LEFT * 1.5, color=YELLOW)
            self.play(Create(arrow_down))
            self.play(FadeIn(group2))
            self.play(FadeOut(arrow_down))
            
            # Transfer from Q1 to Q2
            transfer_arrow = Arrow(start=q1_rect.get_bottom(), end=q2_rect.get_top() + RIGHT * 0.5, color=RED)
            transfer_label = Text("Transfer", font_size=18, color=RED)
            transfer_label.next_to(transfer_arrow, LEFT, buff=0.1)
            
            self.play(Create(transfer_arrow), Write(transfer_label))
            
            new_elem1 = Rectangle(width=1, height=0.8, color=BLUE, fill_opacity=0.7)
            new_elem1.move_to(q2_rect.get_center() + RIGHT * 0.5)
            new_text1 = Text("10", font_size=20, color=WHITE)
            new_text1.move_to(new_elem1.get_center())
            new_group1 = VGroup(new_elem1, new_text1)
            
            self.play(FadeOut(group1), FadeIn(new_group1))
            self.play(FadeOut(transfer_arrow), FadeOut(transfer_label))
            
            # Swap queues
            swap_text = Text("Swap Q1 ↔ Q2", font_size=20, color=PURPLE)
            swap_text.move_to(DOWN * 2.8)
            self.play(FadeOut(step2), Write(swap_text))
            
            self.play(group2.animate.move_to(q1_rect.get_center() + LEFT * 1.5),
                     new_group1.animate.move_to(q1_rect.get_center() + RIGHT * 0.5))
            self.wait(1)
            self.play(FadeOut(swap_text))
            
        with self.voiceover(text="Step three: Push thirty. We repeat the same process. Enqueue thirty to queue two, transfer all elements from queue one, then swap. Now thirty is at the front, which is exactly what we need for stack behavior.") as tracker:
            # Push 30
            step3 = Text("Step 3: Push(30)", font_size=24, color=YELLOW)
            step3.move_to(DOWN * 2)
            self.play(Write(step3))
            
            # Enqueue 30 to Q2
            elem3 = Rectangle(width=1, height=0.8, color=BLUE, fill_opacity=0.7)
            elem3.move_to(q2_rect.get_center() + LEFT * 2)
            text3 = Text("30", font_size=20, color=WHITE)
            text3.move_to(elem3.get_center())
            group3 = VGroup(elem3, text3)
            
            self.play(FadeIn(group3))
            
            # Transfer animation
            final_group2 = VGroup(elem2.copy(), text2.copy())
            final_group1 = VGroup(elem1.copy(), text1.copy())
            
            self.play(
                final_group2.animate.move_to(q2_rect.get_center() + LEFT * 0.2),
                final_group1.animate.move_to(q2_rect.get_center() + RIGHT * 1.2)
            )
            
            # Swap to Q1
            self.play(
                group3.animate.move_to(q1_rect.get_center() + LEFT * 2),
                final_group2.animate.move_to(q1_rect.get_center() + LEFT * 0.2),
                final_group1.animate.move_to(q1_rect.get_center() + RIGHT * 1.2)
            )
            
            result = Text("Result: [30, 20, 10] in Q1", font_size=22, color=GREEN)
            result.move_to(DOWN * 2.8)
            self.play(FadeOut(step3), Write(result))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def pop_operation_two_queues(self):
        with self.voiceover(text="The pop operation with two queues is much simpler than push. Since we've maintained our stack with the most recent element at the front of queue one, we simply dequeue from queue one.") as tracker:
            title = Text("Pop Operation: Two Queues", font_size=30, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Setup queue with elements
            q1_rect = Rectangle(width=6, height=1, color=GREEN)
            q1_rect.move_to(UP * 0.8)
            q1_label = Text("Q1", font_size=20, color=GREEN).next_to(q1_rect, LEFT, buff=0.2)
            
            self.play(Create(q1_rect), Write(q1_label))
            
            # Add elements [30, 20, 10]
            elem3 = Rectangle(width=1, height=0.8, color=BLUE, fill_opacity=0.7)
            elem3.move_to(q1_rect.get_center() + LEFT * 2)
            text3 = Text("30", font_size=20, color=WHITE)
            text3.move_to(elem3.get_center())
            
            elem2 = Rectangle(width=1, height=0.8, color=BLUE, fill_opacity=0.7)
            elem2.move_to(q1_rect.get_center() + LEFT * 0.2)
            text2 = Text("20", font_size=20, color=WHITE)
            text2.move_to(elem2.get_center())
            
            elem1 = Rectangle(width=1, height=0.8, color=BLUE, fill_opacity=0.7)
            elem1.move_to(q1_rect.get_center() + RIGHT * 1.2)
            text1 = Text("10", font_size=20, color=WHITE)
            text1.move_to(elem1.get_center())
            
            elements = VGroup(elem3, text3, elem2, text2, elem1, text1)
            self.play(FadeIn(elements))
            
        with self.voiceover(text="Let's perform a pop operation. We dequeue the front element from queue one, which is thirty. This gives us the Last In First Out behavior we need, and the operation is very efficient.") as tracker:
            pop_label = Text("Pop() → 30", font_size=24, color=RED)
            pop_label.move_to(DOWN * 1.5)
            self.play(Write(pop_label))
            
            arrow = Arrow(start=q1_rect.get_left() + LEFT * 0.5, end=q1_rect.get_left() + LEFT * 2, color=RED)
            self.play(Create(arrow))
            
            self.play(FadeOut(VGroup(elem3, text3)))
            self.wait(1)
            
            result = Text("Remaining: [20, 10]", font_size=22, color=GREEN)
            result.move_to(DOWN * 2.3)
            self.play(Write(result))
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def single_queue_approach(self):
        with self.voiceover(text="Now let's explore the second approach, which uses only a single queue. This is more space-efficient as we don't need a helper queue. The clever trick here is rotation.") as tracker:
            title = Text("Approach 2: Single Queue", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            subtitle = Text("Using Rotation", font_size=26, color=YELLOW)
            subtitle.next_to(title, DOWN, buff=0.4)
            self.play(Write(subtitle))
            
        with self.voiceover(text="The key idea is this: when we push a new element, we first enqueue it. Then we rotate the queue by dequeuing and enqueuing all the previous elements. This brings the new element to the front.") as tracker:
            # Create single queue
            queue_rect = Rectangle(width=6, height=1.2, color=PURPLE)
            queue_rect.move_to(DOWN * 0.3)
            queue_label = Text("Queue", font_size=22, color=PURPLE)
            queue_label.next_to(queue_rect, LEFT, buff=0.3)
            
            self.play(Create(queue_rect), Write(queue_label))
            
            # Show rotation concept
            rotation_text = Text("Rotate = Dequeue + Enqueue", font_size=22, color=ORANGE)
            rotation_text.move_to(DOWN * 2)
            self.play(Write(rotation_text))
            
            # Visual rotation demonstration
            arrow1 = Arrow(start=queue_rect.get_left() + DOWN * 0.6, end=queue_rect.get_left() + DOWN * 1.8, color=RED)
            deq_label = Text("Dequeue", font_size=18, color=RED)
            deq_label.next_to(arrow1, LEFT, buff=0.1)
            
            arrow2 = Arrow(start=queue_rect.get_right() + DOWN * 1.8, end=queue_rect.get_right() + DOWN * 0.6, color=GREEN)
            enq_label = Text("Enqueue", font_size=18, color=GREEN)
            enq_label.next_to(arrow2, RIGHT, buff=0.1)
            
            self.play(Create(arrow1), Write(deq_label), Create(arrow2), Write(enq_label))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def push_operation_single_queue(self):
        with self.voiceover(text="Let's see the single queue push operation in action. We'll push ten, twenty, and thirty, and observe how rotation maintains the stack order.") as tracker:
            title = Text("Push Operation: Single Queue", font_size=30, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Setup queue
            queue_rect = Rectangle(width=7, height=1, color=PURPLE)
            queue_rect.move_to(UP * 1.2)
            queue_label = Text("Q", font_size=20, color=PURPLE).next_to(queue_rect, LEFT, buff=0.2)
            
            self.play(Create(queue_rect), Write(queue_label))
            
        with self.voiceover(text="Push ten. The queue is empty, so we just enqueue ten. No rotation needed for the first element. The size is now one.") as tracker:
            step1 = Text("Push(10): Enqueue 10", font_size=22, color=YELLOW)
            step1.move_to(DOWN * 0.5)
            self.play(Write(step1))
            
            elem1 = Rectangle(width=1, height=0.8, color=BLUE, fill_opacity=0.7)
            elem1.move_to(queue_rect.get_center())
            text1 = Text("10", font_size=20, color=WHITE)
            text1.move_to(elem1.get_center())
            group1 = VGroup(elem1, text1)
            
            self.play(FadeIn(group1))
            
            size_text = Text("Size = 1", font_size=20, color=GREEN)
            size_text.move_to(DOWN * 1.2)
            self.play(Write(size_text))
            self.wait(1)
            self.play(FadeOut(step1), FadeOut(size_text))
            
        with self.voiceover(text="Push twenty. First, enqueue twenty to the rear. Now the queue has ten at front and twenty at rear. We need to rotate.") as tracker:
            step2a = Text("Push(20): Enqueue 20", font_size=22, color=YELLOW)
            step2a.move_to(DOWN * 0.5)
            self.play(Write(step2a))
            
            elem2 = Rectangle(width=1, height=0.8, color=BLUE, fill_opacity=0.7)
            elem2.move_to(queue_rect.get_center() + RIGHT * 1.5)
            text2 = Text("20", font_size=20, color=WHITE)
            text2.move_to(elem2.get_center())
            group2 = VGroup(elem2, text2)
            
            self.play(group1.animate.move_to(queue_rect.get_center() + LEFT * 1.5))
            self.play(FadeIn(group2))
            self.play(FadeOut(step2a))
            
        with self.voiceover(text="Now rotate size minus one times, which is one rotation. Dequeue ten from the front and enqueue it at the rear. Now twenty is at the front, giving us the correct stack order.") as tracker:
            step2b = Text("Rotate 1 time", font_size=22, color=ORANGE)
            step2b.move_to(DOWN * 0.5)
            self.play(Write(step2b))
            
            # Show rotation
            rotation_arrow = CurvedArrow(start_point=queue_rect.get_left() + DOWN * 0.5, 
                                        end_point=queue_rect.get_right() + DOWN * 0.5, 
                                        color=ORANGE, angle=-TAU/4)
            self.play(Create(rotation_arrow))
            
            # Move elements
            self.play(
                group1.animate.move_to(queue_rect.get_center() + RIGHT * 1.5),
                group2.animate.move_to(queue_rect.get_center() + LEFT * 1.5)
            )
            self.play(FadeOut(rotation_arrow))
            
            result1 = Text("Order: [20, 10]", font_size=20, color=GREEN)
            result1.move_to(DOWN * 1.2)
            self.play(FadeOut(step2b), Write(result1))
            self.wait(1)
            self.play(FadeOut(result1))
            
        with self.voiceover(text="Push thirty. Enqueue thirty at the rear. Now we have twenty, ten, thirty. We need to rotate two times to bring thirty to the front.") as tracker:
            step3a = Text("Push(30): Enqueue 30", font_size=22, color=YELLOW)
            step3a.move_to(DOWN * 0.5)
            self.play(Write(step3a))
            
            elem3 = Rectangle(width=1, height=0.8, color=BLUE, fill_opacity=0.7)
            elem3.move_to(queue_rect.get_center() + RIGHT * 2.8)
            text3 = Text("30", font_size=20, color=WHITE)
            text3.move_to(elem3.get_center())
            group3 = VGroup(elem3, text3)
            
            self.play(
                group2.animate.move_to(queue_rect.get_center() + LEFT * 2.8),
                group1.animate.move_to(queue_rect.get_center() + LEFT * 0.2)
            )
            self.play(FadeIn(group3))
            self.play(FadeOut(step3a))
            
        with self.voiceover(text="First rotation: dequeue twenty, enqueue twenty. Second rotation: dequeue ten, enqueue ten. Perfect! Now thirty is at the front, maintaining our stack property.") as tracker:
            step3b = Text("Rotate 2 times", font_size=22, color=ORANGE)
            step3b.move_to(DOWN * 0.5)
            self.play(Write(step3b))
            
            # First rotation
            self.play(
                group2.animate.move_to(queue_rect.get_center() + RIGHT * 2.8),
                group1.animate.move_to(queue_rect.get_center() + LEFT * 2.8),
                group3.animate.move_to(queue_rect.get_center() + LEFT * 0.2)
            )
            self.wait(0.5)
            
            # Second rotation
            self.play(
                group1.animate.move_to(queue_rect.get_center() + RIGHT * 2.8),
                group3.animate.move_to(queue_rect.get_center() + LEFT * 2.8),
                group2.animate.move_to(queue_rect.get_center() + LEFT * 0.2)
            )
            
            result2 = Text("Final Order: [30, 20, 10]", font_size=20, color=GREEN)
            result2.move_to(DOWN * 1.2)
            self.play(FadeOut(step3b), Write(result2))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def complete_example(self):
        with self.voiceover(text="Let's walk through a complete example with multiple push and pop operations to see how everything works together. We'll use the single queue approach for this demonstration.") as tracker:
            title = Text("Complete Example", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            operations = Text("Operations: Push(1), Push(2), Pop(), Push(3), Pop(), Pop()", 
                            font_size=22, color=YELLOW)
            operations.next_to(title, DOWN, buff=0.4)
            self.play(Write(operations))
            
        with self.voiceover(text="We start with an empty queue. Let's execute push one, push two, then pop, followed by push three, pop, and pop again.") as tracker:
            # Setup
            queue_rect = Rectangle(width=6, height=1, color=PURPLE)
            queue_rect.move_to(UP * 0.5)
            queue_label = Text("Queue", font_size=20, color=PURPLE).next_to(queue_rect, LEFT, buff=0.2)
            
            self.play(Create(queue_rect), Write(queue_label))
            
            # Track current state
            state = Text("State: []", font_size=20, color=WHITE)
            state.move_to(DOWN * 1.5)
            self.play(Write(state))
            
        with self.voiceover(text="Push one: We enqueue one. No rotation needed. State is now one.") as tracker:
            op1 = Text("Push(1)", font_size=22, color=GREEN)
            op1.move_to(DOWN * 2.3)
            self.play(Write(op1))
            
            e1 = Rectangle(width=0.9, height=0.8, color=BLUE, fill_opacity=0.7)
            e1.move_to(queue_rect.get_center())
            t1 = Text("1", font_size=20, color=WHITE).move_to(e1.get_center())
            g1 = VGroup(e1, t1)
            self.play(FadeIn(g1))
            
            new_state = Text("State: [1]", font_size=20, color=WHITE)
            new_state.move_to(DOWN * 1.5)
            self.play(Transform(state, new_state))
            self.wait(0.5)
            self.play(FadeOut(op1))
            
        with self.voiceover(text="Push two: Enqueue two, then rotate once. Now two is at the front. State is two, one.") as tracker:
            op2 = Text("Push(2)", font_size=22, color=GREEN)
            op2.move_to(DOWN * 2.3)
            self.play(Write(op2))
            
            e2 = Rectangle(width=0.9, height=0.8, color=BLUE, fill_opacity=0.7)
            e2.move_to(queue_rect.get_center() + RIGHT * 1.2)
            t2 = Text("2", font_size=20, color=WHITE).move_to(e2.get_center())
            g2 = VGroup(e2, t2)
            
            self.play(g1.animate.move_to(queue_rect.get_center() + LEFT * 1.2))
            self.play(FadeIn(g2))
            
            # Rotate
            self.play(
                g2.animate.move_to(queue_rect.get_center() + LEFT * 1.2),
                g1.animate.move_to(queue_rect.get_center() + RIGHT * 1.2)
            )
            
            new_state = Text("State: [2, 1]", font_size=20, color=WHITE)
            new_state.move_to(DOWN * 1.5)
            self.play(Transform(state, new_state))
            self.wait(0.5)
            self.play(FadeOut(op2))
            
        with self.voiceover(text="Pop: Dequeue from front. We remove two. State is now just one.") as tracker:
            op3 = Text("Pop() → 2", font_size=22, color=RED)
            op3.move_to(DOWN * 2.3)
            self.play(Write(op3))
            
            self.play(FadeOut(g2))
            self.play(g1.animate.move_to(queue_rect.get_center()))
            
            new_state = Text("State: [1]", font_size=20, color=WHITE)
            new_state.move_to(DOWN * 1.5)
            self.play(Transform(state, new_state))
            self.wait(0.5)
            self.play(FadeOut(op3))
            
        with self.voiceover(text="Push three: Enqueue three, then rotate once. State becomes three, one.") as tracker:
            op4 = Text("Push(3)", font_size=22, color=GREEN)
            op4.move_to(DOWN * 2.3)
            self.play(Write(op4))
            
            e3 = Rectangle(width=0.9, height=0.8, color=BLUE, fill_opacity=0.7)
            e3.move_to(queue_rect.get_center() + RIGHT * 1.2)
            t3 = Text("3", font_size=20, color=WHITE).move_to(e3.get_center())
            g3 = VGroup(e3, t3)
            
            self.play(g1.animate.move_to(queue_rect.get_center() + LEFT * 1.2))
            self.play(FadeIn(g3))
            
            # Rotate
            self.play(
                g3.animate.move_to(queue_rect.get_center() + LEFT * 1.2),
                g1.animate.move_to(queue_rect.get_center() + RIGHT * 1.2)
            )
            
            new_state = Text("State: [3, 1]", font_size=20, color=WHITE)
            new_state.move_to(DOWN * 1.5)
            self.play(Transform(state, new_state))
            self.wait(0.5)
            self.play(FadeOut(op4))
            
        with self.voiceover(text="Pop: Remove three from front. State is one. Final pop: Remove one. Queue is now empty. Example complete!") as tracker:
            op5 = Text("Pop() → 3", font_size=22, color=RED)
            op5.move_to(DOWN * 2.3)
            self.play(Write(op5))
            
            self.play(FadeOut(g3))
            self.play(g1.animate.move_to(queue_rect.get_center()))
            
            new_state = Text("State: [1]", font_size=20, color=WHITE)
            new_state.move_to(DOWN * 1.5)
            self.play(Transform(state, new_state))
            self.wait(0.5)
            self.play(FadeOut(op5))
            
            # Final pop
            op6 = Text("Pop() → 1", font_size=22, color=RED)
            op6.move_to(DOWN * 2.3)
            self.play(Write(op6))
            
            self.play(FadeOut(g1))
            
            new_state = Text("State: []", font_size=20, color=WHITE)
            new_state.move_to(DOWN * 1.5)
            self.play(Transform(state, new_state))
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def complexity_analysis(self):
        with self.voiceover(text="Now let's analyze the time and space complexity of both approaches. This is crucial for understanding which method to choose in practice.") as tracker:
            title = Text("Complexity Analysis", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
        with self.voiceover(text="For the two queues approach, push has a time complexity of O of n, where n is the number of elements, because we transfer all elements. Pop is O of one, constant time.") as tracker:
            # Two queues complexity
            two_q_title = Text("Two Queues Approach", font_size=26, color=GREEN)
            two_q_title.move_to(LEFT * 3.5 + UP * 1.5)
            self.play(Write(two_q_title))
            
            push_complex = MathTex(r"\text{Push: } O(n)").scale(0.8)
            push_complex.move_to(LEFT * 3.5 + UP * 0.5)
            pop_complex = MathTex(r"\text{Pop: } O(1)").scale(0.8)
            pop_complex.move_to(LEFT * 3.5 + DOWN * 0.2)
            space_complex1 = MathTex(r"\text{Space: } O(n)").scale(0.8)
            space_complex1.move_to(LEFT * 3.5 + DOWN * 0.9)
            
            self.play(Write(push_complex))
            self.play(Write(pop_complex))
            self.play(Write(space_complex1))
            
        with self.voiceover(text="For the single queue approach, push is also O of n due to rotation. Pop remains O of one. However, single queue uses less space as we don't need a helper queue.") as tracker:
            # Single queue complexity
            one_q_title = Text("Single Queue Approach", font_size=26, color=PURPLE)
            one_q_title.move_to(RIGHT * 3.5 + UP * 1.5)
            self.play(Write(one_q_title))
            
            push_complex2 = MathTex(r"\text{Push: } O(n)").scale(0.8)
            push_complex2.move_to(RIGHT * 3.5 + UP * 0.5)
            pop_complex2 = MathTex(r"\text{Pop: } O(1)").scale(0.8)
            pop_complex2.move_to(RIGHT * 3.5 + DOWN * 0.2)
            space_complex2 = MathTex(r"\text{Space: } O(n)").scale(0.8)
            space_complex2.move_to(RIGHT * 3.5 + DOWN * 0.9)
            
            self.play(Write(push_complex2))
            self.play(Write(pop_complex2))
            self.play(Write(space_complex2))
            
        with self.voiceover(text="In practice, the single queue method is often preferred because it's more space-efficient and the code is simpler. Both have the same time complexity, so the choice depends on your specific requirements.") as tracker:
            conclusion_box = Rectangle(width=10, height=1.5, color=YELLOW)
            conclusion_box.move_to(DOWN * 2.2)
            
            conclusion = Text("Single Queue: Better space efficiency\nTwo Queues: Conceptually clearer", 
                            font_size=20, color=WHITE)
            conclusion.move_to(conclusion_box.get_center())
            
            self.play(Create(conclusion_box))
            self.play(Write(conclusion))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def conclusion(self):
        with self.voiceover(text="We've completed our journey through stack implementation using queues. Let's summarize what we learned today.") as tracker:
            title = Text("Summary", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
        with self.voiceover(text="We explored two approaches: the two queues method, which transfers elements between queues, and the single queue method, which uses rotation. Both achieve stack behavior from queue operations.") as tracker:
            point1 = Text("✓ Two Queues: Transfer method", font_size=24, color=GREEN)
            point1.move_to(UP * 1.2)
            
            point2 = Text("✓ Single Queue: Rotation method", font_size=24, color=PURPLE)
            point2.move_to(UP * 0.3)
            
            self.play(Write(point1))
            self.wait(0.5)
            self.play(Write(point2))
            self.wait(0.5)
            
        with self.voiceover(text="Key takeaways: Push is O of n for both approaches. Pop is O of one. Single queue is more space-efficient. This problem teaches us how to think creatively about data structures and their properties.") as tracker:
            point3 = Text("✓ Push: O(n), Pop: O(1)", font_size=24, color=ORANGE)
            point3.move_to(DOWN * 0.6)
            
            point4 = Text("✓ Space: Single queue wins", font_size=24, color=YELLOW)
            point4.move_to(DOWN * 1.5)
            
            self.play(Write(point3))
            self.wait(0.5)
            self.play(Write(point4))
            self.wait(1)
            
        with self.voiceover(text="Thank you for watching this detailed explanation. Practice implementing both methods, and you'll gain a deeper understanding of how data structures can transform into one another. Happy coding!") as tracker:
            self.play(FadeOut(*self.mobjects))
            
            thanks = Text("Thank You!", font_size=36, color=BLUE)
            thanks.move_to(ORIGIN)
            
            subscribe = Text("Practice both approaches to master the concept", 
                           font_size=22, color=YELLOW)
            subscribe.next_to(thanks, DOWN, buff=0.8)
            
            self.play(Write(thanks))
            self.play(FadeIn(subscribe))
            self.wait(3)

# To render this animation, run:
# manim -pql stack_using_queue.py StackUsingQueueExplanation