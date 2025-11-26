# NOTE: This code has been automatically post-processed to fix common issues:
# - Indexed SurroundingRectangle calls have been disabled
# - Layout spacing has been adjusted to prevent overlaps
# - Axis labels have been positioned to stay within frame
# - Font sizes have been capped to prevent massive text
# Undefined color constants have been replaced with standard Manim colors.

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import numpy as np

class MarkovChainsExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        # Introduction
        self.introduction()
        
        # Historical context
        self.historical_context()
        
        # Basic definition and properties
        self.basic_definition()
        
        # Simple weather example
        self.weather_example()
        
        # Transition matrix explanation
        self.transition_matrix_explanation()
        
        # State diagram visualization
        self.state_diagram_visualization()
        
        # Matrix multiplication and prediction
        self.matrix_multiplication()
        
        # Steady state concept
        self.steady_state_explanation()
        
        # Real world applications
        self.real_world_applications()
        
        # Advanced properties
        self.advanced_properties()
        
        # Conclusion
        self.conclusion()

    def introduction(self):
        with self.voiceover(text="Welcome to this comprehensive explanation of Markov Chains, one of the most powerful tools in probability theory and stochastic processes. Markov Chains are used everywhere, from Google's PageRank algorithm to predicting weather patterns, from modeling stock markets to understanding the behavior of molecules in statistical mechanics.") as tracker:
            title = Text("Markov Chains", font_size=36, color=BLUE, weight=BOLD)
            title.to_edge(UP, buff=1.0)
            subtitle = Text("A Journey Through Stochastic Processes", font_size=28, color=YELLOW)
            subtitle.next_to(title, DOWN, buff=0.4)
            
            self.play(Write(title), run_time=2)
            self.play(FadeIn(subtitle), run_time=1.5)
            
        with self.voiceover(text="Today, we will explore what makes Markov Chains special, understand their mathematical foundations, work through detailed examples, and see how they apply to real-world problems. By the end of this video, you will have a deep understanding of this fundamental concept.") as tracker:
            # Create decorative elements
            dots = VGroup(*[Dot(color=BLUE) for _ in range(5)])
            dots.arrange(RIGHT, buff=0.8)
            dots.move_to(DOWN * 1.5)
            
            arrows = VGroup(*[Arrow(dots[i].get_right(), dots[i+1].get_left(), 
                                   buff=0.1, color=GREEN) for i in range(4)])
            
            self.play(Create(dots), run_time=2)
            self.play(Create(arrows), run_time=2)
            
        self.play(FadeOut(*self.mobjects))

    def historical_context(self):
        with self.voiceover(text="Markov Chains are named after the Russian mathematician Andrey Markov, who introduced them in the early nineteen hundreds. Markov was studying sequences of random variables and wanted to understand how past events influence future outcomes.") as tracker:
            title = Text("Historical Context", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Create timeline
            timeline = Line(LEFT * 5, RIGHT * 5, color=WHITE)
            timeline.move_to(DOWN * 0.5)
            
            year_1906 = Text("1906", font_size=24).next_to(timeline.get_left(), UP, buff=0.3)
            year_now = Text("Today", font_size=24).next_to(timeline.get_right(), UP, buff=0.3)
            
            self.play(Create(timeline), Write(year_1906), Write(year_now))
            
        with self.voiceover(text="The key insight that Markov discovered was the memoryless property. This means that the future state of the system depends only on the current state, not on the sequence of events that preceded it. This seemingly simple property has profound implications and makes the mathematics tractable while still capturing important real-world phenomena.") as tracker:
            # Markov property equation
            markov_property = MathTex(
                r"P(X_{n+1} | X_n, X_{n-1}, ..., X_0) = P(X_{n+1} | X_n)",
                font_size=32
            )
            markov_property.move_to(DOWN * 2)
            
            self.play(Write(markov_property), run_time=3)
            
            # Highlight the memoryless property
            box = SurroundingRectangle(markov_property, color=YELLOW, buff=0.15)
            label = Text("Memoryless Property", font_size=24, color=YELLOW)
            label.next_to(box, DOWN, buff=0.3)
            
            self.play(Create(box), Write(label))
            
        self.play(FadeOut(*self.mobjects))

    def basic_definition(self):
        with self.voiceover(text="Let's formally define a Markov Chain. A Markov Chain is a sequence of random variables X zero, X one, X two, and so on, where each variable can take values from a finite or countable set called the state space. The defining characteristic is that the probability of moving to the next state depends only on the current state.") as tracker:
            title = Text("Formal Definition", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # State sequence
            sequence = MathTex(r"X_0, X_1, X_2, X_3, \ldots", font_size=36)
            sequence.move_to(UP * 1.5)
            self.play(Write(sequence))
            
            # State space
            state_space = MathTex(r"\text{State Space: } S = \{s_1, s_2, \ldots, s_n\}", 
                                font_size=32)
            state_space.move_to(UP * 0.3)
            self.play(Write(state_space))
            
        with self.voiceover(text="The transition probabilities form the core of the Markov Chain. We denote P of i to j as the probability of transitioning from state i to state j. These probabilities must satisfy two important conditions: they must be non-negative, and the sum of probabilities leaving any state must equal one, since the system must transition somewhere.") as tracker:
            # Transition probability definition
            transition_prob = MathTex(
                r"P_{ij} = P(X_{n+1} = j \mid X_n = i)",
                font_size=32
            )
            transition_prob.move_to(DOWN * 0.5)
            self.play(Write(transition_prob))
            
            # Conditions
            condition1 = MathTex(r"P_{ij} \geq 0 \text{ for all } i, j", font_size=28)
            condition2 = MathTex(r"\sum_{j} P_{ij} = 1 \text{ for all } i", font_size=28)
            
            conditions = VGroup(condition1, condition2).arrange(DOWN, buff=0.4)
            conditions.move_to(DOWN * 2)
            
            self.play(Write(condition1))
            self.play(Write(condition2))
            
        self.play(FadeOut(*self.mobjects))

    def weather_example(self):
        with self.voiceover(text="Let's make this concrete with a classic example: weather prediction. Imagine we want to model whether tomorrow will be sunny or rainy based on today's weather. We have two states: sunny and rainy. This is a simple two-state Markov Chain that captures the basic idea beautifully.") as tracker:
            title = Text("Example: Weather Prediction", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Create weather states
            sunny = Circle(radius=0.8, color=YELLOW, fill_opacity=0.3)
            sunny_label = Text("Sunny", font_size=28).move_to(sunny.get_center())
            sunny_group = VGroup(sunny, sunny_label)
            sunny_group.shift(LEFT * 3.5 + DOWN * 0.5)
            
            rainy = Circle(radius=0.8, color=BLUE, fill_opacity=0.3)
            rainy_label = Text("Rainy", font_size=28).move_to(rainy.get_center())
            rainy_group = VGroup(rainy, rainy_label)
            rainy_group.shift(RIGHT * 3.5 + DOWN * 0.5)
            
            self.play(Create(sunny_group), Create(rainy_group))
            
        with self.voiceover(text="Let's say that if today is sunny, there is a seventy percent chance tomorrow will also be sunny, and a thirty percent chance it will be rainy. Conversely, if today is rainy, there is a forty percent chance tomorrow will be sunny, and a sixty percent chance it will remain rainy. These probabilities capture the persistence of weather patterns.") as tracker:
            # Add transition arrows and probabilities
            # Sunny to Sunny (self-loop)
            sunny_to_sunny = CurvedArrow(
                sunny.get_top() + LEFT * 0.3,
                sunny.get_top() + RIGHT * 0.3,
                color=GREEN,
                angle=-TAU/4
            )
            ss_prob = MathTex("0.7", font_size=24, color=GREEN)
            ss_prob.next_to(sunny, UP, buff=0.5)
            
            # Sunny to Rainy
            sunny_to_rainy = Arrow(
                sunny.get_right(),
                rainy.get_left(),
                buff=0.2,
                color=ORANGE
            )
            sr_prob = MathTex("0.3", font_size=24, color=ORANGE)
            sr_prob.next_to(sunny_to_rainy, UP, buff=0.1)
            
            # Rainy to Sunny
            rainy_to_sunny = Arrow(
                rainy.get_left(),
                sunny.get_right(),
                buff=0.2,
                color=PURPLE
            )
            rs_prob = MathTex("0.4", font_size=24, color=PURPLE)
            rs_prob.next_to(rainy_to_sunny, DOWN, buff=0.1)
            
            # Rainy to Rainy (self-loop)
            rainy_to_rainy = CurvedArrow(
                rainy.get_top() + LEFT * 0.3,
                rainy.get_top() + RIGHT * 0.3,
                color=RED,
                angle=-TAU/4
            )
            rr_prob = MathTex("0.6", font_size=24, color=RED)
            rr_prob.next_to(rainy, UP, buff=0.5)
            
            self.play(
                Create(sunny_to_sunny), Write(ss_prob),
                Create(rainy_to_rainy), Write(rr_prob)
            )
            self.play(
                Create(sunny_to_rainy), Write(sr_prob),
                Create(rainy_to_sunny), Write(rs_prob)
            )
            
        self.play(FadeOut(*self.mobjects))

    def transition_matrix_explanation(self):
        with self.voiceover(text="We can represent all transition probabilities compactly using a transition matrix, usually denoted by P. Each row of this matrix corresponds to a starting state, and each column corresponds to an ending state. The entry in row i and column j gives us the probability of transitioning from state i to state j.") as tracker:
            title = Text("Transition Matrix", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Create the transition matrix
            matrix_label = MathTex("P = ", font_size=36)
            matrix = MathTex(
                r"\begin{bmatrix} 0.7 & 0.3 \\ 0.4 & 0.6 \end{bmatrix}",
                font_size=36
            )
            
            matrix_group = VGroup(matrix_label, matrix).arrange(RIGHT, buff=0.3)
            matrix_group.move_to(UP * 0.8)
            
            self.play(Write(matrix_label))
            self.play(Write(matrix))
            
        with self.voiceover(text="Let's label the rows and columns to make this crystal clear. The rows represent the current state: sunny or rainy. The columns represent the next state: sunny or rainy. So the top-left entry, zero point seven, is the probability of going from sunny to sunny. The top-right entry, zero point three, is the probability of going from sunny to rainy.") as tracker:
            # Add labels
            row_labels = MathTex(r"\begin{matrix} \text{Sunny} \\ \text{Rainy} \end{matrix}", 
                               font_size=28)
            row_labels.next_to(matrix, LEFT, buff=0.5)
            
            col_labels = MathTex(r"\begin{matrix} \text{Sunny} & \text{Rainy} \end{matrix}", 
                               font_size=28)
            col_labels.next_to(matrix, UP, buff=0.3)
            
            self.play(Write(row_labels), Write(col_labels))
            
            # Highlight entries
            # highlight1 = SurroundingRectangle(matrix[0][2:5], color=YELLOW, buff=0.08)  # Auto-disabled: indexed SurroundingRectangle
            label1 = Text("Sunny → Sunny", font_size=20, color=YELLOW)
            label1.move_to(DOWN * 1.2 + LEFT * 3)
            
            # self.play(Create(highlight1), Write(label1))  # Auto-disabled: uses disabled SurroundingRectangle
            self.wait(1)
            
            # highlight2 = SurroundingRectangle(matrix[0][6:9], color=ORANGE, buff=0.08)  # Auto-disabled: indexed SurroundingRectangle
            label2 = Text("Sunny → Rainy", font_size=20, color=ORANGE)
            label2.move_to(DOWN * 1.8 + LEFT * 3)
            
            self.play(
                # Transform(highlight1, highlight2),  # Auto-disabled: uses disabled SurroundingRectangle
                Transform(label1, label2)
            )
            
        with self.voiceover(text="Notice that each row sums to one. This is essential because from any current state, the probabilities of all possible next states must sum to one hundred percent. We have to end up somewhere! This is a fundamental property that every valid transition matrix must satisfy.") as tracker:
            # Show row sum
            row_sum = MathTex(r"0.7 + 0.3 = 1.0", font_size=32, color=GREEN)
            row_sum.move_to(DOWN * 2.3)
            
            # self.play(FadeOut(highlight1), FadeOut(label1))  # Auto-disabled: uses disabled SurroundingRectangle
            self.play(Write(row_sum))
            
        self.play(FadeOut(*self.mobjects))

    def state_diagram_visualization(self):
        with self.voiceover(text="Now let's visualize how a Markov Chain actually evolves over time. We'll start in the sunny state and simulate several transitions according to our probability rules. This will help us develop intuition for how the system behaves dynamically.") as tracker:
            title = Text("State Evolution", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Create state boxes
            states = VGroup()
            state_labels = ["Day 0", "Day 1", "Day 2", "Day 3", "Day 4"]
            
            for i, label in enumerate(state_labels):
                day_label = Text(label, font_size=20)
                state_box = Rectangle(height=0.8, width=1.2, color=WHITE)
                group = VGroup(day_label, state_box)
                group.arrange(DOWN, buff=0.2)
                states.add(group)
            
            states.arrange(RIGHT, buff=0.6)
            states.move_to(DOWN * 0.5)
            
            self.play(Create(states))
            
        with self.voiceover(text="Let's trace through a possible sequence. We start sunny on day zero. Based on our transition probabilities, we have a seventy percent chance of staying sunny and thirty percent chance of becoming rainy. Let's say we stay sunny on day one. Then on day two, we might transition to rainy. Day three might be rainy again, and day four could be sunny. Each transition follows the probability rules we established.") as tracker:
            # Fill in states
            weather_sequence = ["☀️", "☀️", "🌧️", "🌧️", "☀️"]
            colors = [YELLOW, YELLOW, BLUE, BLUE, YELLOW]
            
            for i, (weather, color) in enumerate(zip(weather_sequence, colors)):
                weather_text = Text(weather, font_size=36)
                weather_text.move_to(states[i][1].get_center())
                states[i][1].set_fill(color, opacity=0.3)
                self.play(
                    states[i][1].animate.set_fill(color, opacity=0.3),
                    Write(weather_text),
                    run_time=0.8
                )
                if i < len(weather_sequence) - 1:
                    arrow = Arrow(
                        states[i][1].get_right(),
                        states[i+1][1].get_left(),
                        buff=0.1,
                        color=GREEN
                    )
                    self.play(Create(arrow), run_time=0.5)
            
        self.play(FadeOut(*self.mobjects))

    def matrix_multiplication(self):
        with self.voiceover(text="One of the most powerful aspects of Markov Chains is that we can predict future states using matrix multiplication. If we know the current probability distribution over states, we can find the distribution after n steps by multiplying by the transition matrix n times. Let me show you exactly how this works.") as tracker:
            title = Text("Prediction via Matrix Powers", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Initial distribution
            initial = MathTex(r"\pi_0 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}", 
                            font_size=32)
            initial_label = Text("(Start: 100% Sunny)", font_size=20)
            initial_group = VGroup(initial, initial_label).arrange(RIGHT, buff=0.4)
            initial_group.move_to(UP * 1.8)
            
            self.play(Write(initial_group))
            
        with self.voiceover(text="Suppose we start with certainty that it's sunny, so our initial state vector is one for sunny and zero for rainy. To find the probability distribution after one day, we multiply this vector by the transition matrix P. Let's work through this calculation step by step.") as tracker:
            # Show P matrix
            P_matrix = MathTex(
                r"P = \begin{bmatrix} 0.7 & 0.3 \\ 0.4 & 0.6 \end{bmatrix}",
                font_size=32
            )
            P_matrix.move_to(UP * 0.6 + LEFT * 3.5)
            
            self.play(Write(P_matrix))
            
            # One step calculation
            one_step = MathTex(
                r"\pi_1 = \pi_0 \cdot P = \begin{bmatrix} 1 & 0 \end{bmatrix} \begin{bmatrix} 0.7 & 0.3 \\ 0.4 & 0.6 \end{bmatrix}",
                font_size=28
            )
            one_step.move_to(DOWN * 0.3)
            
            self.play(Write(one_step))
            
            result1 = MathTex(
                r"= \begin{bmatrix} 0.7 & 0.3 \end{bmatrix}",
                font_size=32
            )
            result1.next_to(one_step, DOWN, buff=0.4)
            
            self.play(Write(result1))
            
        with self.voiceover(text="After one day, we have seventy percent chance of sunny and thirty percent chance of rainy. Now, what about two days? We multiply by P again. After three days, we multiply by P three times total. We can write this as P to the power of three. As we take more and more steps, something remarkable happens.") as tracker:
            # Two steps
            two_steps = MathTex(
                r"\pi_2 = \pi_1 \cdot P = \begin{bmatrix} 0.57 & 0.43 \end{bmatrix}",
                font_size=28
            )
            two_steps.next_to(result1, DOWN, buff=0.5)
            
            self.play(Write(two_steps))
            
            # Three steps
            three_steps = MathTex(
                r"\pi_3 = \pi_0 \cdot P^3 = \begin{bmatrix} 0.547 & 0.453 \end{bmatrix}",
                font_size=28
            )
            three_steps.next_to(two_steps, DOWN, buff=0.3)
            
            self.play(Write(three_steps))
            
        self.play(FadeOut(*self.mobjects))

    def steady_state_explanation(self):
        with self.voiceover(text="As we just hinted, something fascinating happens when we keep multiplying by the transition matrix. The probability distribution starts to converge to a fixed distribution called the steady state or stationary distribution. This is one of the most important concepts in Markov Chain theory.") as tracker:
            title = Text("Steady State Distribution", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Definition
            definition = MathTex(
                r"\pi = \pi \cdot P",
                font_size=36
            )
            definition.move_to(UP * 1.3)
            
            self.play(Write(definition))
            
            def_label = Text("(Stationary Condition)", font_size=24, color=YELLOW)
            def_label.next_to(definition, DOWN, buff=0.3)
            self.play(Write(def_label))
            
        with self.voiceover(text="The steady state pi satisfies the equation pi equals pi times P. In other words, if we're in the steady state and we apply one transition, we stay in the same distribution. For our weather example, we can solve for this algebraically. Let's denote the steady state as pi sunny and pi rainy.") as tracker:
            # Set up equations
            eq_title = Text("Solving for Steady State:", font_size=28, color=GREEN)
            eq_title.move_to(UP * 0.2)
            self.play(Write(eq_title))
            
            eq1 = MathTex(
                r"\pi_S = 0.7\pi_S + 0.4\pi_R",
                font_size=30
            )
            eq1.move_to(DOWN * 0.5)
            
            eq2 = MathTex(
                r"\pi_R = 0.3\pi_S + 0.6\pi_R",
                font_size=30
            )
            eq2.next_to(eq1, DOWN, buff=0.3)
            
            eq3 = MathTex(
                r"\pi_S + \pi_R = 1",
                font_size=30
            )
            eq3.next_to(eq2, DOWN, buff=0.3)
            
            self.play(Write(eq1))
            self.play(Write(eq2))
            self.play(Write(eq3))
            
        with self.voiceover(text="From the first equation, we get zero point three pi sunny equals zero point four pi rainy. Combined with the constraint that probabilities sum to one, we can solve to find that pi sunny equals four sevenths, approximately zero point five seven one, and pi rainy equals three sevenths, approximately zero point four two nine. This is the long-run proportion of sunny versus rainy days.") as tracker:
            # Solution
            solution = MathTex(
                r"\pi = \begin{bmatrix} \frac{4}{7} & \frac{3}{7} \end{bmatrix} \approx \begin{bmatrix} 0.571 & 0.429 \end{bmatrix}",
                font_size=32,
                color=YELLOW
            )
            solution.move_to(DOWN * 2.3)
            
            box = SurroundingRectangle(solution, color=YELLOW, buff=0.15)
            
            self.play(Write(solution))
            self.play(Create(box))
            
        self.play(FadeOut(*self.mobjects))

    def real_world_applications(self):
        with self.voiceover(text="Markov Chains are not just theoretical constructs. They power countless real-world applications. Google's PageRank algorithm, which revolutionized web search, models the internet as a giant Markov Chain where web pages are states and hyperlinks define transition probabilities. Random surfers clicking links eventually settle into a steady state distribution that ranks page importance.") as tracker:
            title = Text("Real-World Applications", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Create application boxes
            app1 = VGroup(
                Rectangle(height=1.2, width=2.8, color=GREEN, fill_opacity=0.2),
                Text("PageRank", font_size=24),
                Text("(Web Search)", font_size=16, color=GRAY)
            ).arrange(DOWN, buff=0.15)
            app1.shift(LEFT * 3.5 + UP * 0.5)
            
            app2 = VGroup(
                Rectangle(height=1.2, width=2.8, color=YELLOW, fill_opacity=0.2),
                Text("Finance", font_size=24),
                Text("(Stock Models)", font_size=16, color=GRAY)
            ).arrange(DOWN, buff=0.15)
            app2.shift(RIGHT * 3.5 + UP * 0.5)
            
            self.play(Create(app1))
            self.play(Create(app2))
            
        with self.voiceover(text="In finance, Markov Chains model stock price movements and credit ratings. In natural language processing, they generate text and predict the next word in a sequence. In biology, they model DNA sequences and protein folding. In queueing theory, they analyze customer service systems and network traffic.") as tracker:
            app3 = VGroup(
                Rectangle(height=1.2, width=2.8, color=BLUE, fill_opacity=0.2),
                Text("NLP", font_size=24),
                Text("(Text Generation)", font_size=16, color=GRAY)
            ).arrange(DOWN, buff=0.15)
            app3.shift(LEFT * 3.5 + DOWN * 1.5)
            
            app4 = VGroup(
                Rectangle(height=1.2, width=2.8, color=RED, fill_opacity=0.2),
                Text("Biology", font_size=24),
                Text("(DNA/Proteins)", font_size=16, color=GRAY)
            ).arrange(DOWN, buff=0.15)
            app4.shift(RIGHT * 3.5 + DOWN * 1.5)
            
            self.play(Create(app3))
            self.play(Create(app4))
            
        self.play(FadeOut(*self.mobjects))

    def advanced_properties(self):
        with self.voiceover(text="Let's explore some advanced properties. A Markov Chain is called irreducible if you can get from any state to any other state in some number of steps. It's called aperiodic if the system doesn't get trapped in cycles. When a chain is both irreducible and aperiodic, we call it ergodic, and ergodic chains have unique steady states.") as tracker:
            title = Text("Advanced Properties", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Property 1: Irreducible
            prop1_title = Text("Irreducible:", font_size=28, color=GREEN, weight=BOLD)
            prop1_title.move_to(UP * 1.3 + LEFT * 3.5)
            prop1_desc = Text("All states communicate", font_size=20)
            prop1_desc.next_to(prop1_title, DOWN, buff=0.2, aligned_edge=LEFT)
            
            self.play(Write(prop1_title))
            self.play(Write(prop1_desc))
            
            # Property 2: Aperiodic
            prop2_title = Text("Aperiodic:", font_size=28, color=YELLOW, weight=BOLD)
            prop2_title.move_to(UP * 1.3 + RIGHT * 3.5)
            prop2_desc = Text("No fixed cycles", font_size=20)
            prop2_desc.next_to(prop2_title, DOWN, buff=0.2, aligned_edge=LEFT)
            
            self.play(Write(prop2_title))
            self.play(Write(prop2_desc))
            
        with self.voiceover(text="The fundamental theorem of Markov Chains states that for an ergodic chain, the steady state distribution exists, is unique, and is independent of the initial state. Moreover, the long-run proportion of time spent in each state equals the steady state probability. This is incredibly powerful for prediction and analysis.") as tracker:
            # Ergodic property
            ergodic = Text("Ergodic = Irreducible + Aperiodic", font_size=28, color=PURPLE)
            ergodic.move_to(ORIGIN)
            
            self.play(Write(ergodic))
            
            # Fundamental theorem
            theorem = MathTex(
                r"\lim_{n \to \infty} P^n \text{ exists and is unique}",
                font_size=30
            )
            theorem.move_to(DOWN * 1.2)
            
            self.play(Write(theorem))
            
            # Time average
            time_avg = Text("Long-run frequency = Steady state probability", 
                          font_size=22, color=YELLOW)
            time_avg.move_to(DOWN * 2.2)
            
            self.play(Write(time_avg))
            
        self.play(FadeOut(*self.mobjects))

    def conclusion(self):
        with self.voiceover(text="Let's recap what we've learned today. Markov Chains are powerful stochastic models based on the memoryless property. They're represented by transition matrices and state diagrams. We can predict future distributions using matrix multiplication, and many chains converge to steady states that tell us about long-run behavior.") as tracker:
            title = Text("Summary", font_size=36, color=BLUE, weight=BOLD)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Key points
            points = VGroup(
                Text("• Memoryless property: Future depends only on present", font_size=22),
                Text("• Transition matrix encodes all probabilities", font_size=22),
                Text("• Matrix powers predict future distributions", font_size=22),
                Text("• Steady states reveal long-run behavior", font_size=22),
                Text("• Applications everywhere: web, finance, AI, biology", font_size=22)
            ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
            points.move_to(DOWN * 0.5)
            
            for point in points:
                self.play(Write(point), run_time=1.2)
            
        with self.voiceover(text="From weather prediction to Google's search algorithm, from modeling gene sequences to predicting stock markets, Markov Chains provide a mathematically rigorous yet intuitive framework for understanding systems that evolve probabilistically over time. I hope this deep dive has given you both the mathematical foundation and the intuition to apply these powerful tools in your own work.") as tracker:
            self.wait(2)
            
        # Final fadeout before thank you
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Thank you for watching this comprehensive guide to Markov Chains. Keep exploring the beautiful world of probability and stochastic processes!") as tracker:
            thanks = Text("Thank You!", font_size=36, color=YELLOW, weight=BOLD)
            thanks.move_to(ORIGIN)
            
            subscribe = Text("Keep Learning!", font_size=28, color=BLUE)
            subscribe.next_to(thanks, DOWN, buff=0.6)
            
            self.play(Write(thanks), run_time=1.5)
            self.play(FadeIn(subscribe), run_time=1)
            self.wait(2)

# To render this animation, run:
# manim -pql markov_chains.py MarkovChainsExplanation
# For high quality: manim -pqh markov_chains.py MarkovChainsExplanation