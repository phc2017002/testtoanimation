from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class MultivariableCalculusExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        # Section 1: Introduction
        self.introduction()
        
        # Section 2: From Single to Multiple Variables
        self.single_to_multiple_variables()
        
        # Section 3: Partial Derivatives Concept
        self.partial_derivatives_concept()
        
        # Section 4: Partial Derivatives Visualization
        self.partial_derivatives_visualization()
        
        # Section 5: Gradient Vector
        self.gradient_vector_explanation()
        
        # Section 6: Directional Derivatives
        self.directional_derivatives()
        
        # Section 7: Multiple Integration
        self.multiple_integration()
        
        # Section 8: Double Integrals Visualization
        self.double_integrals_visualization()
        
        # Section 9: Chain Rule in Multiple Variables
        self.chain_rule_multivariable()
        
        # Section 10: Applications
        self.applications()
        
        # Section 11: Summary
        self.summary()

    def introduction(self):
        with self.voiceover(text="Welcome to this comprehensive exploration of multivariate calculus. Multivariate calculus extends the concepts of single-variable calculus to functions of multiple variables, opening up a world of applications in physics, engineering, economics, and data science.") as tracker:
            title = Text("Multivariate Calculus", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            subtitle = Text("Functions of Multiple Variables", font_size=32, color=WHITE)
            subtitle.move_to(ORIGIN)
            self.play(FadeIn(subtitle, shift=UP))
        
        with self.voiceover(text="In this presentation, we will explore partial derivatives, gradient vectors, directional derivatives, and multiple integrals. We will visualize these concepts in three-dimensional space to build intuition about how functions behave when they depend on more than one variable.") as tracker:
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def single_to_multiple_variables(self):
        with self.voiceover(text="Let's begin by understanding the transition from single-variable to multivariable functions. In single-variable calculus, we studied functions like f of x, which maps a single input to a single output.") as tracker:
            title = Text("From Single to Multiple Variables", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Single variable function
            single_var = MathTex(r"f(x) = x^2", font_size=36)
            single_var.move_to(UP * 1.5)
            self.play(Write(single_var))
            
            # Create a simple 2D graph
            axes_2d = Axes(
                x_range=[-3, 3, 1],
                y_range=[0, 9, 2],
                x_length=7,
                y_length=4,
                axis_config={"include_tip": True}
            )
            axes_2d.move_to(DOWN * 1.2)
            
            graph_2d = axes_2d.plot(lambda x: x**2, color=YELLOW)
            x_label = axes_2d.get_x_axis_label("x").shift(DOWN * 0.6).shift(DOWN * 0.8)
            y_label = axes_2d.get_y_axis_label("f", direction=LEFT).shift(LEFT * 0.8).shift(LEFT * 0.8)
            
            self.play(Create(axes_2d), Write(x_label), Write(y_label))
            self.play(Create(graph_2d))
        
        with self.voiceover(text="In multivariate calculus, we extend this to functions of two or more variables, such as f of x and y. For example, the function z equals x squared plus y squared creates a paraboloid surface in three-dimensional space.") as tracker:
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Here is an example of a multivariable function. The function f of x comma y equals x squared plus y squared takes two inputs and produces one output, forming a beautiful three-dimensional surface.") as tracker:
            title = Text("Multivariable Function", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            multi_var = MathTex(r"f(x,y) = x^2 + y^2", font_size=36)
            multi_var.to_edge(UP, buff=2.2)
            self.play(Write(multi_var))
            
            # Create 3D axes (smaller to fit)
            axes_3d = ThreeDAxes(
                x_range=[-2, 2, 1],
                y_range=[-2, 2, 1],
                z_range=[0, 8, 2],
                x_length=7,
                y_length=4,
                z_length=3
            )
            axes_3d.move_to(DOWN * 0.8)
            
            # Create surface
            surface = Surface(
                lambda u, v: axes_3d.c2p(u, v, u**2 + v**2),
                u_range=[-2, 2],
                v_range=[-2, 2],
                resolution=(20, 20),
                fill_opacity=0.7,
                checkerboard_colors=[BLUE, BLUE]
            )
            
            self.play(Create(axes_3d))
            self.play(Create(surface))
        
        self.play(FadeOut(*self.mobjects))

    def partial_derivatives_concept(self):
        with self.voiceover(text="Now let's explore partial derivatives, one of the fundamental concepts in multivariate calculus. When we have a function of multiple variables, we can take derivatives with respect to each variable individually, treating all other variables as constants.") as tracker:
            title = Text("Partial Derivatives", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            function = MathTex(r"f(x,y) = x^2 y + xy^2", font_size=36)
            function.move_to(UP * 1.8)
            self.play(Write(function))
        
        with self.voiceover(text="The partial derivative of f with respect to x is denoted by del f del x or f sub x. To compute it, we differentiate with respect to x while treating y as a constant. For our example, the partial derivative with respect to x is two x y plus y squared.") as tracker:
            partial_x_label = Text("Partial derivative with respect to x:", font_size=28)
            partial_x_label.move_to(UP * 0.6)
            self.play(Write(partial_x_label))
            
            partial_x = MathTex(r"\frac{\partial f}{\partial x} = 2xy + y^2", font_size=36)
            partial_x.move_to(ORIGIN)
            self.play(Write(partial_x))
        
        with self.voiceover(text="Similarly, the partial derivative with respect to y treats x as a constant. For our function, the partial derivative with respect to y equals x squared plus two x y. These partial derivatives tell us how the function changes as we move in the x direction or the y direction independently.") as tracker:
            self.wait(1)
            
            partial_y_label = Text("Partial derivative with respect to y:", font_size=28)
            partial_y_label.move_to(DOWN * 1.0)
            self.play(Write(partial_y_label))
            
            partial_y = MathTex(r"\frac{\partial f}{\partial y} = x^2 + 2xy", font_size=36)
            partial_y.move_to(DOWN * 1.8)
            self.play(Write(partial_y))
        
        self.play(FadeOut(*self.mobjects))

    def partial_derivatives_visualization(self):
        with self.voiceover(text="Let's visualize what partial derivatives mean geometrically. Consider the surface z equals x squared plus y squared. The partial derivative with respect to x represents the slope of the surface in the x direction, which we can visualize as a slice through the surface parallel to the x-z plane.") as tracker:
            title = Text("Visualizing Partial Derivatives", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            equation = MathTex(r"z = x^2 + y^2", font_size=36)
            equation.to_edge(UP, buff=2.2)
            self.play(Write(equation))
            
            # Surface visualization
            axes = ThreeDAxes(
                x_range=[-2, 2, 1],
                y_range=[-2, 2, 1],
                z_range=[0, 6, 2],
                x_length=7,
                y_length=4,
                z_length=3
            )
            axes.move_to(DOWN * 1.5)
            
            surface = Surface(
                lambda u, v: axes.c2p(u, v, u**2 + v**2),
                u_range=[-2, 2],
                v_range=[-2, 2],
                resolution=(15, 15),
                fill_opacity=0.6,
                checkerboard_colors=[GREEN, GREEN]
            )
            
            self.play(Create(axes))
            self.play(Create(surface))
        
        with self.voiceover(text="When we fix y equals one and vary x, we get a cross-section of the surface. The partial derivative del z del x at this point gives us the slope of this curve. This represents the instantaneous rate of change of z as we move in the positive x direction while keeping y constant.") as tracker:
            # Highlight a curve on the surface (y = 1)
            curve = ParametricFunction(
                lambda t: axes.c2p(t, 1, t**2 + 1),
                t_range=[-2, 2],
                color=YELLOW,
                stroke_width=6
            )
            self.play(Create(curve))
            
            partial_annotation = MathTex(r"\frac{\partial z}{\partial x}\bigg|_{y=1} = 2x", font_size=32)
            partial_annotation.to_corner(DR, buff=0.5)
            self.play(Write(partial_annotation))
        
        self.play(FadeOut(*self.mobjects))

    def gradient_vector_explanation(self):
        with self.voiceover(text="The gradient is a vector that combines all the partial derivatives of a function. For a function f of x and y, the gradient is denoted as del f or grad f, and it points in the direction of the steepest ascent of the function.") as tracker:
            title = Text("The Gradient Vector", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            function = MathTex(r"f(x,y) = x^2 + y^2", font_size=36)
            function.move_to(UP * 2.0)
            self.play(Write(function))
            
            gradient_def = MathTex(
                r"\nabla f = \left\langle \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \right\rangle",
                font_size=36
            )
            gradient_def.move_to(UP * 0.8)
            self.play(Write(gradient_def))
        
        with self.voiceover(text="For our example function f of x comma y equals x squared plus y squared, we first compute the partial derivatives. The partial derivative with respect to x is two x, and the partial derivative with respect to y is two y. Therefore, the gradient vector is the vector with components two x and two y.") as tracker:
            partials = MathTex(
                r"\frac{\partial f}{\partial x} = 2x, \quad \frac{\partial f}{\partial y} = 2y",
                font_size=32
            )
            partials.move_to(ORIGIN)
            self.play(Write(partials))
            
            gradient = MathTex(r"\nabla f = \langle 2x, 2y \rangle", font_size=36, color=YELLOW)
            gradient.move_to(DOWN * 1.0)
            self.play(Write(gradient))
        
        with self.voiceover(text="The gradient vector has a beautiful geometric interpretation. At any point on the surface, the gradient points in the direction where the function increases most rapidly. The magnitude of the gradient tells us how steep the function is in that direction.") as tracker:
            interpretation = Text("Points in direction of steepest ascent", font_size=24, color=GREEN)
            interpretation.move_to(DOWN * 2.2)
            self.play(Write(interpretation))
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Let's visualize the gradient vector field. Each arrow represents the gradient at that point, showing both the direction and magnitude of the steepest increase. Notice how the arrows point radially outward from the origin, which makes sense because our function grows as we move away from the center.") as tracker:
            title = Text("Gradient Vector Field", font_size=34, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            equation = MathTex(r"f(x,y) = x^2 + y^2", font_size=32)
            equation.move_to(UP * 2.4)
            self.play(Write(equation))
            
            # Create vector field
            plane = NumberPlane(
                x_range=[-3, 3, 1],
                y_range=[-3, 3, 1],
                x_length=7,
                y_length=4
            )
            plane.move_to(DOWN * 1.2)
            
            def gradient_field(pos):
                x, y = pos[0], pos[1]
                return np.array([2*x, 2*y, 0]) * 0.25
            
            vector_field = ArrowVectorField(
                gradient_field,
                x_range=[-2.5, 2.5, 0.8],
                y_range=[-2, 2, 0.8],
                color=YELLOW,
                vector_config={"max_tip_length_to_length_ratio": 0.25, "stroke_width": 3}
            )
            vector_field.move_to(DOWN * 0.2)
            
            self.play(Create(plane))
            self.play(Create(vector_field))
        
        self.play(FadeOut(*self.mobjects))

    def directional_derivatives(self):
        with self.voiceover(text="While partial derivatives tell us the rate of change in the coordinate directions, directional derivatives tell us the rate of change in any direction. The directional derivative of f in the direction of a unit vector u is given by the dot product of the gradient with u.") as tracker:
            title = Text("Directional Derivatives", font_size=34, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            dir_deriv_formula = MathTex(
                r"D_{\mathbf{u}}f = \nabla f \cdot \mathbf{u}",
                font_size=36
            )
            dir_deriv_formula.move_to(UP * 1.5)
            self.play(Write(dir_deriv_formula))
        
        with self.voiceover(text="Let's work through an example. Suppose we have the function f of x comma y equals x squared minus y squared, and we want to find the directional derivative at the point one comma one in the direction of the vector one comma one. First, we need to normalize this direction vector to make it a unit vector.") as tracker:
            example = MathTex(r"f(x,y) = x^2 - y^2", font_size=32)
            example.move_to(UP * 0.5)
            self.play(Write(example))
            
            point = MathTex(r"\text{At point } (1, 1)", font_size=28)
            point.move_to(ORIGIN)
            self.play(Write(point))
            
            direction = MathTex(r"\text{Direction: } \mathbf{v} = \langle 1, 1 \rangle", font_size=28)
            direction.move_to(DOWN * 0.7)
            self.play(Write(direction))
            
            unit_vec = MathTex(
                r"\mathbf{u} = \frac{\mathbf{v}}{|\mathbf{v}|} = \left\langle \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right\rangle",
                font_size=28
            )
            unit_vec.move_to(DOWN * 1.6)
            self.play(Write(unit_vec))
        
        with self.voiceover(text="Next, we compute the gradient of f. The partial derivative with respect to x is two x, and with respect to y is negative two y. At the point one comma one, the gradient equals the vector two comma negative two. Finally, we take the dot product of this gradient with our unit vector to get the directional derivative, which equals zero. This means the function is not changing in this particular direction at this point.") as tracker:
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Let's continue our calculation. The gradient at point one comma one is two comma negative two. Now we compute the dot product with our unit vector one over root two comma one over root two.") as tracker:
            title = Text("Directional Derivative Calculation", font_size=30, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            grad_calc = MathTex(
                r"\nabla f(1,1) = \langle 2(1), -2(1) \rangle = \langle 2, -2 \rangle",
                font_size=32
            )
            grad_calc.move_to(UP * 1.5)
            self.play(Write(grad_calc))
            
            dot_product = MathTex(
                r"D_{\mathbf{u}}f = \langle 2, -2 \rangle \cdot \left\langle \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right\rangle",
                font_size=32
            )
            dot_product.move_to(UP * 0.5)
            self.play(Write(dot_product))
            
            result = MathTex(
                r"= \frac{2}{\sqrt{2}} - \frac{2}{\sqrt{2}} = 0",
                font_size=32,
                color=YELLOW
            )
            result.move_to(DOWN * 0.5)
            self.play(Write(result))
            
            interpretation = Text(
                "The function is not changing in this direction!",
                font_size=24,
                color=GREEN
            )
            interpretation.move_to(DOWN * 1.5)
            self.play(Write(interpretation))
        
        self.play(FadeOut(*self.mobjects))

    def multiple_integration(self):
        with self.voiceover(text="Just as we extend derivatives to multiple dimensions, we also extend integration. Double integrals and triple integrals allow us to integrate functions over regions in two-dimensional and three-dimensional space. A double integral computes the volume under a surface.") as tracker:
            title = Text("Multiple Integration", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            double_integral = MathTex(
                r"\iint_R f(x,y) \, dA",
                font_size=36
            )
            double_integral.move_to(UP * 1.2)
            self.play(Write(double_integral))
            
            meaning = Text("Volume under surface z = f(x,y)", font_size=28)
            meaning.move_to(ORIGIN)
            self.play(Write(meaning))
        
        with self.voiceover(text="We can evaluate double integrals as iterated integrals, integrating first with respect to one variable and then the other. The order of integration matters when the bounds depend on the variables. Let's look at a concrete example.") as tracker:
            iterated = MathTex(
                r"\iint_R f(x,y) \, dA = \int_a^b \int_{g_1(x)}^{g_2(x)} f(x,y) \, dy \, dx",
                font_size=28
            )
            iterated.move_to(DOWN * 1.2)
            self.play(Write(iterated))
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Let's compute the double integral of the function f of x comma y equals x times y over the rectangular region where x goes from zero to two and y goes from zero to one. We can set this up as an iterated integral.") as tracker:
            title = Text("Example: Double Integral", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            problem = MathTex(
                r"\int_0^2 \int_0^1 xy \, dy \, dx",
                font_size=36
            )
            problem.move_to(UP * 1.5)
            self.play(Write(problem))
        
        with self.voiceover(text="First, we integrate with respect to y, treating x as a constant. The antiderivative of x y with respect to y is x times y squared over two. Evaluating from zero to one gives us x over two.") as tracker:
            step1 = MathTex(
                r"= \int_0^2 \left[ \frac{xy^2}{2} \right]_0^1 dx",
                font_size=32
            )
            step1.move_to(UP * 0.4)
            self.play(Write(step1))
            
            step2 = MathTex(
                r"= \int_0^2 \frac{x}{2} \, dx",
                font_size=32
            )
            step2.move_to(DOWN * 0.3)
            self.play(Write(step2))
        
        with self.voiceover(text="Now we integrate with respect to x. The antiderivative of x over two is x squared over four. Evaluating from zero to two gives us four over four, which equals one. So the volume under this surface over the given region is exactly one cubic unit.") as tracker:
            step3 = MathTex(
                r"= \left[ \frac{x^2}{4} \right]_0^2",
                font_size=32
            )
            step3.move_to(DOWN * 1.1)
            self.play(Write(step3))
            
            final = MathTex(
                r"= \frac{4}{4} - 0 = 1",
                font_size=36,
                color=YELLOW
            )
            final.move_to(DOWN * 2.2)
            self.play(Write(final))
        
        self.play(FadeOut(*self.mobjects))

    def double_integrals_visualization(self):
        with self.voiceover(text="Let's visualize what a double integral represents geometrically. We'll look at the function z equals one plus x squared plus y squared over a rectangular region. The double integral gives us the volume between this surface and the x-y plane.") as tracker:
            title = Text("Visualizing Double Integrals", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            equation = MathTex(r"z = 1 + x^2 + y^2", font_size=32)
            equation.move_to(UP * 2.9)
            self.play(Write(equation))
            
            # Create 3D axes with shorter x-axis to avoid overlap with grid
            axes = ThreeDAxes(
                x_range=[-1.5, 1.5, 0.5],
                y_range=[-1.5, 1.5, 0.5],
                z_range=[0, 5, 1],
                x_length=6,
                y_length=4,
                z_length=3.5,
                axis_config={"tip_length": 0.2}
            )
            axes.move_to(DOWN * 1.5)
            
            # Create surface
            surface = Surface(
                lambda u, v: axes.c2p(u, v, 1 + u**2 + v**2),
                u_range=[-1.5, 1.5],
                v_range=[-1.5, 1.5],
                resolution=(15, 15),
                fill_opacity=0.7,
                checkerboard_colors=[BLUE, BLUE]
            )
            
            self.play(Create(axes))
            self.play(Create(surface))
        
        with self.voiceover(text="The volume we're computing is the space between this curved surface and the flat x-y plane below it. We can approximate this volume by dividing the region into small rectangles, computing the volume of thin boxes, and summing them up. As we make the rectangles smaller and smaller, we approach the exact value given by the double integral.") as tracker:
            # Add a region outline on the base with padding from grid
            rectangle = Rectangle(
                width=2.5,
                height=2.5,
                color=YELLOW,
                stroke_width=4
            )
            rectangle.move_to(axes.c2p(0, 0, 0))
            self.play(Create(rectangle))
        
        self.play(FadeOut(*self.mobjects))

    def chain_rule_multivariable(self):
        with self.voiceover(text="The chain rule extends to multivariable calculus as well. When we have a composition of functions, we need to account for all the paths through which one variable affects another. This is where the multivariable chain rule becomes essential.") as tracker:
            title = Text("Chain Rule in Multiple Variables", font_size=30, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            setup = MathTex(
                r"z = f(x, y), \quad x = x(t), \quad y = y(t)",
                font_size=32
            )
            setup.move_to(UP * 1.5)
            self.play(Write(setup))
        
        with self.voiceover(text="Suppose z is a function of x and y, and both x and y are functions of t. To find how z changes with respect to t, we use the chain rule. The derivative of z with respect to t equals the partial derivative of z with respect to x times the derivative of x with respect to t, plus the partial derivative of z with respect to y times the derivative of y with respect to t.") as tracker:
            chain_rule = MathTex(
                r"\frac{dz}{dt} = \frac{\partial z}{\partial x} \frac{dx}{dt} + \frac{\partial z}{\partial y} \frac{dy}{dt}",
                font_size=36
            )
            chain_rule.move_to(UP * 0.3)
            self.play(Write(chain_rule))
        
        with self.voiceover(text="Let's work through an example. Suppose z equals x squared plus y squared, where x equals cosine of t and y equals sine of t. We want to find d z d t. First, we compute the partial derivatives of z with respect to x and y, which are two x and two y respectively.") as tracker:
            example = MathTex(
                r"z = x^2 + y^2, \quad x = \cos(t), \quad y = \sin(t)",
                font_size=28
            )
            example.move_to(DOWN * 0.6)
            self.play(Write(example))
            
            partials = MathTex(
                r"\frac{\partial z}{\partial x} = 2x, \qquad \frac{\partial z}{\partial y} = 2y",
                font_size=28
            )
            partials.move_to(DOWN * 1.5)
            self.play(Write(partials))
            
            derivatives = MathTex(
                r"\frac{dx}{dt} = -\sin(t), \qquad \frac{dy}{dt} = \cos(t)",
                font_size=28
            )
            derivatives.move_to(DOWN * 2.4)
            self.play(Write(derivatives))
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Now we apply the chain rule. We substitute our expressions for the partial derivatives and the derivatives of x and y. This gives us two times cosine t times negative sine t plus two times sine t times cosine t. When we simplify, the two terms cancel out, giving us zero. This makes sense geometrically because x equals cosine t and y equals sine t traces out a circle of radius one, so z equals x squared plus y squared is constantly equal to one, and its derivative is indeed zero.") as tracker:
            title = Text("Applying the Chain Rule", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            application = MathTex(
                r"\frac{dz}{dt} = 2x(-\sin t) + 2y(\cos t)",
                font_size=32
            )
            application.move_to(UP * 1.2)
            self.play(Write(application))
            
            substitution = MathTex(
                r"= 2\cos(t)(-\sin t) + 2\sin(t)(\cos t)",
                font_size=32
            )
            substitution.move_to(UP * 0.3)
            self.play(Write(substitution))
            
            simplification = MathTex(
                r"= -2\cos(t)\sin(t) + 2\sin(t)\cos(t) = 0",
                font_size=32,
                color=YELLOW
            )
            simplification.move_to(DOWN * 0.6)
            self.play(Write(simplification))
            
            insight = Text(
                "z = 1 (constant on the unit circle!)",
                font_size=24,
                color=GREEN
            )
            insight.move_to(DOWN * 1.8)
            self.play(Write(insight))
        
        self.play(FadeOut(*self.mobjects))

    def applications(self):
        with self.voiceover(text="Multivariate calculus has countless applications across science and engineering. Let's explore a few important ones. In optimization, we use the gradient to find maximum and minimum values of functions of multiple variables, which is crucial in machine learning and economics.") as tracker:
            title = Text("Applications of Multivariate Calculus", font_size=30, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            app1_title = Text("1. Optimization", font_size=28, color=YELLOW)
            app1_title.move_to(LEFT * 3.5 + UP * 1.5)
            self.play(Write(app1_title))
            
            app1_desc = Text(
                "Finding maxima/minima\nMachine learning\nEconomics",
                font_size=20,
                line_spacing=1.5
            )
            app1_desc.move_to(LEFT * 3.5 + UP * 0.2)
            self.play(FadeIn(app1_desc))
            
            app2_title = Text("2. Physics", font_size=28, color=YELLOW)
            app2_title.move_to(RIGHT * 3.5 + UP * 1.5)
            self.play(Write(app2_title))
            
            app2_desc = Text(
                "Electromagnetic fields\nFluid dynamics\nHeat flow",
                font_size=20,
                line_spacing=1.5
            )
            app2_desc.move_to(RIGHT * 3.5 + UP * 0.2)
            self.play(FadeIn(app2_desc))
        
        with self.voiceover(text="In physics, multivariate calculus describes electromagnetic fields, fluid flow, and heat transfer. The gradient tells us the direction of maximum temperature increase, while divergence and curl describe how vector fields flow and rotate. In engineering, we use partial differential equations to model everything from vibrating strings to air flow over aircraft wings.") as tracker:
            app3_title = Text("3. Engineering", font_size=28, color=YELLOW)
            app3_title.move_to(LEFT * 3.5 + DOWN * 1.2)
            self.play(Write(app3_title))
            
            app3_desc = Text(
                "Structural analysis\nControl systems\nSignal processing",
                font_size=20,
                line_spacing=1.5
            )
            app3_desc.move_to(LEFT * 3.5 + DOWN * 2.5)
            self.play(FadeIn(app3_desc))
            
            app4_title = Text("4. Data Science", font_size=28, color=YELLOW)
            app4_title.move_to(RIGHT * 3.5 + DOWN * 1.2)
            self.play(Write(app4_title))
            
            app4_desc = Text(
                "Gradient descent\nNeural networks\nStatistical modeling",
                font_size=20,
                line_spacing=1.6
            )
            app4_desc.move_to(RIGHT * 3.5 + DOWN * 2.5)
            self.play(FadeIn(app4_desc))
        
        with self.voiceover(text="In data science and machine learning, gradient descent uses the gradient to iteratively find the minimum of a loss function, which is how neural networks learn from data. Statistical models often involve functions of many variables, requiring multivariate calculus for analysis and optimization.") as tracker:
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def summary(self):
        with self.voiceover(text="Let's recap what we've learned about multivariate calculus. We explored partial derivatives, which measure how functions change with respect to individual variables. We studied the gradient vector, which points in the direction of steepest ascent and combines all partial derivatives into a single geometric object.") as tracker:
            title = Text("Summary", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            point1 = Text("• Partial Derivatives: Rate of change in each direction", font_size=24)
            point1.move_to(UP * 1.5 + LEFT * 0.5)
            self.play(FadeIn(point1, shift=RIGHT))
            
            point2 = Text("• Gradient: Vector of all partial derivatives", font_size=24)
            point2.move_to(UP * 0.7 + LEFT * 0.5)
            self.play(FadeIn(point2, shift=RIGHT))
            
            point3 = Text("• Directional Derivatives: Change in any direction", font_size=24)
            point3.move_to(DOWN * 0.1 + LEFT * 0.5)
            self.play(FadeIn(point3, shift=RIGHT))
        
        with self.voiceover(text="We learned about directional derivatives, which extend the concept to any direction in space, and we saw how the chain rule generalizes to handle compositions of multivariable functions. We also explored double and triple integrals for computing volumes and other quantities over regions in higher dimensions.") as tracker:
            point4 = Text("• Multiple Integrals: Volume and integration in 2D/3D", font_size=24)
            point4.move_to(DOWN * 0.9 + LEFT * 0.5)
            self.play(FadeIn(point4, shift=RIGHT))
            
            point5 = Text("• Chain Rule: Derivatives of composite functions", font_size=24)
            point5.move_to(DOWN * 1.7 + LEFT * 0.5)
            self.play(FadeIn(point5, shift=RIGHT))
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Multivariate calculus is a powerful tool that extends single-variable calculus to the multi-dimensional world we live in. From optimizing complex systems to understanding physical phenomena, these concepts are fundamental to modern science, engineering, and technology. Thank you for watching this exploration of multivariate calculus!") as tracker:
            thanks = Text("Thank You!", font_size=36, color=BLUE)
            thanks.move_to(ORIGIN)
            self.play(Write(thanks))
            
            closing = Text(
                "Keep exploring the multidimensional world!",
                font_size=28,
                color=WHITE
            )
            closing.move_to(DOWN * 1.8)
            self.play(FadeIn(closing))
            self.wait(2)

if __name__ == "__main__":
    scene = MultivariableCalculusExplanation()
    scene.render()