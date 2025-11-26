from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class StackLinkedListVisualization(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))
        
        # Introduction
        self.show_introduction()
        
        # Theory of Stack
        self.explain_stack_concept()
        
        # Stack vs Array vs Linked List
        self.compare_implementations()
        
        # Node Structure
        self.explain_node_structure()
        
        # Stack Class Structure
        self.show_stack_class()
        
        # Push Operation
        self.visualize_push_operation()
        
        # Pop Operation
        self.visualize_pop_operation()
        
        # Peek and isEmpty Operations
        self.show_other_operations()
        
        # Time Complexity Analysis
        self.analyze_complexity()
        
        # Complete Example Walkthrough
        self.complete_example()
        
        # Real World Applications
        self.show_applications()
        
        # Conclusion
        self.show_conclusion()

    def show_introduction(self):
        with self.voiceover(text="Welcome to this comprehensive tutorial on implementing a stack data structure using a linked list. Today, we will explore every aspect of this fundamental data structure, from basic concepts to detailed implementation.") as tracker:
            title = Text("Stack Implementation", font_size=36, color=BLUE)
            subtitle = Text("Using Linked List", font_size=28, color=GREEN)
            subtitle.next_to(title, DOWN, buff=0.4)
            
            self.play(Write(title))
            self.play(FadeIn(subtitle, shift=UP))
            self.wait(2)
        
        with self.voiceover(text="A stack is one of the most important data structures in computer science. It follows the Last In First Out principle, meaning the last element added is the first one to be removed. Think of it like a stack of plates where you can only add or remove from the top.") as tracker:
            self.play(FadeOut(title), FadeOut(subtitle))
            
            # Create visual representation of plates
            plate1 = Rectangle(width=2, height=0.3, color=RED, fill_opacity=0.7)
            plate2 = Rectangle(width=2, height=0.3, color=ORANGE, fill_opacity=0.7)
            plate3 = Rectangle(width=2, height=0.3, color=YELLOW, fill_opacity=0.7)
            
            plate1.move_to(DOWN * 1.5)
            plate2.move_to(DOWN * 0.8)
            plate3.move_to(DOWN * 0.1)
            
            self.play(FadeIn(plate1, shift=UP))
            self.wait(0.5)
            self.play(FadeIn(plate2, shift=UP))
            self.wait(0.5)
            self.play(FadeIn(plate3, shift=UP))
            
            lifo_text = Text("LIFO: Last In, First Out", font_size=24, color=BLUE)
            lifo_text.to_edge(UP, buff=1.0)
            self.play(Write(lifo_text))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def explain_stack_concept(self):
        with self.voiceover(text="Let's understand the core operations of a stack. A stack supports several fundamental operations that define its behavior and make it useful for various programming tasks.") as tracker:
            operations_title = Text("Stack Operations", font_size=32, color=BLUE)
            operations_title.to_edge(UP, buff=1.0)
            self.play(Write(operations_title))
            
            operations = VGroup(
                Text("• Push: Add element to top", font_size=24),
                Text("• Pop: Remove element from top", font_size=24),
                Text("• Peek: View top element", font_size=24),
                Text("• isEmpty: Check if stack is empty", font_size=24)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
            operations.move_to(DOWN * 0.5)
            
            self.play(Write(operations[0]))
            self.wait(0.8)
            self.play(Write(operations[1]))
            self.wait(0.8)
            self.play(Write(operations[2]))
            self.wait(0.8)
            self.play(Write(operations[3]))
            self.wait(1)
        
        with self.voiceover(text="These operations are the building blocks of stack functionality. Push adds a new element, pop removes the most recently added element, peek lets us see what's on top without removing it, and isEmpty tells us if the stack has any elements. Each operation is crucial for different programming scenarios.") as tracker:
            # Highlight each operation
            for op in operations:
                self.play(op.animate.set_color(YELLOW), run_time=0.6)
                self.play(op.animate.set_color(WHITE), run_time=0.4)
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def compare_implementations(self):
        with self.voiceover(text="Before diving into linked list implementation, let's compare different ways to implement a stack. We can use arrays or linked lists, and each approach has its own advantages and trade-offs.") as tracker:
            comparison_title = Text("Implementation Comparison", font_size=32, color=BLUE)
            comparison_title.to_edge(UP, buff=1.0)
            self.play(Write(comparison_title))
            
            # Array implementation side
            array_label = Text("Array Implementation", font_size=24, color=ORANGE)
            array_label.move_to(LEFT * 3.5 + UP * 1.5)
            
            array_pros = VGroup(
                Text("✓ Fast access", font_size=18, color=GREEN),
                Text("✓ Cache friendly", font_size=18, color=GREEN)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            array_pros.next_to(array_label, DOWN, buff=0.4)
            
            array_cons = VGroup(
                Text("✗ Fixed size", font_size=18, color=RED),
                Text("✗ Waste space", font_size=18, color=RED)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            array_cons.next_to(array_pros, DOWN, buff=0.4)
            
            self.play(Write(array_label))
            self.play(Write(array_pros))
            self.play(Write(array_cons))
        
        with self.voiceover(text="In contrast, the linked list implementation offers dynamic sizing without pre-allocation. There's no wasted space, and the stack can grow as needed. However, each element requires extra memory for storing pointers, and we lose the cache efficiency of arrays. The trade-off is flexibility versus memory overhead.") as tracker:
            # Linked List implementation side
            ll_label = Text("Linked List Implementation", font_size=24, color=GREEN)
            ll_label.move_to(RIGHT * 3.5 + UP * 1.5)
            
            ll_pros = VGroup(
                Text("✓ Dynamic size", font_size=18, color=GREEN),
                Text("✓ No waste", font_size=18, color=GREEN)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            ll_pros.next_to(ll_label, DOWN, buff=0.4)
            
            ll_cons = VGroup(
                Text("✗ Extra memory", font_size=18, color=RED),
                Text("✗ Pointer overhead", font_size=18, color=RED)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            ll_cons.next_to(ll_pros, DOWN, buff=0.4)
            
            self.play(Write(ll_label))
            self.play(Write(ll_pros))
            self.play(Write(ll_cons))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def explain_node_structure(self):
        with self.voiceover(text="The foundation of our linked list stack is the Node structure. Each node contains two essential components: the data it holds, and a pointer to the next node in the chain. This simple structure allows us to build dynamic, flexible data structures.") as tracker:
            node_title = Text("Node Structure", font_size=32, color=BLUE)
            node_title.to_edge(UP, buff=1.0)
            self.play(Write(node_title))
            
            # Create node visualization
            node_rect = Rectangle(width=3, height=1.5, color=WHITE)
            node_rect.move_to(DOWN * 0.5)
            
            # Divide into two parts
            divider = Line(node_rect.get_top(), node_rect.get_bottom(), color=WHITE)
            divider.move_to(node_rect.get_center() + LEFT * 0.75)
            
            data_label = Text("data", font_size=22)
            data_label.move_to(node_rect.get_center() + LEFT * 1.1)
            
            next_label = Text("next", font_size=22)
            next_label.move_to(node_rect.get_center() + RIGHT * 0.8)
            
            self.play(Create(node_rect))
            self.play(Create(divider))
            self.play(Write(data_label), Write(next_label))
            self.wait(1)
        
        with self.voiceover(text="Let's see the actual code for our Node class. We define an initializer that takes data as a parameter and sets the next pointer to None by default. This creates a self-contained unit that can be linked to other nodes. The data field can hold any type of value, making our stack versatile and reusable.") as tracker:
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
            code.move_to(DOWN * 1.5)
            
            self.play(FadeOut(node_rect, divider, data_label, next_label))
            self.play(Create(code))
            self.wait(3)
        
        self.play(FadeOut(*self.mobjects))

    def show_stack_class(self):
        with self.voiceover(text="Now let's examine the Stack class itself. Our stack maintains a single pointer called 'top' that always points to the most recently added node. When the stack is empty, top is None. This simple design gives us constant time access to the top element.") as tracker:
            stack_title = Text("Stack Class Structure", font_size=32, color=BLUE)
            stack_title.to_edge(UP, buff=1.0)
            self.play(Write(stack_title))
            
            class_code = Code(
                code="""class Stack:
    def __init__(self):
        self.top = None
    
    def isEmpty(self):
        return self.top is None""",
                language="python",
                font_size=20,
                background="window",
                insert_line_no=False
            )
            class_code.move_to(DOWN * 0.8)
            
            self.play(Create(class_code))
            self.wait(2)
        
        with self.voiceover(text="The isEmpty method is straightforward but essential. It simply checks if the top pointer is None, which indicates an empty stack. This method is used internally by other operations to prevent errors when trying to pop or peek at an empty stack. It's a defensive programming technique that makes our code more robust.") as tracker:
            # Highlight isEmpty method
            highlight_rect = SurroundingRectangle(class_code, color=YELLOW, buff=0.1)
            self.play(Create(highlight_rect))
            self.wait(2)
            self.play(FadeOut(highlight_rect))
        
        self.play(FadeOut(*self.mobjects))

    def visualize_push_operation(self):
        with self.voiceover(text="The push operation is where things get interesting. When we push a new element onto the stack, we create a new node, set its next pointer to the current top, and then update top to point to this new node. Let's visualize this step by step.") as tracker:
            push_title = Text("Push Operation", font_size=32, color=BLUE)
            push_title.to_edge(UP, buff=1.0)
            self.play(Write(push_title))
            
            # Show initial empty stack
            top_pointer = Text("top → None", font_size=24, color=RED)
            top_pointer.move_to(UP * 1.5 + LEFT * 4)
            self.play(Write(top_pointer))
            self.wait(1)
        
        with self.voiceover(text="Let's push the value ten onto our empty stack. First, we create a new node containing ten. Then we set the new node's next pointer to the current top, which is None. Finally, we update top to point to our new node. The stack now has one element.") as tracker:
            # Create first node
            node1 = self.create_node("10", DOWN * 0.5)
            self.play(Create(node1))
            
            # Update top pointer
            new_top = Text("top", font_size=24, color=RED)
            new_top.next_to(node1, LEFT, buff=0.8)
            arrow1 = Arrow(new_top.get_right(), node1.get_left(), color=RED, buff=0.1)
            
            self.play(FadeOut(top_pointer))
            self.play(Write(new_top), Create(arrow1))
            self.wait(1)
        
        with self.voiceover(text="Now let's push twenty. We create a new node for twenty, set its next to point to the node containing ten, and update top to point to the new node. Notice how the new element is always added at the top, maintaining the Last In First Out property.") as tracker:
            # Create second node
            node2 = self.create_node("20", UP * 0.8)
            self.play(Create(node2))
            
            # Create connection from node2 to node1
            connection = Arrow(node2.get_bottom() + DOWN * 0.1, node1.get_top() + UP * 0.1, 
                             color=GREEN, buff=0.1, stroke_width=3)
            self.play(Create(connection))
            
            # Update top pointer
            self.play(FadeOut(arrow1))
            arrow2 = Arrow(new_top.get_right(), node2.get_left(), color=RED, buff=0.1)
            new_top.next_to(node2, LEFT, buff=0.8)
            self.play(Write(new_top), Create(arrow2))
            self.wait(1)
        
        with self.voiceover(text="Let's add one more element, thirty, to see the pattern clearly. Each new node is inserted at the beginning of the chain, and top always points to the most recent addition. This gives us constant time insertion, regardless of how many elements are in the stack.") as tracker:
            # Create third node
            node3 = self.create_node("30", UP * 2.1)
            self.play(Create(node3))
            
            # Create connection from node3 to node2
            connection2 = Arrow(node3.get_bottom() + DOWN * 0.1, node2.get_top() + UP * 0.1, 
                              color=GREEN, buff=0.1, stroke_width=3)
            self.play(Create(connection2))
            
            # Update top pointer
            self.play(FadeOut(arrow2))
            arrow3 = Arrow(new_top.get_right(), node3.get_left(), color=RED, buff=0.1)
            new_top.next_to(node3, LEFT, buff=0.8)
            self.play(Write(new_top), Create(arrow3))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Here's the complete Python code for the push operation. We create a new node with the given data, set its next pointer to the current top, and then update top to the new node. It's elegant in its simplicity, yet powerful in its efficiency.") as tracker:
            code_title = Text("Push Implementation", font_size=28, color=BLUE)
            code_title.to_edge(UP, buff=1.0)
            self.play(Write(code_title))
            
            push_code = Code(
                code="""def push(self, data):
    # Create new node
    new_node = Node(data)
    
    # Set new node's next to current top
    new_node.next = self.top
    
    # Update top to new node
    self.top = new_node""",
                language="python",
                font_size=20,
                background="window",
                insert_line_no=False
            )
            push_code.move_to(DOWN * 0.5)
            
            self.play(Create(push_code))
            self.wait(3)
        
        self.play(FadeOut(*self.mobjects))

    def visualize_pop_operation(self):
        with self.voiceover(text="The pop operation is the reverse of push. We need to remove the top element and return its data. But we must be careful to check if the stack is empty first, otherwise we'll encounter an error trying to access None.") as tracker:
            pop_title = Text("Pop Operation", font_size=32, color=BLUE)
            pop_title.to_edge(UP, buff=1.0)
            self.play(Write(pop_title))
            
            # Create initial stack with 3 nodes
            top_label = Text("top", font_size=24, color=RED)
            top_label.move_to(UP * 2.1 + LEFT * 4)
            
            node1 = self.create_node("30", UP * 2.1)
            node2 = self.create_node("20", UP * 0.8)
            node3 = self.create_node("10", DOWN * 0.5)
            
            arrow_top = Arrow(top_label.get_right(), node1.get_left(), color=RED, buff=0.1)
            conn1 = Arrow(node1.get_bottom() + DOWN * 0.1, node2.get_top() + UP * 0.1, 
                         color=GREEN, buff=0.1, stroke_width=3)
            conn2 = Arrow(node2.get_bottom() + DOWN * 0.1, node3.get_top() + UP * 0.1, 
                         color=GREEN, buff=0.1, stroke_width=3)
            
            self.play(Write(top_label), Create(node1), Create(node2), Create(node3))
            self.play(Create(arrow_top), Create(conn1), Create(conn2))
            self.wait(1)
        
        with self.voiceover(text="To pop, we first store the data from the top node. Then we update top to point to the next node in the chain. The old top node is effectively removed from the stack. We return the stored data value. Let's see this in action.") as tracker:
            # Highlight the node being popped
            highlight = SurroundingRectangle(node1, color=YELLOW, buff=0.1)
            self.play(Create(highlight))
            
            # Show data being extracted
            data_text = Text("Return: 30", font_size=24, color=YELLOW)
            data_text.next_to(node1, RIGHT, buff=1.0)
            self.play(Write(data_text))
            self.wait(1)
            
            # Remove top node
            self.play(FadeOut(node1), FadeOut(highlight), FadeOut(conn1), FadeOut(arrow_top))
            
            # Update top pointer
            new_arrow = Arrow(top_label.get_right(), node2.get_left(), color=RED, buff=0.1)
            top_label.next_to(node2, LEFT, buff=0.8)
            self.play(Write(top_label), Create(new_arrow))
            self.wait(2)
        
        with self.voiceover(text="If we pop again, we remove twenty and top now points to ten. Each pop operation removes the most recently added element, maintaining our Last In First Out behavior. Notice how we always work with the top of the stack, never needing to traverse the entire list.") as tracker:
            # Pop second element
            highlight2 = SurroundingRectangle(node2, color=YELLOW, buff=0.1)
            self.play(FadeOut(data_text))
            self.play(Create(highlight2))
            
            data_text2 = Text("Return: 20", font_size=24, color=YELLOW)
            data_text2.next_to(node2, RIGHT, buff=1.0)
            self.play(Write(data_text2))
            self.wait(1)
            
            self.play(FadeOut(node2), FadeOut(highlight2), FadeOut(conn2), FadeOut(new_arrow))
            
            final_arrow = Arrow(top_label.get_right(), node3.get_left(), color=RED, buff=0.1)
            top_label.next_to(node3, LEFT, buff=0.8)
            self.play(Write(top_label), Create(final_arrow))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Here's the complete pop implementation. We check if the stack is empty and return None if it is. Otherwise, we store the top's data, move top to the next node, and return the stored data. Error handling is crucial here to prevent runtime exceptions.") as tracker:
            code_title = Text("Pop Implementation", font_size=28, color=BLUE)
            code_title.to_edge(UP, buff=1.0)
            self.play(Write(code_title))
            
            pop_code = Code(
                code="""def pop(self):
    # Check if stack is empty
    if self.isEmpty():
        return None
    
    # Store data to return
    popped_data = self.top.data
    
    # Move top to next node
    self.top = self.top.next
    
    # Return the data
    return popped_data""",
                language="python",
                font_size=18,
                background="window",
                insert_line_no=False
            )
            pop_code.move_to(DOWN * 0.3)
            
            self.play(Create(pop_code))
            self.wait(3)
        
        self.play(FadeOut(*self.mobjects))

    def show_other_operations(self):
        with self.voiceover(text="Besides push and pop, we have two other important operations. The peek operation lets us view the top element without removing it. This is useful when we need to check what's on top before deciding whether to pop it.") as tracker:
            other_title = Text("Peek and isEmpty Operations", font_size=32, color=BLUE)
            other_title.to_edge(UP, buff=1.0)
            self.play(Write(other_title))
            
            peek_code = Code(
                code="""def peek(self):
    # Check if stack is empty
    if self.isEmpty():
        return None
    
    # Return top data without removing
    return self.top.data""",
                language="python",
                font_size=20,
                background="window",
                insert_line_no=False
            )
            peek_code.move_to(LEFT * 3.0 + DOWN * 0.5)
            
            self.play(Create(peek_code))
            self.wait(2)
        
        with self.voiceover(text="The isEmpty operation is equally important. It returns True if the stack has no elements, False otherwise. This is used both internally by other methods and externally by code using the stack. It's a simple boolean check that prevents many potential errors.") as tracker:
            empty_code = Code(
                code="""def isEmpty(self):
    return self.top is None
    
# Usage example:
if not stack.isEmpty():
    value = stack.peek()""",
                language="python",
                font_size=20,
                background="window",
                insert_line_no=False
            )
            empty_code.move_to(RIGHT * 3.0 + DOWN * 0.5)
            
            self.play(Create(empty_code))
            self.wait(3)
        
        self.play(FadeOut(*self.mobjects))

    def analyze_complexity(self):
        with self.voiceover(text="Let's analyze the time and space complexity of our stack operations. Understanding complexity helps us make informed decisions about when to use this data structure.") as tracker:
            complexity_title = Text("Time Complexity Analysis", font_size=32, color=BLUE)
            complexity_title.to_edge(UP, buff=1.0)
            self.play(Write(complexity_title))
            
            table_data = [
                ["Operation", "Time", "Explanation"],
                ["Push", "O(1)", "Direct insertion at top"],
                ["Pop", "O(1)", "Direct removal from top"],
                ["Peek", "O(1)", "Direct access to top"],
                ["isEmpty", "O(1)", "Simple pointer check"]
            ]
            
            # Create table manually with proper positioning
            header = VGroup(
                Text("Operation", font_size=20, weight=BOLD),
                Text("Time", font_size=20, weight=BOLD),
                Text("Explanation", font_size=20, weight=BOLD)
            ).arrange(RIGHT, buff=1.2)
            header.move_to(UP * 1.5)
            
            self.play(Write(header))
            self.wait(1)
        
        with self.voiceover(text="All our basic operations run in constant time, O(1). Push doesn't need to traverse the list, it just adds at the top. Pop removes from the top directly. Peek accesses the top immediately. And isEmpty is just a pointer comparison. This constant time performance is one of the key advantages of the stack data structure.") as tracker:
            # Add rows one by one
            rows = VGroup()
            y_pos = 0.5
            for i, row in enumerate(table_data[1:]):
                row_group = VGroup(
                    Text(row[0], font_size=18),
                    Text(row[1], font_size=18, color=GREEN),
                    Text(row[2], font_size=16)
                ).arrange(RIGHT, buff=1.2)
                row_group.move_to(UP * y_pos)
                rows.add(row_group)
                y_pos -= 0.7
                
                self.play(FadeIn(row_group, shift=UP), run_time=0.8)
            
            self.wait(2)
        
        with self.voiceover(text="The space complexity is O(n) where n is the number of elements in the stack. Each element requires a node with data and a next pointer. While this is more memory than a simple array, it gives us the flexibility of dynamic sizing without pre-allocation.") as tracker:
            space_text = Text("Space Complexity: O(n)", font_size=24, color=YELLOW)
            space_text.move_to(DOWN * 2.5)
            self.play(Write(space_text))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def complete_example(self):
        with self.voiceover(text="Let's walk through a complete example that demonstrates all our operations in sequence. We'll create a stack, push several elements, peek at the top, pop some elements, and check if it's empty. This will show how everything works together in practice.") as tracker:
            example_title = Text("Complete Example Walkthrough", font_size=32, color=BLUE)
            example_title.to_edge(UP, buff=1.0)
            self.play(Write(example_title))
            
            code = Code(
                code="""# Create empty stack
stack = Stack()

# Push elements
stack.push(5)
stack.push(10)
stack.push(15)

# Peek at top
top_value = stack.peek()  # Returns 15

# Pop elements
stack.pop()  # Returns 15
stack.pop()  # Returns 10

# Check state
is_empty = stack.isEmpty()  # Returns False""",
                language="python",
                font_size=18,
                background="window",
                insert_line_no=False
            )
            code.move_to(DOWN * 0.5)
            
            self.play(Create(code))
            self.wait(3)
        
        with self.voiceover(text="Let's visualize this example step by step. We start with an empty stack. Then we push five, ten, and fifteen. After peeking at fifteen, we pop twice, removing fifteen and ten. The stack now contains only five, so isEmpty returns False. This demonstrates the complete lifecycle of stack operations.") as tracker:
            self.play(FadeOut(code))
            
            # Create visualization area
            steps = VGroup(
                Text("1. Empty stack", font_size=20),
                Text("2. Push 5, 10, 15", font_size=20),
                Text("3. Peek → 15", font_size=20),
                Text("4. Pop → 15, 10", font_size=20),
                Text("5. Stack: [5]", font_size=20)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
            steps.move_to(LEFT * 3.5 + DOWN * 0.5)
            
            for step in steps:
                self.play(Write(step), run_time=1.2)
                self.wait(0.8)
            
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def show_applications(self):
        with self.voiceover(text="Stacks are used extensively in real-world applications. Let's explore some of the most important use cases where stacks are essential to solving complex problems efficiently.") as tracker:
            app_title = Text("Real-World Applications", font_size=32, color=BLUE)
            app_title.to_edge(UP, buff=1.0)
            self.play(Write(app_title))
            
            applications = VGroup(
                Text("• Function Call Stack", font_size=24),
                Text("• Expression Evaluation", font_size=24),
                Text("• Backtracking Algorithms", font_size=24),
                Text("• Undo/Redo Functionality", font_size=24),
                Text("• Browser History", font_size=24)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
            applications.move_to(DOWN * 0.5)
            
            for app in applications:
                self.play(Write(app), run_time=0.8)
                self.wait(0.6)
            
            self.wait(1)
        
        with self.voiceover(text="The function call stack is fundamental to how programming languages work. When you call a function, its context is pushed onto the call stack. When it returns, the context is popped. Expression evaluation uses stacks to convert infix notation to postfix and evaluate complex mathematical expressions. Backtracking algorithms in maze solving and puzzle games use stacks to remember paths.") as tracker:
            self.wait(4)
        
        with self.voiceover(text="Undo and redo features in text editors and graphics programs rely on stacks to track operations. Browser history uses stacks to implement the back button functionality. These applications demonstrate why understanding stack implementation is crucial for every programmer. The stack's Last In First Out property naturally models these real-world scenarios.") as tracker:
            self.wait(4)
        
        self.play(FadeOut(*self.mobjects))

    def show_conclusion(self):
        with self.voiceover(text="We've completed our comprehensive journey through stack implementation using linked lists. Let's recap the key points we've covered today.") as tracker:
            conclusion_title = Text("Summary and Key Takeaways", font_size=32, color=BLUE)
            conclusion_title.to_edge(UP, buff=1.0)
            self.play(Write(conclusion_title))
            
            key_points = VGroup(
                Text("✓ Stack follows LIFO principle", font_size=22, color=GREEN),
                Text("✓ Linked list provides dynamic sizing", font_size=22, color=GREEN),
                Text("✓ All operations are O(1) time", font_size=22, color=GREEN),
                Text("✓ Space complexity is O(n)", font_size=22, color=GREEN),
                Text("✓ Used in many critical applications", font_size=22, color=GREEN)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
            key_points.move_to(DOWN * 0.5)
            
            for point in key_points:
                self.play(Write(point), run_time=0.9)
                self.wait(0.6)
            
            self.wait(2)
        
        with self.voiceover(text="Understanding stack implementation is fundamental to computer science. The linked list approach gives us flexibility and constant time operations. Whether you're building compilers, implementing recursion, or creating user interfaces, stacks are an essential tool in your programming toolkit. Thank you for watching this comprehensive tutorial!") as tracker:
            self.wait(3)
        
        self.play(FadeOut(*self.mobjects))
        
        # Final thank you
        with self.voiceover(text="Keep practicing, keep coding, and remember that mastering data structures is the key to becoming a great programmer. Good luck!") as tracker:
            thank_you = Text("Thank You!", font_size=36, color=BLUE)
            subscribe = Text("Happy Coding!", font_size=28, color=GREEN)
            subscribe.next_to(thank_you, DOWN, buff=0.6)
            
            self.play(Write(thank_you))
            self.play(FadeIn(subscribe, shift=UP))
            self.wait(3)

    def create_node(self, data, position):
        """Helper function to create a node with data and next pointer."""
        node_rect = Rectangle(width=2.0, height=0.8, color=WHITE)
        node_rect.move_to(position)
        
        divider = Line(node_rect.get_top(), node_rect.get_bottom(), color=WHITE)
        divider.move_to(node_rect.get_center() + LEFT * 0.5)
        
        data_text = Text(str(data), font_size=22)
        data_text.move_to(node_rect.get_center() + LEFT * 0.7)
        
        next_arrow = Arrow(ORIGIN, RIGHT * 0.3, color=GREEN, buff=0, stroke_width=3)
        next_arrow.move_to(node_rect.get_center() + RIGHT * 0.5)
        
        return VGroup(node_rect, divider, data_text, next_arrow)


# Instructions to run:
# Save this file as stack_linked_list.py
# Run: manim -pql stack_linked_list.py StackLinkedListVisualization
# For high quality: manim -pqh stack_linked_list.py StackLinkedListVisualization