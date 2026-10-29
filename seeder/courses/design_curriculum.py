"""
UI/UX Design & Product Strategy Curriculums
Contains:
1. UI/UX Design Systems & Visual Hierarchy (15 Days)
2. Product Design, Wireframing & Figma Prototyping (15 Days)
"""

from seeder.curriculum_builder import make_day, make_course

# =========================================================================
# COURSE 1: UI/UX Design Systems & Visual Hierarchy (15 Days)
# =========================================================================
DESIGN_SYS_DAYS = []

ds_titles = {
    1: ("The 8pt Spatial Grid & Mathematical Layouts", "Modern screen layouts align to an 8-point spatial system for visual consistency and seamless developer handoff.", "Laying uniform ceramic tiles on a floor; if every tile is 8cm, cuts and grout lines align with mathematical perfection."),
    2: ("Visual Hierarchy: Scale, Weight & Contrast Levers", "Direct user attention using size, font weight, and tonal contrast rather than rainbow colors.", "A front-page newspaper; the eye hits the headline first, then the photo, then the subhead, and finally body text."),
    3: ("Color Theory: Palettes, Shades & The 60-30-10 Rule", "Distribute visual weight: 60% dominant neutral background, 30% secondary structure, 10% high-contrast brand accent.", "A tailored suit: 60% charcoal jacket and trousers, 30% crisp white shirt, 10% vibrant burgundy silk tie."),
    4: ("Typography Scales & Font Pairing Harmonization", "Use a mathematical type scale (1.25 Major Third) to create proportional headings and readable body copy.", "A musical chord progression; notes are separated by mathematical harmonic intervals that sound pleasant to the ear."),
    5: ("WCAG 2.1 Accessibility: Contrast Ratios & Alt Text", "Ensure software is usable for people with disabilities, requiring >= 4.5:1 contrast for normal text.", "A wheelchair ramp on a public building; designing for accessibility creates a better experience for everyone."),
    6: ("Design Tokens: Variables, Aliases & System Synchronization", "Tokens capture visual constants as platform-agnostic code variables.", "A master currency exchange board; updating the central dollar exchange rate immediately propagates across all branch registers."),
    7: ("Iconography, SVG Optimization & Visual Metaphors", "Icons must possess uniform bounding boxes, stroke weights, and universally recognized metaphors.", "International airport road signs; whether you land in Tokyo or Paris, the restroom and exit symbols are instantly clear."),
    8: ("Micro-Interactions, Hover States & Animated Feedback", "Interactive feedback confirms user actions and imparts tactile delight to digital products.", "The satisfying mechanical click and slight haptic vibration when turning a luxury car's volume dial."),
    9: ("Card Component Anatomy & Information Chunking", "Group related information into scannable cards with consistent padding, borders, and actions.", "A collection of clean baseball cards; each card holds a photo, stats, and biography in the exact same structured layout."),
    10: ("Form Design: Inputs, Labels & Validation Error States", "Design low-friction forms with clear labels, floating help text, and real-time inline validation.", "A passport application form with clear numbered boxes; it tells you immediately if you missed your birthday before you submit."),
    11: ("Navigation Patterns: Sidebars, Tab Bars & Breadcrumbs", "Navigation informs users where they are, where they have been, and where they can go next.", "A hiking trail with color-coded wooden trail markers at every fork so hikers never feel lost in the forest."),
    12: ("Dark Mode Theming: Contrast, Elevation & True Blacks", "Dark mode requires surface elevation using lighter gray tints rather than harsh pure black.", "A moonlit landscape; trees and hills are distinguishable by subtle gradients of deep navy and charcoal, not pitch blackness."),
    13: ("Responsive Breakpoints & Fluid Container Layouts", "Fluid grids adapt content harmoniously from 360px mobile screens to 4K ultra-wide monitors.", "Water poured into a cup becomes the cup; responsive layouts reshape naturally to fit the device viewport."),
    14: ("Design QA, Auditing & Eliminating Inconsistencies", "Audit live code against Figma designs to eliminate padding drift, font mismatches, and broken states.", "A building inspector walking through a newly framed house with a level and tape measure to ensure walls are true."),
    15: ("Capstone: Architecting an Enterprise Multi-Brand Design System", "Construct a scalable design system with tokens, atoms, components, and documentation.", "You are a senior design systems architect ready to lead enterprise design operations.")
}

for day_num in range(1, 16):
    t_info = ds_titles.get(day_num, (f"Day {day_num}: Design System Engineering", "Scale visual systems.", "Mathematical design."))
    DESIGN_SYS_DAYS.append(make_day(
        order=day_num,
        title=f"Day {day_num}: {t_info[0]}",
        concept=t_info[1],
        analogy=t_info[2],
        sections=[
            (f"Visual Architecture of {t_info[0]}", f"Mastering {t_info[0]} gives designers and frontend developers a shared language of tokens, spacing, and accessibility that scales across multi-platform products."),
            ("Practical Component Engineering & Guidelines", "Build scalable components with documented states (Default, Hover, Active, Disabled, Loading) that pass WCAG compliance with zero regressions.")
        ],
        snippets=[
            (f"{t_info[0]} CSS Design Tokens", f"""/* Design Tokens for Day {day_num} */
:root {{
  --spacing-unit-{day_num}: 8px;
  --color-primary-{day_num}: #EC4899;
  --elevation-surface-{day_num}: #1E293B;
  --radius-component-{day_num}: 8px;
}}""", "css"),
            ("Contrast Ratio Validator (Python)", """def check_wcag_compliance(ratio: float) -> str:
    if ratio >= 7.0: return 'AAA (Enhanced)'
    if ratio >= 4.5: return 'AA (Standard Pass)'
    if ratio >= 3.0: return 'AA Large Text Only'
    return 'FAIL (Inaccessible)'

print("Contrast 5.2:1 ->", check_wcag_compliance(5.2))""", "python")
        ],
        challenge=(f"Design Challenge Day {day_num}", "Write a function `round_to_8pt_grid(pixels)` that rounds any integer pixel value to the nearest multiple of 8.",
                   "def round_to_8pt_grid(pixels: int) -> int:\n    pass",
                   "def round_to_8pt_grid(pixels: int) -> int:\n    return round(pixels / 8.0) * 8", "24"),
        quizzes=[
            (f"What is the foundational principle of {t_info[0]}?", [f"To leverage {t_info[0]} to create consistent, accessible, and mathematically harmonious UI", "To use as many random fonts as possible", "To hide all text from users", "To make every button purple"], f"To leverage {t_info[0]} to create consistent, accessible, and mathematically harmonious UI", f"Day {day_num} focuses on {t_info[0]}."),
            ("Why is the 8pt grid the industry standard across digital product design?", ["Most screen resolutions divide cleanly by 8, preventing anti-aliasing rendering blur", "It is the only grid format approved by the government", "It was invented in 1920 for printing newspapers", "It makes websites load 100x faster"], "Most screen resolutions divide cleanly by 8, preventing anti-aliasing rendering blur", "The 8pt grid scales crisply across 1x, 2x, and 3x screen densities."),
            ("What does the 60-30-10 rule dictate in color distribution?", ["60% dominant neutral, 30% secondary structure/cards, 10% vibrant accent for CTAs", "60 colors, 30 fonts, 10 images", "60% transparent, 30% opaque, 10% visible", "60 buttons on every screen"], "60% dominant neutral, 30% secondary structure/cards, 10% vibrant accent for CTAs", "This ratio creates balanced visual weight without sensory overload."),
            ("What is the minimum WCAG 2.1 AA contrast requirement for standard body text?", ["4.5:1 contrast ratio against the background", "1.5:1", "100:1", "Contrast does not matter"], "4.5:1 contrast ratio against the background", "4.5:1 ensures users with vision impairments can comfortably read text."),
            ("Why are Design Tokens preferred over hardcoded hex values in codebases?", ["Tokens allow global theme updates (e.g. dark mode) from a single source of truth across iOS, Android, and Web", "Tokens are faster to type", "Hardcoded hex values are illegal in open source software", "Tokens decrease computer battery usage"], "Tokens allow global theme updates (e.g. dark mode) from a single source of truth across iOS, Android, and Web", "Tokens unify design constants across multiple engineering repositories.")
        ]
    ))

DESIGN_SYSTEMS_BLUEPRINT = make_course(
    title="UI/UX Design Systems & Visual Hierarchy",
    category="Design",
    description=(
        "The complete 15-Day masterclass on modern design systems and visual interface engineering. "
        "Master the 8pt spatial grid, typography scales, color theory (60-30-10), WCAG 2.1 accessibility, "
        "design tokens, dark mode elevation, and enterprise multi-brand component libraries."
    ),
    color="#EC4899",
    days=DESIGN_SYS_DAYS
)


# =========================================================================
# COURSE 2: Product Design, Wireframing & Figma Prototyping (15 Days)
# =========================================================================
FIGMA_DAYS = []

figma_titles = {
    1: ("The Design Thinking Process: Empathize to Test", "Design thinking is a human-centered innovation framework that solves validated user problems.", "A detective solving a mystery; you interview witnesses, gather evidence, form hypotheses, and test them with clues."),
    2: ("User Research, Empathy Maps & Journey Mapping", "Map the emotional highs and lows a user experiences as they navigate a product workflow.", "Plotting a roller coaster ride; you identify where riders feel thrill and where they feel motion sickness."),
    3: ("Information Architecture & Sitemaps", "Organize complex software features into intuitive, hierarchical mental models.", "The index and table of contents of an encyclopedia; finding any topic takes three logical clicks."),
    4: ("Low-Fidelity Wireframing & Rapid Paper Prototyping", "Sketch layouts rapidly on paper or wireframes before committing to high-fidelity pixels.", "An architect sketching floor plans on napkins during lunch before drafting 3D CAD blueprints."),
    5: ("Figma Core: Frames, Vector Networks & Groups", "Frames are powerful layout containers that behave like responsive HTML divs.", "A picture frame that automatically expands or contracts as you insert different sized canvases."),
    6: ("Auto Layout Mastery: Padding, Gap & Resizing Constraints", "Auto Layout mimics CSS flexbox, allowing buttons and cards to resize dynamically with content.", "A stretchy spandex shirt that expands naturally as you breathe and contracts when you exhale."),
    7: ("Figma Component Sets, Variants & Component Properties", "Create multi-state components (Hover, Pressed, Disabled) with boolean toggle properties.", "A Swiss Army Knife; one tool handle holding folding scissors, blades, and bottle openers in a unified unit."),
    8: ("Interactive Prototyping: Smart Animate & Overlays", "Connect screens with micro-transitions that simulate a fully coded native mobile app.", "A stop-motion animation flipbook; flipping pages rapidly creates fluid lifelike movement."),
    9: ("Conducting Usability Testing & Synthesizing Findings", "Watch real users attempt specific tasks to uncover usability friction and confusing copy.", "A one-way mirror in a test kitchen watching chefs try a new knife without giving them instructions."),
    10: ("Heuristic Evaluation: Nielsen's 10 Usability Principles", "Audit interfaces against time-tested human factors engineering principles (e.g. error prevention, recognition over recall).", "A pilot pre-flight inspection checklist; ensuring landing gear, flaps, and instruments meet standard tolerances."),
    11: ("Mobile App Onboarding & Reducing Time-to-Value (TTV)", "Guide users to their core value proposition in under 3 taps without boring intro carousels.", "A friendly hotel concierge who carries your bags directly to your room rather than making you read a 20-page hotel handbook."),
    12: ("SaaS Dashboard Layouts & Data Visualization UX", "Present complex analytical metrics through progressive disclosure and scannable visual cards.", "A high-speed train control cabin; the engineer sees the primary track speed and brake pressure front and center."),
    13: ("Figma Variables: Scopes, Modes & Theme Switching", "Use native Figma Variables to switch between light mode, dark mode, and languages instantly.", "Wearing polarized sunglasses; the underlying world remains identical, but the tint and contrast shift seamlessly."),
    14: ("Developer Handoff: Inspect Panel, Redlines & Spec Docs", "Deliver production-ready Figma specs with exported SVG assets, CSS tokens, and edge cases.", "A master architect handing blueprints with exact millimeter measurements to the general contractor."),
    15: ("Capstone: Complete End-to-End Mobile App Case Study", "Synthesize user research, wireframes, component design, and interactive prototypes into a portfolio case study.", "You are a professional product designer capable of leading UI/UX from initial concept to live launch.")
}

for day_num in range(1, 16):
    t_info = figma_titles.get(day_num, (f"Day {day_num}: Product Design", "Design user experiences.", "Iterative product design."))
    FIGMA_DAYS.append(make_day(
        order=day_num,
        title=f"Day {day_num}: {t_info[0]}",
        concept=t_info[1],
        analogy=t_info[2],
        sections=[
            (f"Product Methodology for {t_info[0]}", f"Mastering {t_info[0]} enables product designers to validate user workflows rapidly, reduce engineering rework, and launch intuitive, engaging software."),
            ("Figma Workflow & User Testing Protocols", "Construct responsive Auto Layout components, wire up Smart Animate micro-interactions, and conduct task-based usability testing sessions.")
        ],
        snippets=[
            (f"{t_info[0]} Design Tokens (Figma/JSON)", f"""{{
  "component": "{t_info[0]}",
  "auto_layout": {{
    "direction": "HORIZONTAL",
    "padding": 16,
    "gap": 8
  }},
  "day": {day_num}
}}""", "json"),
            ("Usability Task Success Rate Calculator (Python)", """def calculate_task_success_rate(completed: int, total_participants: int) -> dict:
    pct = round((completed / total_participants) * 100, 1) if total_participants > 0 else 0.0
    status = 'EXCELLENT' if pct >= 80.0 else 'NEEDS_ITERATION'
    return {'success_rate': pct, 'status': status}

print("Task Completion:", calculate_task_success_rate(9, 10))""", "python")
        ],
        challenge=(f"Product UX Challenge Day {day_num}", "Write a function `calculate_sus_score(raw_sum_answers)` that multiplies a raw score by 2.5 and returns the System Usability Scale (SUS) score.",
                   "def calculate_sus_score(raw_sum_answers: float) -> float:\n    pass",
                   "def calculate_sus_score(raw_sum_answers: float) -> float:\n    return raw_sum_answers * 2.5", "85.0"),
        quizzes=[
            (f"What is the primary objective of {t_info[0]}?", [f"To leverage {t_info[0]} to create intuitive, human-centered digital products", "To make designs as confusing as possible", "To avoid testing prototypes with real users", "To delete the Figma project file"], f"To leverage {t_info[0]} to create intuitive, human-centered digital products", f"Day {day_num} focuses on {t_info[0]}."),
            ("What does Auto Layout in Figma enable designers to do?", ["Create components that dynamically resize based on their content, mimicking CSS Flexbox", "Automatically code the backend in C++", "Draw freehand oil paintings", "Upload apps directly to the Google Play Store"], "Create components that dynamically resize based on their content, mimicking CSS Flexbox", "Auto Layout ensures responsive resizing and consistent internal padding."),
            ("Why are low-fidelity paper wireframes valuable before high-fidelity visual design?", ["They allow rapid iteration on layout and user flow without getting distracted by colors and fonts", "They take longer to make than finished code", "They are legally required for patents", "They use less computer battery"], "They allow rapid iteration on layout and user flow without getting distracted by colors and fonts", "Low-fi sketches explore broad structural options with near-zero time investment."),
            ("What is the primary rule of conducting a usability test?", ["Observe what users do without leading them or explaining how the UI works", "Interrupt the user every 5 seconds to tell them they are wrong", "Do the test for the user while they watch", "Argue with the user if they cannot find a button"], "Observe what users do without leading them or explaining how the UI works", "True usability tests uncover genuine friction by observing unguided behavior."),
            ("What does Smart Animate in Figma do during prototyping?", ["Seamlessly interpolates position, size, and opacity between identical layer names across screens", "Generates artificial intelligence voice narration", "Converts wireframes into 3D holograms", "Deletes redundant prototype noodles"], "Seamlessly interpolates position, size, and opacity between identical layer names across screens", "Smart Animate creates smooth, realistic micro-interactions between screens.")
        ]
    ))

FIGMA_PROTOTYPING_BLUEPRINT = make_course(
    title="Product Design, Wireframing & Figma Prototyping",
    category="Design",
    description=(
        "The end-to-end 15-Day curriculum on UX research, wireframing, and Figma prototyping mastery. "
        "Master the Design Thinking process, user journey maps, Auto Layout constraints, component variants, "
        "interactive Smart Animate prototypes, usability testing, and seamless developer handoff."
    ),
    color="#DB2777",
    days=FIGMA_DAYS
)
