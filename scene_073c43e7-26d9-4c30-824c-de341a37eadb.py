from manim import *
from manim_voiceover import VoiceoverScene
from manimator.services import ElevenLabsService

class SchrodingerEquationExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(ElevenLabsService(voice_id="Rachel"))

        # Introduction
        self.introduction()
        
        # What is the Schrödinger Equation?
        self.what_is_schrodinger_equation()
        
        # Wave Functions
        self.explain_wave_functions()
        
        # Probability Density
        self.explain_probability_density()
        
        # Time-Independent Schrödinger Equation
        self.time_independent_schrodinger()
        
        # Physical Interpretation
        self.physical_interpretation()
        
        # Particle in a Box Example
        self.particle_in_box()
        
        # Conclusion
        self.conclusion()

    def introduction(self):
        with self.voiceover(text="Welcome to this deep dive into one of the most fundamental equations in quantum mechanics: the Schrödinger equation.") as tracker:
            title = Text("The Schrödinger Equation", font_size=48, color=BLUE, weight=BOLD)
            subtitle = Text("Wave Functions and Probability Density", font_size=28, color=WHITE)
            subtitle.next_to(title, DOWN, buff=0.5)
            
            self.play(Write(title))
            self.play(FadeIn(subtitle, shift=UP))
            
        with self.voiceover(text="This equation describes how quantum systems evolve over time and helps us understand the probabilistic nature of particles at the quantum scale.") as tracker:
            self.wait(1)
            
        self.play(FadeOut(title), FadeOut(subtitle))

    def what_is_schrodinger_equation(self):
        with self.voiceover(text="Let's start with the time-dependent Schrödinger equation. This is the master equation of quantum mechanics.") as tracker:
            section_title = Text("The Schrödinger Equation", font_size=36, color=BLUE)
            section_title.to_edge(UP)
            self.play(Write(section_title))
            
        with self.voiceover(text="The equation reads: i times h-bar times the partial derivative of psi with respect to time equals the Hamiltonian operator acting on psi.") as tracker:
            schrodinger_eq = MathTex(
                r"i\hbar \frac{\partial \psi}{\partial t} = \hat{H} \psi",
                font_size=60
            )
            schrodinger_eq.move_to(ORIGIN)
            self.play(Write(schrodinger_eq))
            
        with self.voiceover(text="Let's break down each component. i is the imaginary unit, h-bar is the reduced Planck constant, and psi is the wave function we're solving for.") as tracker:
            # Highlight components
            i_box = SurroundingRectangle(schrodinger_eq[0][0], color=YELLOW, buff=0.1)
            hbar_box = SurroundingRectangle(schrodinger_eq[0][1], color=GREEN, buff=0.1)
            psi_box = SurroundingRectangle(schrodinger_eq[0][3:6], color=RED, buff=0.1)
            
            i_label = Text("Imaginary unit", font_size=20, color=YELLOW).next_to(i_box, DOWN, buff=0.3)
            hbar_label = Text("Reduced Planck constant", font_size=20, color=GREEN).next_to(hbar_box, DOWN, buff=0.6)
            psi_label = Text("Wave function", font_size=20, color=RED).next_to(psi_box, DOWN, buff=0.9)
            
            self.play(Create(i_box), Write(i_label))
            self.wait(0.5)
            self.play(Create(hbar_box), Write(hbar_label))
            self.wait(0.5)
            self.play(Create(psi_box), Write(psi_label))
            
        with self.voiceover(text="The Hamiltonian operator, H-hat, represents the total energy of the system, combining kinetic and potential energy.") as tracker:
            self.play(FadeOut(i_box), FadeOut(hbar_box), FadeOut(psi_box),
                     FadeOut(i_label), FadeOut(hbar_label), FadeOut(psi_label))
            
            hamiltonian_box = SurroundingRectangle(schrodinger_eq[0][9:11], color=BLUE, buff=0.1)
            hamiltonian_label = Text("Hamiltonian (Total Energy)", font_size=20, color=BLUE)
            hamiltonian_label.next_to(hamiltonian_box, DOWN, buff=0.3)
            
            self.play(Create(hamiltonian_box), Write(hamiltonian_label))
            
        with self.voiceover(text="The Hamiltonian can be expanded as the sum of the kinetic energy operator and the potential energy operator.") as tracker:
            self.play(FadeOut(hamiltonian_box), FadeOut(hamiltonian_label))
            self.play(schrodinger_eq.animate.shift(UP * 1.5))
            
            hamiltonian_expanded = MathTex(
                r"\hat{H} = \frac{-\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x)",
                font_size=50
            )
            hamiltonian_expanded.next_to(schrodinger_eq, DOWN, buff=0.8)
            self.play(Write(hamiltonian_expanded))
            
            kinetic_label = Text("Kinetic Energy", font_size=18, color=YELLOW)
            potential_label = Text("Potential Energy", font_size=18, color=GREEN)
            kinetic_label.next_to(hamiltonian_expanded, DOWN, buff=0.5).shift(LEFT * 2)
            potential_label.next_to(hamiltonian_expanded, DOWN, buff=0.5).shift(RIGHT * 2)
            
            kinetic_arrow = Arrow(kinetic_label.get_top(), hamiltonian_expanded[0][2:9].get_bottom(), color=YELLOW, buff=0.1)
            potential_arrow = Arrow(potential_label.get_top(), hamiltonian_expanded[0][10:].get_bottom(), color=GREEN, buff=0.1)
            
            self.play(Write(kinetic_label), Create(kinetic_arrow))
            self.wait(0.5)
            self.play(Write(potential_label), Create(potential_arrow))
            
        self.play(FadeOut(*self.mobjects))

    def explain_wave_functions(self):
        with self.voiceover(text="Now let's explore what a wave function actually is. The wave function, psi, is a complex-valued function that contains all the information about a quantum system.") as tracker:
            section_title = Text("Wave Functions", font_size=36, color=BLUE)
            section_title.to_edge(UP)
            self.play(Write(section_title))
            
        with self.voiceover(text="For a particle in one dimension, the wave function depends on position x and time t. It's written as psi of x and t.") as tracker:
            wave_function_def = MathTex(r"\psi(x, t)", font_size=70)
            wave_function_def.move_to(ORIGIN)
            self.play(Write(wave_function_def))
            
        with self.voiceover(text="The wave function itself is not directly observable. However, it contains complete information about the quantum state of the particle.") as tracker:
            self.play(wave_function_def.animate.shift(UP * 2).scale(0.7))
            
            info_text = Text("Contains all quantum information", font_size=24, color=YELLOW)
            info_text.next_to(wave_function_def, DOWN, buff=0.5)
            self.play(FadeIn(info_text))
            
        with self.voiceover(text="Let's visualize a simple wave function. Here we see the real part of a wave packet, oscillating in space.") as tracker:
            self.play(FadeOut(wave_function_def), FadeOut(info_text))
            
            axes = Axes(
                x_range=[-6, 6, 1],
                y_range=[-1.5, 1.5, 0.5],
                x_length=10,
                y_length=4,
                axis_config={"color": WHITE}
            )
            axes.move_to(ORIGIN)
            
            x_label = axes.get_x_axis_label(r"x", edge=RIGHT, direction=RIGHT, buff=0.2)
            y_label = axes.get_y_axis_label(r"\text{Re}(\psi)", edge=UP, direction=UP, buff=0.2)
            
            self.play(Create(axes), Write(x_label), Write(y_label))
            
        with self.voiceover(text="This wave function represents a Gaussian wave packet. Notice how it oscillates while maintaining a localized envelope.") as tracker:
            # Create wave function: Gaussian envelope with oscillation
            wave = axes.plot(
                lambda x: np.exp(-0.3 * x**2) * np.cos(3 * x),
                color=BLUE,
                x_range=[-6, 6]
            )
            
            wave_label = MathTex(r"\psi(x) = e^{-\alpha x^2} \cos(kx)", font_size=36, color=BLUE)
            wave_label.next_to(axes, UP, buff=0.3)
            
            self.play(Create(wave), Write(wave_label))
            
        with self.voiceover(text="The wave function can also have an imaginary part. In quantum mechanics, both the real and imaginary components are essential.") as tracker:
            imaginary_wave = axes.plot(
                lambda x: np.exp(-0.3 * x**2) * np.sin(3 * x),
                color=RED,
                x_range=[-6, 6]
            )
            
            imag_label = MathTex(r"\text{Im}(\psi)", font_size=24, color=RED)
            imag_label.next_to(wave_label, DOWN, buff=0.3)
            
            self.play(Create(imaginary_wave), Write(imag_label))
            
        self.play(FadeOut(*self.mobjects))

    def explain_probability_density(self):
        with self.voiceover(text="While the wave function itself is not directly measurable, we can extract physical predictions from it through the probability density.") as tracker:
            section_title = Text("Probability Density", font_size=36, color=BLUE)
            section_title.to_edge(UP)
            self.play(Write(section_title))
            
        with self.voiceover(text="The probability density is given by the absolute square of the wave function: the magnitude of psi squared.") as tracker:
            prob_density_eq = MathTex(
                r"P(x, t) = |\psi(x, t)|^2 = \psi^*(x, t) \psi(x, t)",
                font_size=50
            )
            prob_density_eq.next_to(section_title, DOWN, buff=0.8)
            self.play(Write(prob_density_eq))
            
        with self.voiceover(text="This quantity tells us the probability of finding the particle at a particular position x at time t.") as tracker:
            interpretation = Text(
                "Probability of finding particle at position x",
                font_size=24,
                color=YELLOW
            )
            interpretation.next_to(prob_density_eq, DOWN, buff=0.6)
            self.play(FadeIn(interpretation))
            
        with self.voiceover(text="Let's visualize this. Here we have our wave function again, and below it, the corresponding probability density.") as tracker:
            self.play(FadeOut(prob_density_eq), FadeOut(interpretation))
            self.play(section_title.animate.scale(0.8).to_edge(UP, buff=0.2))
            
            # Create axes for wave function
            axes_wave = Axes(
                x_range=[-6, 6, 2],
                y_range=[-1.2, 1.2, 0.5],
                x_length=9,
                y_length=2.5,
                axis_config={"color": WHITE}
            )
            axes_wave.shift(UP * 1.5)
            
            wave_label_axis = Text("Wave Function ψ(x)", font_size=20, color=BLUE)
            wave_label_axis.next_to(axes_wave, LEFT, buff=0.3)
            
            self.play(Create(axes_wave), Write(wave_label_axis))
            
        with self.voiceover(text="The blue curve shows the real part of the wave function oscillating within its envelope.") as tracker:
            wave = axes_wave.plot(
                lambda x: np.exp(-0.3 * x**2) * np.cos(3 * x),
                color=BLUE,
                x_range=[-6, 6]
            )
            self.play(Create(wave))
            
        with self.voiceover(text="Now, when we take the absolute square of this wave function, we get the probability density shown below.") as tracker:
            # Create axes for probability density
            axes_prob = Axes(
                x_range=[-6, 6, 2],
                y_range=[0, 1.2, 0.5],
                x_length=9,
                y_length=2.5,
                axis_config={"color": WHITE}
            )
            axes_prob.shift(DOWN * 1.5)
            
            prob_label_axis = Text("Probability Density |ψ|²", font_size=20, color=ORANGE)
            prob_label_axis.next_to(axes_prob, LEFT, buff=0.3)
            
            self.play(Create(axes_prob), Write(prob_label_axis))
            
            prob_density = axes_prob.plot(
                lambda x: np.exp(-0.6 * x**2) * (np.cos(3 * x))**2,
                color=ORANGE,
                x_range=[-6, 6]
            )
            self.play(Create(prob_density))
            
        with self.voiceover(text="Notice that the probability density is always positive or zero, never negative. The oscillations in the wave function create a modulated probability distribution.") as tracker:
            self.wait(1)
            
        with self.voiceover(text="An important property is normalization. The total probability of finding the particle somewhere must equal one.") as tracker:
            normalization_eq = MathTex(
                r"\int_{-\infty}^{\infty} |\psi(x, t)|^2 \, dx = 1",
                font_size=40
            )
            normalization_eq.to_edge(DOWN, buff=0.5)
            self.play(Write(normalization_eq))
            
        self.play(FadeOut(*self.mobjects))

    def time_independent_schrodinger(self):
        with self.voiceover(text="For many problems, we use the time-independent Schrödinger equation. This applies when the potential energy doesn't change with time.") as tracker:
            section_title = Text("Time-Independent Schrödinger Equation", font_size=32, color=BLUE)
            section_title.to_edge(UP)
            self.play(Write(section_title))
            
        with self.voiceover(text="We can separate the time and space parts of the wave function. The spatial part satisfies this eigenvalue equation.") as tracker:
            time_indep_eq = MathTex(
                r"\hat{H} \psi(x) = E \psi(x)",
                font_size=60
            )
            time_indep_eq.move_to(ORIGIN + UP * 0.5)
            self.play(Write(time_indep_eq))
            
        with self.voiceover(text="Where E is the energy eigenvalue. This equation tells us that the Hamiltonian operator acting on the wave function gives back the same wave function multiplied by its energy.") as tracker:
            e_label = Text("Energy eigenvalue", font_size=22, color=YELLOW)
            e_label.next_to(time_indep_eq, DOWN, buff=0.5)
            e_arrow = Arrow(e_label.get_top(), time_indep_eq[0][6].get_bottom(), color=YELLOW, buff=0.1)
            self.play(Write(e_label), Create(e_arrow))
            
        with self.voiceover(text="Expanding the Hamiltonian, we get the full form with kinetic and potential energy terms.") as tracker:
            self.play(FadeOut(e_label), FadeOut(e_arrow))
            self.play(time_indep_eq.animate.shift(UP * 1.2))
            
            expanded_eq = MathTex(
                r"\frac{-\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V(x)\psi(x) = E\psi(x)",
                font_size=48
            )
            expanded_eq.next_to(time_indep_eq, DOWN, buff=0.7)
            self.play(Write(expanded_eq))
            
        with self.voiceover(text="This is a differential equation we can solve for different potential energy functions V of x. The solutions give us the allowed energy levels and corresponding wave functions.") as tracker:
            self.wait(1)
            
        self.play(FadeOut(*self.mobjects))

    def physical_interpretation(self):
        with self.voiceover(text="Let's understand the physical meaning behind these mathematical expressions. The wave function describes quantum superposition.") as tracker:
            section_title = Text("Physical Interpretation", font_size=36, color=BLUE)
            section_title.to_edge(UP)
            self.play(Write(section_title))
            
        with self.voiceover(text="Unlike classical particles which have definite positions, quantum particles exist in a superposition of many possible positions simultaneously.") as tracker:
            classical_text = Text("Classical Particle", font_size=24, color=RED)
            classical_text.shift(LEFT * 3.5 + UP * 1.5)
            
            quantum_text = Text("Quantum Particle", font_size=24, color=BLUE)
            quantum_text.shift(RIGHT * 3.5 + UP * 1.5)
            
            self.play(Write(classical_text), Write(quantum_text))
            
        with self.voiceover(text="A classical particle has a definite position, represented by a single point.") as tracker:
            classical_line = Line(LEFT * 5.5 + UP * 0.2, LEFT * 1.5 + UP * 0.2, color=WHITE)
            classical_dot = Dot(LEFT * 3.5 + UP * 0.2, color=RED, radius=0.15)
            
            self.play(Create(classical_line), Create(classical_dot))
            
        with self.voiceover(text="A quantum particle, however, is described by a wave function spread over space. The particle doesn't have a single definite position until measured.") as tracker:
            axes_quantum = Axes(
                x_range=[-2, 2, 1],
                y_range=[0, 1.2, 0.5],
                x_length=4,
                y_length=2,
                axis_config={"color": WHITE, "include_tip": False}
            )
            axes_quantum.shift(RIGHT * 3.5 + DOWN * 0.5)
            
            quantum_wave = axes_quantum.plot(
                lambda x: np.exp(-1.5 * x**2),
                color=BLUE,
                x_range=[-2, 2]
            )
            
            self.play(Create(axes_quantum), Create(quantum_wave))
            
        with self.voiceover(text="The height of the wave function squared at each point gives the probability of finding the particle there upon measurement.") as tracker:
            # Add shading under curve
            area = axes_quantum.get_area(quantum_wave, x_range=[-2, 2], color=BLUE, opacity=0.3)
            self.play(FadeIn(area))
            
        with self.voiceover(text="This probabilistic interpretation is fundamentally different from classical physics and is one of the key features of quantum mechanics.") as tracker:
            self.wait(1)
            
        self.play(FadeOut(*self.mobjects))

    def particle_in_box(self):
        with self.voiceover(text="Let's apply these concepts to a concrete example: a particle in a one-dimensional box. This is one of the simplest quantum systems.") as tracker:
            section_title = Text("Example: Particle in a Box", font_size=36, color=BLUE)
            section_title.to_edge(UP)
            self.play(Write(section_title))
            
        with self.voiceover(text="Imagine a particle confined between two walls at x equals zero and x equals L. Inside the box, the potential is zero. Outside, it's infinite.") as tracker:
            # Draw the box
            box_width = 6
            box_height = 3
            
            left_wall = Line(LEFT * box_width/2 + DOWN * box_height/2, 
                           LEFT * box_width/2 + UP * box_height/2, 
                           color=WHITE, stroke_width=8)
            right_wall = Line(RIGHT * box_width/2 + DOWN * box_height/2, 
                            RIGHT * box_width/2 + UP * box_height/2, 
                            color=WHITE, stroke_width=8)
            bottom = Line(LEFT * box_width/2 + DOWN * box_height/2, 
                         RIGHT * box_width/2 + DOWN * box_height/2, 
                         color=WHITE, stroke_width=4)
            
            label_0 = MathTex("x = 0", font_size=24).next_to(left_wall, DOWN, buff=0.3)
            label_L = MathTex("x = L", font_size=24).next_to(right_wall, DOWN, buff=0.3)
            
            v_inside = MathTex("V = 0", font_size=28, color=GREEN).move_to(ORIGIN)
            v_outside_left = MathTex("V = \infty", font_size=24, color=RED).next_to(left_wall, LEFT, buff=0.5)
            v_outside_right = MathTex("V = \infty", font_size=24, color=RED).next_to(right_wall, RIGHT, buff=0.5)
            
            self.play(Create(left_wall), Create(right_wall), Create(bottom))
            self.play(Write(label_0), Write(label_L))
            self.play(Write(v_inside), Write(v_outside_left), Write(v_outside_right))
            
        with self.voiceover(text="Since the potential is infinite at the walls, the wave function must be zero there. Inside, we solve the Schrödinger equation.") as tracker:
            self.play(FadeOut(v_inside), FadeOut(v_outside_left), FadeOut(v_outside_right))
            
            boundary_conditions = MathTex(r"\psi(0) = 0, \quad \psi(L) = 0", font_size=36)
            boundary_conditions.next_to(section_title, DOWN, buff=0.4)
            self.play(Write(boundary_conditions))
            
        with self.voiceover(text="The solutions are standing waves, similar to waves on a vibrating string. The allowed wave functions are sine functions.") as tracker:
            self.play(FadeOut(boundary_conditions))
            
            solution_eq = MathTex(
                r"\psi_n(x) = \sqrt{\frac{2}{L}} \sin\left(\frac{n\pi x}{L}\right)",
                font_size=40
            )
            solution_eq.next_to(section_title, DOWN, buff=0.4)
            self.play(Write(solution_eq))
            
        with self.voiceover(text="Let's visualize the first three energy levels. n equals one is the ground state, the lowest energy configuration.") as tracker:
            self.play(solution_eq.animate.scale(0.7).to_edge(UP, buff=1.2))
            
            # Create axes for wave functions
            axes = Axes(
                x_range=[0, 6, 1],
                y_range=[-1.5, 1.5, 0.5],
                x_length=box_width,
                y_length=2.5,
                axis_config={"color": WHITE, "include_tip": False}
            )
            axes.move_to(ORIGIN + DOWN * 0.3)
            
            # n=1 ground state
            wave_n1 = axes.plot(
                lambda x: np.sqrt(2/6) * np.sin(np.pi * x / 6),
                color=BLUE,
                x_range=[0, 6]
            )
            
            n1_label = MathTex("n = 1", font_size=30, color=BLUE)
            n1_label.next_to(axes, DOWN, buff=0.5).shift(LEFT * 2)
            
            self.play(FadeOut(left_wall), FadeOut(right_wall), FadeOut(bottom),
                     FadeOut(label_0), FadeOut(label_L))
            self.play(Create(axes))
            self.play(Create(wave_n1), Write(n1_label))
            
        with self.voiceover(text="The second energy level, n equals two, has one node in the middle where the wave function crosses zero.") as tracker:
            wave_n2 = axes.plot(
                lambda x: np.sqrt(2/6) * np.sin(2 * np.pi * x / 6),
                color=GREEN,
                x_range=[0, 6]
            )
            
            n2_label = MathTex("n = 2", font_size=30, color=GREEN)
            n2_label.next_to(n1_label, RIGHT, buff=1.5)
            
            self.play(Transform(wave_n1, wave_n2), Transform(n1_label, n2_label))
            
        with self.voiceover(text="The third level, n equals three, has two nodes. Higher n means more nodes and higher energy.") as tracker:
            wave_n3 = axes.plot(
                lambda x: np.sqrt(2/6) * np.sin(3 * np.pi * x / 6),
                color=RED,
                x_range=[0, 6]
            )
            
            n3_label = MathTex("n = 3", font_size=30, color=RED)
            n3_label.next_to(n2_label, RIGHT, buff=1.5)
            
            self.play(Transform(wave_n1, wave_n3), Transform(n1_label, n3_label))
            
        with self.voiceover(text="The energy levels are quantized, meaning only specific discrete energies are allowed. The energy formula is shown here.") as tracker:
            self.play(FadeOut(wave_n1), FadeOut(n1_label), FadeOut(axes))
            
            energy_eq = MathTex(
                r"E_n = \frac{n^2 \pi^2 \hbar^2}{2mL^2}, \quad n = 1, 2, 3, \ldots",
                font_size=44
            )
            energy_eq.move_to(ORIGIN)
            self.play(Write(energy_eq))
            
        with self.voiceover(text="Notice that the energy is proportional to n squared. This means energy levels get further apart as n increases. This quantization is a fundamental feature of confined quantum systems.") as tracker:
            self.wait(1)
            
        self.play(FadeOut(*self.mobjects))

    def conclusion(self):
        with self.voiceover(text="Let's summarize what we've learned about the Schrödinger equation and its physical meaning.") as tracker:
            title = Text("Summary", font_size=42, color=BLUE, weight=BOLD)
            title.to_edge(UP)
            self.play(Write(title))
            
        with self.voiceover(text="First, the Schrödinger equation is the fundamental equation governing quantum mechanical systems. It describes how wave functions evolve in time.") as tracker:
            point1 = Text("• Schrödinger equation governs quantum systems", font_size=26)
            point1.next_to(title, DOWN, buff=0.8).to_edge(LEFT, buff=1)
            self.play(FadeIn(point1, shift=RIGHT))
            
        with self.voiceover(text="Second, the wave function contains complete information about a quantum system, but is not directly observable.") as tracker:
            point2 = Text("• Wave function ψ contains all quantum information", font_size=26)
            point2.next_to(point1, DOWN, buff=0.4).align_to(point1, LEFT)
            self.play(FadeIn(point2, shift=RIGHT))
            
        with self.voiceover(text="Third, the probability density, given by the absolute square of the wave function, tells us where we're likely to find the particle.") as tracker:
            point3 = Text("• Probability density |ψ|² gives measurement probabilities", font_size=26)
            point3.next_to(point2, DOWN, buff=0.4).align_to(point1, LEFT)
            self.play(FadeIn(point3, shift=RIGHT))
            
        with self.voiceover(text="Fourth, quantum systems exhibit quantization. In confined systems, only discrete energy levels are allowed.") as tracker:
            point4 = Text("• Confined systems have quantized energy levels", font_size=26)
            point4.next_to(point3, DOWN, buff=0.4).align_to(point1, LEFT)
            self.play(FadeIn(point4, shift=RIGHT))
            
        with self.voiceover(text="Finally, quantum mechanics is fundamentally probabilistic. Particles exist in superposition states until measured, unlike classical definite states.") as tracker:
            point5 = Text("• Quantum mechanics is fundamentally probabilistic", font_size=26)
            point5.next_to(point4, DOWN, buff=0.4).align_to(point1, LEFT)
            self.play(FadeIn(point5, shift=RIGHT))
            
        with self.voiceover(text="The Schrödinger equation opened the door to understanding atoms, molecules, and the quantum world. It remains one of the most important equations in all of physics.") as tracker:
            self.wait(1)
            
        with self.voiceover(text="Thank you for watching this exploration of the Schrödinger equation, wave functions, and probability density. I hope this deepened your understanding of quantum mechanics.") as tracker:
            self.play(FadeOut(point1), FadeOut(point2), FadeOut(point3), 
                     FadeOut(point4), FadeOut(point5))
            
            thanks = Text("Thank you for watching!", font_size=40, color=BLUE)
            thanks.move_to(ORIGIN)
            self.play(Write(thanks))
            self.wait(1)
            
        self.play(FadeOut(*self.mobjects))

# Run the animation
if __name__ == "__main__":
    scene = SchrodingerEquationExplanation()
    scene.render()
