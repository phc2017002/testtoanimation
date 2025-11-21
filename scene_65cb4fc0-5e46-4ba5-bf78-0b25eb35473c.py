from manim import *
from manim_voiceover import VoiceoverScene
from manimator.services import ElevenLabsService
import numpy as np

class SchrodingerEquationExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(ElevenLabsService(voice_id="Rachel"))
        
        # Introduction
        self.introduction()
        
        # Historical Context
        self.historical_context()
        
        # The Time-Dependent Schrödinger Equation
        self.time_dependent_equation()
        
        # Understanding the Wave Function
        self.wave_function_intro()
        
        # Wave Function Properties
        self.wave_function_properties()
        
        # Probability Density
        self.probability_density_concept()
        
        # The Time-Independent Schrödinger Equation
        self.time_independent_equation()
        
        # Simple Example: Particle in a Box
        self.particle_in_box()
        
        # Energy Levels and Quantization
        self.energy_levels()
        
        # The Quantum Harmonic Oscillator
        self.harmonic_oscillator()
        
        # Probability Current and Conservation
        self.probability_current()
        
        # The Uncertainty Principle Connection
        self.uncertainty_principle()
        
        # Conclusion
        self.conclusion()

    def introduction(self):
        with self.voiceover(text="Welcome to this comprehensive explanation of the Schrödinger equation, one of the most fundamental equations in quantum mechanics. This equation describes how quantum states evolve over time and is the cornerstone of our understanding of the microscopic world.") as tracker:
            title = Text("The Schrödinger Equation", font_size=48, color=BLUE, weight=BOLD)
            subtitle = Text("Wave Functions and Probability Density", font_size=28, color=WHITE)
            subtitle.next_to(title, DOWN, buff=0.5)
            
            self.play(Write(title))
            self.wait(0.5)
            self.play(FadeIn(subtitle))
        
        with self.voiceover(text="Named after Austrian physicist Erwin Schrödinger, this equation revolutionized physics when it was introduced in nineteen twenty-six. Today, we'll explore its meaning, its components, and how it predicts the behavior of quantum particles.") as tracker:
            self.wait()
        
        self.play(FadeOut(title), FadeOut(subtitle))

    def historical_context(self):
        with self.voiceover(text="Before diving into the mathematics, let's understand the historical context. In the early twentieth century, physicists discovered that light could behave as both a wave and a particle. This wave-particle duality was puzzling.") as tracker:
            section_title = Text("Historical Context", font_size=40, color=BLUE)
            section_title.to_edge(UP)
            self.play(Write(section_title))
            
            # Wave representation
            wave = FunctionGraph(
                lambda x: 0.5 * np.sin(2 * x),
                x_range=[-3, 3],
                color=YELLOW
            ).shift(UP)
            wave_label = Text("Wave", font_size=24).next_to(wave, DOWN)
            
            self.play(Create(wave), Write(wave_label))
        
        with self.voiceover(text="Louis de Broglie proposed that if light can be a particle, then matter particles like electrons should also have wave properties. This was a radical idea that needed mathematical formulation.") as tracker:
            # Particle representation
            particle = Dot(color=RED, radius=0.2).shift(DOWN * 1.5)
            particle_label = Text("Particle", font_size=24).next_to(particle, DOWN)
            
            self.play(Create(particle), Write(particle_label))
        
        with self.voiceover(text="Schrödinger developed his famous equation to describe these matter waves mathematically. It provided the framework to calculate how quantum systems evolve and predict experimental results with stunning accuracy.") as tracker:
            self.wait()
        
        self.play(FadeOut(*self.mobjects))

    def time_dependent_equation(self):
        with self.voiceover(text="Let's now look at the time-dependent Schrödinger equation. This is the most general form of the equation, describing how a quantum state changes with time.") as tracker:
            section_title = Text("Time-Dependent Schrödinger Equation", font_size=36, color=BLUE)
            section_title.to_edge(UP)
            self.play(Write(section_title))
        
        with self.voiceover(text="Here is the equation in its full glory. I h-bar times the partial derivative of psi with respect to time equals the Hamiltonian operator acting on psi.") as tracker:
            equation = MathTex(
                r"i\hbar\frac{\partial \psi}{\partial t} = \hat{H}\psi",
                font_size=50
            )
            equation.shift(UP * 0.5)
            self.play(Write(equation))
        
        with self.voiceover(text="Let's break down each component. Psi, the Greek letter, represents the wave function. This is the quantum state of the system and contains all the information we can know about the particle.") as tracker:
            psi_box = SurroundingRectangle(equation[0][3], color=YELLOW, buff=0.1)
            psi_label = Text("Wave Function ψ", font_size=28, color=YELLOW)
            psi_label.next_to(equation, DOWN, buff=1.5)
            
            self.play(Create(psi_box))
            self.play(Write(psi_label))
            self.wait(1)
            self.play(FadeOut(psi_box), FadeOut(psi_label))
        
        with self.voiceover(text="The letter i is the imaginary unit, equal to the square root of negative one. Its presence tells us that quantum mechanics is fundamentally complex-valued, not just real numbers.") as tracker:
            i_box = SurroundingRectangle(equation[0][0], color=GREEN, buff=0.1)
            i_label = MathTex(r"i = \sqrt{-1}", font_size=32, color=GREEN)
            i_label.next_to(equation, DOWN, buff=1.5)
            
            self.play(Create(i_box))
            self.play(Write(i_label))
            self.wait(1)
            self.play(FadeOut(i_box), FadeOut(i_label))
        
        with self.voiceover(text="H-bar is the reduced Planck constant, approximately one point zero five times ten to the minus thirty-four joule seconds. It sets the scale of quantum effects.") as tracker:
            hbar_box = SurroundingRectangle(equation[0][1], color=ORANGE, buff=0.1)
            hbar_label = MathTex(r"\hbar \approx 1.05 \times 10^{-34} \text{ J·s}", font_size=28, color=ORANGE)
            hbar_label.next_to(equation, DOWN, buff=1.5)
            
            self.play(Create(hbar_box))
            self.play(Write(hbar_label))
            self.wait(1)
            self.play(FadeOut(hbar_box), FadeOut(hbar_label))
        
        with self.voiceover(text="The Hamiltonian operator, H-hat, represents the total energy of the system. It includes both kinetic energy and potential energy terms. For a single particle, it looks like this.") as tracker:
            hamiltonian_box = SurroundingRectangle(equation[0][9:11], color=RED, buff=0.1)
            hamiltonian_label = MathTex(
                r"\hat{H} = -\frac{\hbar^2}{2m}\nabla^2 + V(\mathbf{r},t)",
                font_size=36,
                color=RED
            )
            hamiltonian_label.next_to(equation, DOWN, buff=1.5)
            
            self.play(Create(hamiltonian_box))
            self.play(Write(hamiltonian_label))
        
        with self.voiceover(text="The first term is the kinetic energy operator, involving the Laplacian. The second term, V, is the potential energy, which depends on position and possibly time.") as tracker:
            self.wait()
        
        self.play(FadeOut(*self.mobjects))

    def wave_function_intro(self):
        with self.voiceover(text="Now let's understand what the wave function actually is. The wave function psi is a complex-valued function that describes the quantum state of a particle or system.") as tracker:
            section_title = Text("Understanding the Wave Function", font_size=36, color=BLUE)
            section_title.to_edge(UP)
            self.play(Write(section_title))
            
            wave_eq = MathTex(r"\psi(x,t)", font_size=48)
            wave_eq.shift(UP * 1.5)
            self.play(Write(wave_eq))
        
        with self.voiceover(text="For a particle in one dimension, psi depends on position x and time t. Being complex-valued means it has both a real part and an imaginary part, which we can visualize separately.") as tracker:
            axes = Axes(
                x_range=[-4, 4, 1],
                y_range=[-2, 2, 1],
                x_length=7,
                y_length=3,
                axis_config={"color": WHITE}
            )
            axes.shift(DOWN * 1)
            
            x_label = axes.get_x_axis_label("x")
            y_label = Text("ψ", font_size=28).next_to(axes.get_y_axis(), UP)
            
            self.play(Create(axes), Write(x_label), Write(y_label))
        
        with self.voiceover(text="Here's an example wave function. The blue curve shows the real part, and the red curve shows the imaginary part. The wave function oscillates in space, which is why we call it a matter wave.") as tracker:
            # Real part
            real_wave = axes.plot(
                lambda x: np.exp(-x**2/4) * np.cos(2*x),
                x_range=[-4, 4],
                color=BLUE
            )
            real_label = Text("Re(ψ)", font_size=24, color=BLUE).next_to(axes, RIGHT).shift(UP * 0.5)
            
            # Imaginary part
            imag_wave = axes.plot(
                lambda x: np.exp(-x**2/4) * np.sin(2*x),
                x_range=[-4, 4],
                color=RED
            )
            imag_label = Text("Im(ψ)", font_size=24, color=RED).next_to(real_label, DOWN, buff=0.3)
            
            self.play(Create(real_wave), Write(real_label))
            self.wait(0.5)
            self.play(Create(imag_wave), Write(imag_label))
        
        with self.voiceover(text="An important point: the wave function itself is not directly observable. We cannot measure psi directly. Instead, we use it to calculate probabilities of measurement outcomes.") as tracker:
            self.wait()
        
        self.play(FadeOut(*self.mobjects))

    def wave_function_properties(self):
        with self.voiceover(text="The wave function must satisfy certain mathematical properties. First and foremost, it must be normalized. This means the total probability of finding the particle somewhere in space must equal one.") as tracker:
            section_title = Text("Wave Function Properties", font_size=36, color=BLUE)
            section_title.to_edge(UP)
            self.play(Write(section_title))
            
            normalization = MathTex(
                r"\int_{-\infty}^{\infty} |\psi(x,t)|^2 dx = 1",
                font_size=44
            )
            normalization.shift(UP * 1.5)
            self.play(Write(normalization))
        
        with self.voiceover(text="This normalization condition is the integral of the absolute value squared of psi over all space equals one. The absolute value squared turns the complex wave function into a real, non-negative number.") as tracker:
            abs_sq_box = SurroundingRectangle(normalization[0][3:9], color=YELLOW, buff=0.1)
            self.play(Create(abs_sq_box))
            self.wait(1)
            self.play(FadeOut(abs_sq_box))
        
        with self.voiceover(text="Second, the wave function must be continuous and have a continuous first derivative everywhere, except possibly at points where the potential energy is infinite.") as tracker:
            continuity = Text("ψ and dψ/dx must be continuous", font_size=32)
            continuity.next_to(normalization, DOWN, buff=1.2)
            self.play(Write(continuity))
        
        with self.voiceover(text="Third, the wave function must be square-integrable, meaning it must go to zero fast enough at infinity that the normalization integral converges. This ensures the particle has a finite probability of being found.") as tracker:
            square_int = MathTex(
                r"\lim_{|x| \to \infty} \psi(x,t) = 0",
                font_size=38
            )
            square_int.next_to(continuity, DOWN, buff=0.8)
            self.play(Write(square_int))
        
        self.play(FadeOut(*self.mobjects))

    def probability_density_concept(self):
        with self.voiceover(text="Now we arrive at one of the most important concepts in quantum mechanics: the probability density. This is how we extract physical predictions from the wave function.") as tracker:
            section_title = Text("Probability Density", font_size=40, color=BLUE)
            section_title.to_edge(UP)
            self.play(Write(section_title))
        
        with self.voiceover(text="The probability density is given by the absolute value squared of the wave function. This is also written as psi-star times psi, where psi-star is the complex conjugate.") as tracker:
            prob_density = MathTex(
                r"\rho(x,t) = |\psi(x,t)|^2 = \psi^*(x,t)\psi(x,t)",
                font_size=42
            )
            prob_density.shift(UP * 1.5)
            self.play(Write(prob_density))
        
        with self.voiceover(text="Rho of x and t gives the probability per unit length of finding the particle at position x at time t. To find the probability in a specific region, we integrate the probability density over that region.") as tracker:
            prob_region = MathTex(
                r"P(a \leq x \leq b) = \int_a^b |\psi(x,t)|^2 dx",
                font_size=38
            )
            prob_region.next_to(prob_density, DOWN, buff=1)
            self.play(Write(prob_region))
        
        with self.voiceover(text="Let me show you a visual example. Here's a wave function in blue, with both its real and imaginary parts oscillating.") as tracker:
            self.play(FadeOut(prob_region))
            
            axes = Axes(
                x_range=[-4, 4, 1],
                y_range=[-1.5, 1.5, 0.5],
                x_length=8,
                y_length=2.5,
                axis_config={"color": WHITE}
            )
            axes.shift(DOWN * 0.5)
            
            x_label = axes.get_x_axis_label("x")
            
            self.play(Create(axes), Write(x_label))
        
        with self.voiceover(text="The wave function has amplitude that varies with position. It's concentrated in the center and decreases as we move away.") as tracker:
            wave_func = axes.plot(
                lambda x: np.exp(-x**2/2) * np.cos(3*x),
                x_range=[-4, 4],
                color=BLUE
            )
            wave_label = MathTex(r"\psi(x)", font_size=28, color=BLUE).next_to(axes, UP).shift(LEFT * 2)
            
            self.play(Create(wave_func), Write(wave_label))
        
        with self.voiceover(text="Now, when we calculate the probability density by squaring the absolute value, we get this red curve. Notice it's always positive and shows where the particle is most likely to be found.") as tracker:
            prob_axes = Axes(
                x_range=[-4, 4, 1],
                y_range=[0, 1.2, 0.5],
                x_length=8,
                y_length=2.5,
                axis_config={"color": WHITE}
            )
            prob_axes.shift(DOWN * 2.8)
            
            prob_func = prob_axes.plot(
                lambda x: np.exp(-x**2),
                x_range=[-4, 4],
                color=RED
            )
            prob_label = MathTex(r"|\psi(x)|^2", font_size=28, color=RED).next_to(prob_axes, UP).shift(LEFT * 2)
            
            self.play(Create(prob_axes), Create(prob_func), Write(prob_label))
        
        with self.voiceover(text="The peak in the probability density tells us the particle is most likely found near x equals zero. The probability drops off as we move to larger positive or negative x values.") as tracker:
            self.wait()
        
        self.play(FadeOut(*self.mobjects))

    def time_independent_equation(self):
        with self.voiceover(text="In many important cases, the potential energy does not depend on time. For these systems, we can separate the time and space parts of the wave function, leading to the time-independent Schrödinger equation.") as tracker:
            section_title = Text("Time-Independent Schrödinger Equation", font_size=34, color=BLUE)
            section_title.to_edge(UP)
            self.play(Write(section_title))
        
        with self.voiceover(text="We can write the wave function as a product: psi of x and t equals lowercase psi of x times a time-dependent phase factor e to the minus i E t over h-bar.") as tracker:
            separation = MathTex(
                r"\psi(x,t) = \psi(x)e^{-iEt/\hbar}",
                font_size=44
            )
            separation.shift(UP * 1.8)
            self.play(Write(separation))
        
        with self.voiceover(text="When we substitute this into the time-dependent equation and simplify, we get the time-independent Schrödinger equation. This equation determines the spatial part of the wave function and the allowed energy values.") as tracker:
            tise = MathTex(
                r"\hat{H}\psi(x) = E\psi(x)",
                font_size=46
            )
            tise.shift(UP * 0.3)
            self.play(Write(tise))
        
        with self.voiceover(text="In expanded form, for a particle in one dimension, this becomes: minus h-bar squared over two m times the second derivative of psi, plus V of x times psi, equals E times psi.") as tracker:
            expanded = MathTex(
                r"-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V(x)\psi(x) = E\psi(x)",
                font_size=40
            )
            expanded.shift(DOWN * 1.2)
            self.play(Write(expanded))
        
        with self.voiceover(text="This is an eigenvalue equation. E is the energy eigenvalue, and psi is the corresponding eigenfunction. For a given potential V, only certain discrete energy values may be allowed.") as tracker:
            eigenvalue_note = Text("Eigenvalue Problem", font_size=32, color=YELLOW)
            eigenvalue_note.shift(DOWN * 2.5)
            self.play(Write(eigenvalue_note))
        
        self.play(FadeOut(*self.mobjects))

    def particle_in_box(self):
        with self.voiceover(text="Let's solve the simplest quantum system: a particle in an infinite square well, also called a particle in a box. This demonstrates quantization beautifully.") as tracker:
            section_title = Text("Particle in a Box", font_size=40, color=BLUE)
            section_title.to_edge(UP)
            self.play(Write(section_title))
        
        with self.voiceover(text="Imagine a particle confined between two impenetrable walls at x equals zero and x equals L. Inside the box, the potential is zero. Outside, it's infinite, so the particle cannot escape.") as tracker:
            # Draw the potential well
            axes = Axes(
                x_range=[-1, 4, 1],
                y_range=[-0.5, 3, 1],
                x_length=7,
                y_length=3,
                axis_config={"color": WHITE}
            )
            axes.shift(DOWN * 0.8)
            
            # Infinite walls
            left_wall = Line(axes.c2p(0, 0), axes.c2p(0, 3), color=RED, stroke_width=6)
            right_wall = Line(axes.c2p(3, 0), axes.c2p(3, 3), color=RED, stroke_width=6)
            
            # Zero potential region
            floor = Line(axes.c2p(0, 0), axes.c2p(3, 0), color=WHITE, stroke_width=4)
            
            # Labels
            v_zero = MathTex("V = 0", font_size=28).move_to(axes.c2p(1.5, 1.5))
            v_inf_left = MathTex("V = \infty", font_size=24, color=RED).next_to(left_wall, LEFT)
            v_inf_right = MathTex("V = \infty", font_size=24, color=RED).next_to(right_wall, RIGHT)
            
            l_label = MathTex("L", font_size=32).next_to(axes.c2p(1.5, 0), DOWN)
            
            self.play(Create(axes), Create(left_wall), Create(right_wall), Create(floor))
            self.play(Write(v_zero), Write(v_inf_left), Write(v_inf_right), Write(l_label))
        
        with self.voiceover(text="Inside the box, the Schrödinger equation simplifies because V equals zero. We need to solve for psi subject to boundary conditions: psi must be zero at both walls.") as tracker:
            equation_box = MathTex(
                r"-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi",
                font_size=34
            )
            equation_box.to_edge(UP).shift(DOWN * 1.2)
            
            boundary = MathTex(
                r"\psi(0) = 0, \quad \psi(L) = 0",
                font_size=32
            )
            boundary.next_to(equation_box, DOWN, buff=0.4)
            
            self.play(Write(equation_box), Write(boundary))
        
        self.play(FadeOut(equation_box), FadeOut(boundary))
        
        with self.voiceover(text="The solutions are standing waves, sine functions that fit exactly into the box. The allowed wave functions are psi-n of x equals the square root of two over L times sine of n pi x over L, where n is a positive integer.") as tracker:
            solution = MathTex(
                r"\psi_n(x) = \sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right)",
                font_size=36
            )
            solution.to_edge(UP).shift(DOWN * 1.2)
            self.play(Write(solution))
        
        with self.voiceover(text="Here are the first three wave functions. N equals one is the ground state, the lowest energy state. N equals two is the first excited state, and n equals three is the second excited state.") as tracker:
            # Plot first three wave functions
            psi1 = axes.plot(
                lambda x: 0.8 * np.sin(np.pi * x / 3),
                x_range=[0, 3],
                color=BLUE
            )
            psi1_label = MathTex("n=1", font_size=24, color=BLUE).next_to(axes.c2p(3.2, 0.4), RIGHT)
            
            self.play(Create(psi1), Write(psi1_label))
            self.wait(1)
            
            psi2 = axes.plot(
                lambda x: 0.8 * np.sin(2 * np.pi * x / 3),
                x_range=[0, 3],
                color=GREEN
            )
            psi2_label = MathTex("n=2", font_size=24, color=GREEN).next_to(psi1_label, DOWN, buff=0.2)
            
            self.play(Create(psi2), Write(psi2_label))
            self.wait(1)
            
            psi3 = axes.plot(
                lambda x: 0.8 * np.sin(3 * np.pi * x / 3),
                x_range=[0, 3],
                color=YELLOW
            )
            psi3_label = MathTex("n=3", font_size=24, color=YELLOW).next_to(psi2_label, DOWN, buff=0.2)
            
            self.play(Create(psi3), Write(psi3_label))
        
        with self.voiceover(text="Notice that each wave function has n minus one nodes, points where the wave function crosses zero. The more nodes, the higher the energy.") as tracker:
            self.wait()
        
        self.play(FadeOut(*self.mobjects))

    def energy_levels(self):
        with self.voiceover(text="The particle in a box reveals one of quantum mechanics' most profound features: energy quantization. The energy cannot take any value; it must be one of specific discrete levels.") as tracker:
            section_title = Text("Energy Quantization", font_size=40, color=BLUE)
            section_title.to_edge(UP)
            self.play(Write(section_title))
        
        with self.voiceover(text="The allowed energy levels for the particle in a box are given by E-n equals n-squared times h-bar squared pi squared over two m L squared. Energy increases with the square of the quantum number n.") as tracker:
            energy_formula = MathTex(
                r"E_n = \frac{n^2\hbar^2\pi^2}{2mL^2}, \quad n = 1, 2, 3, \ldots",
                font_size=40
            )
            energy_formula.shift(UP * 2)
            self.play(Write(energy_formula))
        
        with self.voiceover(text="Let me visualize these energy levels. Each horizontal line represents an allowed energy state. The spacing between levels increases as we go higher in energy.") as tracker:
            # Energy level diagram
            level_start_x = -3
            level_length = 6
            
            levels = VGroup()
            labels = VGroup()
            
            for n in range(1, 6):
                y_pos = -2 + 0.6 * (n**2 - 1) / 4
                level = Line(
                    [level_start_x, y_pos, 0],
                    [level_start_x + level_length, y_pos, 0],
                    color=BLUE,
                    stroke_width=3
                )
                label = MathTex(f"n={n}", font_size=28).next_to(level, RIGHT, buff=0.3)
                
                levels.add(level)
                labels.add(label)
            
            self.play(Create(levels), Write(labels))
        
        with self.voiceover(text="The lowest energy level, n equals one, is called the ground state. Even in the ground state, the particle has non-zero energy. This is the zero-point energy, a purely quantum mechanical effect.") as tracker:
            ground_state_box = SurroundingRectangle(levels[0], color=YELLOW, buff=0.1)
            ground_label = Text("Ground State (Zero-point energy)", font_size=24, color=YELLOW)
            ground_label.next_to(ground_state_box, DOWN, buff=0.4)
            
            self.play(Create(ground_state_box), Write(ground_label))
            self.wait(1)
            self.play(FadeOut(ground_state_box), FadeOut(ground_label))
        
        with self.voiceover(text="Classical mechanics would allow the particle to have zero energy, sitting still at the bottom. But quantum mechanics forbids this. The uncertainty principle ensures the particle always has some kinetic energy.") as tracker:
            self.wait()
        
        self.play(FadeOut(*self.mobjects))

    def harmonic_oscillator(self):
        with self.voiceover(text="Another fundamental quantum system is the harmonic oscillator. This models atoms in molecules, vibrations of crystals, and even quantum fields. The potential energy is proportional to the square of displacement.") as tracker:
            section_title = Text("Quantum Harmonic Oscillator", font_size=38, color=BLUE)
            section_title.to_edge(UP)
            self.play(Write(section_title))
        
        with self.voiceover(text="The potential is V of x equals one-half m omega-squared x-squared, where omega is the angular frequency of oscillation. This is a parabolic potential well.") as tracker:
            potential = MathTex(
                r"V(x) = \frac{1}{2}m\omega^2 x^2",
                font_size=42
            )
            potential.shift(UP * 2.2)
            self.play(Write(potential))
            
            # Plot parabolic potential
            axes = Axes(
                x_range=[-3, 3, 1],
                y_range=[0, 3, 1],
                x_length=7,
                y_length=3,
                axis_config={"color": WHITE}
            )
            axes.shift(DOWN * 0.5)
            
            parabola = axes.plot(
                lambda x: 0.3 * x**2,
                x_range=[-2.8, 2.8],
                color=RED
            )
            
            x_label = axes.get_x_axis_label("x")
            v_label = Text("V(x)", font_size=28).next_to(axes.get_y_axis(), UP)
            
            self.play(Create(axes), Create(parabola), Write(x_label), Write(v_label))
        
        with self.voiceover(text="The Schrödinger equation for the harmonic oscillator can be solved exactly. The energy levels are equally spaced, unlike the particle in a box. The allowed energies are E-n equals h-bar omega times the quantity n plus one-half.") as tracker:
            energy_eq = MathTex(
                r"E_n = \hbar\omega\left(n + \frac{1}{2}\right), \quad n = 0, 1, 2, \ldots",
                font_size=36
            )
            energy_eq.shift(DOWN * 2.7)
            self.play(Write(energy_eq))
        
        self.play(FadeOut(energy_eq))
        
        with self.voiceover(text="Let me show the first few energy levels superimposed on the potential. Each level is equally spaced by h-bar omega. Notice the ground state n equals zero has energy one-half h-bar omega, again showing zero-point energy.") as tracker:
            # Add energy levels
            for n in range(4):
                e_n = 0.5 + n * 0.6
                level_line = Line(
                    axes.c2p(-2.5, e_n),
                    axes.c2p(2.5, e_n),
                    color=YELLOW,
                    stroke_width=2
                )
                level_label = MathTex(f"n={n}", font_size=22, color=YELLOW).next_to(level_line, RIGHT, buff=0.1)
                
                self.play(Create(level_line), Write(level_label), run_time=0.6)
        
        with self.voiceover(text="The wave functions for the harmonic oscillator are products of Gaussian functions and Hermite polynomials. The ground state is a simple Gaussian, perfectly centered in the potential well.") as tracker:
            # Ground state wave function
            ground_wave = axes.plot(
                lambda x: 1.5 * np.exp(-0.5 * x**2) + 0.5,
                x_range=[-2.8, 2.8],
                color=BLUE
            )
            ground_label = MathTex(r"\psi_0", font_size=28, color=BLUE).next_to(axes.c2p(2, 1.5), RIGHT)
            
            self.play(Create(ground_wave), Write(ground_label))
        
        with self.voiceover(text="Higher energy states have more oscillations. The number of nodes in the wave function equals the quantum number n. This is a general pattern in quantum mechanics.") as tracker:
            self.wait()
        
        self.play(FadeOut(*self.mobjects))

    def probability_current(self):
        with self.voiceover(text="An important concept related to probability is the probability current. This describes how probability flows through space, ensuring that probability is conserved over time.") as tracker:
            section_title = Text("Probability Current", font_size=40, color=BLUE)
            section_title.to_edge(UP)
            self.play(Write(section_title))
        
        with self.voiceover(text="The probability current density is defined as j equals h-bar over m times the imaginary part of psi-star times the gradient of psi. This is a vector quantity pointing in the direction of probability flow.") as tracker:
            current = MathTex(
                r"\mathbf{j} = \frac{\hbar}{m}\text{Im}(\psi^*\nabla\psi)",
                font_size=42
            )
            current.shift(UP * 1.8)
            self.play(Write(current))
        
        with self.voiceover(text="The probability density and current satisfy a continuity equation: the partial derivative of rho with respect to time plus the divergence of j equals zero. This is exactly like the continuity equation for fluid flow or electric charge.") as tracker:
            continuity = MathTex(
                r"\frac{\partial \rho}{\partial t} + \nabla \cdot \mathbf{j} = 0",
                font_size=42
            )
            continuity.shift(UP * 0.3)
            self.play(Write(continuity))
        
        with self.voiceover(text="This equation guarantees that probability is neither created nor destroyed. If probability decreases in one region, it must increase somewhere else. Total probability is conserved, as it must be in a consistent physical theory.") as tracker:
            conservation_text = Text("Conservation of Probability", font_size=32, color=YELLOW)
            conservation_text.shift(DOWN * 1.2)
            self.play(Write(conservation_text))
        
        with self.voiceover(text="For stationary states, solutions of the time-independent equation, the probability current is zero everywhere. These states have time-independent probability distributions. However, for superpositions of different energy states, the current is generally non-zero.") as tracker:
            stationary_note = Text("Stationary states: j = 0", font_size=28)
            stationary_note.shift(DOWN * 2.2)
            self.play(Write(stationary_note))
        
        self.play(FadeOut(*self.mobjects))

    def uncertainty_principle(self):
        with self.voiceover(text="The Schrödinger equation is intimately connected to Heisenberg's uncertainty principle. This principle states that certain pairs of physical quantities cannot be simultaneously known with arbitrary precision.") as tracker:
            section_title = Text("Connection to Uncertainty Principle", font_size=36, color=BLUE)
            section_title.to_edge(UP)
            self.play(Write(section_title))
        
        with self.voiceover(text="The most famous example is position and momentum. The uncertainty principle states that delta x times delta p is greater than or equal to h-bar over two, where delta represents the standard deviation.") as tracker:
            uncertainty = MathTex(
                r"\Delta x \cdot \Delta p \geq \frac{\hbar}{2}",
                font_size=48
            )
            uncertainty.shift(UP * 1.5)
            self.play(Write(uncertainty))
        
        with self.voiceover(text="This is not a statement about measurement limitations or experimental error. It's a fundamental property of quantum states themselves. A wave function that is highly localized in position must have a broad distribution in momentum, and vice versa.") as tracker:
            explanation = Text(
                "Fundamental quantum property,\nnot measurement limitation",
                font_size=28,
                line_spacing=1.5
            )
            explanation.shift(UP * 0.2)
            self.play(Write(explanation))
        
        with self.voiceover(text="Let me visualize this. Here's a wave function that is very localized in position. It's a narrow wave packet centered at x equals zero.") as tracker:
            self.play(FadeOut(explanation))
            
            # Position space
            axes_x = Axes(
                x_range=[-4, 4, 2],
                y_range=[0, 1.2, 0.5],
                x_length=6,
                y_length=2,
                axis_config={"color": WHITE}
            )
            axes_x.shift(UP * 0.5)
            
            # Narrow wave packet in position
            narrow_psi = axes_x.plot(
                lambda x: np.exp(-4 * x**2),
                x_range=[-2, 2],
                color=BLUE
            )
            
            x_label = axes_x.get_x_axis_label("x")
            psi_x_label = MathTex(r"|\psi(x)|^2", font_size=28).next_to(axes_x, UP).shift(LEFT * 2)
            
            small_delta_x = Text("Small Δx", font_size=26, color=YELLOW).next_to(axes_x, DOWN, buff=0.8)
            
            self.play(Create(axes_x), Create(narrow_psi), Write(x_label), Write(psi_x_label), Write(small_delta_x))
        
        with self.voiceover(text="When we calculate the momentum distribution for this state, which involves the Fourier transform of the wave function, we get a broad distribution. The momentum is highly uncertain.") as tracker:
            # Momentum space
            axes_p = Axes(
                x_range=[-4, 4, 2],
                y_range=[0, 1.2, 0.5],
                x_length=6,
                y_length=2,
                axis_config={"color": WHITE}
            )
            axes_p.shift(DOWN * 1.8)
            
            # Broad distribution in momentum
            broad_phi = axes_p.plot(
                lambda p: 0.5 * np.exp(-0.15 * p**2),
                x_range=[-4, 4],
                color=RED
            )
            
            p_label = axes_p.get_x_axis_label("p")
            phi_p_label = MathTex(r"|\phi(p)|^2", font_size=28).next_to(axes_p, UP).shift(LEFT * 2)
            
            large_delta_p = Text("Large Δp", font_size=26, color=YELLOW).next_to(axes_p, DOWN, buff=0.5)
            
            self.play(Create(axes_p), Create(broad_phi), Write(p_label), Write(phi_p_label), Write(large_delta_p))
        
        with self.voiceover(text="This reciprocal relationship is built into the mathematical structure of the Schrödinger equation. The momentum operator involves a derivative, which spreads out localized functions. You cannot beat the uncertainty principle.") as tracker:
            self.wait()
        
        self.play(FadeOut(*self.mobjects))

    def conclusion(self):
        with self.voiceover(text="We've covered a lot of ground in this exploration of the Schrödinger equation. Let's recap the key points we've learned.") as tracker:
            section_title = Text("Conclusion", font_size=48, color=BLUE)
            section_title.to_edge(UP)
            self.play(Write(section_title))
        
        with self.voiceover(text="First, the Schrödinger equation is the fundamental equation governing quantum mechanics. It describes how the wave function, which contains all information about a quantum system, evolves in time.") as tracker:
            point1 = Text("• Schrödinger equation governs quantum evolution", font_size=28)
            point1.shift(UP * 1.5 + LEFT * 0.5)
            self.play(Write(point1))
        
        with self.voiceover(text="Second, the wave function itself is not directly observable, but its absolute value squared gives the probability density. This probabilistic interpretation is at the heart of quantum mechanics.") as tracker:
            point2 = Text("• |ψ|² gives probability density", font_size=28)
            point2.next_to(point1, DOWN, buff=0.5, aligned_edge=LEFT)
            self.play(Write(point2))
        
        with self.voiceover(text="Third, for time-independent potentials, we can solve the time-independent Schrödinger equation to find stationary states and energy eigenvalues. Many systems exhibit quantized energy levels.") as tracker:
            point3 = Text("• Energy quantization in bound systems", font_size=28)
            point3.next_to(point2, DOWN, buff=0.5, aligned_edge=LEFT)
            self.play(Write(point3))
        
        with self.voiceover(text="Fourth, the wave function must satisfy normalization and continuity conditions. These mathematical requirements ensure physical predictions make sense.") as tracker:
            point4 = Text("• Wave functions must be normalized and continuous", font_size=28)
            point4.next_to(point3, DOWN, buff=0.5, aligned_edge=LEFT)
            self.play(Write(point4))
        
        with self.voiceover(text="Fifth, the uncertainty principle is a direct consequence of the wave nature of quantum particles. Position and momentum cannot both be precisely determined simultaneously.") as tracker:
            point5 = Text("• Uncertainty principle is fundamental", font_size=28)
            point5.next_to(point4, DOWN, buff=0.5, aligned_edge=LEFT)
            self.play(Write(point5))
        
        with self.voiceover(text="The Schrödinger equation has been extraordinarily successful. It explains atomic structure, chemical bonding, semiconductor physics, superconductivity, and countless other phenomena. It's one of the greatest achievements in the history of science.") as tracker:
            self.wait()
        
        with self.voiceover(text="Thank you for watching this deep dive into the Schrödinger equation. I hope you now have a better understanding of how quantum mechanics describes the microscopic world. Keep exploring, keep questioning, and remember: the universe is far stranger and more beautiful than we can imagine!") as tracker:
            self.play(FadeOut(point1), FadeOut(point2), FadeOut(point3), FadeOut(point4), FadeOut(point5))
            
            final_message = Text(
                "Thank you for watching!\nKeep exploring quantum mechanics!",
                font_size=36,
                color=BLUE,
                line_spacing=1.5
            )
            self.play(Write(final_message))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

# Instructions to run:
# 1. Save this file as schrodinger_animation.py
# 2. Make sure you have manim and manim-voiceover installed
# 3. Set up your ElevenLabs API key
# 4. Run: manim -pqh schrodinger_animation.py SchrodingerEquationExplanation
