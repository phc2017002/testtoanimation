"""
3D Animation Generation Prompts

Comprehensive system prompts for generating 3D animations covering all STEM visualizations.
"""

SYSTEM_PROMPT_3D = """You are an expert at creating educational 3D animations using Manim's ThreeDScene.

Your task is to generate Python code using Manim that creates stunning, educational 3D visualizations.

CRITICAL REQUIREMENTS:
1. Use ThreeDScene as the base class (NOT Scene)
2. Import from manim: from manim import *
3. Always set camera orientation appropriately
4. Use 3D objects and coordinate systems
5. Include smooth camera movements when appropriate
6. Add voiceover narration using manim-voiceover
7. Use proper lighting and perspective

AVAILABLE 3D OBJECTS:
- Basic shapes: Sphere(), Cube(), Cone(), Cylinder(), Torus(), Prism()
- Arrows: Arrow3D(), Vector()
- Axes: ThreeDAxes()
- Surfaces: Surface(), ParametricSurface()
- Lines/Points: Line3D(), Dot3D()
- Text: Text(), Tex(), MathTex() with add_fixed_in_frame_mobjects()

CAMERA CONTROLS:
- set_camera_orientation(phi=angle, theta=angle, zoom=value)
  * phi: vertical rotation (0 to 2*PI)
  * theta: horizontal rotation (0 to 2*PI)
  * zoom: camera zoom level
- move_camera(phi=angle, theta=angle, zoom=value, run_time=seconds)
- begin_ambient_camera_rotation(rate=0.2)
- stop_ambient_camera_rotation()

STEM VISUALIZATION CATEGORIES:

1. MATHEMATICAL VISUALIZATIONS:
   - 3D function surfaces: f(x,y) = z
   - Parametric surfaces
   - Vector fields in 3D space
   - Calculus: gradients, curl, divergence
   - Complex transformations
   - Topology and manifolds

2. SCIENTIFIC MODELS:
   - Molecular structures (atoms, bonds)
   - Physics simulations (orbits, forces, fields)
   - Crystal lattices
   - Wave propagation
   - Electromagnetic fields
   - Quantum mechanics visualizations

3. GEOMETRIC DEMONSTRATIONS:
   - 3D shapes and transformations
   - Rotation matrices
   - Cross products and dot products
   - Planes and their intersections
   - Volume calculations
   - Symmetry groups

4. DATA VISUALIZATION:
   - 3D scatter plots
   - Surface plots from data
   - 3D bar charts
   - Network graphs in 3D
   - Animated data evolution

CODE STRUCTURE:
```python
from manim import *
from manim_voiceover import VoiceoverScene
from manimator.services import ElevenLabsService

class YourSceneName(VoiceoverScene, ThreeDScene):
    def construct(self):
        # Initialize voiceover with natural AI voice
        self.set_speech_service(ElevenLabsService(voice_id="Rachel"))
        # Other voice options: Adam, Bella, Josh, Antoni
        
        # Set camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        
        # Create 3D axes
        axes = ThreeDAxes()
        
        # Your 3D animations here
        with self.voiceover(text="Narration here"):
            self.play(Create(axes))
        
        # Camera movements
        self.move_camera(phi=60*DEGREES, theta=-60*DEGREES, run_time=2)
        
        # More animations...
```

BEST PRACTICES:
1. Start with a good camera angle for the visualization
2. Use smooth camera movements to show different perspectives
3. Add labels using add_fixed_in_frame_mobjects() for 2D text in 3D space
4. Use proper scaling - 3D objects can appear different sizes
5. Include clear narration explaining what's being shown
6. Use color coding to distinguish different elements
7. Add mathematical equations when relevant
8. Make animations self-paced with appropriate run times
9. Use ambient camera rotation for overview shots
10. Show multiple viewpoints for complex structures

LIGHTING TIPS:
- Default lighting works for most cases
- For special effects, consider adding custom light sources
- Use transparency for overlapping structures (opacity parameter)

Remember: Generate complete, runnable code that creates engaging, educational 3D visualizations!
"""


EXAMPLES_3D = {
    "vector_field": """
Example: 3D Vector Field Visualization
```python
from manim import *
from manim_voiceover import VoiceoverScene
from manimator.services import ElevenLabsService

class VectorField3DDemo(VoiceoverScene, ThreeDScene):
    def construct(self):
        self.set_speech_service(ElevenLabsService(voice_id="Rachel"))
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)
        
        axes = ThreeDAxes(x_range=[-3, 3], y_range=[-3, 3], z_range=[-3, 3])
        
        with self.voiceover(text="Let's visualize a 3D vector field"):
            self.play(Create(axes))
        
        # Create vector field
        vectors = VGroup()
        for x in range(-2, 3):
            for y in range(-2, 3):
                for z in range(-2, 3):
                    point = np.array([x, y, z])
                    # Example field: rotating field
                    field = np.array([-y, x, 0.5*z])
                    if np.linalg.norm(field) > 0:
                        arrow = Arrow3D(
                            start=point,
                            end=point + 0.3 * field / np.linalg.norm(field),
                            color=BLUE
                        )
                        vectors.add(arrow)
        
        with self.voiceover(text="Each arrow shows the direction and magnitude of the field"):
            self.play(Create(vectors), run_time=3)
        
        with self.voiceover(text="Let's rotate to see different perspectives"):
            self.move_camera(phi=30*DEGREES, theta=-60*DEGREES, run_time=3)
```
""",
    
    "molecule": """
Example: Molecular Structure
```python
from manim import *
from manim_voiceover import VoiceoverScene
from manimator.services import ElevenLabsService

class WaterMolecule(VoiceoverScene, ThreeDScene):
    def construct(self):
        self.set_speech_service(ElevenLabsService(voice_id="Rachel"))
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        
        with self.voiceover(text="Let's build a water molecule in 3D"):
            pass
        
        # Oxygen atom (red)
        oxygen = Sphere(radius=0.5, color=RED)
        oxygen.move_to(ORIGIN)
        
        # Hydrogen atoms (white)
        h1 = Sphere(radius=0.3, color=WHITE)
        h1.move_to([1, 0.5, 0])
        
        h2 = Sphere(radius=0.3, color=WHITE)
        h2.move_to([1, -0.5, 0])
        
        # Bonds
        bond1 = Line3D(start=ORIGIN, end=[1, 0.5, 0], color=GRAY)
        bond2 = Line3D(start=ORIGIN, end=[1, -0.5, 0], color=GRAY)
        
        with self.voiceover(text="The oxygen atom is shown in red"):
            self.play(Create(oxygen))
        
        with self.voiceover(text="Two hydrogen atoms in white"):
            self.play(Create(h1), Create(h2))
        
        with self.voiceover(text="Connected by covalent bonds"):
            self.play(Create(bond1), Create(bond2))
        
        molecule = VGroup(oxygen, h1, h2, bond1, bond2)
        
        with self.voiceover(text="The molecule rotates to show its 3D structure"):
            self.play(Rotate(molecule, angle=2*PI, axis=UP, run_time=4))
```
""",
    
    "surface": """
Example: Mathematical Surface
```python
from manim import *
from manim_voiceover import VoiceoverScene
from manimator.services import ElevenLabsService

class ParametricSurfaceDemo(VoiceoverScene, ThreeDScene):
    def construct(self):
        self.set_speech_service(ElevenLabsService(voice_id="Rachel"))
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        
        axes = ThreeDAxes(x_range=[-4, 4], y_range=[-4, 4], z_range=[-2, 2])
        
        with self.voiceover(text="Let's visualize a 3D mathematical surface"):
            self.play(Create(axes))
        
        # Define surface z = sin(x) * cos(y)
        surface = Surface(
            lambda u, v: axes.c2p(u, v, np.sin(u) * np.cos(v)),
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(30, 30),
            fill_opacity=0.8
        )
        surface.set_color_by_gradient(BLUE, GREEN, YELLOW, RED)
        
        with self.voiceover(text="This surface represents z equals sine x times cosine y"):
            self.play(Create(surface), run_time=3)
        
        # Add equation
        equation = MathTex(r"z = \sin(x) \cos(y)")
        self.add_fixed_in_frame_mobjects(equation)
        equation.to_corner(UL)
        
        with self.voiceover(text="Notice how the surface oscillates"):
            self.play(Write(equation))
            self.begin_ambient_camera_rotation(rate=0.3)
            self.wait(5)
            self.stop_ambient_camera_rotation()
```
"""
}


def get_3d_system_prompt() -> str:
    """Get the complete 3D system prompt with examples"""
    return SYSTEM_PROMPT_3D


def get_3d_examples() -> dict:
    """Get example 3D animations"""
    return EXAMPLES_3D
