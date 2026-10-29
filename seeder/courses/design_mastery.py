"""
UI/UX Design Systems & Visual Design Mastery Blueprint
Comprehensive curriculum covering visual hierarchy, design tokens, color theory,
typography systems, wireframing, WCAG accessibility, and scalable UI components.
"""

from seeder.course_blueprint import (
    CourseBlueprint,
    DayBlueprint,
    QuizQuestionBlueprint,
    CodingChallengeBlueprint,
)

DAYS = [
    DayBlueprint(
        order=1,
        title="Day 1: Visual Hierarchy & The 8pt Spatial System",
        concept="Visual hierarchy directs the user's subconscious attention through scale, contrast, and mathematical spacing.",
        analogy="Think of a newspaper front page. You don't read every sentence sequentially; your eyes instantly jump to the huge bold headline, then the photograph, then the subhead, and finally the body text. That order is created purely by visual hierarchy.",
        theory_sections=[
            {
                "heading": "The 8pt Spatial Grid Rule",
                "body": "Modern responsive digital interfaces are built on an 8-point spatial system (8px, 16px, 24px, 32px, 48px, 64px). Because virtually all modern screen resolutions are divisible by 8 (or 4 for micro-spacing), sticking to this grid eliminates visual friction and aligns designs cleanly with code tokens."
            },
            {
                "heading": "The 3 Levers of Hierarchy: Size, Weight, and Contrast",
                "body": "When designing cards or screens, never rely on size alone. Use contrasting font weights (Bold vs Medium) and muted neutral text colors (e.g., #0F172A for headings, #64748B for subtitles) to establish instant scanning order without clutter."
            }
        ],
        code_snippets=[
            {
                "title": "Design Tokens Configuration (CSS)",
                "explanation": "Standardized spatial and typography tokens based on the 8pt system.",
                "language": "css",
                "code": """:root {
  /* Spatial System (8pt Grid) */
  --space-1: 4px;   /* micro */
  --space-2: 8px;   /* xs */
  --space-3: 16px;  /* sm */
  --space-4: 24px;  /* md */
  --space-5: 32px;  /* lg */
  --space-6: 48px;  /* xl */
  --space-7: 64px;  /* 2xl */

  /* Type Scale (1.25 Major Third) */
  --font-xs: 0.75rem;   /* 12px */
  --font-sm: 0.875rem;  /* 14px */
  --font-base: 1rem;    /* 16px */
  --font-lg: 1.25rem;   /* 20px */
  --font-xl: 1.563rem;  /* 25px */
  --font-2xl: 1.953rem; /* 31px */
}"""
            },
            {
                "title": "Contrast Ratio Checker (Python)",
                "explanation": "Evaluates relative luminance between background and foreground to check WCAG compliance.",
                "language": "python",
                "code": """def calculate_relative_luminance(r: int, g: int, b: int) -> float:
    # Convert sRGB to linear luminance
    channels = [c / 255.0 for c in (r, g, b)]
    transformed = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return 0.2126 * transformed[0] + 0.7152 * transformed[1] + 0.0722 * transformed[2]

def get_contrast_ratio(rgb1: tuple, rgb2: tuple) -> float:
    l1 = calculate_relative_luminance(*rgb1)
    l2 = calculate_relative_luminance(*rgb2)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return round((lighter + 0.05) / (darker + 0.05), 2)

ratio = get_contrast_ratio((15, 23, 42), (255, 255, 255)) # Dark slate vs white
print(f"Contrast Ratio: {ratio}:1 (WCAG AAA >= 7.0:1)")"""
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="WCAG AA Contrast Evaluator",
            description="Write a function `is_wcag_aa_compliant(contrast_ratio, is_large_text)` that returns True if normal text meets >= 4.5:1 or large text meets >= 3.0:1.",
            starter_code="""def is_wcag_aa_compliant(contrast_ratio: float, is_large_text: bool) -> bool:
    # Your code here
    pass""",
            solution_code="""def is_wcag_aa_compliant(contrast_ratio: float, is_large_text: bool) -> bool:
    threshold = 3.0 if is_large_text else 4.5
    return contrast_ratio >= threshold""",
            expected_output="True"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="Why is the 8-point grid standard across modern UI/UX design?",
                options=[
                    "Most digital screen display resolutions divide cleanly into multiples of 8",
                    "It is the only grid format supported by HTML5 and CSS3 specifications",
                    "It reduces font sizes to ensure maximum information density",
                    "It prevents users from taking screenshots on mobile devices"
                ],
                correct_answer="Most digital screen display resolutions divide cleanly into multiples of 8",
                explanation="Multiples of 8 render sharply across varied pixel densities (1x, 2x, 3x) without anti-aliasing artifacts."
            ),
            QuizQuestionBlueprint(
                question="What is the minimum WCAG AA contrast ratio requirement for standard body text?",
                options=[
                    "4.5:1",
                    "1.5:1",
                    "10:1",
                    "2.0:1"
                ],
                correct_answer="4.5:1",
                explanation="WCAG 2.1 Level AA requires at least 4.5:1 for normal text and 3.0:1 for large text (18pt+ or 14pt bold)."
            ),
            QuizQuestionBlueprint(
                question="Which method creates the cleanest hierarchy between a card title and subtitle?",
                options=[
                    "Use high font weight and dark neutral color for title, and a lighter muted neutral for subtitle",
                    "Underline all words and make every letter uppercase",
                    "Make both lines exactly the same font size, weight, and color",
                    "Add three different flashing borders around each word"
                ],
                correct_answer="Use high font weight and dark neutral color for title, and a lighter muted neutral for subtitle",
                explanation="Contrasting font weight and color temperature creates an effortless scanning order without visual noise."
            ),
            QuizQuestionBlueprint(
                question="What are 'Design Tokens' in design systems engineering?",
                options=[
                    "Named entities that store design choices like colors, spacing, and typography across platforms",
                    "Cryptocurrency coins used to purchase stock design templates online",
                    "Single-use security passwords required to open design software",
                    "Vector icons stored exclusively in SVG format"
                ],
                correct_answer="Named entities that store design choices like colors, spacing, and typography across platforms",
                explanation="Design tokens capture visual constants (e.g. `--color-primary-500`) in code, keeping UI synchronized across platforms."
            ),
            QuizQuestionBlueprint(
                question="In UX design, what does 'Affordance' refer to?",
                options=[
                    "Visual cues that signal how an element is intended to be used (e.g. a 3D bevel on a button)",
                    "The total subscription cost of a design editing suite",
                    "The number of users who abandon an incomplete checkout form",
                    "The maximum file size permitted for bitmap assets"
                ],
                correct_answer="Visual cues that signal how an element is intended to be used (e.g. a 3D bevel on a button)",
                explanation="Affordances are design characteristics that intuitively communicate an object's function (e.g. a button looking clickable)."
            )
        ]
    ),
    DayBlueprint(
        order=2,
        title="Day 2: Component Architecture & Responsive Layouts",
        concept="Reusable components with clear variant states create consistent, scalable interfaces.",
        analogy="Think of building with Lego bricks. Rather than carving an entire plastic castle from a single block of wood, you snap together standardized, predictable bricks that can be rearranged into infinite configurations.",
        theory_sections=[
            {
                "heading": "Atomic Design Methodology",
                "body": "Atomic Design breaks interfaces down into 5 stages: Atoms (buttons, inputs, icons), Molecules (search bar with button), Organisms (header nav), Templates (page layouts), and Pages (live content instances). Building modular atoms first prevents visual divergence."
            },
            {
                "heading": "Stateful Component Design",
                "body": "A button is not just a rectangle; it is an interactive state machine. Every component must define Default, Hover, Focused (accessibility ring), Active/Pressed, Disabled, and Loading states."
            }
        ],
        code_snippets=[
            {
                "title": "Interactive Button Component (CSS)",
                "explanation": "Stateful styling with micro-transitions and accessible focus states.",
                "language": "css",
                "code": """.btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 12px 24px;
  background-color: #3B82F6;
  color: #FFFFFF;
  font-weight: 600;
  border-radius: 8px;
  transition: all 150ms cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
}

.btn-primary:hover {
  background-color: #2563EB;
  transform: translateY(-1px);
}

.btn-primary:focus-visible {
  outline: 2px solid #3B82F6;
  outline-offset: 2px;
}

.btn-primary:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  transform: none;
}"""
            },
            {
                "title": "Component Variant Prop Validator (Python)",
                "explanation": "Validates allowed variant tokens for a design component.",
                "language": "python",
                "code": """ALLOWED_VARIANTS = {'primary', 'secondary', 'ghost', 'danger'}
ALLOWED_SIZES = {'sm', 'md', 'lg'}

def validate_button_props(variant: str, size: str) -> bool:
    return variant in ALLOWED_VARIANTS and size in ALLOWED_SIZES

print("Valid:", validate_button_props('primary', 'md'))    # True
print("Invalid:", validate_button_props('huge', 'xxl'))    # False"""
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Compute Touch Target Padding",
            description="Write a function `ensure_min_touch_target(current_size_px, min_size_px=48)` that returns the padding needed on each side to reach the accessible 48px touch target.",
            starter_code="""def ensure_min_touch_target(current_size_px: int, min_size_px: int = 48) -> int:
    # Your code here
    pass""",
            solution_code="""def ensure_min_touch_target(current_size_px: int, min_size_px: int = 48) -> int:
    if current_size_px >= min_size_px:
        return 0
    diff = min_size_px - current_size_px
    return (diff + 1) // 2""",
            expected_output="12"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the recommended minimum interactive touch target size for mobile UI?",
                options=[
                    "44px by 44px (iOS) / 48dp by 48dp (Android)",
                    "10px by 10px",
                    "120px by 120px",
                    "There is no minimum recommendation"
                ],
                correct_answer="44px by 44px (iOS) / 48dp by 48dp (Android)",
                explanation="Standard mobile guidelines specify 44-48px targets so fingers can reliably tap without accidental misclicks."
            ),
            QuizQuestionBlueprint(
                question="In Atomic Design, what represents an 'Organism'?",
                options=[
                    "A complex distinct UI section composed of molecules and atoms, like a Navigation Bar",
                    "A single HTML color hex code",
                    "A raw SVG vector path with no styling",
                    "A whole multi-page marketing website"
                ],
                correct_answer="A complex distinct UI section composed of molecules and atoms, like a Navigation Bar",
                explanation="Organisms are relatively complex UI components formed by groups of molecules and atoms joined together."
            ),
            QuizQuestionBlueprint(
                question="Why is the `:focus-visible` CSS pseudo-class critical in accessible design?",
                options=[
                    "It displays a clear outline for keyboard navigators while keeping mouse clicks clean",
                    "It hides the entire element from screen readers",
                    "It changes the font size based on the device's battery level",
                    "It prevents users from inspecting the website's source code"
                ],
                correct_answer="It displays a clear outline for keyboard navigators while keeping mouse clicks clean",
                explanation=":focus-visible shows a focus indicator when navigating via keyboard without annoying mouse users with outlines."
            ),
            QuizQuestionBlueprint(
                question="What does 'Mobile-First' responsive design dictate?",
                options=[
                    "Designing for the most constrained screen first, then progressively enhancing for larger viewports",
                    "Only publishing mobile native apps and deleting desktop websites",
                    "Disabling all images when viewed on desktop monitors",
                    "Using non-vector low-resolution graphics on all platforms"
                ],
                correct_answer="Designing for the most constrained screen first, then progressively enhancing for larger viewports",
                explanation="Mobile-first forces focus on the core value proposition and essential content before adding complex desktop layouts."
            ),
            QuizQuestionBlueprint(
                question="What is the primary benefit of documenting component states (Hover, Active, Disabled)?",
                options=[
                    "Eliminates ambiguity for developers and guarantees seamless user feedback during interactions",
                    "Automatically compiles backend SQL queries",
                    "Reduces the server hosting costs of the database",
                    "Prevents external APIs from timing out"
                ],
                correct_answer="Eliminates ambiguity for developers and guarantees seamless user feedback during interactions",
                explanation="Specifying all states ensures users receive visual cues and developers build accessible interactive widgets without guessing."
            )
        ]
    )
]

DESIGN_MASTERY_COURSE_BLUEPRINT = CourseBlueprint(
    title="UI/UX Design Systems & Visual Design",
    category="Design",
    description=(
        "The end-to-end masterclass on modern UI/UX design. Master spatial grids (8pt system), "
        "color theory, WCAG accessibility, typography scaling, responsive component architectures, "
        "and seamless developer handoffs for web and mobile platforms."
    ),
    color="#EC4899",
    days=DAYS
)
