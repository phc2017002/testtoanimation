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
        
        # Transition matrices
        self.transition_matrices()
        
        # Weather example
        self.weather_example()
        
        # State diagrams
        self.state_diagrams()
        
        # Chapman-Kolmogorov equation
        self.chapman_kolmogorov()
        
        # Steady state and long-term behavior
        self.steady_state()
        
        # Applications
        self.applications()
        
        # Conclusion
        self.conclusion()

    def introduction(self):
        with self.voiceover(text="Welcome to this comprehensive exploration of Markov Chains, one of the most powerful concepts in probability theory and stochastic processes. Markov Chains are mathematical systems that transition from one state to another according to certain probabilistic rules. They have profound applications across many fields including physics, economics, biology, and computer science.") as tracker:
            title = Text("Markov Chains", font_size=36, color=BLUE, weight=BOLD)
            title.to_edge(UP, buff=1.0)
            
            subtitle = Text("A Journey Through Probability", font_size=28, color=LIGHT_GRAY)
            subtitle.next_to(title, DOWN, buff=0.4)
            
            self.play(Write(title), run_time=2)
            self.play(FadeIn(subtitle), run_time=1.5)
            
        with self.voiceover(text="Today we will explore the fundamental properties of Markov Chains, understand their mathematical foundations, work through detailed examples, and discover how they model real-world phenomena from weather prediction to Google's PageRank algorithm.") as tracker:
            topics = VGroup(
                Text("• Mathematical Foundations", font_size=24),
                Text("• Transition Matrices", font_size=24),
                Text("• Practical Examples", font_size=24),
                Text("• Real-World Applications", font_size=24)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            topics.move_to(ORIGIN)
            
            self.play(FadeIn(topics, shift=UP), run_time=2)
            self.wait(2)
            
        self.play(FadeOut(*self.mobjects))

    def historical_context(self):
        with self.voiceover(text="The concept of Markov Chains was introduced by the Russian mathematician Andrey Markov in nineteen oh six. Markov was studying the statistical properties of letter sequences in Russian literature, particularly in Alexander Pushkin's novel Eugene Onegin.") as tracker:
            historical_title = Text("Historical Origins", font_size=36, color=GOLD)
            historical_title.to_edge(UP, buff=1.0)
            self.play(Write(historical_title))
            
            markov_name = Text("Andrey Markov", font_size=32, color=BLUE)
            markov_name.move_to(UP * 1.5)
            
            dates = Text("(1856 - 1922)", font_size=24, color=GRAY)
            dates.next_to(markov_name, DOWN, buff=0.3)
            
            self.play(Write(markov_name), Write(dates))
            
        with self.voiceover(text="Markov's groundbreaking insight was that in certain random processes, the future state depends only on the current state, not on the sequence of events that preceded it. This property, now called the Markov property or memorylessness, became the foundation for an entire branch of mathematics. His work revolutionized our understanding of stochastic processes and laid the groundwork for modern probability theory.") as tracker:
            markov_property = MathTex(
                r"P(X_{n+1} | X_n, X_{n-1}, \ldots, X_0) = P(X_{n+1} | X_n)",
                font_size=32
            )
            markov_property.move_to(DOWN * 0.5)
            
            property_label = Text("The Markov Property", font_size=26, color=YELLOW)
            property_label.next_to(markov_property, DOWN, buff=0.5)
            
            self.play(Write(markov_property), run_time=2)
            self.play(FadeIn(property_label))
            self.wait(2)
            
        self.play(FadeOut(*self.mobjects))

    def basic_definition(self):
        with self.voiceover(text="Let us now formally define a Markov Chain. A Markov Chain is a stochastic process that satisfies the Markov property. We denote the state at time n as X sub n, which takes values in a state space S. The state space can be finite or infinite, discrete or continuous.") as tracker:
            definition_title = Text("Formal Definition", font_size=36, color=GREEN)
            definition_title.to_edge(UP, buff=1.0)
            self.play(Write(definition_title))
            
            state_notation = MathTex(
                r"X_n \in S = \{s_1, s_2, \ldots, s_k\}",
                font_size=36
            )
            state_notation.move_to(UP * 1.5)
            
            self.play(Write(state_notation), run_time=2)
            
        with self.voiceover(text="The key defining property is that the conditional probability of the next state, given all previous states, depends only on the current state. Mathematically, this means that the probability of transitioning to state j at time n plus one, given that we are in state i at time n, is independent of how we arrived at state i.") as tracker:
            markov_def = MathTex(
                r"P(X_{n+1} = j \mid X_n = i, X_{n-1}, \ldots, X_0)",
                r"= P(X_{n+1} = j \mid X_n = i)",
                font_size=32
            )
            markov_def.move_to(ORIGIN)
            
            self.play(Write(markov_def[0]), run_time=2)
            self.wait(1)
            self.play(Write(markov_def[1]), run_time=2)
            
        with self.voiceover(text="We denote the transition probability from state i to state j as p sub i j. If these probabilities do not depend on time n, we call the Markov Chain time-homogeneous or stationary. Most practical applications involve stationary Markov Chains, which we will focus on today.") as tracker:
            transition_prob = MathTex(
                r"p_{ij} = P(X_{n+1} = j \mid X_n = i)",
                font_size=36
            )
            transition_prob.move_to(DOWN * 1.5)
            
            self.play(Write(transition_prob), run_time=2)
            self.wait(2)
            
        self.play(FadeOut(*self.mobjects))

    def transition_matrices(self):
        with self.voiceover(text="The transition probabilities can be organized into a transition matrix P, where each entry p sub i j represents the probability of moving from state i to state j. This matrix is a powerful tool for analyzing Markov Chains and computing future state probabilities.") as tracker:
            matrix_title = Text("Transition Matrices", font_size=36, color=PURPLE)
            matrix_title.to_edge(UP, buff=1.0)
            self.play(Write(matrix_title))
            
            matrix_def = MathTex(
                r"P = \begin{bmatrix} p_{11} & p_{12} & \cdots & p_{1k} \\ p_{21} & p_{22} & \cdots & p_{2k} \\ \vdots & \vdots & \ddots & \vdots \\ p_{k1} & p_{k2} & \cdots & p_{kk} \end{bmatrix}",
                font_size=32
            )
            matrix_def.move_to(UP * 0.5)
            
            self.play(Write(matrix_def), run_time=3)
            
        with self.voiceover(text="The transition matrix has two crucial properties. First, all entries are non-negative since they represent probabilities. Second, each row must sum to one, because from any given state, the chain must transition to some state, possibly staying in the same state. This makes P a stochastic matrix.") as tracker:
            properties = VGroup(
                MathTex(r"p_{ij} \geq 0 \text{ for all } i, j", font_size=28),
                MathTex(r"\sum_{j=1}^{k} p_{ij} = 1 \text{ for all } i", font_size=28)
            ).arrange(DOWN, buff=0.6)
            properties.move_to(DOWN * 1.5)
            
            self.play(Write(properties[0]), run_time=2)
            self.play(Write(properties[1]), run_time=2)
            self.wait(1)
            
        with self.voiceover(text="A remarkable property of transition matrices is that the n-step transition probabilities, that is, the probability of going from state i to state j in exactly n steps, are given by the entries of P raised to the power n. This follows from the Chapman-Kolmogorov equation, which we will explore shortly.") as tracker:
            n_step = MathTex(
                r"P(X_{n} = j \mid X_0 = i) = (P^n)_{ij}",
                font_size=36
            )
            n_step.move_to(DOWN * 0.5)
            
            self.play(FadeOut(properties))
            self.play(TransformFromCopy(matrix_def, n_step), run_time=2)
            self.wait(2)
            
        self.play(FadeOut(*self.mobjects))

    def weather_example(self):
        with self.voiceover(text="Let us illustrate these concepts with a classic example: a simple weather model. Suppose we classify each day as either sunny or rainy. If today is sunny, there is a seventy percent chance tomorrow will be sunny and a thirty percent chance it will be rainy. If today is rainy, there is a forty percent chance tomorrow will be sunny and a sixty percent chance it will remain rainy.") as tracker:
            example_title = Text("Example: Weather Model", font_size=36, color=ORANGE)
            example_title.to_edge(UP, buff=1.0)
            self.play(Write(example_title))
            
            states_label = Text("States: Sunny (S) and Rainy (R)", font_size=26)
            states_label.move_to(UP * 2)
            self.play(Write(states_label))
            
            probabilities = VGroup(
                Text("Sunny → Sunny: 0.7", font_size=24, color=YELLOW),
                Text("Sunny → Rainy: 0.3", font_size=24, color=BLUE),
                Text("Rainy → Sunny: 0.4", font_size=24, color=YELLOW),
                Text("Rainy → Rainy: 0.6", font_size=24, color=BLUE)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            probabilities.move_to(UP * 0.2)
            
            self.play(FadeIn(probabilities, shift=RIGHT), run_time=2)
            
        with self.voiceover(text="We can represent this weather model as a transition matrix. The first row corresponds to sunny weather, and the second row to rainy weather. The columns represent the probabilities of transitioning to sunny or rainy conditions respectively. Notice how each row sums to one, satisfying our stochastic matrix requirement.") as tracker:
            weather_matrix = MathTex(
                r"P = \begin{bmatrix} 0.7 & 0.3 \\ 0.4 & 0.6 \end{bmatrix}",
                font_size=36
            )
            weather_matrix.move_to(DOWN * 1.2)
            
            row_labels = VGroup(
                Text("S", font_size=24).next_to(weather_matrix, LEFT, buff=0.8).shift(UP * 0.3),
                Text("R", font_size=24).next_to(weather_matrix, LEFT, buff=0.8).shift(DOWN * 0.3)
            )
            
            col_labels = VGroup(
                Text("S", font_size=24).next_to(weather_matrix, UP, buff=0.5).shift(LEFT * 0.4),
                Text("R", font_size=24).next_to(weather_matrix, UP, buff=0.5).shift(RIGHT * 0.4)
            )
            
            self.play(Write(weather_matrix), run_time=2)
            self.play(FadeIn(row_labels), FadeIn(col_labels))
            self.wait(2)
            
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Now let's answer a practical question: if today is sunny, what is the probability that it will be sunny two days from now? We need to compute P squared. We can calculate this by matrix multiplication. The entry in the first row, first column of P squared gives us our answer.") as tracker:
            question_title = Text("Computing P²", font_size=36, color=GREEN)
            question_title.to_edge(UP, buff=1.0)
            self.play(Write(question_title))
            
            computation = MathTex(
                r"P^2 = \begin{bmatrix} 0.7 & 0.3 \\ 0.4 & 0.6 \end{bmatrix} \times \begin{bmatrix} 0.7 & 0.3 \\ 0.4 & 0.6 \end{bmatrix}",
                font_size=32
            )
            computation.move_to(UP * 1.2)
            
            self.play(Write(computation), run_time=2)
            
            calculation = MathTex(
                r"= \begin{bmatrix} 0.49 + 0.12 & 0.21 + 0.18 \\ 0.28 + 0.24 & 0.12 + 0.36 \end{bmatrix}",
                font_size=32
            )
            calculation.next_to(computation, DOWN, buff=0.6)
            
            self.play(Write(calculation), run_time=2)
            
            result = MathTex(
                r"= \begin{bmatrix} 0.61 & 0.39 \\ 0.52 & 0.48 \end{bmatrix}",
                font_size=36
            )
            result.next_to(calculation, DOWN, buff=0.6)
            
            self.play(Write(result), run_time=2)
            
            answer = Text("Answer: 61% chance of sun in 2 days!", font_size=28, color=YELLOW)
            answer.move_to(DOWN * 2.2)
            self.play(FadeIn(answer))
            self.wait(2)
            
        self.play(FadeOut(*self.mobjects))

    def state_diagrams(self):
        with self.voiceover(text="Markov Chains can be beautifully visualized using state diagrams. Each state is represented by a circle or node, and arrows between nodes show possible transitions. The arrow labels display the transition probabilities. Let's create the state diagram for our weather example.") as tracker:
            diagram_title = Text("State Diagram Visualization", font_size=36, color=TEAL)
            diagram_title.to_edge(UP, buff=1.0)
            self.play(Write(diagram_title))
            
            # Create states
            sunny_state = Circle(radius=0.6, color=YELLOW, fill_opacity=0.3)
            sunny_state.move_to(LEFT * 3)
            sunny_label = Text("S", font_size=32, color=YELLOW)
            sunny_label.move_to(sunny_state.get_center())
            
            rainy_state = Circle(radius=0.6, color=BLUE, fill_opacity=0.3)
            rainy_state.move_to(RIGHT * 3)
            rainy_label = Text("R", font_size=32, color=BLUE)
            rainy_label.move_to(rainy_state.get_center())
            
            self.play(Create(sunny_state), Write(sunny_label))
            self.play(Create(rainy_state), Write(rainy_label))
            
        with self.voiceover(text="Now we add the transition arrows. The curved arrow from sunny to rainy shows the zero point three probability of rain tomorrow given sun today. Similarly, the arrow from rainy to sunny shows the zero point four probability. The self-loops represent the probability of staying in the same state. Notice that all arrows leaving each state have probabilities that sum to one.") as tracker:
            # Transitions
            sunny_to_rainy = CurvedArrow(
                sunny_state.get_right() + UP * 0.2,
                rainy_state.get_left() + UP * 0.2,
                color=WHITE,
                angle=-TAU/8
            )
            sr_label = MathTex("0.3", font_size=24).next_to(sunny_to_rainy, UP, buff=0.1)
            
            rainy_to_sunny = CurvedArrow(
                rainy_state.get_left() + DOWN * 0.2,
                sunny_state.get_right() + DOWN * 0.2,
                color=WHITE,
                angle=-TAU/8
            )
            rs_label = MathTex("0.4", font_size=24).next_to(rainy_to_sunny, DOWN, buff=0.1)
            
            self.play(Create(sunny_to_rainy), Write(sr_label))
            self.play(Create(rainy_to_sunny), Write(rs_label))
            
            # Self loops
            sunny_loop = Arc(
                radius=0.8,
                start_angle=PI/4,
                angle=PI,
                arc_center=sunny_state.get_center() + UP * 0.5 + LEFT * 0.3,
                color=YELLOW
            ).add_tip()
            ss_label = MathTex("0.7", font_size=24, color=YELLOW).move_to(sunny_state.get_center() + UP * 1.3 + LEFT * 0.5)
            
            rainy_loop = Arc(
                radius=0.8,
                start_angle=-PI/4,
                angle=-PI,
                arc_center=rainy_state.get_center() + UP * 0.5 + RIGHT * 0.3,
                color=BLUE
            ).add_tip()
            rr_label = MathTex("0.6", font_size=24, color=BLUE).move_to(rainy_state.get_center() + UP * 1.3 + RIGHT * 0.5)
            
            self.play(Create(sunny_loop), Write(ss_label))
            self.play(Create(rainy_loop), Write(rr_label))
            self.wait(2)
            
        self.play(FadeOut(*self.mobjects))

    def chapman_kolmogorov(self):
        with self.voiceover(text="A fundamental theorem in Markov Chain theory is the Chapman-Kolmogorov equation. This equation allows us to compute multi-step transition probabilities by breaking them down into smaller steps. It states that the probability of going from state i to state k in m plus n steps equals the sum over all intermediate states j of the probability of going from i to j in m steps, times the probability of going from j to k in n steps.") as tracker:
            ck_title = Text("Chapman-Kolmogorov Equation", font_size=36, color=RED)
            ck_title.to_edge(UP, buff=1.0)
            self.play(Write(ck_title))
            
            ck_equation = MathTex(
                r"p_{ik}^{(m+n)} = \sum_{j} p_{ij}^{(m)} p_{jk}^{(n)}",
                font_size=36
            )
            ck_equation.move_to(UP * 1)
            
            self.play(Write(ck_equation), run_time=3)
            
        with self.voiceover(text="This equation has profound implications. In matrix notation, it simply says that P to the power m plus n equals P to the power m times P to the power n. This is why we can compute multi-step transition probabilities by matrix exponentiation. The Chapman-Kolmogorov equation is the mathematical foundation that makes Markov Chains tractable and computationally efficient.") as tracker:
            matrix_form = MathTex(
                r"P^{(m+n)} = P^{(m)} \cdot P^{(n)}",
                font_size=36
            )
            matrix_form.move_to(ORIGIN)
            
            self.play(Write(matrix_form), run_time=2)
            
            interpretation = Text(
                "Matrix multiplication computes all paths!",
                font_size=28,
                color=YELLOW
            )
            interpretation.move_to(DOWN * 1.5)
            
            self.play(FadeIn(interpretation))
            self.wait(2)
            
        with self.voiceover(text="Let's visualize this concept. Imagine we want to go from state A to state C in two steps. We can go through intermediate state B or through state D. The Chapman-Kolmogorov equation tells us to sum the probabilities of all possible paths. This is exactly what matrix multiplication does automatically when we compute P squared.") as tracker:
            # Clear previous
            self.play(FadeOut(ck_equation), FadeOut(matrix_form), FadeOut(interpretation))
            
            # Create simple path diagram
            state_a = Circle(radius=0.4, color=GREEN).move_to(LEFT * 4)
            label_a = Text("A", font_size=24).move_to(state_a.get_center())
            
            state_b = Circle(radius=0.4, color=BLUE).move_to(UP * 1.5)
            label_b = Text("B", font_size=24).move_to(state_b.get_center())
            
            state_d = Circle(radius=0.4, color=BLUE).move_to(DOWN * 1.5)
            label_d = Text("D", font_size=24).move_to(state_d.get_center())
            
            state_c = Circle(radius=0.4, color=RED).move_to(RIGHT * 4)
            label_c = Text("C", font_size=24).move_to(state_c.get_center())
            
            self.play(
                Create(state_a), Write(label_a),
                Create(state_b), Write(label_b),
                Create(state_d), Write(label_d),
                Create(state_c), Write(label_c)
            )
            
            # Paths
            path1 = VGroup(
                Arrow(state_a.get_top(), state_b.get_left(), color=YELLOW, buff=0.1),
                Arrow(state_b.get_right(), state_c.get_top(), color=YELLOW, buff=0.1)
            )
            
            path2 = VGroup(
                Arrow(state_a.get_bottom(), state_d.get_left(), color=ORANGE, buff=0.1),
                Arrow(state_d.get_right(), state_c.get_bottom(), color=ORANGE, buff=0.1)
            )
            
            self.play(Create(path1))
            self.play(Create(path2))
            self.wait(2)
            
        self.play(FadeOut(*self.mobjects))

    def steady_state(self):
        with self.voiceover(text="One of the most important questions in Markov Chain theory is: what happens in the long run? Many Markov Chains have a steady-state distribution, also called a stationary distribution or equilibrium distribution. This is a probability distribution over states that remains unchanged after one transition step.") as tracker:
            steady_title = Text("Steady State Distribution", font_size=36, color=PURPLE)
            steady_title.to_edge(UP, buff=1.0)
            self.play(Write(steady_title))
            
            steady_def = MathTex(
                r"\pi P = \pi",
                font_size=36
            )
            steady_def.move_to(UP * 1.5)
            
            self.play(Write(steady_def), run_time=2)
            
            constraint = MathTex(
                r"\sum_{i} \pi_i = 1",
                font_size=36
            )
            constraint.next_to(steady_def, DOWN, buff=0.8)
            
            self.play(Write(constraint), run_time=1.5)
            
        with self.voiceover(text="For our weather example, we can find the steady state by solving the equation pi times P equals pi, subject to the constraint that the probabilities sum to one. Let pi sub s be the long-run probability of sunny weather, and pi sub r be the long-run probability of rainy weather. We need to solve this system of equations.") as tracker:
            weather_steady = VGroup(
                MathTex(r"\pi_s \cdot 0.7 + \pi_r \cdot 0.4 = \pi_s", font_size=28),
                MathTex(r"\pi_s \cdot 0.3 + \pi_r \cdot 0.6 = \pi_r", font_size=28),
                MathTex(r"\pi_s + \pi_r = 1", font_size=28)
            ).arrange(DOWN, buff=0.5)
            weather_steady.move_to(DOWN * 0.3)
            
            self.play(FadeOut(steady_def), FadeOut(constraint))
            self.play(Write(weather_steady), run_time=3)
            
        with self.voiceover(text="Solving this system, we find that pi sub s equals four sevenths, approximately zero point five seven one, and pi sub r equals three sevenths, approximately zero point four two nine. This means that in the long run, regardless of whether we start with a sunny or rainy day, the weather will be sunny about fifty seven percent of the time and rainy about forty three percent of the time. This is a remarkable result showing that the system forgets its initial condition.") as tracker:
            solution = VGroup(
                MathTex(r"\pi_s = \frac{4}{7} \approx 0.571", font_size=36, color=YELLOW),
                MathTex(r"\pi_r = \frac{3}{7} \approx 0.429", font_size=36, color=BLUE)
            ).arrange(DOWN, buff=0.6)
            solution.move_to(DOWN * 1.2)
            
            self.play(FadeOut(weather_steady))
            self.play(Write(solution), run_time=2)
            
            interpretation = Text(
                "Long-run: ~57% sunny, ~43% rainy",
                font_size=28,
                color=GREEN
            )
            interpretation.move_to(DOWN * 2.5)
            
            self.play(FadeIn(interpretation))
            self.wait(2)
            
        self.play(FadeOut(*self.mobjects))

    def applications(self):
        with self.voiceover(text="Markov Chains have extraordinary applications across diverse fields. In finance, they model stock prices and credit ratings. In biology, they describe population dynamics and genetic evolution. In computer science, they power the PageRank algorithm that Google uses to rank web pages. In physics, they model particle motion and thermodynamic systems.") as tracker:
            app_title = Text("Real-World Applications", font_size=36, color=GOLD)
            app_title.to_edge(UP, buff=1.0)
            self.play(Write(app_title))
            
            applications = VGroup(
                Text("• Google PageRank Algorithm", font_size=26, color=BLUE),
                Text("• Financial Market Modeling", font_size=26, color=GREEN),
                Text("• DNA Sequence Analysis", font_size=26, color=RED),
                Text("• Speech Recognition Systems", font_size=26, color=PURPLE),
                Text("• Queue Theory & Networks", font_size=26, color=ORANGE),
                Text("• Game Theory & Economics", font_size=26, color=TEAL)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            applications.move_to(DOWN * 0.5)
            
            self.play(FadeIn(applications, lag_ratio=0.3), run_time=3)
            self.wait(2)
            
        with self.voiceover(text="Let's briefly explore the PageRank algorithm. Imagine the internet as a giant Markov Chain where each webpage is a state, and hyperlinks are transitions. A random surfer clicks links with probability d, or jumps to a random page with probability one minus d. The steady-state distribution gives each page's importance. Pages with high steady-state probability are ranked higher in search results. This simple idea revolutionized web search.") as tracker:
            self.play(FadeOut(applications))
            
            pagerank_title = Text("PageRank Example", font_size=32, color=BLUE)
            pagerank_title.move_to(UP * 2.5)
            self.play(Write(pagerank_title))
            
            # Simple web graph
            page1 = Circle(radius=0.4, color=YELLOW).move_to(LEFT * 3 + UP * 0.5)
            page2 = Circle(radius=0.4, color=GREEN).move_to(RIGHT * 0 + UP * 0.5)
            page3 = Circle(radius=0.4, color=RED).move_to(RIGHT * 3 + UP * 0.5)
            page4 = Circle(radius=0.4, color=BLUE).move_to(ORIGIN + DOWN * 1.5)
            
            p1_label = Text("1", font_size=20).move_to(page1.get_center())
            p2_label = Text("2", font_size=20).move_to(page2.get_center())
            p3_label = Text("3", font_size=20).move_to(page3.get_center())
            p4_label = Text("4", font_size=20).move_to(page4.get_center())
            
            self.play(
                Create(page1), Create(page2), Create(page3), Create(page4),
                Write(p1_label), Write(p2_label), Write(p3_label), Write(p4_label)
            )
            
            # Links
            link1 = Arrow(page1.get_right(), page2.get_left(), buff=0.1, color=WHITE)
            link2 = Arrow(page2.get_right(), page3.get_left(), buff=0.1, color=WHITE)
            link3 = Arrow(page1.get_bottom(), page4.get_left() + UP * 0.2, buff=0.1, color=WHITE)
            link4 = Arrow(page3.get_bottom(), page4.get_right() + UP * 0.2, buff=0.1, color=WHITE)
            link5 = Arrow(page4.get_top(), page2.get_bottom(), buff=0.1, color=WHITE)
            
            self.play(Create(link1), Create(link2), Create(link3), Create(link4), Create(link5))
            self.wait(2)
            
        self.play(FadeOut(*self.mobjects))

    def conclusion(self):
        with self.voiceover(text="We have explored the fascinating world of Markov Chains, from their historical origins with Andrey Markov to their modern applications in technology and science. We learned about the Markov property, transition matrices, and the Chapman-Kolmogorov equation. We computed steady-state distributions and saw how these mathematical tools model real-world phenomena.") as tracker:
            conclusion_title = Text("Summary", font_size=36, color=BLUE, weight=BOLD)
            conclusion_title.to_edge(UP, buff=1.0)
            self.play(Write(conclusion_title))
            
            key_concepts = VGroup(
                Text("✓ Markov Property: Future depends only on present", font_size=24),
                Text("✓ Transition Matrices: Organize probabilities", font_size=24),
                Text("✓ Chapman-Kolmogorov: Multi-step transitions", font_size=24),
                Text("✓ Steady State: Long-run equilibrium", font_size=24),
                Text("✓ Applications: From web search to biology", font_size=24)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            key_concepts.move_to(UP * 0.3)
            
            self.play(FadeIn(key_concepts, lag_ratio=0.4), run_time=3)
            
        with self.voiceover(text="The beauty of Markov Chains lies in their simplicity and power. With just the memoryless property and some linear algebra, we can model incredibly complex systems and make precise predictions. Whether you're analyzing web traffic, modeling weather patterns, or studying molecular dynamics, Markov Chains provide an elegant mathematical framework. Thank you for joining this journey through probability theory.") as tracker:
            self.wait(3)
            
            final_equation = MathTex(
                r"\pi P = \pi",
                font_size=36,
                color=YELLOW
            )
            final_equation.move_to(DOWN * 1.8)
            
            self.play(Write(final_equation), run_time=2)
            self.wait(2)
            
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Thank you for watching. Keep exploring the wonderful world of mathematics and probability!") as tracker:
            thanks = Text("Thank You!", font_size=36, color=GOLD, weight=BOLD)
            thanks.move_to(ORIGIN)
            
            self.play(Write(thanks), run_time=2)
            self.wait(2)