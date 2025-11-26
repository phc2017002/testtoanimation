from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class QueueUsingStacksExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))
        
        # Introduction
        self.introduction()
        
        # Explain Queue basics
        self.explain_queue_basics()
        
        # Explain Stack basics
        self.explain_stack_basics()
        
        # The challenge
        self.explain_the_challenge()
        
        # Two-stack approach explanation
        self.explain_two_stack_approach()
        
        # Enqueue operation visualization
        self.visualize_enqueue_operation()
        
        # Dequeue operation visualization
        self.visualize_dequeue_operation()
        
        # Complete example walkthrough
        self.complete_example_walkthrough()
        
        # Time complexity analysis
        self.time_complexity_analysis()
        
        # Applications and use cases
        self.applications_and_use_cases()
        
        # Summary and conclusion
        self.summary_and_conclusion()

    def introduction(self):
        with self.voiceover(
            text="Welcome to this comprehensive tutorial on implementing a queue data structure using stacks. This is a classic computer science problem that demonstrates how we can build one data structure using another with different properties."
        ) as tracker:
            title = Text("Queue Implementation\nUsing Stacks", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
        with self.voiceover(
            text="By the end of this video, you will understand the fundamental differences between queues and stacks, learn the two-stack technique, and see how operations work step by step with detailed visualizations."
        ) as tracker:
            subtitle = Text(
                "A Deep Dive into Data Structure Design",
                font_size=28,
                color=YELLOW
            )
            subtitle.move_to(DOWN * 0.5)
            self.play(FadeIn(subtitle))
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def explain_queue_basics(self):
        with self.voiceover(
            text="Let's start by understanding what a queue is. A queue is a linear data structure that follows the First In First Out principle, commonly abbreviated as F I F O."
        ) as tracker:
            title = Text("What is a Queue?", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            fifo_text = Text("FIFO: First In, First Out", font_size=32, color=GREEN)
            fifo_text.move_to(UP * 1.5)
            self.play(Write(fifo_text))
        
        with self.voiceover(
            text="Think of a queue like a line of people waiting at a ticket counter. The first person to join the line is the first person to be served. New people join at the back, and people are served from the front."
        ) as tracker:
            # Create queue visualization
            queue_boxes = VGroup()
            values = ["1", "2", "3", "4"]
            for i, val in enumerate(values):
                box = Rectangle(width=1.2, height=1.2, color=BLUE, fill_opacity=0.3)
                text = Text(val, font_size=28)
                box_group = VGroup(box, text)
                queue_boxes.add(box_group)
            
            queue_boxes.arrange(RIGHT, buff=0.3)
            queue_boxes.move_to(DOWN * 0.5)
            
            self.play(Create(queue_boxes))
            
            # Add labels
            front_label = Text("Front\n(Dequeue)", font_size=22, color=RED)
            front_label.next_to(queue_boxes[0], DOWN, buff=0.5)
            
            rear_label = Text("Rear\n(Enqueue)", font_size=22, color=GREEN)
            rear_label.next_to(queue_boxes[-1], DOWN, buff=0.5)
            
            self.play(Write(front_label), Write(rear_label))
        
        with self.voiceover(
            text="The two main operations on a queue are enqueue, which adds an element to the rear, and dequeue, which removes an element from the front. Let's see these operations in action."
        ) as tracker:
            # Show enqueue operation
            new_box = Rectangle(width=1.2, height=1.2, color=GREEN, fill_opacity=0.3)
            new_text = Text("5", font_size=28)
            new_element = VGroup(new_box, new_text)
            new_element.next_to(queue_boxes, RIGHT, buff=2)
            
            self.play(FadeIn(new_element))
            self.play(new_element.animate.next_to(queue_boxes[-1], RIGHT, buff=0.3))
            queue_boxes.add(new_element)
            
            # Show dequeue operation
            self.wait(0.5)
            removed = queue_boxes[0]
            self.play(removed.animate.shift(DOWN * 2), FadeOut(removed))
        
        self.play(FadeOut(*self.mobjects))

    def explain_stack_basics(self):
        with self.voiceover(
            text="Now let's understand stacks. A stack is also a linear data structure, but it follows a different principle called Last In First Out, or L I F O."
        ) as tracker:
            title = Text("What is a Stack?", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            lifo_text = Text("LIFO: Last In, First Out", font_size=32, color=ORANGE)
            lifo_text.move_to(UP * 2.0)
            self.play(Write(lifo_text))
        
        with self.voiceover(
            text="Think of a stack like a pile of plates. You can only add a plate to the top, and you can only remove a plate from the top. The last plate you put on is the first one you take off."
        ) as tracker:
            # Create stack visualization
            stack_boxes = VGroup()
            values = ["1", "2", "3", "4"]
            for i, val in enumerate(values):
                box = Rectangle(width=2.0, height=0.8, color=ORANGE, fill_opacity=0.3)
                text = Text(val, font_size=28)
                box_group = VGroup(box, text)
                stack_boxes.add(box_group)
            
            stack_boxes.arrange(DOWN, buff=0.1, aligned_edge=LEFT)
            stack_boxes.move_to(ORIGIN)
            
            self.play(Create(stack_boxes))
            
            # Add top label
            top_label = Text("Top\n(Push/Pop)", font_size=24, color=RED)
            top_label.next_to(stack_boxes[0], RIGHT, buff=0.8)
            
            bottom_label = Text("Bottom", font_size=24, color=GRAY)
            bottom_label.next_to(stack_boxes[-1], RIGHT, buff=0.8)
            
            self.play(Write(top_label), Write(bottom_label))
        
        with self.voiceover(
            text="The two main operations on a stack are push, which adds an element to the top, and pop, which removes the top element. Notice how this is fundamentally different from a queue."
        ) as tracker:
            # Show push operation
            new_box = Rectangle(width=2.0, height=0.8, color=GREEN, fill_opacity=0.3)
            new_text = Text("5", font_size=28)
            new_element = VGroup(new_box, new_text)
            new_element.next_to(stack_boxes[0], UP, buff=2)
            
            self.play(FadeIn(new_element))
            self.play(new_element.animate.next_to(stack_boxes[0], UP, buff=0.1))
            
            # Show pop operation
            self.wait(0.5)
            self.play(new_element.animate.shift(UP * 2), FadeOut(new_element))
        
        self.play(FadeOut(*self.mobjects))

    def explain_the_challenge(self):
        with self.voiceover(
            text="Here's the challenge: How can we implement a queue's First In First Out behavior using only stacks, which have Last In First Out behavior? This seems contradictory at first."
        ) as tracker:
            title = Text("The Challenge", font_size=36, color=RED)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            challenge = Text(
                "Implement FIFO using LIFO",
                font_size=32,
                color=YELLOW
            )
            challenge.move_to(UP * 1.5)
            self.play(Write(challenge))
        
        with self.voiceover(
            text="The key insight is that we can use two stacks to reverse the order of elements. When we move elements from one stack to another, their order gets reversed. By doing this twice, we can achieve the queue behavior we need."
        ) as tracker:
            # Show two stacks side by side
            stack1_boxes = VGroup()
            for i in range(3):
                box = Rectangle(width=1.5, height=0.7, color=BLUE, fill_opacity=0.3)
                text = Text(str(i+1), font_size=24)
                box_group = VGroup(box, text)
                stack1_boxes.add(box_group)
            
            stack1_boxes.arrange(DOWN, buff=0.1)
            stack1_boxes.move_to(LEFT * 3.5 + DOWN * 0.5)
            
            stack2_boxes = VGroup()
            for i in range(3):
                box = Rectangle(width=1.5, height=0.7, color=GREEN, fill_opacity=0.3)
                stack2_boxes.add(box)
            
            stack2_boxes.arrange(DOWN, buff=0.1)
            stack2_boxes.move_to(RIGHT * 3.5 + DOWN * 0.5)
            
            stack1_label = Text("Stack 1", font_size=24, color=BLUE)
            stack1_label.next_to(stack1_boxes, UP, buff=0.5)
            
            stack2_label = Text("Stack 2", font_size=24, color=GREEN)
            stack2_label.next_to(stack2_boxes, UP, buff=0.5)
            
            self.play(
                Create(stack1_boxes),
                Create(stack2_boxes),
                Write(stack1_label),
                Write(stack2_label)
            )
            
            # Show arrow indicating transfer
            arrow = Arrow(
                stack1_boxes.get_right() + RIGHT * 0.2,
                stack2_boxes.get_left() + LEFT * 0.2,
                color=YELLOW,
                buff=0
            )
            arrow_label = Text("Reverse Order", font_size=20, color=YELLOW)
            arrow_label.next_to(arrow, RIGHT, buff=0.2)
            
            self.play(Create(arrow), Write(arrow_label))
        
        self.play(FadeOut(*self.mobjects))

    def explain_two_stack_approach(self):
        with self.voiceover(
            text="The solution uses two stacks: Stack One for enqueue operations and Stack Two for dequeue operations. Let's call them the input stack and the output stack respectively."
        ) as tracker:
            title = Text("Two-Stack Approach", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Create two empty stacks
            stack1_rect = Rectangle(width=2.5, height=4, color=BLUE)
            stack1_rect.move_to(LEFT * 3.5 + DOWN * 0.5)
            
            stack2_rect = Rectangle(width=2.5, height=4, color=GREEN)
            stack2_rect.move_to(RIGHT * 3.5 + DOWN * 0.5)
            
            stack1_label = Text("Stack 1\n(Input)", font_size=26, color=BLUE)
            stack1_label.next_to(stack1_rect, UP, buff=0.4)
            
            stack2_label = Text("Stack 2\n(Output)", font_size=26, color=GREEN)
            stack2_label.next_to(stack2_rect, UP, buff=0.4)
            
            self.play(
                Create(stack1_rect),
                Create(stack2_rect),
                Write(stack1_label),
                Write(stack2_label)
            )
        
        with self.voiceover(
            text="The algorithm works as follows: For enqueue, we simply push the element onto Stack One. For dequeue, we pop from Stack Two. But if Stack Two is empty, we first transfer all elements from Stack One to Stack Two, which reverses their order."
        ) as tracker:
            # Show algorithm steps
            algo_steps = VGroup(
                Text("Enqueue:", font_size=24, color=YELLOW),
                Text("  → Push to Stack 1", font_size=22),
                Text("Dequeue:", font_size=24, color=YELLOW),
                Text("  → If Stack 2 empty:", font_size=22),
                Text("      Transfer Stack 1 → Stack 2", font_size=20),
                Text("  → Pop from Stack 2", font_size=22)
            )
            algo_steps.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            algo_steps.move_to(DOWN * 1.2)
            
            self.play(Write(algo_steps))
        
        self.play(FadeOut(*self.mobjects))

    def visualize_enqueue_operation(self):
        with self.voiceover(
            text="Let's visualize the enqueue operation in detail. When we want to add an element to our queue, we push it onto Stack One. This is a simple operation with constant time complexity."
        ) as tracker:
            title = Text("Enqueue Operation", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Create stacks
            stack1_base = Rectangle(width=2.5, height=4, color=BLUE, stroke_opacity=0.5)
            stack1_base.move_to(LEFT * 3.5 + DOWN * 0.5)
            
            stack2_base = Rectangle(width=2.5, height=4, color=GREEN, stroke_opacity=0.5)
            stack2_base.move_to(RIGHT * 3.5 + DOWN * 0.5)
            
            stack1_label = Text("Stack 1", font_size=26, color=BLUE)
            stack1_label.next_to(stack1_base, UP, buff=0.4)
            
            stack2_label = Text("Stack 2", font_size=26, color=GREEN)
            stack2_label.next_to(stack2_base, UP, buff=0.4)
            
            self.play(
                Create(stack1_base),
                Create(stack2_base),
                Write(stack1_label),
                Write(stack2_label)
            )
        
        with self.voiceover(
            text="Let's enqueue the numbers one, two, and three. Watch how each element is pushed onto Stack One. Notice that Stack Two remains empty during enqueue operations."
        ) as tracker:
            stack1_elements = VGroup()
            
            for i, val in enumerate(["1", "2", "3"]):
                # Create new element
                box = Rectangle(width=2.0, height=0.7, color=BLUE, fill_opacity=0.4)
                text = Text(val, font_size=28)
                element = VGroup(box, text)
                
                # Start position (above stack)
                element.move_to(LEFT * 3.5 + UP * 2.5)
                
                # Animate arrival
                self.play(FadeIn(element))
                
                # Calculate target position
                target_y = stack1_base.get_bottom()[1] + 0.4 + i * 0.8
                target_pos = LEFT * 3.5 + UP * target_y
                
                # Push onto stack
                self.play(element.animate.move_to(target_pos))
                stack1_elements.add(element)
                
                # Add operation label
                op_label = Text(f"enqueue({val})", font_size=24, color=YELLOW)
                op_label.move_to(UP * 1.8)
                self.play(Write(op_label))
                self.wait(0.3)
                self.play(FadeOut(op_label))
        
        with self.voiceover(
            text="As you can see, enqueue is straightforward. We simply push elements onto Stack One, building up our queue from the bottom up."
        ) as tracker:
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def visualize_dequeue_operation(self):
        with self.voiceover(
            text="Now let's see the dequeue operation, which is more interesting. When Stack Two is empty and we want to dequeue, we must transfer all elements from Stack One to Stack Two."
        ) as tracker:
            title = Text("Dequeue Operation", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Create stacks with elements in Stack 1
            stack1_base = Rectangle(width=2.5, height=4, color=BLUE, stroke_opacity=0.5)
            stack1_base.move_to(LEFT * 3.5 + DOWN * 0.5)
            
            stack2_base = Rectangle(width=2.5, height=4, color=GREEN, stroke_opacity=0.5)
            stack2_base.move_to(RIGHT * 3.5 + DOWN * 0.5)
            
            stack1_label = Text("Stack 1", font_size=26, color=BLUE)
            stack1_label.next_to(stack1_base, UP, buff=0.4)
            
            stack2_label = Text("Stack 2", font_size=26, color=GREEN)
            stack2_label.next_to(stack2_base, UP, buff=0.4)
            
            self.play(
                Create(stack1_base),
                Create(stack2_base),
                Write(stack1_label),
                Write(stack2_label)
            )
            
            # Create elements in Stack 1
            stack1_elements = VGroup()
            for i, val in enumerate(["1", "2", "3"]):
                box = Rectangle(width=2.0, height=0.7, color=BLUE, fill_opacity=0.4)
                text = Text(val, font_size=28)
                element = VGroup(box, text)
                target_y = stack1_base.get_bottom()[1] + 0.4 + i * 0.8
                element.move_to(LEFT * 3.5 + UP * target_y)
                stack1_elements.add(element)
            
            self.play(Create(stack1_elements))
        
        with self.voiceover(
            text="The transfer process pops each element from Stack One and pushes it onto Stack Two. This reverses the order. The element that was at the bottom of Stack One becomes the top of Stack Two."
        ) as tracker:
            stack2_elements = VGroup()
            
            # Transfer elements one by one
            for i in range(len(stack1_elements) - 1, -1, -1):
                element = stack1_elements[i]
                
                # Pop from Stack 1
                self.play(element.animate.shift(UP * 1.5))
                
                # Move to Stack 2
                target_y = stack2_base.get_bottom()[1] + 0.4 + (2 - i) * 0.8
                target_pos = RIGHT * 3.5 + UP * target_y
                
                # Change color
                element[0].set_color(GREEN)
                self.play(element.animate.move_to(target_pos))
                stack2_elements.add(element)
                self.wait(0.3)
        
        with self.voiceover(
            text="Now when we dequeue, we simply pop from Stack Two. Notice that we get element one first, which was the first element we enqueued. This gives us the correct First In First Out behavior."
        ) as tracker:
            # Dequeue operation
            dequeued = stack2_elements[-1]
            dequeue_label = Text("dequeue() → 1", font_size=26, color=YELLOW)
            dequeue_label.move_to(UP * 1.8)
            
            self.play(Write(dequeue_label))
            self.play(
                dequeued.animate.shift(UP * 2),
                FadeOut(dequeued)
            )
            self.wait(0.5)
        
        self.play(FadeOut(*self.mobjects))

    def complete_example_walkthrough(self):
        with self.voiceover(
            text="Let's walk through a complete example with multiple operations to see how the two stacks work together. We'll perform a sequence of enqueues and dequeues."
        ) as tracker:
            title = Text("Complete Example", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
        
        with self.voiceover(
            text="We'll start by enqueuing the numbers ten, twenty, thirty, and forty into our queue implementation."
        ) as tracker:
            # Setup stacks
            stack1_base = Rectangle(width=2.2, height=3.5, color=BLUE, stroke_opacity=0.5)
            stack1_base.move_to(LEFT * 3.5 + DOWN * 0.8)
            
            stack2_base = Rectangle(width=2.2, height=3.5, color=GREEN, stroke_opacity=0.5)
            stack2_base.move_to(RIGHT * 3.5 + DOWN * 0.8)
            
            stack1_label = Text("Stack 1: Input", font_size=24, color=BLUE)
            stack1_label.next_to(stack1_base, UP, buff=0.3)
            
            stack2_label = Text("Stack 2: Output", font_size=24, color=GREEN)
            stack2_label.next_to(stack2_base, UP, buff=0.3)
            
            self.play(
                Create(stack1_base),
                Create(stack2_base),
                Write(stack1_label),
                Write(stack2_label)
            )
            
            # Enqueue operations
            stack1_elements = VGroup()
            values = ["10", "20", "30", "40"]
            
            for i, val in enumerate(values):
                box = Rectangle(width=1.8, height=0.6, color=BLUE, fill_opacity=0.4)
                text = Text(val, font_size=22)
                element = VGroup(box, text)
                
                target_y = stack1_base.get_bottom()[1] + 0.35 + i * 0.7
                element.move_to(LEFT * 3.5 + UP * target_y)
                
                op = Text(f"enqueue({val})", font_size=22, color=YELLOW)
                op.to_edge(DOWN, buff=0.5)
                
                self.play(Write(op), FadeIn(element))
                stack1_elements.add(element)
                self.wait(0.2)
                self.play(FadeOut(op))
        
        with self.voiceover(
            text="Now let's perform our first dequeue. Since Stack Two is empty, we transfer all elements from Stack One to Stack Two, then pop from Stack Two to get ten."
        ) as tracker:
            # Transfer all elements
            stack2_elements = VGroup()
            
            for i in range(len(stack1_elements) - 1, -1, -1):
                element = stack1_elements[i]
                self.play(element.animate.shift(UP * 1.2))
                
                target_y = stack2_base.get_bottom()[1] + 0.35 + (3 - i) * 0.7
                element[0].set_color(GREEN)
                self.play(element.animate.move_to(RIGHT * 3.5 + UP * target_y))
                stack2_elements.add(element)
            
            # Dequeue
            dequeued = stack2_elements[-1]
            op = Text("dequeue() → 10", font_size=22, color=YELLOW)
            op.to_edge(DOWN, buff=0.5)
            self.play(Write(op))
            self.play(FadeOut(dequeued))
            stack2_elements.remove(dequeued)
            self.wait(0.3)
            self.play(FadeOut(op))
        
        with self.voiceover(
            text="Next, we enqueue fifty. This goes onto Stack One. Then we dequeue again. This time, Stack Two is not empty, so we simply pop from it, getting twenty without any transfer."
        ) as tracker:
            # Enqueue 50
            box = Rectangle(width=1.8, height=0.6, color=BLUE, fill_opacity=0.4)
            text = Text("50", font_size=22)
            element = VGroup(box, text)
            element.move_to(LEFT * 3.5 + stack1_base.get_bottom() + UP * 0.35)
            
            op = Text("enqueue(50)", font_size=22, color=YELLOW)
            op.to_edge(DOWN, buff=0.5)
            self.play(Write(op), FadeIn(element))
            self.wait(0.3)
            self.play(FadeOut(op))
            
            # Dequeue (from Stack 2)
            dequeued = stack2_elements[-1]
            op = Text("dequeue() → 20", font_size=22, color=YELLOW)
            op.to_edge(DOWN, buff=0.5)
            self.play(Write(op))
            self.play(FadeOut(dequeued))
            self.wait(0.3)
            self.play(FadeOut(op))
        
        self.play(FadeOut(*self.mobjects))

    def time_complexity_analysis(self):
        with self.voiceover(
            text="Let's analyze the time complexity of our queue implementation. This is important for understanding the efficiency of our solution."
        ) as tracker:
            title = Text("Time Complexity Analysis", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
        
        with self.voiceover(
            text="For the enqueue operation, we simply push onto Stack One, which takes constant time, O of one. This is straightforward and efficient."
        ) as tracker:
            enqueue_analysis = VGroup(
                Text("Enqueue Operation:", font_size=28, color=YELLOW),
                MathTex(r"\text{Time: } O(1)", font_size=32, color=GREEN),
                Text("• Single push to Stack 1", font_size=22),
                Text("• No transfer needed", font_size=22)
            )
            enqueue_analysis.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
            enqueue_analysis.move_to(UP * 0.8)
            
            self.play(Write(enqueue_analysis))
        
        with self.voiceover(
            text="For dequeue, the analysis is more interesting. In the worst case, we transfer all n elements from Stack One to Stack Two, which takes O of n time. However, each element is transferred at most once."
        ) as tracker:
            self.play(FadeOut(enqueue_analysis))
            
            dequeue_analysis = VGroup(
                Text("Dequeue Operation:", font_size=28, color=YELLOW),
                MathTex(r"\text{Worst case: } O(n)", font_size=32, color=RED),
                Text("• Transfer all elements once", font_size=22),
                MathTex(r"\text{Amortized: } O(1)", font_size=32, color=GREEN),
                Text("• Each element moved at most twice", font_size=22)
            )
            dequeue_analysis.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
            dequeue_analysis.move_to(UP * 0.5)
            
            self.play(Write(dequeue_analysis))
        
        with self.voiceover(
            text="Using amortized analysis, we can show that dequeue also has constant amortized time. Over a sequence of operations, each element is pushed twice and popped twice, giving us O of one amortized time per operation."
        ) as tracker:
            amortized_box = Rectangle(
                width=10,
                height=2,
                color=YELLOW,
                fill_opacity=0.1
            )
            amortized_box.move_to(DOWN * 1.5)
            
            amortized_text = VGroup(
                Text("Amortized Analysis:", font_size=24, color=YELLOW),
                Text("Over n operations:", font_size=20),
                MathTex(r"\text{Total time: } 4n = O(n)", font_size=24),
                MathTex(r"\text{Per operation: } O(1)", font_size=24, color=GREEN)
            )
            amortized_text.arrange(DOWN, buff=0.25)
            amortized_text.move_to(DOWN * 1.5)
            
            self.play(Create(amortized_box))
            self.play(Write(amortized_text))
        
        self.play(FadeOut(*self.mobjects))

    def applications_and_use_cases(self):
        with self.voiceover(
            text="This two-stack queue implementation has several practical applications in computer science and software engineering."
        ) as tracker:
            title = Text("Applications & Use Cases", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
        
        with self.voiceover(
            text="First, it's commonly used in interview questions to test understanding of data structures. Many companies ask this problem to evaluate problem-solving skills and knowledge of time complexity analysis."
        ) as tracker:
            app1 = VGroup(
                Text("1. Interview Problems", font_size=28, color=YELLOW),
                Text("• Tests data structure knowledge", font_size=22),
                Text("• Evaluates problem-solving", font_size=22),
                Text("• Common at top tech companies", font_size=22)
            )
            app1.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            app1.move_to(UP * 1.2)
            
            self.play(Write(app1))
        
        with self.voiceover(
            text="Second, it demonstrates important design patterns. The technique of using multiple data structures to implement another is a fundamental concept in algorithm design and can be applied to many other problems."
        ) as tracker:
            self.play(FadeOut(app1))
            
            app2 = VGroup(
                Text("2. Design Patterns", font_size=28, color=YELLOW),
                Text("• Building complex from simple", font_size=22),
                Text("• Multiple structure collaboration", font_size=22),
                Text("• Amortized analysis techniques", font_size=22)
            )
            app2.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            app2.move_to(UP * 1.2)
            
            self.play(Write(app2))
        
        with self.voiceover(
            text="Third, it has real-world applications in systems where you have limited memory or specific hardware constraints. For example, embedded systems with separate memory regions or undo-redo functionality in applications."
        ) as tracker:
            self.play(FadeOut(app2))
            
            app3 = VGroup(
                Text("3. Real-World Systems", font_size=28, color=YELLOW),
                Text("• Embedded systems", font_size=22),
                Text("• Memory-constrained devices", font_size=22),
                Text("• Undo/Redo implementations", font_size=22),
                Text("• Browser history navigation", font_size=22)
            )
            app3.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            app3.move_to(UP * 0.8)
            
            self.play(Write(app3))
        
        self.play(FadeOut(*self.mobjects))

    def summary_and_conclusion(self):
        with self.voiceover(
            text="Let's summarize everything we've learned about implementing a queue using two stacks."
        ) as tracker:
            title = Text("Summary", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
        
        with self.voiceover(
            text="We learned that queues follow First In First Out, while stacks follow Last In First Out. By using two stacks together, we can reverse the order twice to achieve queue behavior."
        ) as tracker:
            summary1 = VGroup(
                Text("Key Concepts:", font_size=30, color=YELLOW),
                Text("✓ Queue: FIFO behavior", font_size=24, color=GREEN),
                Text("✓ Stack: LIFO behavior", font_size=24, color=GREEN),
                Text("✓ Two stacks reverse order", font_size=24, color=GREEN)
            )
            summary1.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
            summary1.move_to(UP * 1.0)
            
            self.play(Write(summary1))
        
        with self.voiceover(
            text="The implementation uses Stack One for enqueue operations and Stack Two for dequeue operations. Elements are transferred from Stack One to Stack Two only when needed, making the amortized time complexity O of one for both operations."
        ) as tracker:
            self.play(FadeOut(summary1))
            
            summary2 = VGroup(
                Text("Implementation Details:", font_size=30, color=YELLOW),
                Text("✓ Stack 1: Input stack", font_size=24, color=GREEN),
                Text("✓ Stack 2: Output stack", font_size=24, color=GREEN),
                Text("✓ Transfer when Stack 2 empty", font_size=24, color=GREEN),
                Text("✓ O(1) amortized time", font_size=24, color=GREEN)
            )
            summary2.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
            summary2.move_to(UP * 0.8)
            
            self.play(Write(summary2))
        
        with self.voiceover(
            text="Thank you for watching this comprehensive tutorial on queue implementation using stacks. I hope this visualization helped you understand both the concept and the implementation details. Keep practicing and happy coding!"
        ) as tracker:
            self.play(FadeOut(*self.mobjects))
            
            thanks = Text("Thank You!", font_size=36, color=BLUE)
            thanks.move_to(UP * 0.5)
            
            subscribe = Text(
                "Subscribe for more data structure tutorials",
                font_size=24,
                color=YELLOW
            )
            subscribe.move_to(DOWN * 1.0)
            
            self.play(Write(thanks))
            self.play(FadeIn(subscribe))
            self.wait(2)