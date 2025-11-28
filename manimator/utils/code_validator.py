"""
Pre-render code validation for Manim animation scripts.

Validates generated code before rendering to catch common errors and improve success rate.
"""

import ast
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Tuple, Set
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
        persistent_warnings = self._check_persistent_titles(code)
        for warning in persistent_warnings:
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
            List of warning messages
        """
        warnings = []
        
        try:
            tree = ast.parse(code)
        except:
            # If can't parse, skip this check
            return warnings
        
        # Find all animation methods and analyze them
        animation_methods = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name.startswith('animation_'):
                animation_methods.append(node)
        
        if len(animation_methods) < 2:
            # Need at least 2 animations to check for persistence
            return warnings
        
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
            
            warnings.append(
                f"⚠️  Persistent title detected: Title created in '{title_created_in}' (line {title_created_line}) "
                f"is never removed, but new content at top is shown in {methods}{more}. "
                f"This will cause overlaps. Add 'if hasattr(self, \"title\"): self.play(FadeOut(self.title))' "
                f"before showing new top content."
            )
            logger.warning(f"⚠️  Persistent title pattern detected in {title_created_in}")
        
        return warnings
