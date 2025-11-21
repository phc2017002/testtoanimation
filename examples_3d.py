"""
Example 3D Animations - Demonstrations for all STEM categories
"""

# Example 1: Mathematical - 3D Surface
SURFACE_EXAMPLE = """
from manim import *
from manim_voiceover import VoiceoverScene
from manimator.services import ElevenLabsService

class MathematicalSurface(VoiceoverScene, ThreeDScene):
    def construct(self):
        self.set_speech_service(ElevenLabsService(voice_id="Rachel"))
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        
        axes = ThreeDAxes(
            x_range=[-4, 4],
            y_range=[-4, 4],
            z_range=[-2, 2]
        )
        
        with self.voiceover(text="Let's visualize a beautiful 3D mathematical surface"):
            self.play(Create(axes))
        
        # Create surface z = sin(sqrt(x^2 + y^2))
        surface = Surface(
            lambda u, v: axes.c2p(
                u, v, np.sin(np.sqrt(u**2 + v**2))
            ),
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(40, 40),
            fill_opacity=0.7
        )
        surface.set_color_by_gradient(BLUE, GREEN, YELLOW, RED)
        
        # Add equation
        equation = MathTex(r"z = \\sin(\\sqrt{x^2 + y^2})")
        self.add_fixed_in_frame_mobjects(equation)
        equation.to_corner(UL)
        
        with self.voiceover(text="This surface represents z equals sine of the square root of x squared plus y squared"):
            self.play(Create(surface), Write(equation), run_time=3)
        
        with self.voiceover(text="Notice the ripple pattern radiating from the center"):
            self.begin_ambient_camera_rotation(rate=0.2)
            self.wait(6)
            self.stop_ambient_camera_rotation()
"""

# Example 2: Scientific - DNA Helix
DNA_EXAMPLE = """
from manim import *
from manim_voiceover import VoiceoverScene
from manimator.services import ElevenLabsService
import numpy as np

class DNAHelix(VoiceoverScene, ThreeDScene):
    def construct(self):
        self.set_speech_service(ElevenLabsService(voice_id="Rachel"))
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        
        with self.voiceover(text="Let's build a DNA double helix in 3D"):
            pass
        
        # Create helixes
        def helix1(t):
            return np.array([
                np.cos(t),
                np.sin(t),
                t / 2
            ])
        
        def helix2(t):
            return np.array([
                -np.cos(t),
                -np.sin(t),
                t / 2
            ])
        
        curve1 = ParametricFunction(
            helix1,
            t_range=[0, 4*PI],
            color=BLUE
        )
        curve1.set_shade_in_3d(True)
        
        curve2 = ParametricFunction(
            helix2,
            t_range=[0, 4*PI],
            color=BLUE
        )
        curve2.set_shade_in_3d(True)
        
        with self.voiceover(text="The DNA backbone forms a double helix structure"):
            self.play(Create(curve1), Create(curve2), run_time=3)
        
        # Add base pairs
        base_pairs = VGroup()
        for t in np.linspace(0, 4*PI, 20):
            p1 = helix1(t)
            p2 = helix2(t)
            line = Line3D(start=p1, end=p2, color=GRAY, stroke_width=2)
            base_pairs.add(line)
        
        with self.voiceover(text="Base pairs connect the two strands like rungs on a ladder"):
            self.play(Create(base_pairs), run_time=2)
        
        dna = VGroup(curve1, curve2, base_pairs)
        
        with self.voiceover(text="Let's rotate to see the complete 3D structure"):
            self.play(Rotate(dna, angle=2*PI, axis=OUT, run_time=6))
"""

# Example 3: Geometric - Rotating Cube
CUBE_EXAMPLE = """
from manim import *
from manim_voiceover import VoiceoverScene
from manimator.services import ElevenLabsService

class RotatingCube(VoiceoverScene, ThreeDScene):
    def construct(self):
        self.set_speech_service(ElevenLabsService(voice_id="Rachel"))
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)
        
        axes = ThreeDAxes()
        
        with self.voiceover(text="Let's explore 3D rotations using a cube"):
            self.play(Create(axes))
        
        cube = Cube(side_length=2, fill_opacity=0.7, stroke_width=2)
        cube.set_color_by_gradient(BLUE, GREEN, YELLOW)
        
        with self.voiceover(text="Here's our cube in 3D space"):
            self.play(Create(cube))
        
        # Rotation around X axis
        with self.voiceover(text="First, rotation around the X axis"):
            self.play(
                Rotate(cube, angle=PI, axis=RIGHT, run_time=2),
            )
        
        # Rotation around Y axis
        with self.voiceover(text="Next, rotation around the Y axis"):
            self.play(
                Rotate(cube, angle=PI, axis=UP, run_time=2),
            )
        
        # Rotation around Z axis
        with self.voiceover(text="Finally, rotation around the Z axis"):
            self.play(
                Rotate(cube, angle=PI, axis=OUT, run_time=2),
            )
        
        # Combined rotation
        with self.voiceover(text="And a combined rotation in all three dimensions"):
            self.play(
                Rotate(cube, angle=2*PI, axis=np.array([1, 1, 1]), run_time=4),
            )
"""

# Example 4: Vector Field
VECTOR_FIELD_EXAMPLE = """
from manim import *
from manim_voiceover import VoiceoverScene
from manimator.services import ElevenLabsService

class VectorField3D(VoiceoverScene, ThreeDScene):
    def construct(self):
        self.set_speech_service(ElevenLabsService(voice_id="Rachel"))
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)
        
        axes = ThreeDAxes(x_range=[-3, 3], y_range=[-3, 3], z_range=[-3, 3])
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y", z_label="z")
        
        with self.voiceover(text="Let's visualize a 3D vector field"):
            self.play(Create(axes), Write(axes_labels))
        
        # Create vector field
        vectors = VGroup()
        for x in np.arange(-2, 2.5, 1):
            for y in np.arange(-2, 2.5, 1):
                for z in np.arange(-2, 2.5, 1):
                    point = np.array([x, y, z])
                    # Circular field around z-axis
                    field = np.array([-y, x, 0.3*z])
                    
                    if np.linalg.norm(field) > 0:
                        magnitude = np.linalg.norm(field)
                        direction = field / magnitude
                        arrow = Arrow3D(
                            start=point,
                            end=point + 0.4 * direction,
                            color=BLUE,
                            thickness=0.02
                        )
                        vectors.add(arrow)
        
        with self.voiceover(text="Each arrow shows the direction and strength of the field at that point"):
            self.play(Create(vectors), run_time=4)
        
        with self.voiceover(text="Notice how the field creates a rotating pattern"):
            self.move_camera(phi=30*DEGREES, theta=-60*DEGREES, run_time=3)
            self.begin_ambient_camera_rotation(rate=0.15)
            self.wait(5)
            self.stop_ambient_camera_rotation()
"""

# Example 5: Molecule - Water
WATER_MOLECULE_EXAMPLE = """
from manim import *
from manim_voiceover import VoiceoverScene
from manimator.services import ElevenLabsService

class WaterMolecule3D(VoiceoverScene, ThreeDScene):
    def construct(self):
        self.set_speech_service(ElevenLabsService(voice_id="Rachel"))
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        
        with self.voiceover(text="Let's build a water molecule, H2O, in three dimensions"):
            pass
        
        # Oxygen atom (larger, red)
        oxygen = Sphere(radius=0.6, color=RED, resolution=(20, 20))
        oxygen.move_to(ORIGIN)
        
        # Hydrogen atoms (smaller, white)
        h1 = Sphere(radius=0.35, color=WHITE, resolution=(15, 15))
        h1.move_to([1.2, 0.5, 0])
        
        h2 = Sphere(radius=0.35, color=WHITE, resolution=(15, 15))
        h2.move_to([1.2, -0.5, 0])
        
        # Bonds (gray cylinders)
        bond1 = Line3D(start=ORIGIN, end=[1.2, 0.5, 0], color=GRAY, thickness=0.05)
        bond2 = Line3D(start=ORIGIN, end=[1.2, -0.5, 0], color=GRAY, thickness=0.05)
        
        # Labels
        o_label = Text("O", color=RED).scale(0.5)
        h1_label = Text("H", color=WHITE).scale(0.4)
        h2_label = Text("H", color=WHITE).scale(0.4)
        
        self.add_fixed_in_frame_mobjects(o_label, h1_label, h2_label)
        o_label.next_to([0, 0, 0], DOWN + LEFT, buff=0.1)
        h1_label.next_to([1.2, 0.5, 0], UP + RIGHT, buff=0.1)
        h2_label.next_to([1.2, -0.5, 0], DOWN + RIGHT, buff=0.1)
        
        with self.voiceover(text="The oxygen atom is shown in red"):
            self.play(Create(oxygen), Write(o_label))
        
        with self.voiceover(text="Two hydrogen atoms are attached, shown in white"):
            self.play(Create(h1), Create(h2), Write(h1_label), Write(h2_label))
        
        with self.voiceover(text="Covalent bonds connect them"):
            self.play(Create(bond1), Create(bond2))
        
        molecule = VGroup(oxygen, h1, h2, bond1, bond2)
        
        with self.voiceover(text="The molecule has a bent shape, with a bond angle of about 104.5 degrees"):
            self.play(Rotate(molecule, angle=PI/2, axis=UP, run_time=3))
        
        with self.voiceover(text="This 3D structure is crucial for water's unique properties"):
            self.begin_ambient_camera_rotation(rate=0.2)
            self.wait(5)
            self.stop_ambient_camera_rotation()
"""


if __name__ == "__main__":
    print("3D Animation Examples")
    print("=" * 60)
    print("\n1. Mathematical Surface")
    print("2. DNA Helix")
    print("3. Rotating Cube")
    print("4. Vector Field")
    print("5. Water Molecule")
    print("\nUse these as templates for creating your own 3D animations!")
