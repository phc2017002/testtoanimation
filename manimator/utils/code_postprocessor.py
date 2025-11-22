"""
Code post-processor for AI-generated Manim code.

Fixes common issues like indexed SurroundingRectangle calls and layout problems.
"""

import re
from typing import List


def extract_code_from_markdown(text: str) -> str:
    """
    Extract Python code from markdown code blocks.
    
    Handles cases where LLM returns code wrapped in ```python ... ```
    
    Args:
        text: Raw text that may contain markdown code fences
    
    Returns:
        Extracted Python code without fences
    """
    # Pattern to match code blocks with optional language specifier
    pattern = r'```(?:python)?\s*\n(.*?)```'
    
    # Try to find code block
    match = re.search(pattern, text, re.DOTALL)
    
    if match:
        # Extract code from within the fences
        return match.group(1).strip()
    
    # No code block found, return original (might already be clean)
    return text.strip()


def fix_surrounding_rectangles(code: str) -> str:
    """
    Fix or remove SurroundingRectangle calls that use indexed access to MathTex.
    
    Problem: AI often generates code like:
        SurroundingRectangle(equation[0][5], ...)
    
    This doesn't work reliably because MathTex indexing is unpredictable.
    
    Solution: Comment out these problematic lines AND all subsequent lines that
    reference the disabled variables.
    
    Args:
        code: Raw generated Manim code
    
    Returns:
        Fixed code with problematic SurroundingRectangle calls commented out
    """
    lines = code.split('\n')
    fixed_lines = []
    disabled_vars = set()  # Track variables that have been disabled
    
    for line in lines:
        # Check if this line defines a SurroundingRectangle with indexed access
        if 'SurroundingRectangle(' in line:
            # Pattern: variable[number] or variable[number:number] inside SurroundingRectangle()
            if re.search(r'SurroundingRectangle\([^,\)]*\[\d+\]', line) or \
               re.search(r'SurroundingRectangle\([^,\)]*\[\d+:\d*\]', line):
                
                # Extract the variable name being assigned
                var_match = re.match(r'\s*(\w+)\s*=\s*SurroundingRectangle', line)
                if var_match:
                    disabled_vars.add(var_match.group(1))
                
                # Comment out the line
                indent = len(line) - len(line.lstrip())
                commented = ' ' * indent + '# ' + line.lstrip() + '  # Auto-disabled: indexed SurroundingRectangle'
                fixed_lines.append(commented)
                continue
        
        # Check if this line references any disabled variables
        should_disable = False
        for var in disabled_vars:
            # Check if variable is referenced in this line
            # Look for the variable name as a whole word
            if re.search(r'\b' + re.escape(var) + r'\b', line):
                should_disable = True
                break
        
        if should_disable:
            # Comment out this line as it references a disabled variable
            indent = len(line) - len(line.lstrip())
            commented = ' ' * indent + '# ' + line.lstrip() + '  # Auto-disabled: uses disabled SurroundingRectangle'
            fixed_lines.append(commented)
        else:
            # Keep the line as is
            fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)


def remove_problematic_indexing(code: str) -> str:
    """
    More aggressive approach: Remove entire blocks that use indexed MathTex highlighting.
    
    This removes the entire voiceover block if it contains indexed SurroundingRectangle.
    """
    # For now, use the commenting approach which is safer
    return fix_surrounding_rectangles(code)


def fix_layout_issues(code: str) -> str:
    """
    Fix common layout issues in Manim code.
    
    - Reduces axis length to prevent out-of-frame graphs
    - Moves axes down to make room for titles
    - Adjusts label positions to avoid overlaps
    - Increases spacing (buff) between elements
    - Caps font sizes to prevent massive text
    """
    # 1. Reduce Axis Lengths (Aggressive)
    # x_length=10 -> x_length=7
    code = re.sub(r'x_length\s*=\s*\d+(\.\d+)?', 'x_length=7', code)
    # y_length=6 -> y_length=4
    code = re.sub(r'y_length\s*=\s*\d+(\.\d+)?', 'y_length=4', code)
    
    # 2. Move Axes Down (Aggressive)
    # If axes are centered or moved slightly down, force them further down
    if 'Axes(' in code or 'NumberPlane(' in code:
        # Replace existing move_to calls for axes
        code = re.sub(r'(axes|plane)\.move_to\(.*?\)', r'\1.move_to(DOWN * 1.5)', code)
        # If no move_to exists, we can't easily inject it without parsing, 
        # but the prompt usually includes it.
    
    # 3. Fix Y-Axis Labels (Collision with axis)
    # direction=LEFT, shift(LEFT * 0.8)
    code = re.sub(
        r'get_y_axis_label\((.*?),.*?\)', 
        r'get_y_axis_label(\1, direction=LEFT).shift(LEFT * 0.8)', 
        code
    )
    
    # 4. Fix X-Axis Labels (Collision with axis)
    # shift(DOWN * 0.8)
    code = re.sub(
        r'get_x_axis_label\((.*?)\)(?!\.shift)', 
        r'get_x_axis_label(\1).shift(DOWN * 0.8)', 
        code
    )
    
    # 5. Ensure Equations are Safe (Top of screen)
    # to_edge(UP) -> to_edge(UP, buff=1.0)
    code = re.sub(r'to_edge\(UP\)', 'to_edge(UP, buff=1.0)', code)
    code = re.sub(r'to_edge\(UP,\s*buff=0\.[1-9]\)', 'to_edge(UP, buff=1.0)', code)
    
    # 6. Increase General Spacing (Buffs)
    # buff=0.1/0.2/0.3/0.4/0.5 -> buff=0.8 (EXCEPT SurroundingRectangle)
    # We do this carefully to not break SurroundingRectangle which needs small buffs
    # code = re.sub(r'buff\s*=\s*0\.[1-5]', 'buff=0.8', code) # Too aggressive
    
    # 7. Cap Font Sizes
    # font_size=48/42 -> font_size=36
    code = re.sub(r'font_size\s*=\s*[4-9]\d', 'font_size=36', code)
    # font_size=38 -> font_size=32
    code = re.sub(r'font_size\s*=\s*3[8-9]', 'font_size=32', code)
    
    # 8. Fix SurroundingRectangle Buffs (Prevent overlap)
    # buff=0.8/0.5 -> buff=0.2 for SurroundingRectangle
    # This is hard to do with regex safely, but we can try to catch common cases
    # SurroundingRectangle(..., buff=LARGE) -> buff=0.2
    # code = re.sub(r'SurroundingRectangle\((.*?),.*buff=[0-9.]+\)', r'SurroundingRectangle(\1, color=YELLOW, buff=0.2)', code)
    
    # 9. Fix Bottom Margin (Prevent cut-off)
    # move_to(DOWN * 3/3.5/4) -> move_to(DOWN * 2.5)
    code = re.sub(r'move_to\(DOWN\s*\*\s*[3-9](\.\d+)?\)', 'move_to(DOWN * 2.5)', code)
    
    # 10. Cap Vertical Height (Title Exclusion Zone)
    # Prevent objects from going above Y=3.0 (reserved for title)
    # We look for UP * 3.X and cap it at UP * 2.5 for safety
    code = re.sub(r'UP\s*\*\s*3\.[1-9]', 'UP * 2.5', code)
    code = re.sub(r'UP\s*\*\s*3(\s*[^.])', r'UP * 2.5\1', code)  # Exact UP * 3
    
    # 11. Fix Arrow Labels (Prevent hitting title)
    # If labeling an arrow/vector with UP, change to RIGHT
    # Pattern: .next_to(arrow, UP) -> .next_to(arrow, RIGHT)
    # We match any variable name that *looks* like it might be an arrow (contains "arrow" or "vector")
    code = re.sub(r'\.next_to\(\s*([a-zA-Z0-9_]*arrow[a-zA-Z0-9_]*)\s*,\s*UP', r'.next_to(\1, RIGHT', code, flags=re.IGNORECASE)
    code = re.sub(r'\.next_to\(\s*([a-zA-Z0-9_]*vector[a-zA-Z0-9_]*)\s*,\s*UP', r'.next_to(\1, RIGHT', code, flags=re.IGNORECASE)
    
    # 12. Fix Invalid Colors (Hallucinations)
    # LIGHT_BLUE -> TEAL_B
    code = code.replace('LIGHT_BLUE', 'TEAL_B')
    code = code.replace('LIGHT_RED', 'RED_A')
    code = code.replace('LIGHT_GREEN', 'GREEN_A')
    
    return code


def fix_missing_imports(code: str) -> str:
    """
    Add missing imports for common libraries if they are used but not imported.
    """
    lines = code.split('\n')
    
    # Check for random usage without import
    # We check for 'random.' usage and ensure 'import random' is present
    if 'random.' in code and not any(line.strip().startswith('import random') for line in lines):
        # Find insertion point (after last import)
        insert_idx = 0
        for i, line in enumerate(lines):
            if line.startswith('import ') or line.startswith('from '):
                insert_idx = i + 1
        
        lines.insert(insert_idx, 'import random')
        return '\n'.join(lines)
        
    return code


def post_process_code(code: str) -> str:
    """
    Main entry point for code post-processing.
    
    Applies all fixes to AI-generated Manim code.
    
    Args:
        code: Raw generated code (may have markdown fences)
    
    Returns:
        Cleaned and fixed code
    """
    # Step 1: Extract code from markdown if needed
    code = extract_code_from_markdown(code)
    
    # Step 2: Apply fixes in order
    code = fix_missing_imports(code)
    code = fix_surrounding_rectangles(code)
    code = fix_layout_issues(code)
    
    # Validate Python syntax
    is_valid, error_msg = validate_python_syntax(code)
    if not is_valid:
        print(f"⚠️  WARNING: Generated code has syntax errors:")
        print(f"   {error_msg}")
        print(f"   The code may fail to render. Attempting to continue anyway...")
        # Add warning comment at top
        warning_header = f"""# ⚠️  SYNTAX ERROR DETECTED:
# {error_msg}
# This code may fail to render. Please review and fix manually.

"""
        code = warning_header + code
    
    # Add header comment explaining post-processing
    header = """# NOTE: This code has been automatically post-processed to fix common issues:
# - Indexed SurroundingRectangle calls have been disabled
# - Layout spacing has been adjusted to prevent overlaps
# - Axis labels have been positioned to stay within frame
# - Font sizes have been capped to prevent massive text

"""
    
    # Only add header if we actually made changes
    if '# Auto-disabled:' in code or '# Auto-fix:' in code or '# Warning:' in code or '# Note:' in code or '# ⚠️  SYNTAX ERROR DETECTED:' in code:
        code = header + code
    
    return code


def validate_python_syntax(code: str) -> tuple[bool, str]:
    """
    Validate that the generated code is syntactically correct Python.
    
    Args:
        code: Python code string
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    import ast
    
    try:
        ast.parse(code)
        return True, ""
    except SyntaxError as e:
        error_msg = f"Line {e.lineno}: {e.msg}"
        if e.text:
            error_msg += f" - Near: {e.text.strip()}"
        return False, error_msg
    except Exception as e:
        return False, f"Unknown parsing error: {str(e)}"


def get_visual_layout_prompt() -> str:
    """
    Get enhanced system prompt that instructs Gemini 3 Pro to avoid layout issues.
    """
    return """
## CRITICAL LAYOUT REQUIREMENTS (Visual Spacing)

You are generating code that will create VISUAL output. Pay extreme attention to spatial layout:

### Frame Boundaries
- Frame dimensions: Approximately -7 to +7 horizontally, -4 to +4 vertically
- Safe zone: Keep all text within -6 to +6 (X) and -3.5 to +3.5 (Y)

### Axis Labels - CRITICAL RULES
1. Y-axis labels: ALWAYS use direction=LEFT parameter and shift(LEFT * 0.6)
2. X-axis labels: Keep text SHORT (max 10 characters) and shift(DOWN * 0.4)

### Spacing Between Elements
1. Always use buff parameter in .next_to() (minimum 0.4)
2. Minimum buff values:
   - Text near text: buff=0.4 minimum
   - Text near graphs: buff=0.5 minimum
   - Title to content: buff=0.6 minimum

### Visual Checklist:
- Are y-axis labels positioned LEFT with shift?
- Do all .next_to() calls have buff >= 0.4?
- Are axis labels short?
- Is all text within safe zone?
- Are multiple labels spaced vertically?
- Are font sizes appropriate?

REMEMBER: You are creating VISUAL output. Prevent overlaps BEFORE they happen!
"""


def validate_code_structure(code: str) -> List[str]:
    """
    Validate the generated code for common issues.
    
    Returns:
        List of warning messages (empty if no issues)
    """
    warnings = []
    
    # Check for common issues
    if 'SurroundingRectangle(' in code:
        if re.search(r'SurroundingRectangle\([^,\)]*\[\d+\]', code):
            warnings.append("Code contains indexed SurroundingRectangle calls (will be auto-fixed)")
    
    if 'from manim_voiceover.services.gtts import GTTSService' in code:
        warnings.append("Code still uses deprecated GTTSService (should use ElevenLabsService)")
    
    # New layout validations
    if 'get_y_axis_label' in code and 'direction=LEFT' not in code:
        warnings.append("Y-axis labels should use direction=LEFT to avoid overlap")
    
    if '.next_to(' in code:
        # Count next_to calls without buff
        import re
        next_to_calls = re.findall(r'\.next_to\([^)]+\)', code)
        no_buff_count = sum(1 for call in next_to_calls if 'buff=' not in call)
        if no_buff_count > 0:
            warnings.append(f"{no_buff_count} .next_to() calls missing buff parameter (risk of overlap)")
    
    return warnings
