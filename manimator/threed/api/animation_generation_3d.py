"""
3D Animation Code Generation

Generates Manim code for 3D animations using LLM.
"""

import os
from typing import Optional
from litellm import completion
from .prompts_3d import get_3d_system_prompt, get_3d_examples


def generate_3d_animation_response(
    user_prompt: str,
    model: Optional[str] = None,
    include_examples: bool = True
) -> str:
    """
    Generate Manim 3D animation code from a text prompt.
    
    Args:
        user_prompt: User's description of the desired 3D animation
        model: LLM model to use (defaults to env variable CODE_GEN_MODEL)
        include_examples: Whether to include example code in the prompt
        
    Returns:
        Generated Python code for Manim 3D animation
        
    Example:
        >>> code = generate_3d_animation_response(
        ...     "Create a 3D animation showing a rotating DNA helix"
        ... )
        >>> print(code)
    """
    if model is None:
        model = os.getenv("CODE_GEN_MODEL", "anthropic/claude-sonnet-4.5")
    
    # Build system prompt
    system_prompt = get_3d_system_prompt()
    
    # Add examples if requested
    if include_examples:
        examples = get_3d_examples()
        examples_text = "\n\n".join([
            f"## {name.upper()} EXAMPLE\n{code}"
            for name, code in examples.items()
        ])
        system_prompt += f"\n\nHERE ARE SOME EXAMPLES:\n\n{examples_text}"
    
    # Build messages
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"""Create a complete, runnable Manim 3D animation for the following request:

{user_prompt}

Requirements:
1. Use ThreeDScene as base class
2. Include voiceover narration
3. Set appropriate camera angles
4. Make it educational and visually appealing
5. Include mathematical equations if relevant
6. Use smooth animations and camera movements
7. Aim for 2-5 minutes duration (or as specified)

Generate ONLY the Python code, nothing else."""}
    ]
    
    # Call LLM
    response = completion(
        model=model,
        messages=messages,
        temperature=0.7,
        max_tokens=4000
    )
    
    return response.choices[0].message.content


def generate_3d_animation_with_category(
    user_prompt: str,
    category: str,
    model: Optional[str] = None
) -> str:
    """
    Generate 3D animation code with a specific STEM category focus.
    
    Args:
        user_prompt: User's description
        category: One of 'mathematical', 'scientific', 'geometric', 'data'
        model: LLM model to use
        
    Returns:
        Generated Python code
    """
    category_prompts = {
        "mathematical": "Focus on mathematical accuracy and clear visualization of mathematical concepts.",
        "scientific": "Focus on scientific accuracy, realistic models, and clear explanations.",
        "geometric": "Focus on geometric properties, transformations, and spatial relationships.",
        "data": "Focus on clear data representation, appropriate chart types, and data-driven insights."
    }
    
    enhanced_prompt = f"""{user_prompt}

CATEGORY: {category.upper()}
{category_prompts.get(category, '')}
"""
    
    return generate_3d_animation_response(enhanced_prompt, model=model)
