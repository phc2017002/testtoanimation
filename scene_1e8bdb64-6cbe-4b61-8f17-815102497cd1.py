from manim import *
from manim_voiceover import VoiceoverScene
from manimator.services import ElevenLabsService

class SchrodingerEquationExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(ElevenLabsService(voice_id="Rachel"))

        # Introduction
        self.introduction()
        
        # The Schrödinger Equation
        self.show_schrodinger_equation()
        
        # Wave Functions
        self.explain_wave_functions()
        
        # Time Evolution
        self.show_time_evolution()
        
        # Probability Density
        self.explain_probability_density()
        
        # Physical Interpretation
        self.physical_interpretation()
        
        # Particle in a Box Example
        self.particle_in_box_example()
        
        # Conclusion
        self.conclusion()

    def introduction(self):
        with self.voiceover(text="Welcome to this deep dive into one of the most fundamental equations in quantum mechanics: the Schrödinger equation.") as tracker:
            title = Text("The Schrödinger Equation", font_size=48, color=BLUE)
            title.move_to(ORIGIN)
            self.play(Write(title))
            self.wait(0.5)
        
        with self.voiceover(text="This equation describes how quantum systems evolve over time and is the cornerstone of wave mechanics.") as tracker:
            subtitle = Text("Foundation of Quantum Mechanics", font_size=28, color=YELLOW)
            subtitle.next_to(title, DOWN, buff=0.5)
            self.play(FadeIn(subtitle))
        
        self.play(FadeOut(title), FadeOut(subtitle))

    def show_schrodinger_equation(self):
        with self.voiceover(text="Let's start with the time-dependent Schrödinger equation in its most general form.") as tracker:
            section_title = Text("The Schrödinger Equation", font_size=36, color=BLUE)
            section_title.to_edge(UP)
            self.play(Write(section_title))
        
        with self.voiceover(text="The equation states that i times the reduced Planck constant times the partial derivative of psi with respect to time equals the Hamiltonian operator acting on psi.") as tracker:
            equation = MathTex(
                r"i\hbar \frac{\partial \psi}{\partial t} = \hat{H} \psi",
                font_size=56
            )
            equation.move_to(ORIGIN)
            self.play(Write(equation))
            self.wait(0.5)
        
        with self.voiceover(text="Let's break down each component. First, i is the imaginary unit, fundamental to quantum mechanics.") as tracker:
            i_box = SurroundingRectangle(equation[0][0], color=YELLOW, buff=0.1)
            i_label = Text("Imaginary unit", font_size=24, color=YELLOW)
            i_label.next_to(i_box, DOWN, buff=0.3)
            self.play(Create(i_box), Write(i_label))
            self.wait(0.5)
            self.play(FadeOut(i_box), FadeOut(i_label))
        
        with self.voiceover(text="h-bar is the reduced Planck constant, connecting energy and frequency in the quantum world.") as tracker:
            hbar_box = SurroundingRectangle(equation[0][1:3], color=GREEN, buff=0.1)
            hbar_label = Text("Reduced Planck constant", font_size=24, color=GREEN)
            hbar_label.next_to(hbar_box, DOWN, buff=0.3)
            hbar_value = MathTex(r"\hbar = \frac{h}{2\pi} \approx 1.055 \times 10^{-34} \text{ J·s}", font_size=28)
            hbar_value.next_to(hbar_label, DOWN, buff=0.2)
            self.play(Create(hbar_box), Write(hbar_label))
            self.play(Write(hbar_value))
            self.wait(0.5)
            self.play(FadeOut(hbar_box), FadeOut(hbar_label), FadeOut(hbar_value))
        
        with self.voiceover(text="Psi is the wave function, which contains all the information about the quantum state of the system.") as tracker:
            psi_box = SurroundingRectangle(equation[0][8:10], color=RED, buff=0.1)
            psi_label = Text("Wave function", font_size=24, color=RED)
            psi_label.next_to(psi_box, UP, buff=0.3)
            self.play(Create(psi_box), Write(psi_label))
            self.wait(0.5)
            self.play(FadeOut(psi_box), FadeOut(psi_label))
        
        with self.voiceover(text="The Hamiltonian operator represents the total energy of the system, including kinetic and potential energy.") as tracker:
            h_box = SurroundingRectangle(equation[0][13:15], color=PURPLE, buff=0.1)
            h_label = Text("Hamiltonian (Energy operator)", font_size=24, color=PURPLE)
            h_label.next_to(h_box, DOWN, buff=0.3)
            self.play(Create(h_box), Write(h_label))
            self.wait(0.5)
            self.play(FadeOut(h_box), FadeOut(h_label))
        
        with self.voiceover(text="For a single particle in one dimension, the Hamiltonian can be written explicitly in terms of kinetic and potential energy operators.") as tracker:
            hamiltonian = MathTex(
                r"\hat{H} = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x)",
                font_size=44
            )
            hamiltonian.next_to(equation, DOWN, buff=0.8)
            self.play(Write(hamiltonian))
        
        with self.voiceover(text="This gives us the full time-dependent Schrödinger equation in position space.") as tracker:
            full_equation = MathTex(
                r"i\hbar \frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2 \psi}{\partial x^2} + V(x)\psi",
                font_size=40
            )
            full_equation.move_to(ORIGIN + DOWN * 0.5)
            self.play(
                FadeOut(equation),
                FadeOut(hamiltonian),
                FadeOut(section_title)
            )
            self.play(Write(full_equation))
            self.wait(1)
        
        self.play(FadeOut(full_equation))

    def explain_wave_functions(self):
        with self.voiceover(text="Now let's explore what wave functions actually are and what they represent.") as tracker:
            section_title = Text("Wave Functions", font_size=36, color=BLUE)
            section_title.to_edge(UP)
            self.play(Write(section_title))
        
        with self.voiceover(text="A wave function psi is a complex-valued function that describes the quantum state of a particle.") as tracker:
            wave_def = MathTex(r"\psi(x, t) \in \mathbb{C}", font_size=44)
            wave_def.move_to(UP * 2)
            self.play(Write(wave_def))
        
        with self.voiceover(text="Let's visualize a simple wave function. We'll look at the real and imaginary parts separately.") as tracker:
            axes = Axes(
                x_range=[-5, 5, 1],
                y_range=[-1.5, 1.5, 0.5],
                x_length=10,
                y_length=4,
                axis_config={"color": BLUE, "include_tip": True}
            )
            axes.move_to(DOWN * 0.5)
            
            x_label = axes.get_x_axis_label("x", direction=RIGHT)
            y_label = axes.get_y_axis_label(r"\psi", direction=UP)
            
            self.play(Create(axes), Write(x_label), Write(y_label))
        
        with self.voiceover(text="Here's the real part of a Gaussian wave packet, a common wave function in quantum mechanics.") as tracker:
            real_wave = axes.plot(
                lambda x: np.exp(-x**2/2) * np.cos(3*x),
                color=GREEN,
                x_range=[-5, 5]
            )
            real_label = Text("Re(ψ)", font_size=28, color=GREEN)
            real_label.next_to(axes, RIGHT, buff=0.3).shift(UP * 1)
            
            self.play(Create(real_wave), Write(real_label))
        
        with self.voiceover(text="And here's the imaginary part, shown in red, which oscillates out of phase with the real part.") as tracker:
            imag_wave = axes.plot(
                lambda x: np.exp(-x**2/2) * np.sin(3*x),
                color=RED,
                x_range=[-5, 5]
            )
            imag_label = Text("Im(ψ)", font_size=28, color=RED)
            imag_label.next_to(axes, RIGHT, buff=0.3).shift(DOWN * 1)
            
            self.play(Create(imag_wave), Write(imag_label))
            self.wait(1)
        
        self.play(FadeOut(axes), FadeOut(x_label), FadeOut(y_label), 
                  FadeOut(real_wave), FadeOut(imag_wave), 
                  FadeOut(real_label), FadeOut(imag_label), 
                  FadeOut(wave_def), FadeOut(section_title))

    def show_time_evolution(self):
        with self.voiceover(text="One of the most fascinating aspects of quantum mechanics is how wave functions evolve in time.") as tracker:
            section_title = Text("Time Evolution", font_size=36, color=BLUE)
            section_title.to_edge(UP)
            self.play(Write(section_title))
        
        with self.voiceover(text="For stationary states, the time dependence can be separated out as a simple phase factor.") as tracker:
            separation = MathTex(
                r"\psi(x,t) = \phi(x) e^{-iEt/\hbar}",
                font_size=48
            )
            separation.move_to(UP * 1.5)
            self.play(Write(separation))
        
        with self.voiceover(text="Here, phi of x is the spatial part, and the exponential represents oscillation in time.") as tracker:
            spatial_box = SurroundingRectangle(separation[0][6:10], color=GREEN, buff=0.1)
            spatial_label = Text("Spatial part", font_size=24, color=GREEN)
            spatial_label.next_to(spatial_box, UP, buff=0.2)
            
            time_box = SurroundingRectangle(separation[0][10:], color=PURPLE, buff=0.1)
            time_label = Text("Time oscillation", font_size=24, color=PURPLE)
            time_label.next_to(time_box, DOWN, buff=0.2)
            
            self.play(Create(spatial_box), Write(spatial_label))
            self.play(Create(time_box), Write(time_label))
            self.wait(0.5)
            self.play(FadeOut(spatial_box), FadeOut(spatial_label), 
                     FadeOut(time_box), FadeOut(time_label))
        
        with self.voiceover(text="Let's see this evolution in action. Watch as the wave function rotates in the complex plane while maintaining its shape.") as tracker:
            # Create a parametric plot showing time evolution
            axes = Axes(
                x_range=[-3, 3, 1],
                y_range=[-1.2, 1.2, 0.5],
                x_length=8,
                y_length=4,
                axis_config={"color": BLUE}
            )
            axes.move_to(DOWN * 1)
            
            x_label = axes.get_x_axis_label("x")
            
            self.play(Create(axes), Write(x_label))
            
            # Animate wave function evolution
            wave = always_redraw(lambda: axes.plot(
                lambda x: np.exp(-x**2/2) * np.cos(3*x - self.renderer.time * 2),
                color=YELLOW,
                x_range=[-3, 3]
            ))
            
            time_tracker = ValueTracker(0)
            time_label = always_redraw(lambda: MathTex(
                f"t = {time_tracker.get_value():.1f}",
                font_size=32,
                color=YELLOW
            ).next_to(axes, UP, buff=0.3))
            
            self.add(wave, time_label)
            self.play(time_tracker.animate.set_value(3), run_time=3, rate_func=linear)
        
        self.play(FadeOut(axes), FadeOut(x_label), FadeOut(wave), 
                  FadeOut(time_label), FadeOut(separation), FadeOut(section_title))

    def explain_probability_density(self):
        with self.voiceover(text="Now we come to one of the most important concepts: the Born interpretation of the wave function.") as tracker:
            section_title = Text("Probability Density", font_size=36, color=BLUE)
            section_title.to_edge(UP)
            self.play(Write(section_title))
        
        with self.voiceover(text="The wave function itself is not directly observable, but its absolute value squared gives us the probability density.") as tracker:
            born_rule = MathTex(
                r"P(x,t) = |\psi(x,t)|^2 = \psi^*(x,t)\psi(x,t)",
                font_size=44
            )
            born_rule.move_to(UP * 2.3)
            self.play(Write(born_rule))
        
        with self.voiceover(text="This probability density tells us the likelihood of finding the particle at position x at time t.") as tracker:
            interpretation = Text(
                "Probability of finding particle at position x",
                font_size=26,
                color=YELLOW
            )
            interpretation.next_to(born_rule, DOWN, buff=0.4)
            self.play(Write(interpretation))
        
        with self.voiceover(text="Let's visualize this. I'll show you a wave function and its corresponding probability density.") as tracker:
            # Create axes for wave function
            axes_wave = Axes(
                x_range=[-4, 4, 1],
                y_range=[-1, 1, 0.5],
                x_length=7,
                y_length=2.5,
                axis_config={"color": BLUE}
            )
            axes_wave.move_to(LEFT * 0 + DOWN * 0.3)
            
            wave_label = Text("ψ(x)", font_size=24, color=GREEN)
            wave_label.next_to(axes_wave, LEFT, buff=0.2)
            
            self.play(Create(axes_wave), Write(wave_label))
            
            # Plot wave function
            wave_function = axes_wave.plot(
                lambda x: np.exp(-x**2/2) * np.cos(3*x),
                color=GREEN,
                x_range=[-4, 4]
            )
            self.play(Create(wave_function))
        
        with self.voiceover(text="Now, when we square the absolute value, we get the probability density, which is always positive and shows where the particle is likely to be found.") as tracker:
            # Create axes for probability density
            axes_prob = Axes(
                x_range=[-4, 4, 1],
                y_range=[0, 1.2, 0.5],
                x_length=7,
                y_length=2.5,
                axis_config={"color": BLUE}
            )
            axes_prob.next_to(axes_wave, DOWN, buff=0.8)
            
            prob_label = Text("|ψ(x)|²", font_size=24, color=ORANGE)
            prob_label.next_to(axes_prob, LEFT, buff=0.2)
            
            self.play(Create(axes_prob), Write(prob_label))
            
            # Plot probability density
            prob_density = axes_prob.plot(
                lambda x: np.exp(-x**2),
                color=ORANGE,
                x_range=[-4, 4]
            )
            self.play(Create(prob_density))
            self.wait(1)
        
        with self.voiceover(text="Notice how the probability density is smooth and peaked where the wave function has large amplitude, regardless of its phase.") as tracker:
            # Highlight peak
            peak_dot_wave = Dot(axes_wave.c2p(0, 1), color=YELLOW, radius=0.08)
            peak_dot_prob = Dot(axes_prob.c2p(0, 1), color=YELLOW, radius=0.08)
            
            self.play(Create(peak_dot_wave), Create(peak_dot_prob))
            self.wait(0.5)
            self.play(FadeOut(peak_dot_wave), FadeOut(peak_dot_prob))
        
        with self.voiceover(text="An important property is normalization: the total probability of finding the particle somewhere must equal one.") as tracker:
            normalization = MathTex(
                r"\int_{-\infty}^{\infty} |\psi(x,t)|^2 \, dx = 1",
                font_size=40
            )
            normalization.move_to(RIGHT * 3.5 + UP * 0.5)
            self.play(Write(normalization))
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def physical_interpretation(self):
        with self.voiceover(text="Let's discuss the profound physical interpretation of these mathematical concepts.") as tracker:
            section_title = Text("Physical Meaning", font_size=36, color=BLUE)
            section_title.to_edge(UP)
            self.play(Write(section_title))
        
        with self.voiceover(text="The wave function represents a superposition of all possible states. The particle doesn't have a definite position until we measure it.") as tracker:
            superposition_text = Text(
                "Superposition: Particle in multiple states simultaneously",
                font_size=28,
                color=YELLOW
            )
            superposition_text.move_to(UP * 1.8)
            self.play(Write(superposition_text))
        
        with self.voiceover(text="Let's visualize this with a simple example. Imagine a particle that could be in one of three positions.") as tracker:
            # Create three position indicators
            positions = VGroup()
            for i in range(3):
                x_pos = (i - 1) * 3
                dot = Dot(point=x_pos * RIGHT + DOWN * 0.5, radius=0.15, color=BLUE)
                label = MathTex(f"x_{i+1}", font_size=32).next_to(dot, DOWN, buff=0.3)
                positions.add(VGroup(dot, label))
            
            self.play(Create(positions))
        
        with self.voiceover(text="Before measurement, the particle exists in a superposition, represented by probability amplitudes at each position.") as tracker:
            # Add probability bars
            prob_bars = VGroup()
            probs = [0.5, 0.3, 0.2]
            for i, prob in enumerate(probs):
                x_pos = (i - 1) * 3
                bar = Rectangle(
                    width=0.6,
                    height=prob * 3,
                    fill_color=GREEN,
                    fill_opacity=0.7,
                    stroke_color=WHITE
                )
                bar.next_to(positions[i][0], UP, buff=0.1, aligned_edge=DOWN)
                prob_label = MathTex(f"{prob:.1f}", font_size=24).next_to(bar, UP, buff=0.1)
                prob_bars.add(VGroup(bar, prob_label))
            
            self.play(Create(prob_bars))
        
        with self.voiceover(text="Upon measurement, the wave function collapses to one definite state, with probabilities determined by the wave function's amplitude.") as tracker:
            # Simulate collapse
            collapse_text = Text("MEASUREMENT!", font_size=32, color=RED)
            collapse_text.move_to(UP * 2.5)
            self.play(Write(collapse_text))
            
            # Choose position 1 (index 0)
            chosen_index = 0
            
            # Fade out non-chosen positions
            fade_indices = [1, 2]
            self.play(
                *[prob_bars[i].animate.set_opacity(0.2) for i in fade_indices],
                *[positions[i].animate.set_opacity(0.2) for i in fade_indices],
                prob_bars[chosen_index][0].animate.set_color(RED),
                run_time=1.5
            )
            
            result_text = Text(
                f"Particle found at position x₁",
                font_size=26,
                color=RED
            )
            result_text.next_to(collapse_text, DOWN, buff=0.3)
            self.play(Write(result_text))
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def particle_in_box_example(self):
        with self.voiceover(text="Let's explore a classic example: the particle in a box, also known as the infinite square well.") as tracker:
            section_title = Text("Particle in a Box", font_size=36, color=BLUE)
            section_title.to_edge(UP)
            self.play(Write(section_title))
        
        with self.voiceover(text="Imagine a particle confined to a one-dimensional box with impenetrable walls. The particle can only exist between x equals zero and x equals L.") as tracker:
            # Draw the box
            box_left = Line(UP * 2 + LEFT * 4, DOWN * 2 + LEFT * 4, color=WHITE, stroke_width=8)
            box_right = Line(UP * 2 + RIGHT * 4, DOWN * 2 + RIGHT * 4, color=WHITE, stroke_width=8)
            box_bottom = Line(DOWN * 2 + LEFT * 4, DOWN * 2 + RIGHT * 4, color=WHITE, stroke_width=4)
            
            label_0 = MathTex("x = 0", font_size=28).next_to(box_left, DOWN, buff=0.3)
            label_L = MathTex("x = L", font_size=28).next_to(box_right, DOWN, buff=0.3)
            
            box = VGroup(box_left, box_right, box_bottom, label_0, label_L)
            self.play(Create(box))
        
        with self.voiceover(text="The boundary conditions require that the wave function equals zero at the walls.") as tracker:
            boundary_cond = MathTex(
                r"\psi(0) = 0, \quad \psi(L) = 0",
                font_size=36
            )
            boundary_cond.move_to(UP * 2.8)
            self.play(Write(boundary_cond))
        
        with self.voiceover(text="Solving the Schrödinger equation with these boundary conditions gives us quantized energy levels and specific wave functions.") as tracker:
            solutions = MathTex(
                r"\psi_n(x) = \sqrt{\frac{2}{L}} \sin\left(\frac{n\pi x}{L}\right)",
                font_size=36
            )
            solutions.next_to(boundary_cond, DOWN, buff=0.4)
            self.play(Write(solutions))
        
        with self.voiceover(text="The energy levels are also quantized, proportional to n squared, where n is a positive integer called the quantum number.") as tracker:
            energy = MathTex(
                r"E_n = \frac{n^2 \pi^2 \hbar^2}{2mL^2}",
                font_size=36
            )
            energy.next_to(solutions, DOWN, buff=0.4)
            self.play(Write(energy))
            self.wait(0.5)
        
        self.play(FadeOut(boundary_cond), FadeOut(solutions), FadeOut(energy))
        
        with self.voiceover(text="Let's visualize the first three energy eigenstates. The ground state, n equals one, has no nodes inside the box.") as tracker:
            # Create axes
            axes = Axes(
                x_range=[0, 1, 0.25],
                y_range=[-1.8, 1.8, 0.5],
                x_length=7,
                y_length=3.5,
                axis_config={"color": BLUE}
            )
            axes.move_to(DOWN * 0.3)
            
            # Ground state n=1
            wave_1 = axes.plot(
                lambda x: np.sqrt(2) * np.sin(np.pi * x),
                color=GREEN,
                x_range=[0, 1]
            )
            label_1 = MathTex("n = 1", font_size=32, color=GREEN)
            label_1.next_to(axes, RIGHT, buff=0.5).shift(UP * 1)
            
            self.play(Create(axes), Create(wave_1), Write(label_1))
            self.wait(0.5)
        
        with self.voiceover(text="The first excited state, n equals two, has one node in the center where the wave function crosses zero.") as tracker:
            wave_2 = axes.plot(
                lambda x: np.sqrt(2) * np.sin(2 * np.pi * x),
                color=YELLOW,
                x_range=[0, 1]
            )
            label_2 = MathTex("n = 2", font_size=32, color=YELLOW)
            label_2.next_to(label_1, DOWN, buff=0.3)
            
            self.play(Create(wave_2), Write(label_2))
            self.wait(0.5)
        
        with self.voiceover(text="The second excited state, n equals three, has two nodes, creating three regions of oscillation.") as tracker:
            wave_3 = axes.plot(
                lambda x: np.sqrt(2) * np.sin(3 * np.pi * x),
                color=RED,
                x_range=[0, 1]
            )
            label_3 = MathTex("n = 3", font_size=32, color=RED)
            label_3.next_to(label_2, DOWN, buff=0.3)
            
            self.play(Create(wave_3), Write(label_3))
            self.wait(1)
        
        self.play(FadeOut(wave_1), FadeOut(wave_2), FadeOut(wave_3),
                  FadeOut(label_1), FadeOut(label_2), FadeOut(label_3))
        
        with self.voiceover(text="Now let's look at the probability densities for these states. Notice how they show where the particle is most likely to be found.") as tracker:
            # Probability density for n=1
            prob_1 = axes.plot(
                lambda x: 2 * (np.sin(np.pi * x))**2,
                color=GREEN,
                x_range=[0, 1]
            )
            prob_label_1 = MathTex("|\\psi_1|^2", font_size=32, color=GREEN)
            prob_label_1.next_to(axes, RIGHT, buff=0.5).shift(UP * 1)
            
            self.play(Create(prob_1), Write(prob_label_1))
            self.wait(0.5)
            
            # Add shading under curve
            area_1 = axes.get_riemann_rectangles(
                prob_1,
                x_range=[0, 1],
                dx=0.02,
                color=GREEN,
                fill_opacity=0.3,
                stroke_width=0
            )
            self.play(Create(area_1))
        
        with self.voiceover(text="For the ground state, the particle is most likely to be found in the center of the box, with probability decreasing toward the walls.") as tracker:
            center_marker = Dot(axes.c2p(0.5, 2 * (np.sin(np.pi * 0.5))**2), color=YELLOW, radius=0.1)
            self.play(Create(center_marker))
            self.wait(0.5)
            self.play(FadeOut(center_marker))
        
        with self.voiceover(text="Higher energy states show more complex probability distributions, with regions where the particle is unlikely to be found.") as tracker:
            self.play(FadeOut(prob_1), FadeOut(area_1), FadeOut(prob_label_1))
            
            prob_2 = axes.plot(
                lambda x: 2 * (np.sin(2 * np.pi * x))**2,
                color=YELLOW,
                x_range=[0, 1]
            )
            prob_label_2 = MathTex("|\\psi_2|^2", font_size=32, color=YELLOW)
            prob_label_2.next_to(axes, RIGHT, buff=0.5).shift(UP * 1)
            
            self.play(Create(prob_2), Write(prob_label_2))
            
            # Highlight node
            node_marker = Dot(axes.c2p(0.5, 0), color=RED, radius=0.1)
            node_label = Text("Node: zero probability", font_size=22, color=RED)
            node_label.next_to(node_marker, UP, buff=0.2)
            self.play(Create(node_marker), Write(node_label))
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def conclusion(self):
        with self.voiceover(text="Let's summarize the key concepts we've explored about the Schrödinger equation.") as tracker:
            title = Text("Summary", font_size=40, color=BLUE)
            title.move_to(UP * 3)
            self.play(Write(title))
        
        with self.voiceover(text="First, the Schrödinger equation is the fundamental equation that governs the evolution of quantum systems over time.") as tracker:
            point1 = Text(
                "• Schrödinger equation: Evolution of quantum states",
                font_size=26,
                color=WHITE
            )
            point1.move_to(UP * 2)
            self.play(Write(point1))
        
        with self.voiceover(text="Second, the wave function contains all information about a quantum system, but it's a complex-valued probability amplitude, not a directly observable quantity.") as tracker:
            point2 = Text(
                "• Wave function ψ: Complex probability amplitude",
                font_size=26,
                color=WHITE
            )
            point2.next_to(point1, DOWN, buff=0.4, aligned_edge=LEFT)
            self.play(Write(point2))
        
        with self.voiceover(text="Third, the probability density, given by the absolute value of psi squared, tells us where we're likely to find the particle upon measurement.") as tracker:
            point3 = Text(
                "• Probability density |ψ|²: Observable predictions",
                font_size=26,
                color=WHITE
            )
            point3.next_to(point2, DOWN, buff=0.4, aligned_edge=LEFT)
            self.play(Write(point3))
        
        with self.voiceover(text="Fourth, quantum systems exist in superposition until measured, when the wave function collapses to a definite state.") as tracker:
            point4 = Text(
                "• Superposition & collapse: Quantum measurement",
                font_size=26,
                color=WHITE
            )
            point4.next_to(point3, DOWN, buff=0.4, aligned_edge=LEFT)
            self.play(Write(point4))
        
        with self.voiceover(text="And finally, boundary conditions lead to quantization, as we saw with the particle in a box, where only specific energy levels are allowed.") as tracker:
            point5 = Text(
                "• Quantization: Discrete energy levels from boundaries",
                font_size=26,
                color=WHITE
            )
            point5.next_to(point4, DOWN, buff=0.4, aligned_edge=LEFT)
            self.play(Write(point5))
        
        with self.voiceover(text="The Schrödinger equation revolutionized our understanding of the atomic and subatomic world, providing a mathematical framework that describes phenomena impossible to explain with classical physics.") as tracker:
            final_equation = MathTex(
                r"i\hbar \frac{\partial \psi}{\partial t} = \hat{H} \psi",
                font_size=50,
                color=YELLOW
            )
            final_equation.move_to(DOWN * 1.5)
            self.play(Write(final_equation))
            self.wait(1)
        
        with self.voiceover(text="Thank you for joining me on this journey through quantum mechanics. Keep exploring the fascinating world of wave functions and probability!") as tracker:
            closing = Text("Thank You!", font_size=48, color=BLUE)
            closing.move_to(DOWN * 2.8)
            self.play(Write(closing))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

# To render this animation, run:
# manim -pql schrodinger_explanation.py SchrodingerEquationExplanation
