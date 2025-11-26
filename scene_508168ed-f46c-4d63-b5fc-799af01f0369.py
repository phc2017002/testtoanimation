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
        
        # Call all sections in order
        self.introduction()
        self.historical_context()
        self.basic_definition()
        self.weather_example()
        self.transition_matrix()
        self.chapman_kolmogorov()
        self.steady_state()
        self.applications()
        self.conclusion()
    
    def introduction(self):
        """Introduction to Markov Chains - approximately 30 seconds"""
        with self.voiceover(text="Welcome to this comprehensive explanation of Markov Chains, one of the most fundamental concepts in probability theory and stochastic processes.") as tracker:
            title = Text("Markov Chains", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            subtitle = Text("A Journey Through Probability", font_size=28, color=YELLOW)
            subtitle.next_to(title, DOWN, buff=0.5)
            self.play(Write(title), run_time=2)
            self.play(FadeIn(subtitle), run_time=1.5)
        
        with self.voiceover(text="Markov Chains are mathematical systems that transition from one state to another according to certain probabilistic rules. They have applications in physics, chemistry, economics, finance, genetics, and even search engines like Google.") as tracker:
            # Create visual representations of applications
            apps = VGroup(
                Text("• Search Engines", font_size=24),
                Text("• Stock Markets", font_size=24),
                Text("• Weather Prediction", font_size=24),
                Text("• Game Theory", font_size=24),
                Text("• Machine Learning", font_size=24)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            apps.move_to(ORIGIN)
            self.play(FadeIn(apps, shift=UP), run_time=2)
            self.wait(2)
        
        # Cleanup
        self.play(FadeOut(*self.mobjects))
    
    def historical_context(self):
        """Historical background - approximately 35 seconds"""
        with self.voiceover(text="Markov Chains are named after the Russian mathematician Andrey Markov, who introduced them in the early nineteen hundreds while studying sequences of random variables.") as tracker:
            title = Text("Historical Context", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Create timeline
            timeline = Line(LEFT * 5, RIGHT * 5, color=WHITE)
            timeline.move_to(DOWN * 0.5)
            self.play(Create(timeline))
            
            # Add key dates
            date1 = Text("1906", font_size=24, color=YELLOW)
            date1.next_to(timeline.point_from_proportion(0.2), UP, buff=0.3)
            label1 = Text("Markov introduces\nthe concept", font_size=18)
            label1.next_to(date1, DOWN, buff=0.5)
            
            date2 = Text("1931", font_size=24, color=YELLOW)
            date2.next_to(timeline.point_from_proportion(0.5), UP, buff=0.3)
            label2 = Text("Kolmogorov's\nequations", font_size=18)
            label2.next_to(date2, DOWN, buff=0.5)
            
            date3 = Text("1998", font_size=24, color=YELLOW)
            date3.next_to(timeline.point_from_proportion(0.8), UP, buff=0.3)
            label3 = Text("PageRank\nalgorithm", font_size=18)
            label3.next_to(date3, DOWN, buff=0.5)
            
            self.play(
                Write(date1), Write(label1),
                Write(date2), Write(label2),
                Write(date3), Write(label3),
                run_time=3
            )
        
        with self.voiceover(text="His work laid the foundation for understanding systems where the future state depends only on the current state, not on the sequence of events that preceded it. This property is known as the Markov property or memorylessness.") as tracker:
            # Highlight the memoryless property
            memoryless = Text("The Markov Property: Memorylessness", font_size=28, color=GREEN)
            memoryless.move_to(UP * 2.5)
            self.play(Write(memoryless), run_time=2)
            self.wait(2)
        
        # Cleanup
        self.play(FadeOut(*self.mobjects))
    
    def basic_definition(self):
        """Mathematical definition - approximately 40 seconds"""
        with self.voiceover(text="Let's now define Markov Chains mathematically. A Markov Chain is a sequence of random variables X zero, X one, X two, and so on, where each variable takes values in a state space.") as tracker:
            title = Text("Mathematical Definition", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Show sequence of random variables
            sequence = MathTex(r"X_0, X_1, X_2, X_3, \ldots, X_n", font_size=36)
            sequence.move_to(UP * 1.5)
            self.play(Write(sequence), run_time=2)
        
        with self.voiceover(text="The defining characteristic is the Markov property. The probability of moving to the next state depends only on the current state, not on any previous states. Mathematically, we express this as follows.") as tracker:
            # Show the Markov property equation
            markov_property = MathTex(
                r"P(X_{n+1} = x_{n+1} \mid X_n = x_n, \ldots, X_0 = x_0)",
                r"= P(X_{n+1} = x_{n+1} \mid X_n = x_n)",
                font_size=32
            )
            markov_property.move_to(ORIGIN)
            self.play(Write(markov_property[0]), run_time=2)
            self.wait(1)
            self.play(Write(markov_property[1]), run_time=2)
        
        with self.voiceover(text="This equation tells us that the conditional probability of the next state, given all previous states, equals the conditional probability of the next state given only the current state. The past is irrelevant once we know the present.") as tracker:
            # Highlight the equality
            box = SurroundingRectangle(markov_property, color=YELLOW, buff=0.2)
            self.play(Create(box), run_time=1.5)
            self.wait(2)
        
        # Cleanup
        self.play(FadeOut(*self.mobjects))
    
    def weather_example(self):
        """Weather example with state diagram - approximately 50 seconds"""
        with self.voiceover(text="To make this concrete, let's consider a simple example. Imagine we're modeling the weather, which can be either sunny or rainy. We'll create a Markov Chain where today's weather depends only on yesterday's weather.") as tracker:
            title = Text("Example: Weather Model", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Create state circles
            sunny_circle = Circle(radius=0.8, color=YELLOW, fill_opacity=0.3)
            sunny_circle.move_to(LEFT * 3.5)
            sunny_label = Text("Sunny", font_size=28, color=YELLOW)
            sunny_label.move_to(sunny_circle.get_center())
            
            rainy_circle = Circle(radius=0.8, color=BLUE, fill_opacity=0.3)
            rainy_circle.move_to(RIGHT * 3.5)
            rainy_label = Text("Rainy", font_size=28, color=BLUE)
            rainy_label.move_to(rainy_circle.get_center())
            
            self.play(
                Create(sunny_circle), Write(sunny_label),
                Create(rainy_circle), Write(rainy_label),
                run_time=2
            )
        
        with self.voiceover(text="Let's say if today is sunny, there's a seventy percent chance tomorrow will be sunny, and a thirty percent chance it will be rainy. Conversely, if today is rainy, there's a forty percent chance tomorrow will be sunny, and a sixty percent chance it will remain rainy.") as tracker:
            # Self-loop for Sunny
            sunny_loop = Arc(radius=1.2, start_angle=PI/3, angle=4*PI/3, color=YELLOW)
            sunny_loop.move_to(sunny_circle.get_center() + UP * 1.2)
            sunny_loop_label = MathTex("0.7", font_size=24, color=YELLOW)
            sunny_loop_label.next_to(sunny_loop, UP, buff=0.1)
            
            # Arrow from Sunny to Rainy
            sunny_to_rainy = CurvedArrow(
                sunny_circle.get_right() + UP * 0.2,
                rainy_circle.get_left() + UP * 0.2,
                color=GREEN,
                angle=-0.3
            )
            sunny_to_rainy_label = MathTex("0.3", font_size=24, color=GREEN)
            sunny_to_rainy_label.next_to(sunny_to_rainy, UP, buff=0.1)
            
            self.play(
                Create(sunny_loop), Write(sunny_loop_label),
                Create(sunny_to_rainy), Write(sunny_to_rainy_label),
                run_time=2
            )
        
        with self.voiceover(text="Now we add the transitions from the rainy state. From rainy to sunny with probability zero point four, and rainy to rainy with probability zero point six. Notice that the probabilities from each state must sum to one.") as tracker:
            # Arrow from Rainy to Sunny
            rainy_to_sunny = CurvedArrow(
                rainy_circle.get_left() + DOWN * 0.2,
                sunny_circle.get_right() + DOWN * 0.2,
                color=ORANGE,
                angle=-0.3
            )
            rainy_to_sunny_label = MathTex("0.4", font_size=24, color=ORANGE)
            rainy_to_sunny_label.next_to(rainy_to_sunny, DOWN, buff=0.1)
            
            # Self-loop for Rainy
            rainy_loop = Arc(radius=1.2, start_angle=-2*PI/3, angle=4*PI/3, color=BLUE)
            rainy_loop.move_to(rainy_circle.get_center() + DOWN * 1.2)
            rainy_loop_label = MathTex("0.6", font_size=24, color=BLUE)
            rainy_loop_label.next_to(rainy_loop, DOWN, buff=0.1)
            
            self.play(
                Create(rainy_to_sunny), Write(rainy_to_sunny_label),
                Create(rainy_loop), Write(rainy_loop_label),
                run_time=2
            )
            self.wait(1)
        
        # Cleanup
        self.play(FadeOut(*self.mobjects))
    
    def transition_matrix(self):
        """Transition matrix explanation - approximately 45 seconds"""
        with self.voiceover(text="We can represent these transition probabilities in a matrix called the transition matrix, denoted by P. Each entry P i j represents the probability of transitioning from state i to state j.") as tracker:
            title = Text("Transition Matrix", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Create transition matrix
            matrix_label = MathTex(r"P = ", font_size=36)
            matrix_label.move_to(LEFT * 4 + UP * 0.5)
            
            matrix = MathTex(
                r"\begin{bmatrix} 0.7 & 0.3 \\ 0.4 & 0.6 \end{bmatrix}",
                font_size=36
            )
            matrix.next_to(matrix_label, RIGHT, buff=0.3)
            
            self.play(Write(matrix_label), Write(matrix), run_time=2)
        
        with self.voiceover(text="Let me explain what each entry means. The top-left entry, zero point seven, is the probability of going from sunny to sunny. The top-right entry, zero point three, is the probability of going from sunny to rainy.") as tracker:
            # Highlight entries with explanations
            # highlight1 = SurroundingRectangle(matrix[0][1:4], color=YELLOW, buff=0.1)  # Auto-disabled: indexed SurroundingRectangle
            label1 = Text("Sunny → Sunny", font_size=20, color=YELLOW)
            label1.next_to(matrix, RIGHT, buff=1.5).shift(UP * 0.8)
            # arrow1 = Arrow(label1.get_left(), highlight1.get_right(), color=YELLOW, buff=0.1)  # Auto-disabled: uses disabled SurroundingRectangle
            
            # self.play(Create(highlight1), Write(label1), Create(arrow1), run_time=2)  # Auto-disabled: uses disabled SurroundingRectangle
            self.wait(1)
            
            # highlight2 = SurroundingRectangle(matrix[0][5:8], color=GREEN, buff=0.1)  # Auto-disabled: indexed SurroundingRectangle
            label2 = Text("Sunny → Rainy", font_size=20, color=GREEN)
            label2.next_to(matrix, RIGHT, buff=1.5).shift(UP * 0.2)
            # arrow2 = Arrow(label2.get_left(), highlight2.get_right(), color=GREEN, buff=0.1)  # Auto-disabled: uses disabled SurroundingRectangle
            
            # Empty self.play() removed - all animations were auto-disabled
            self.wait(1)  # Brief pause instead
        
        with self.voiceover(text="Similarly, the bottom-left entry, zero point four, represents rainy to sunny, and the bottom-right entry, zero point six, represents rainy to rainy. Notice that each row sums to one, which is a fundamental property of transition matrices.") as tracker:
            # self.play(FadeOut(highlight2), FadeOut(label2), FadeOut(arrow2))  # Auto-disabled: uses disabled SurroundingRectangle
            
            # Show row sums
            row_sum1 = MathTex(r"0.7 + 0.3 = 1", font_size=28, color=YELLOW)
            row_sum1.next_to(matrix, RIGHT, buff=1.5).shift(UP * 0.5)
            
            row_sum2 = MathTex(r"0.4 + 0.6 = 1", font_size=28, color=BLUE)
            row_sum2.next_to(matrix, RIGHT, buff=1.5).shift(DOWN * 0.5)
            
            self.play(Write(row_sum1), Write(row_sum2), run_time=2)
            self.wait(1)
        
        # Cleanup
        self.play(FadeOut(*self.mobjects))
    
    def chapman_kolmogorov(self):
        """Chapman-Kolmogorov equations - approximately 50 seconds"""
        with self.voiceover(text="One of the most important results in Markov Chain theory is the Chapman-Kolmogorov equation. This allows us to compute multi-step transition probabilities by taking powers of the transition matrix.") as tracker:
            title = Text("Chapman-Kolmogorov Equations", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Show the equation
            ck_equation = MathTex(
                r"P^{(n)}_{ij} = \sum_{k} P^{(m)}_{ik} P^{(n-m)}_{kj}",
                font_size=36
            )
            ck_equation.move_to(UP * 1.8)
            self.play(Write(ck_equation), run_time=2)
        
        with self.voiceover(text="In matrix form, this simply means that the n-step transition matrix equals the transition matrix raised to the power n. Let's calculate what happens after two days in our weather example.") as tracker:
            # Show matrix equation
            matrix_eq = MathTex(
                r"P^{(2)} = P \times P = P^2",
                font_size=32
            )
            matrix_eq.next_to(ck_equation, DOWN, buff=0.6)
            self.play(Write(matrix_eq), run_time=2)
        
        with self.voiceover(text="Let's compute P squared for our weather model. We multiply the transition matrix by itself. The calculation gives us the two-step transition probabilities.") as tracker:
            # Show the calculation
            calc = MathTex(
                r"P^2 = \begin{bmatrix} 0.7 & 0.3 \\ 0.4 & 0.6 \end{bmatrix}",
                r"\times \begin{bmatrix} 0.7 & 0.3 \\ 0.4 & 0.6 \end{bmatrix}",
                font_size=28
            )
            calc.move_to(DOWN * 0.3)
            self.play(Write(calc[0]), run_time=1.5)
            self.play(Write(calc[1]), run_time=1.5)
        
        with self.voiceover(text="After performing the matrix multiplication, we get our two-step transition matrix. For example, the probability of going from sunny to sunny in two days is zero point six one. This means if today is sunny, there's a sixty-one percent chance it will be sunny two days from now.") as tracker:
            # Show the result
            result = MathTex(
                r"= \begin{bmatrix} 0.61 & 0.39 \\ 0.52 & 0.48 \end{bmatrix}",
                font_size=32
            )
            result.next_to(calc, DOWN, buff=0.6)
            self.play(Write(result), run_time=2)
            self.wait(1)
        
        # Cleanup
        self.play(FadeOut(*self.mobjects))
    
    def steady_state(self):
        """Steady state distribution - approximately 55 seconds"""
        with self.voiceover(text="An important question in Markov Chain analysis is: what happens in the long run? Does the system converge to a steady state distribution? For many Markov Chains, the answer is yes.") as tracker:
            title = Text("Steady State Distribution", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Definition of steady state
            steady_def = MathTex(
                r"\pi = \pi P",
                font_size=36
            )
            steady_def.move_to(UP * 1.8)
            self.play(Write(steady_def), run_time=2)
        
        with self.voiceover(text="The steady state distribution, denoted by pi, is a probability distribution that remains unchanged when multiplied by the transition matrix. It represents the long-term proportion of time the system spends in each state.") as tracker:
            explanation = Text(
                "π: Long-term state probabilities",
                font_size=24,
                color=YELLOW
            )
            explanation.next_to(steady_def, DOWN, buff=0.5)
            self.play(Write(explanation), run_time=2)
        
        with self.voiceover(text="For our weather example, we need to solve the equation pi equals pi P, along with the constraint that the probabilities sum to one. Let's denote pi as a vector with components pi sunny and pi rainy.") as tracker:
            # Set up the system of equations
            system = MathTex(
                r"\begin{bmatrix} \pi_S & \pi_R \end{bmatrix}",
                r"= \begin{bmatrix} \pi_S & \pi_R \end{bmatrix}",
                r"\begin{bmatrix} 0.7 & 0.3 \\ 0.4 & 0.6 \end{bmatrix}",
                font_size=28
            )
            system.move_to(UP * 0.5)
            self.play(Write(system), run_time=3)
        
        with self.voiceover(text="Expanding this matrix equation gives us two equations. Pi sunny equals zero point seven pi sunny plus zero point four pi rainy. And pi rainy equals zero point three pi sunny plus zero point six pi rainy. We also know that pi sunny plus pi rainy equals one.") as tracker:
            # Show expanded equations
            eq1 = MathTex(r"\pi_S = 0.7\pi_S + 0.4\pi_R", font_size=26)
            eq2 = MathTex(r"\pi_R = 0.3\pi_S + 0.6\pi_R", font_size=26)
            eq3 = MathTex(r"\pi_S + \pi_R = 1", font_size=26, color=YELLOW)
            
            equations = VGroup(eq1, eq2, eq3).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            equations.move_to(DOWN * 1.2)
            
            self.play(Write(eq1), run_time=1.5)
            self.play(Write(eq2), run_time=1.5)
            self.play(Write(eq3), run_time=1.5)
        
        with self.voiceover(text="Solving this system of equations, we find that pi sunny equals four sevenths, approximately zero point five seven, and pi rainy equals three sevenths, approximately zero point four three. This means in the long run, about fifty-seven percent of days will be sunny.") as tracker:
            # Show solution
            solution = MathTex(
                r"\pi_S = \frac{4}{7} \approx 0.57, \quad \pi_R = \frac{3}{7} \approx 0.43",
                font_size=32,
                color=GREEN
            )
            solution.move_to(DOWN * 2.8)
            box = SurroundingRectangle(solution, color=GREEN, buff=0.2)
            self.play(Write(solution), Create(box), run_time=2)
            self.wait(1)
        
        # Cleanup
        self.play(FadeOut(*self.mobjects))
    
    def applications(self):
        """Real-world applications - approximately 50 seconds"""
        with self.voiceover(text="Markov Chains have numerous applications across many fields. Let's explore some of the most important ones, starting with Google's PageRank algorithm, which revolutionized internet search.") as tracker:
            title = Text("Real-World Applications", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # PageRank explanation
            pagerank_title = Text("1. PageRank Algorithm", font_size=28, color=YELLOW)
            pagerank_title.move_to(UP * 2.2)
            self.play(Write(pagerank_title), run_time=1.5)
            
            # Create simple web graph
            page1 = Circle(radius=0.4, color=BLUE, fill_opacity=0.3)
            page1.move_to(LEFT * 3 + UP * 0.3)
            p1_label = Text("A", font_size=20)
            p1_label.move_to(page1.get_center())
            
            page2 = Circle(radius=0.4, color=BLUE, fill_opacity=0.3)
            page2.move_to(ORIGIN + UP * 0.3)
            p2_label = Text("B", font_size=20)
            p2_label.move_to(page2.get_center())
            
            page3 = Circle(radius=0.4, color=BLUE, fill_opacity=0.3)
            page3.move_to(RIGHT * 3 + UP * 0.3)
            p3_label = Text("C", font_size=20)
            p3_label.move_to(page3.get_center())
            
            # Links between pages
            link1 = Arrow(page1.get_right(), page2.get_left(), buff=0.1, color=WHITE)
            link2 = Arrow(page2.get_right(), page3.get_left(), buff=0.1, color=WHITE)
            link3 = Arrow(page3.get_bottom(), page1.get_bottom(), buff=0.1, color=WHITE)
            
            web_graph = VGroup(page1, p1_label, page2, p2_label, page3, p3_label, link1, link2, link3)
            
            self.play(Create(web_graph), run_time=2)
        
        with self.voiceover(text="PageRank models a random surfer clicking on links. The steady state distribution gives the importance of each webpage. Pages with higher steady state probabilities rank higher in search results.") as tracker:
            explanation = Text(
                "Web pages = States, Links = Transitions",
                font_size=22,
                color=GREEN
            )
            explanation.move_to(DOWN * 1.0)
            self.play(Write(explanation), run_time=2)
            self.wait(1)
            
            self.play(FadeOut(web_graph), FadeOut(explanation))
        
        with self.voiceover(text="Another major application is in finance, where Markov Chains model stock prices and credit ratings. In queuing theory, they analyze waiting lines and service systems. In genetics, they model DNA sequences and evolutionary processes.") as tracker:
            # List other applications
            apps = VGroup(
                Text("2. Finance: Stock prices, credit ratings", font_size=24),
                Text("3. Queuing Theory: Service systems", font_size=24),
                Text("4. Genetics: DNA sequence analysis", font_size=24),
                Text("5. Machine Learning: Hidden Markov Models", font_size=24),
                Text("6. Physics: Statistical mechanics", font_size=24)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            apps.move_to(DOWN * 0.2)
            
            self.play(FadeIn(apps, shift=UP), run_time=3)
            self.wait(2)
        
        # Cleanup
        self.play(FadeOut(*self.mobjects))
    
    def conclusion(self):
        """Conclusion and summary - approximately 35 seconds"""
        with self.voiceover(text="Let's summarize what we've learned about Markov Chains. They are stochastic processes with the Markov property, where the future depends only on the present, not the past.") as tracker:
            title = Text("Summary", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Key points
            key_points = VGroup(
                Text("✓ Markov Property: Future depends only on present", font_size=24),
                Text("✓ Transition Matrix: Describes state changes", font_size=24),
                Text("✓ Chapman-Kolmogorov: Multi-step transitions", font_size=24),
                Text("✓ Steady State: Long-term behavior", font_size=24),
                Text("✓ Applications: Search, finance, genetics, ML", font_size=24)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            key_points.move_to(DOWN * 0.3)
            
            self.play(FadeIn(key_points[0], shift=UP), run_time=1.5)
            self.play(FadeIn(key_points[1], shift=UP), run_time=1.5)
            self.play(FadeIn(key_points[2], shift=UP), run_time=1.5)
            self.play(FadeIn(key_points[3], shift=UP), run_time=1.5)
            self.play(FadeIn(key_points[4], shift=UP), run_time=1.5)
        
        with self.voiceover(text="Markov Chains provide a powerful framework for modeling systems that evolve probabilistically over time. From predicting weather to ranking web pages, their applications continue to grow. Thank you for watching this explanation of Markov Chains!") as tracker:
            self.wait(3)
        
        # Final cleanup and thank you
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="I hope you found this journey through Markov Chains educational and insightful. Keep exploring the fascinating world of probability and stochastic processes!") as tracker:
            thanks = Text("Thank You!", font_size=36, color=GOLD)
            thanks.move_to(ORIGIN)
            self.play(Write(thanks), run_time=2)
            self.wait(2)
        
        self.play(FadeOut(thanks))

# Instructions to render:
# Run the following command in your terminal:
# manim -pql markov_chains.py MarkovChainsExplanation
# 
# For high quality:
# manim -pqh markov_chains.py MarkovChainsExplanation
#
# The animation will be approximately 5-6 minutes long with comprehensive coverage of:
# 1. Introduction (30s)
# 2. Historical context (35s)
# 3. Mathematical definition (40s)
# 4. Weather example (50s)
# 5. Transition matrix (45s)
# 6. Chapman-Kolmogorov (50s)
# 7. Steady state (55s)
# 8. Applications (50s)
# 9. Conclusion (35s)
# Total: ~390 seconds (6.5 minutes)