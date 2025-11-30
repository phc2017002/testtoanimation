"""
Pre-render code validation for Manim animation scripts.

Validates generated code before rendering to catch common errors and improve success rate.
"""

import ast
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Tuple, Set, Optional
import logging

logger = logging.getLogger(__name__)


@dataclass
class ValidationResult:
    """Result of code validation with errors, warnings, and suggestions"""
    is_valid: bool
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    suggestions: List[str] = field(default_factory=list)
    
    def add_error(self, message: str):
        """Add an error and mark as invalid"""
        self.errors.append(message)
        self.is_valid = False
    
    def add_warning(self, message: str):
        """Add a warning (doesn't invalidate)"""
        self.warnings.append(message)
    
    def add_suggestion(self, message: str):
        """Add a suggestion for improvement"""
        self.suggestions.append(message)
    
    def format_message(self) -> str:
        """Format validation result as human-readable message"""
        lines = ["Code Validation Result:", ""]
        
        if self.errors:
            lines.append("ERRORS (must fix):")
            for error in self.errors:
                lines.append(f"  ✗ {error}")
            lines.append("")
        
        if self.warnings:
            lines.append("WARNINGS (should fix):")
            for warning in self.warnings:
                lines.append(f"  ⚠️  {warning}")
            lines.append("")
        
        if self.suggestions:
            lines.append("SUGGESTIONS:")
            for suggestion in self.suggestions:
                lines.append(f"  → {suggestion}")
            lines.append("")
        
        if self.is_valid:
            lines.append("✅ Validation PASSED - code is ready to render")
        else:
            lines.append(f"❌ Validation FAILED - {len(self.errors)} error(s) found")
        
        return "\n".join(lines)


class CodeValidator:
    """Validates generated Manim code before rendering"""
    
    def __init__(self):
        self.required_imports = [
            ('from manim import', 'Manim library'),
            ('VoiceoverScene', 'VoiceoverScene class'),
            ('GTTSService', 'GTTS service'),
        ]
    
    def validate(self, code_file: Path) -> ValidationResult:
        """
        Run all validation checks on the code file.
        
        Args:
            code_file: Path to the Python file to validate
            
        Returns:
            ValidationResult with errors, warnings, and suggestions
        """
        result = ValidationResult(is_valid=True)
        
        try:
            code = code_file.read_text()
        except Exception as e:
            result.add_error(f"Failed to read code file: {e}")
            return result
        
        # Run all validation checks
        logger.info(f"🔍 Validating code file: {code_file.name}")
        
        # Check 1: Python syntax
        syntax_errors = self._check_syntax(code)
        for error in syntax_errors:
            result.add_error(error)
        
        # Check 2: Required structure  
        structure_errors = self._check_structure(code)
        for error in structure_errors:
            result.add_error(error)
        
        # Check 3: Variable definitions
        variable_errors = self._check_variables(code)
        for error in variable_errors:
            result.add_error(error)
        
        # Check 4: Animation methods
        animation_errors, animation_warnings = self._check_animations(code)
        for error in animation_errors:
            result.add_error(error)
        for warning in animation_warnings:
            result.add_warning(warning)
        
        # Check 5: Common Manim mistakes
        api_errors, api_warnings = self._check_manim_api(code)
        for error in api_errors:
            result.add_error(error)
        for warning in api_warnings:
            result.add_warning(warning)
        
        # Check 6: Imports
        import_errors = self._check_imports(code)
        for error in import_errors:
            result.add_error(error)
        
        # Check 7: Voiceover text length (NEW - catches GTTS limits)
        voiceover_errors, voiceover_warnings = self._check_voiceover_length(code)
        for error in voiceover_errors:
            result.add_error(error)
        for warning in voiceover_warnings:
            result.add_warning(warning)

        # Check 8: Persistent titles (NEW - catches title overlap bug)
        # FIX 1: Use method that returns (errors, warnings) tuple
        persistent_errors, persistent_warnings = self._check_persistent_titles(code)
        for error in persistent_errors:
            result.add_error(error)
        for warning in persistent_warnings:
            result.add_warning(warning)

        # Check 9: Duration matching (NEW - prevents black screens & sync issues)
        duration_errors, duration_warnings = self._check_voiceover_animation_duration_match(code)
        for error in duration_errors:
            result.add_error(error)
        for warning in duration_warnings:
            result.add_warning(warning)

        # Check 10: Visual density (NEW - prevents mostly-black screens)
        density_errors, density_warnings = self._check_visual_density(code)
        for error in density_errors:
            result.add_error(error)
        for warning in density_warnings:
            result.add_warning(warning)

        # Check 11: Positioning overlaps (Phase 2 - prevents element overlapping)
        overlap_errors, overlap_warnings = self._check_positioning_overlaps(code)
        for error in overlap_errors:
            result.add_error(error)
        for warning in overlap_warnings:
            result.add_warning(warning)

        # Check 12: Animation activity (Black screen fix - ensures continuous engagement)
        activity_errors, activity_warnings = self._check_animation_activity(code)
        for error in activity_errors:
            result.add_error(error)
        for warning in activity_warnings:
            result.add_warning(warning)

        
        # Add suggestions if valid but has warnings
        if result.is_valid and result.warnings:
            result.add_suggestion("Address warnings to improve code quality")
        
        logger.info(f"Validation complete: {'✅ PASSED' if result.is_valid else '❌ FAILED'}")
        if not result.is_valid:
            logger.warning(f"Found {len(result.errors)} error(s)")
        
        return result
    
    def _check_syntax(self, code: str) -> List[str]:
        """Validate Python syntax using compile()"""
        errors = []
        try:
            compile(code, '<string>', 'exec')
            logger.debug("✓ Python syntax valid")
        except SyntaxError as e:
            errors.append(f"Syntax error at line {e.lineno}: {e.msg}")
            logger.error(f"✗ Syntax error found")
        return errors
    
    def _check_structure(self, code: str) -> List[str]:
        """Validate required class structure"""
        errors = []
        
        # Check for VoiceoverScene inheritance
        if not re.search(r'class\s+\w+\s*\(\s*VoiceoverScene\s*\)', code):
            errors.append("Class must inherit from VoiceoverScene")
        
        # Check for construct method
        if 'def construct(self):' not in code:
            errors.append("Missing construct() method")
        
        # Check for animation methods
        animation_methods = re.findall(r'def (animation_(\d+))\(self\)', code)
        if not animation_methods:
            errors.append("No animation_N() methods found - code must use animation_0(), animation_1(), etc.")
        else:
            # Check sequential numbering
            numbers = sorted([int(num) for _, num in animation_methods])
            expected = list(range(len(numbers)))
            
            if numbers != expected:
                missing = set(expected) - set(numbers)
                if missing:
                    errors.append(f"Animation methods not sequential - missing: {sorted(missing)}")
                duplicates = [n for n in numbers if numbers.count(n) > 1]
                if duplicates:
                    errors.append(f"Duplicate animation methods: animation_{duplicates}")
            
            logger.debug(f"✓ Found {len(numbers)} animation methods: animation_0 to animation_{max(numbers)}")
        
        return errors
    
    def _check_variables(self, code: str) -> List[str]:
        """Check for undefined variables using AST analysis"""
        errors = []
        
        try:
            tree = ast.parse(code)
            
            # Simple check: look for common undefined variable patterns
            # More sophisticated analysis would require full data flow tracking
            
            # Find self.play() calls with arguments that might be undefined
            for node in ast.walk(tree):
                if isinstance(node, ast.Call):
                    # Check if this is self.play()
                    if (isinstance(node.func, ast.Attribute) and
                        node.func.attr == 'play' and
                        isinstance(node.func.value, ast.Name) and
                        node.func.value.id == 'self'):
                        
                        # Check arguments for potential undefined variables
                        for arg in node.args:
                            if isinstance(arg, ast.Call):
                                # Check for FadeOut(var), Create(var), etc.
                                if isinstance(arg.func, ast.Name):
                                    for arg_inner in arg.args:
                                        if isinstance(arg_inner, ast.Name):
                                            # This is a variable - we'd need to track if it's defined
                                            # For now, just log it
                                            pass
            
            logger.debug("✓ Variable analysis complete (basic)")
            
        except Exception as e:
            logger.warning(f"AST analysis failed: {e}")
        
        return errors
    
    def _check_animations(self, code: str) -> Tuple[List[str], List[str]]:
        """Validate animation methods"""
        errors = []
        warnings = []
        
        # Find all animation methods with their bodies
        pattern = r'def (animation_\d+)\(self\):(.*?)(?=\n    def |\nclass |\Z)'
        matches = re.findall(pattern, code, re.DOTALL)
        
        for method_name, method_body in matches:
            # Check for voiceover block
            if 'with self.voiceover' not in method_body:
                warnings.append(f"{method_name}(): Missing voiceover block")
            
            # Check for animation calls
            has_animation = any(call in method_body for call in [
                'self.play(',
                'self.add(',
                'self.remove(',
                'self.wait('
            ])
            
            if not has_animation:
                warnings.append(f"{method_name}(): No animation calls found (self.play, self.add, etc.)")
        
        if matches:
            logger.debug(f"✓ Validated {len(matches)} animation methods")
        
        return errors, warnings
    
    def _check_manim_api(self, code: str) -> Tuple[List[str], List[str]]:
        """Check for common Manim API mistakes"""
        errors = []
        warnings = []
        
        # Check for lowercase color names (should use constants)
        lowercase_colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'white', 'black']
        for color in lowercase_colors:
            if f'color="{color}"' in code or f"color='{color}'" in code:
                warnings.append(f'Use uppercase color constant: {color.upper()} instead of "{color}"')
        
        # Check for MathTex usage (we prefer Text for compatibility)
        if 'MathTex(' in code:
            count = code.count('MathTex(')
            warnings.append(f"Found {count} MathTex usage(s) - consider using Text() for better compatibility")
        
        # Check for extreme coordinates (potential off-screen issues)
        extreme_coords = re.findall(r'(?:UP|DOWN|LEFT|RIGHT)\s*\*\s*(\d+)', code)
        for coord in extreme_coords:
            if int(coord) > 5:
                warnings.append(f"Large coordinate multiplier ({coord}) may place objects off-screen")
        
        logger.debug("✓ Manim API checks complete")
        
        return errors, warnings
    
    def _check_imports(self, code: str) -> List[str]:
        """Validate required imports"""
        errors = []
        
        for import_pattern, description in self.required_imports:
            if import_pattern not in code:
                errors.append(f"Missing import: {description} ({import_pattern})")
        
        if not errors:
            logger.debug("✓ All required imports present")
        
        return errors
    
    def _check_voiceover_length(self, code: str) -> Tuple[List[str], List[str]]:
        """
        Check for voiceover text that exceeds GTTS character limits.
        
        GTTS (Google Text-to-Speech) has a limit of approximately 5000 characters
        per request. This check identifies voiceover blocks that exceed this limit
        to prevent runtime failures.
        """
        errors = []
        warnings = []
        
        # GTTS limit is approximately 5000 characters per request
        MAX_CHARS = 5000
        WARN_THRESHOLD = 4000
        
        # Find all voiceover blocks with their text content
        # Pattern: with self.voiceover(text="""...""") as tracker:
        pattern = r'with\s+self\.voiceover\s*\(\s*text\s*=\s*"""(.*?)"""\s*\)'
        matches = re.findall(pattern, code, re.DOTALL)
        
        if not matches:
            logger.debug("No voiceover blocks found to check")
            return errors, warnings
        
        logger.debug(f"Checking {len(matches)} voiceover blocks for length")
        
        for idx, text in enumerate(matches):
            # Count actual characters (strip to remove excess whitespace)
            char_count = len(text.strip())
            
            if char_count > MAX_CHARS:
                errors.append(
                    f"Voiceover block #{idx} exceeds GTTS limit: {char_count} characters "
                    f"(max: {MAX_CHARS}). Split into smaller blocks or reduce text."
                )
                logger.error(f"✗ Voiceover block #{idx}: {char_count} chars (EXCEEDS LIMIT)")
            elif char_count > WARN_THRESHOLD:
                warnings.append(
                    f"Voiceover block #{idx} is close to GTTS limit: {char_count} characters "
                    f"(limit: {MAX_CHARS}). Consider reducing text."
                )
                logger.warning(f"⚠️  Voiceover block #{idx}: {char_count} chars (approaching limit)")
            else:
                logger.debug(f"✓ Voiceover block #{idx}: {char_count} chars (OK)")
        
        if not errors and not warnings:
            logger.debug("✓ All voiceover blocks within limits")
        
        return errors, warnings
    
    def _check_persistent_titles(self, code: str) -> List[str]:
        """
        Detect titles that are created but never removed across scenes.
        
        This catches the common bug where animation_0() creates a title at the top,
        but subsequent animations show new content at the top without removing the old title,
        causing overlaps.
        
        Returns:
            (errors, warnings) tuple
        """
        warnings = []
        errors = []  # CRITICAL FIX: Initialize errors list!
        
        try:
            tree = ast.parse(code)
        except:
            # If can't parse, skip this check
            return errors, warnings
        
        # Find all animation methods and analyze them
        animation_methods = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name.startswith('animation_'):
                animation_methods.append(node)
        
        if len(animation_methods) < 2:
            # Need at least 2 animations to check for persistence
            return errors, warnings
        
        # Sort by animation number
        animation_methods.sort(key=lambda x: int(x.name.split('_')[1]) if x.name.split('_')[1].isdigit() else 0)
        
        # Check for title creation and removal pattern
        title_created_in = None
        title_created_line = None
        title_removed = False
        new_content_at_top_after_title = []
        
        for method in animation_methods:
            method_name = method.name
            anim_num = int(method.name.split('_')[1]) if method.name.split('_')[1].isdigit() else 0
            
            # Check if this method creates self.title
            for node in ast.walk(method):
                if isinstance(node, ast.Assign):
                    for target in node.targets:
                        if (isinstance(target, ast.Attribute) and 
                            isinstance(target.value, ast.Name) and
                            target.value.id == 'self' and
                            target.attr in ['title', 'main_title', 'heading']):
                            title_created_in = method_name
                            title_created_line = getattr(node, 'lineno', '?')
                            break
            
            # If title was created in a previous animation, check for removal/conflict
            if title_created_in and anim_num > int(title_created_in.split('_')[1]):
                
                # Check if title is explicitly removed
                for node in ast.walk(method):
                    if isinstance(node, ast.Call):
                        # Look for FadeOut or remove() calls
                        if (hasattr(node.func, 'attr') and 
                            node.func.attr in ['FadeOut', 'remove', 'clear']):
                            # Check if any argument references self.title
                            for arg in node.args:
                                if isinstance(arg, ast.Attribute):
                                    if (isinstance(arg.value, ast.Name) and
                                        arg.value.id == 'self' and
                                        arg.attr in ['title', 'main_title', 'heading']):
                                        title_removed = True
                                    elif isinstance(arg.value, ast.Attribute) and arg.value.attr == 'mobjects':
                                        # FadeOut(*self.mobjects) removes everything
                                        title_removed = True
                
                # Check if NEW content is being placed at the top
                for node in ast.walk(method):
                    if isinstance(node, ast.Call):
                        # Look for .to_edge(UP) or .move_to(...UP...)
                        if hasattr(node.func, 'attr') and node.func.attr in ['to_edge', 'move_to']:
                            for arg in node.args:
                                # Check for UP constant
                                if isinstance(arg, ast.Name) and arg.id == 'UP':
                                    new_content_at_top_after_title.append(method_name)
                                    break
                                # Check for expressions containing UP
                                elif isinstance(arg, ast.BinOp):
                                    for subnode in ast.walk(arg):
                                        if isinstance(subnode, ast.Name) and subnode.id == 'UP':
                                            new_content_at_top_after_title.append(method_name)
                                            break
        
        # Generate warning if title persists and new top content is added
        if title_created_in and not title_removed and new_content_at_top_after_title:
            methods = ", ".join(set(new_content_at_top_after_title[:3]))  # Show first 3
            more = f" and {len(new_content_at_top_after_title) - 3} more" if len(new_content_at_top_after_title) > 3 else ""
            
            # Fix 1: Change to ERROR (was WARNING) to block generation!
            errors.append(
                f"❌ Persistent title detected: Title created in '{title_created_in}' (line {title_created_line}) "
                f"is never removed, but new content at top is shown in {methods}{more}.\n"
                f"   This will cause OVERLAPS (title + equation/content clashing)!\n"
                f"   \n"
                f"   MANDATORY FIX: Add cleanup code at start of {methods.split(',')[0]}:\n"
                f"   \n"
                f"   def {methods.split(',')[0]}(self):\n"
                f"       with self.voiceover(text=\"...\") as tracker:\n"
                f"           # CLEANUP FIRST!\n"
                f"           if hasattr(self, 'title'):\n"
                f"               self.play(FadeOut(self.title))\n"
                f"           \n"
                f"           # Then add new content...\n"
                f"   \n"
                f"   Or position title very high: .to_edge(UP, buff=2.0) for Y>3.0"
            )
            logger.warning(f"⚠️  Persistent title pattern detected in {title_created_in}")
        
        return errors, warnings
    
    def _check_voiceover_animation_duration_match(self, code: str) -> Tuple[List[str], List[str]]:
        """
        Verify that animation durations match voiceover durations.
        
        Prevents:
        - Black screens (animations too short)
        - Sync drift (too many rapid transitions)
        
        Formula: voiceover_chars / 35 = expected_duration_seconds
        
        Returns:
            Tuple of (errors, warnings)
        """
        errors = []
        warnings = []
        
        try:
            tree = ast.parse(code)
        except:
            return errors, warnings
        
        GTTS_RATE = 35.0  # characters per second for GTTS
        DEFAULT_PLAY_TIME = 1.0  # default play() duration
        
        for node in ast.walk(tree):
            if not (isinstance(node, ast.FunctionDef) and node.name.startswith('animation_')):
                continue
            
            voiceover_duration = 0
            animation_duration = 0
            voiceover_text = ""
            
            # Find voiceover block and extract text
            for subnode in ast.walk(node):
                if isinstance(subnode, ast.With):
                    for item in subnode.items:
                        if isinstance(item.context_expr, ast.Call):
                            if hasattr(item.context_expr.func, 'attr') and item.context_expr.func.attr == 'voiceover':
                                # Extract text keyword argument
                                for keyword in item.context_expr.keywords:
                                    if keyword.arg == 'text' and isinstance(keyword.value, ast.Constant):
                                        voiceover_text = keyword.value.value
                                        voiceover_duration = len(voiceover_text) / GTTS_RATE
            
            if not voiceover_text:
                continue  # No voiceover in this animation
            
            # Count play() calls and their run_times
            for subnode in ast.walk(node):
                if isinstance(subnode, ast.Call):
                    if hasattr(subnode.func, 'attr') and subnode.func.attr == 'play':
                        # Check for run_time keyword
                        run_time = DEFAULT_PLAY_TIME
                        for keyword in subnode.keywords:
                            if keyword.arg == 'run_time':
                                if isinstance(keyword.value, ast.Constant):
                                    run_time = keyword.value.value
                                elif isinstance(keyword.value, ast.Num):  # Python 3.7 compatibility
                                    run_time = keyword.value.n
                        animation_duration += run_time
            
            if animation_duration == 0:
                continue  # No animations found (might be error elsewhere)
            
            # Calculate duration mismatch
            duration_diff = abs(voiceover_duration - animation_duration)
            mismatch_percent = (duration_diff / voiceover_duration * 100) if voiceover_duration > 0 else 0
            
            # Error threshold: >50% mismatch (relaxed from 30%)
            # Phase 2: Relaxed threshold - 70% error (was 50%)
            if mismatch_percent > 70:
                errors.append(
                    f"❌ {node.name}: Severe duration mismatch! "
                    f"Voiceover: {voiceover_duration:.1f}s ({len(voiceover_text)} chars), "
                    f"Animation: {animation_duration:.1f}s ({duration_diff:.1f}s gap, {mismatch_percent:.0f}% mismatch). "
                    f"{'Add' if animation_duration < voiceover_duration else 'Remove'} {abs(duration_diff):.1f}s of animations "
                    f"or {'reduce' if animation_duration < voiceover_duration else 'increase'} voiceover length."
                )
            # Warning threshold: >25% mismatch (relaxed from 15%)
            # Phase 2: Relaxed threshold - 40% warning (was 25%)
            elif mismatch_percent > 40:
                warnings.append(
                    f"⚠️  {node.name}: Duration mismatch detected. "
                    f"Voiceover: {voiceover_duration:.1f}s, Animation: {animation_duration:.1f}s "
                    f"({duration_diff:.1f}s gap, {mismatch_percent:.0f}% mismatch). "
                    f"Consider {'adding' if animation_duration < voiceover_duration else 'removing'} "
                    f"{abs(duration_diff):.1f}s of animations for perfect sync."
                )
            # All good! Log success
            else:
                logger.debug(f"✓ {node.name}: Duration match OK ({voiceover_duration:.1f}s vs {animation_duration:.1f}s)")
        
        if not errors and not warnings:
            logger.debug("✓ All animation durations match voiceover durations")
        
        return errors, warnings

    def _check_visual_density(self, code: str) -> tuple[list[str], list[str]]:
        """Check if animations have sufficient visual density to avoid mostly-black screens."""
        errors = []
        warnings = []
        
        try:
            tree = ast.parse(code)
        except SyntaxError:
            return errors, warnings  # Skip if code has syntax errors
        
        # Visual element types to count
        VISUAL_ELEMENTS = {
            'Text', 'MathTex', 'Tex', 'Title',  # Text elements
            'Circle', 'Square', 'Rectangle', 'Polygon', 'Triangle',  # Shapes
            'Arrow', 'Line', 'Dot', 'Point',  # Lines/points
            'VGroup', 'Group',  # Groups
            'Axes', 'NumberPlane', 'CoordinateSystem',  # Coordinate systems
            'Graph', 'ParametricFunction',  # Graphs
        }
        
        BACKGROUND_ELEMENTS = {
            'NumberPlane', 'Axes', 'CoordinateSystem'
        }
        
        has_background = False
        animation_0_checked = False
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name.startswith('animation_'):
                # Count visual elements in this animation
                visual_count = 0
                has_local_background = False
                
                for child in ast.walk(node):
                    if isinstance(child, ast.Call):
                        # Extract function name from Call node
                        func_name = None
                        if isinstance(child.func, ast.Name):
                            func_name = child.func.id
                        elif isinstance(child.func, ast.Attribute):
                            func_name = child.func.attr
                        
                        if func_name:
                            # Check for background elements
                            if func_name in BACKGROUND_ELEMENTS:
                                has_local_background = True
                                if node.name == 'animation_0':
                                    has_background = True
                            
                            # Count visual elements
                            if func_name in VISUAL_ELEMENTS:
                                visual_count += 1
                
                # Check animation_0 for background
                if node.name == 'animation_0':
                    animation_0_checked = True
                    if not has_local_background:
                        warnings.append(
                            f"⚠️  {node.name}: No background element detected. "
                            f"Add NumberPlane() or Axes() in animation_0 to eliminate black backgrounds. "
                            f"Example: background = NumberPlane(...); self.add(background)"
                        )
                
                
                # Phase 2: Duration-based visual density
                # Extract voiceover duration for this animation
                voiceover_text = None
                for child in ast.walk(node):
                    if isinstance(child, ast.With):
                        if hasattr(child.items[0].context_expr, 'func'):
                            func = child.items[0].context_expr.func
                            if hasattr(func, 'attr') and func.attr == 'voiceover':
                                for keyword in child.items[0].context_expr.keywords:
                                    if keyword.arg == 'text':
                                        if isinstance(keyword.value, ast.Constant):
                                            voiceover_text = keyword.value.value
                                        break
                
                # Calculate duration-based minimum elements
                voiceover_duration = len(voiceover_text) / 35.0 if voiceover_text else 0
                
                if voiceover_duration < 3:
                    min_elements = 1  # Short: allow 1 element
                    duration_desc = "short (<3s)"
                elif voiceover_duration < 8:
                    min_elements = 2  # Medium: need 2
                    duration_desc = "medium (3-8s)"
                else:
                    min_elements = 3  # Long: need 3
                    duration_desc = "long (>8s)"
                
                # Check visual density with duration context
                if visual_count < min_elements:
                    if visual_count == 0:
                        # Truly empty - always an error
                        errors.append(
                            f"❌ {node.name}: No visual elements detected!\n"
                            f"   Animation is completely empty. Add at least {min_elements} visual element(s)\n"
                            f"   (title, shape, diagram, or text) to prevent black screen.\n"
                            f"   \n"
                            f"   Voiceover duration: {voiceover_duration:.1f}s ({duration_desc})"
                        )
                    else:
                        # Insufficient for duration
                        errors.append(
                            f"❌ {node.name}: Insufficient visual elements for {voiceover_duration:.1f}s voiceover!\n"
                            f"   Found: {visual_count} element(s), Required: {min_elements}+ ({duration_desc} voiceover)\n"
                            f"   \n"
                            f"   Long voiceover needs more visual content to stay engaging!\n"
                            f"   Add: shapes, diagrams, labels, or annotations"
                        )
                elif visual_count < 4 and voiceover_duration >= 3:
                    # Low density for non-short animations
                    warnings.append(
                        f"⚠️  {node.name}: Low visual density for {voiceover_duration:.1f}s voiceover.\n"
                        f"   Found {visual_count} visual elements, recommended 4+ for better engagement.\n"
                        f"   Consider adding more annotations, labels, or visual aids."
                    )
        
        # Overall background check (changed to warning)
        if animation_0_checked and not has_background:
            warnings.append(
                "⚠️  No background element found in animation_0. "
                "Consider adding NumberPlane() or Axes() for better visuals and to prevent mostly-black screens. "
                "Example: background = NumberPlane(...); self.add(background)"
            )
        
        if not errors and not warnings:
            logger.debug("✓ Visual density check passed - sufficient visual elements")
        
        return errors, warnings

    def _check_positioning_overlaps(self, code: str) -> Tuple[List[str], List[str]]:
        """
        Detect positioning code likely to cause overlaps (Phase 2).
        
        Checks:
        1. .next_to() with buff < 0.8
        2. Text positioned via move_to(DOWN * value) where value < 2.0 (middle zone)
        3. Text boxes positioned in middle zone
        
        Returns:
            (errors, warnings) tuple
        """
        errors = []
        warnings = []
        
        try:
            tree = ast.parse(code)
        except SyntaxError:
            return errors, warnings
        
        # Track all .next_to() calls and positioning calls
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                # Check for .next_to() calls
                if hasattr(node.func, 'attr') and node.func.attr == 'next_to':
                    # Extract buff parameter if present
                    buff_value = None
                    for keyword in node.keywords:
                        if keyword.arg == 'buff':
                            if isinstance(keyword.value, ast.Constant):
                                buff_value = keyword.value.value
                            elif isinstance(keyword.value, (ast.Num)):  # Python 3.7 compatibility
                                buff_value = keyword.value.n
                    
                    # Check if buff is too small
                    # Fix 3: Relaxed threshold - ERROR only for very small buff
                    if buff_value is not None and buff_value < 0.5:
                        errors.append(
                            f"❌ Overlap risk: .next_to(buff={buff_value}) detected.\n"
                            f"   Problem: buff={buff_value} is too small, elements will overlap!\n"
                            f"   \n"
                            f"   Fix (Option 1 - Increase buff):\n"
                            f"   label.next_to(obj, DOWN, buff=0.8)  # Minimum safe distance\n"
                            f"   \n"
                            f"   Fix (Option 2 - Use fixed positioning, RECOMMENDED):\n"
                            f"   label.to_edge(DOWN, buff=1.0)  # Y≈-3.0, safe in LOWER zone"
                        )
                    # Warning for medium-small buff (0.5-0.8)
                    elif buff_value is not None and buff_value < 0.8:
                        warnings.append(
                            f"⚠️  Small buff: .next_to(buff={buff_value}) detected.\n"
                            f"   Recommended: Use buff=0.8 or higher for safer spacing.\n"
                            f"   Current buff={buff_value} may work but is tight."
                        )
                    elif buff_value is None:
                        # No buff specified - default is 0.25, too small!
                        warnings.append(
                            f"⚠️  .next_to() without buff parameter (default 0.25 is too small). "
                            f"Add buff=0.8 or use to_edge() for safe positioning"
                        )
                
                # Check for .move_to() calls with dangerous positioning
                elif hasattr(node.func, 'attr') and node.func.attr == 'move_to':
                    if len(node.args) > 0:
                        arg = node.args[0]
                        y_coord = self._extract_y_from_expression(arg)
                        
                        if y_coord is not None:
                            # Check if in dangerous middle zone
                            if -2.0 < y_coord < 2.0 and y_coord != 0:
                                warnings.append(
                                    f"⚠️  Element positioned at Y≈{y_coord} via move_to().\n"
                                    f"   Problem: This is in MIDDLE zone where tree/diagram exists!\n"
                                    f"   \n"
                                    f"   Current code (WRONG):\n"
                                    f"   element.move_to(DOWN * {abs(y_coord)})  # Y={y_coord}, OVERLAPS!\n"
                                    f"   \n"
                                    f"   Fixed code (CORRECT):\n"
                                    f"   element.to_edge(DOWN, buff=1.0)  # Y≈-3.0, safe in LOWER zone"
                                )
                
                # Check for Rectangle/Square positioned in middle
                elif hasattr(node.func, 'id') and node.func.id in ['Rectangle', 'Square']:
                    # Look for subsequent .move_to() in same statement
                    pass  # Handled by move_to check above
        
        # Additional check: Look for Text objects with tree/diagram in same function
        for func_node in [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]:
            if func_node.name.startswith('animation_'):
                has_tree_keywords = False
                has_text_in_middle = False
                
                # Check if function contains tree-related code
                func_source = ast.get_source_segment(code, func_node)
                if func_source:
                    tree_keywords = ['tree', 'Tree', 'graph', 'Graph', 'node', 'Node', 'Circle']
                    has_tree_keywords = any(keyword in func_source for keyword in tree_keywords)
                    
                    # Check for Text with move_to in dangerous zone
                    if has_tree_keywords and ('Text(' in func_source):
                        # If has both tree and text, check positioning
                        if '.move_to(DOWN' in func_source and '* 0.' in func_source:
                            warnings.append(
                                f"⚠️  {func_node.name}: Tree diagram + text positioning detected. "
                                f"Ensure ALL explanatory text uses Y<-2.0 (to_edge(DOWN)) "
                                f"to avoid overlapping with tree in middle zone"
                            )
        
        return errors, warnings
    
    def _extract_y_from_expression(self, node) -> Optional[float]:
        """
        Extract Y coordinate from positioning expression like:
        - DOWN * 0.5 => -0.5
        - UP * 2 => 2.0
        - DOWN * 2.5 => -2.5
        """
        try:
            # Handle BinOp (multiplication)
            if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mult):
                # Check if it's DOWN or UP multiplication
                left_name = None
                if isinstance(node.left, ast.Name):
                    left_name = node.left.id
                
                multiplier = None
                if isinstance(node.right, ast.Constant):
                    multiplier = node.right.value
                elif isinstance(node.right, (ast.Num)):  # Python 3.7
                    multiplier = node.right.n
                
                if left_name and multiplier is not None:
                    # DOWN = [0, -1, 0], so DOWN * 0.5 = Y=-0.5
                    if left_name == 'DOWN':
                        return -multiplier
                    # UP = [0, 1, 0], so UP * 2 = Y=2.0
                    elif left_name == 'UP':
                        return multiplier
            
            # Handle ORIGIN (Y=0)
            elif isinstance(node, ast.Name) and node.id == 'ORIGIN':
                return 0.0
        
        except Exception:
            pass
        
        return None

    def _check_animation_activity(self, code: str) -> Tuple[List[str], List[str]]:
        """
        Phase 1: Ensure animation activity matches voiceover duration.
        
        Problem: Long voiceover (5 to 8 seconds) with only 1 second of animation equals boring black screens.
        Solution: Require continuous animations throughout voiceover duration.
        
        Rules:
        - Short voiceover (less than 3 sec): At least 1 animation
        - Medium voiceover (3 to 8 sec): At least 2-3 animations  
        - Long voiceover (more than 8 sec): At least 3-5 animations
        
        Returns:
            (errors, warnings) tuple
        """
        errors = []
        warnings = []
        
        try:
            tree = ast.parse(code)
        except SyntaxError:
            return errors, warnings
        
        # Find all animation_N methods
        for node in [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]:
            if not node.name.startswith('animation_'):
                continue
            
            # Extract voiceover text and estimate duration
            voiceover_text = None
            for child in ast.walk(node):
                if isinstance(child, ast.With):
                    # Look for with self.voiceover(text=...) pattern
                    if hasattr(child.items[0].context_expr, 'func'):
                        func = child.items[0].context_expr.func
                        if hasattr(func, 'attr') and func.attr == 'voiceover':
                            # Extract text argument
                            for keyword in child.items[0].context_expr.keywords:
                                if keyword.arg == 'text':
                                    if isinstance(keyword.value, ast.Constant):
                                        voiceover_text = keyword.value.value
                                    break
            
            if not voiceover_text:
                continue
            
            # Estimate duration (35 chars/second for speech)
            voiceover_duration = len(voiceover_text) / 35.0
            
            # Count self.play() calls (actual animations)
            animation_count = 0
            # Fix 3: Also count self.add() calls (static content)
            static_add_count = 0
            
            for child in ast.walk(node):
                if isinstance(child, ast.Call):
                    if hasattr(child.func, 'attr'):
                        if child.func.attr == 'play':
                            if hasattr(child.func, 'value'):
                                if isinstance(child.func.value, ast.Name) and child.func.value.id == 'self':
                                    animation_count += 1
                        # Fix 3: Count static adds
                        elif child.func.attr == 'add':
                            if hasattr(child.func, 'value'):
                                if isinstance(child.func.value, ast.Name) and child.func.value.id == 'self':
                                    static_add_count += 1
            
            # Determine required minimum animations based on duration
            if voiceover_duration < 3:
                min_animations = 1
                duration_desc = "Short"
            elif voiceover_duration < 8:
                min_animations = 2
                duration_desc = "Medium"
            else:
                min_animations = 3
                duration_desc = "Long"
            
            # Check if sufficient animations
            if animation_count < min_animations:
                errors.append(
                    f"❌ {node.name}: Insufficient animation activity for {voiceover_duration:.1f}s voiceover!\n"
                    f"   Found: {animation_count} animation(s), Required: {min_animations}+ ({duration_desc} voiceover)\n"
                    f"   \n"
                    f"   Problem: Long voiceover with few animations = boring static screens!\n"
                    f"   \n"
                    f"   Fix: Add more self.play() calls to fill the {voiceover_duration:.1f}s:\n"
                    f"   - Write/Create text or shapes (run_time=1-2s)\n"
                    f"   - Transform/morph elements (run_time=1-2s)\n"
                    f"   - FadeIn/FadeOut transitions (run_time=0.5-1s)\n"
                    f"   - Indicate/Flash to highlight (run_time=0.5s)\n"
                    f"   \n"
                    f"   Example: {voiceover_duration:.1f}s voiceover needs {min_animations}+ animations with combined run_time ≈ {voiceover_duration:.1f}s"
                )
            elif animation_count < min_animations + 1:
                # Close to minimum, give warning
                warnings.append(
                    f"⚠️  {node.name}: Low animation activity for {voiceover_duration:.1f}s voiceover.\n"
                    f"   Found: {animation_count} animation(s), Recommended: {min_animations + 1}+\n"
                    f"   Consider adding 1-2 more animations for better engagement."
                )
            
            # Fix 3: Warn about too many static elements
            if static_add_count > 2 and animation_count < min_animations:
                warnings.append(
                    f"⚠️  {node.name}: Too many static .add() calls ({static_add_count}) with few animations ({animation_count})!\n"
                    f"   Problem: Static elements (self.add) appear instantly without animation.\n"
                    f"   \n"
                    f"   Better: Use self.play() for animated content:\n"
                    f"   - Instead of: self.add(title) → Use: self.play(Write(title))\n"
                    f"   - Instead of: self.add(shape) → Use: self.play(Create(shape))\n"
                    f"   - Instead of: self.add(text) → Use: self.play(FadeIn(text))\n"
                    f"   \n"
                    f"   This creates visual engagement instead of instant static screens!"
                )
        
        return errors, warnings


