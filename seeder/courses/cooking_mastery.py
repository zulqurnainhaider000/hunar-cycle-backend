"""
Culinary Arts, Recipe Formulation & Food Safety Mastery Blueprint
Comprehensive curriculum covering kitchen knife skills, the science of heat transfer,
food safety (HACCP), seasoning & flavor profiles, baker's percentages, and catering prep.
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
        title="Day 1: Kitchen Knife Fundamentals & Mise en Place",
        concept="Mastery of professional cooking begins with disciplined preparation (Mise en Place) and uniform knife cuts.",
        analogy="Think of cooking like a theatrical stage play. The actor cannot pause mid-monologue to build the stage lights or write their script. Everything—props, lighting, costumes—must be pre-positioned. That is 'Mise en Place' (everything in its place) in a professional kitchen.",
        theory_sections=[
            {
                "heading": "The French Classical Knife Cuts",
                "body": "Uniform cutting is not just about aesthetics; it guarantees that every piece of food cooks at the exact same rate. Classical cuts include Brunoise (1/8 inch dice), Small Dice (1/4 inch), Medium Dice (1/2 inch), Batonnet (1/4 x 1/4 x 2 inches), and Julienne (1/8 x 1/8 x 2 inches)."
            },
            {
                "heading": "The Anatomy of Knife Safety and the 'Claw Grip'",
                "body": "Always curl your guide fingers inward like a bear claw, with the flat side of the chef's knife blade resting gently against your knuckles. This guarantees the blade cannot physically touch your fingertips during rapid chopping."
            }
        ],
        code_snippets=[
            {
                "title": "Kitchen Prep Scaler (Python)",
                "explanation": "Calculates ingredient weights dynamically based on serving size.",
                "language": "python",
                "code": """def scale_recipe_ingredients(base_servings: int, target_servings: int, ingredients: dict) -> dict:
    multiplier = target_servings / base_servings
    scaled = {}
    for item, weight_grams in ingredients.items():
        scaled[item] = round(weight_grams * multiplier, 1)
    return scaled

base = {'onions': 200.0, 'carrots': 100.0, 'celery': 100.0, 'butter': 50.0}
print("Scaled for 12 servings:", scale_recipe_ingredients(4, 12, base))"""
            },
            {
                "title": "Knife Cut Dimensions Verifier",
                "explanation": "Verifies that cut dimensions match classical culinary culinary standards.",
                "language": "python",
                "code": """CUT_SPECS_MM = {
    'julienne': (3.0, 3.0, 50.0),
    'brunoise': (3.0, 3.0, 3.0),
    'batonnet': (6.0, 6.0, 50.0),
    'small_dice': (6.0, 6.0, 6.0)
}

def verify_knife_cut(cut_name: str, width: float, height: float, length: float) -> bool:
    expected = CUT_SPECS_MM.get(cut_name.lower())
    if not expected:
        return False
    return (abs(width - expected[0]) <= 0.5 and 
            abs(height - expected[1]) <= 0.5 and 
            abs(length - expected[2]) <= 1.0)

print("Brunoise Accuracy Check:", verify_knife_cut('brunoise', 3.1, 3.0, 3.0))"""
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Mirepoix Ratio Calculator",
            description="Write a function `calculate_mirepoix(total_weight_g)` that returns a tuple of `(onions_g, carrots_g, celery_g)` following the classic 2:1:1 French ratio.",
            starter_code="""def calculate_mirepoix(total_weight_g: float) -> tuple:
    # Your code here
    pass""",
            solution_code="""def calculate_mirepoix(total_weight_g: float) -> tuple:
    onions = round(total_weight_g * 0.5, 1)
    carrots = round(total_weight_g * 0.25, 1)
    celery = round(total_weight_g * 0.25, 1)
    return (onions, carrots, celery)""",
            expected_output="(200.0, 100.0, 100.0)"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What does the French culinary term 'Mise en Place' literally mean?",
                options=[
                    "Everything in its place",
                    "Cooked to medium-rare",
                    "Seasoned with fresh black pepper",
                    "Cleaned with boiling water"
                ],
                correct_answer="Everything in its place",
                explanation="Mise en place means organizing and prepping all ingredients and utensils before firing the stove."
            ),
            QuizQuestionBlueprint(
                question="What is the traditional weight ratio for a classical French Mirepoix?",
                options=[
                    "2 parts Onions, 1 part Carrots, 1 part Celery (2:1:1)",
                    "1 part Onions, 1 part Carrots, 1 part Celery (1:1:1)",
                    "3 parts Garlic, 1 part Ginger, 1 part Chili (3:1:1)",
                    "4 parts Tomatoes, 1 part Onions, 1 part Butter (4:1:1)"
                ],
                correct_answer="2 parts Onions, 1 part Carrots, 1 part Celery (2:1:1)",
                explanation="Classic mirepoix uses 50% onions, 25% carrots, and 25% celery by weight."
            ),
            QuizQuestionBlueprint(
                question="Why is uniform vegetable cutting essential in professional cooking?",
                options=[
                    "It ensures that all pieces cook evenly at the exact same rate",
                    "It doubles the nutritional vitamin content of the food",
                    "It allows vegetables to be stored without refrigeration",
                    "It is a legal health department requirement in all restaurants"
                ],
                correct_answer="It ensures that all pieces cook evenly at the exact same rate",
                explanation="Non-uniform cuts cause smaller pieces to turn to mush while larger chunks remain raw in the center."
            ),
            QuizQuestionBlueprint(
                question="What is the purpose of the 'Claw Grip' during knife work?",
                options=[
                    "Protects guide fingertips by curling nails inward away from the blade",
                    "Increases cutting speed by pressing the thumb against the cutting board",
                    "Allows the chef to hold three carrots simultaneously",
                    "Prevents the cutting board from sliding on the counter"
                ],
                correct_answer="Protects guide fingertips by curling nails inward away from the blade",
                explanation="The claw grip keeps fingertips curled safely away from the knife's path, resting knuckles against the blade."
            ),
            QuizQuestionBlueprint(
                question="What classical cut dimensions define a 'Julienne'?",
                options=[
                    "1/8 inch x 1/8 inch x 2 inches",
                    "1/2 inch x 1/2 inch x 1/2 inch",
                    "1 inch x 1 inch x 4 inches",
                    "Paper-thin round slices"
                ],
                correct_answer="1/8 inch x 1/8 inch x 2 inches",
                explanation="A classical Julienne (matchstick cut) measures precisely 1/8 in. x 1/8 in. x 2 in. (approx 3mm x 3mm x 50mm)."
            )
        ]
    ),
    DayBlueprint(
        order=2,
        title="Day 2: Heat Transfer, The Maillard Reaction & Food Safety (HACCP)",
        concept="Cooking is the chemistry of heat transfer; understanding the Danger Zone and Maillard reaction creates safe, flavorful food.",
        analogy="Think of searing a steak like developing a photograph under heat. If the pan isn't hot enough, the meat simply steams in its own gray juices. But at high dry heat, amino acids and sugars fuse to create hundreds of new flavor molecules—the Maillard crust.",
        theory_sections=[
            {
                "heading": "The Temperature Danger Zone & HACCP",
                "body": "The Temperature Danger Zone is between 40°F and 140°F (4°C - 60°C). Bacteria doubles every 20 minutes in this range. Perishable foods must never sit in the Danger Zone for more than 2 cumulative hours. Poultry must reach 165°F (74°C) internal temperature instantly to kill salmonella."
            },
            {
                "heading": "The Maillard Reaction vs Caramelization",
                "body": "Caramelization occurs above 320°F (160°C) with pure sugars. The Maillard reaction occurs between 280°F and 330°F (140°C - 165°C) between amino acids (proteins) and reducing sugars, producing complex savory, nutty, and roasted flavors. Excess surface moisture prevents Maillard browning by capping surface temperature at boiling (212°F / 100°C)."
            }
        ],
        code_snippets=[
            {
                "title": "HACCP Food Safety Temperature Auditor (Python)",
                "explanation": "Validates whether internal meat temperatures comply with FDA/HACCP health safety guidelines.",
                "language": "python",
                "code": """MIN_SAFE_TEMPS_F = {
    'poultry': 165,
    'ground_meat': 160,
    'beef_steak': 145,
    'pork': 145,
    'fish': 145
}

def audit_food_temp(item: str, temp_f: float) -> str:
    required = MIN_SAFE_TEMPS_F.get(item.lower())
    if not required:
        return "UNKNOWN_ITEM"
    return "SAFE TO SERVE" if temp_f >= required else f"UNSAFE: Needs at least {required}°F"

print("Chicken 166°F:", audit_food_temp('poultry', 166.0))
print("Chicken 150°F:", audit_food_temp('poultry', 150.0))"""
            },
            {
                "title": "Baker's Percentage Formula Calculator",
                "explanation": "Calculates ingredient weights scaled from flour weight in commercial baking.",
                "language": "python",
                "code": """def calculate_baker_formula(flour_weight_g: float, water_pct: float, salt_pct: float, yeast_pct: float) -> dict:
    return {
        'flour_g': flour_weight_g,
        'water_g': round(flour_weight_g * (water_pct / 100.0), 1),
        'salt_g': round(flour_weight_g * (salt_pct / 100.0), 1),
        'yeast_g': round(flour_weight_g * (yeast_pct / 100.0), 1),
    }

bread_batch = calculate_baker_formula(flour_weight_g=1000.0, water_pct=72.0, salt_pct=2.0, yeast_pct=1.0)
print("Sourdough Batch:", bread_batch)"""
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Baker's Hydration Checker",
            description="Write a function `calculate_hydration_percentage(water_g, flour_g)` that returns the hydration percentage rounded to 1 decimal place.",
            starter_code="""def calculate_hydration_percentage(water_g: float, flour_g: float) -> float:
    # Your code here
    pass""",
            solution_code="""def calculate_hydration_percentage(water_g: float, flour_g: float) -> float:
    if flour_g <= 0:
        return 0.0
    return round((water_g / flour_g) * 100, 1)""",
            expected_output="75.0"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the Temperature Danger Zone for food safety according to health guidelines?",
                options=[
                    "40°F to 140°F (4°C to 60°C)",
                    "0°F to 32°F (-18°C to 0°C)",
                    "180°F to 212°F (82°C to 100°C)",
                    "350°F to 400°F (175°C to 204°C)"
                ],
                correct_answer="40°F to 140°F (4°C to 60°C)",
                explanation="Pathogenic bacteria reproduce most rapidly between 40°F and 140°F (4°C to 60°C)."
            ),
            QuizQuestionBlueprint(
                question="What is the minimum safe internal cooking temperature for chicken and all poultry?",
                options=[
                    "165°F (74°C)",
                    "120°F (49°C)",
                    "140°F (60°C)",
                    "212°F (100°C)"
                ],
                correct_answer="165°F (74°C)",
                explanation="165°F (74°C) provides instant lethality against Salmonella and other foodborne pathogens in poultry."
            ),
            QuizQuestionBlueprint(
                question="What chemical reaction occurs between proteins and reducing sugars that causes golden-brown searing?",
                options=[
                    "The Maillard reaction",
                    "Fermentation",
                    "Emulsification",
                    "Hydrolysis"
                ],
                correct_answer="The Maillard reaction",
                explanation="The Maillard reaction is the chemical interaction between amino acids and reducing sugars under dry heat that produces deep savory flavors."
            ),
            QuizQuestionBlueprint(
                question="Why is patting meat dry with paper towels necessary before searing in a hot pan?",
                options=[
                    "Surface moisture boils at 212°F (100°C), steaming the meat and preventing Maillard browning",
                    "Moisture removes the natural salt content of the meat",
                    "Wet meat causes the cast iron skillet to shatter",
                    "Moisture causes the meat to become toxic"
                ],
                correct_answer="Surface moisture boils at 212°F (100°C), steaming the meat and preventing Maillard browning",
                explanation="Water absorbs thermal energy while evaporating at 212°F, preventing the pan from reaching the 280°F+ required for the Maillard reaction."
            ),
            QuizQuestionBlueprint(
                question="In Baker's Percentages, what ingredient is always set as the 100% baseline?",
                options=[
                    "Total Flour weight",
                    "Total Water weight",
                    "Total Yeast weight",
                    "Total Butter weight"
                ],
                correct_answer="Total Flour weight",
                explanation="In professional baking formulas, total flour weight represents 100%, and every other ingredient is expressed as a percentage of flour."
            )
        ]
    )
]

COOKING_MASTERY_COURSE_BLUEPRINT = CourseBlueprint(
    title="Culinary Arts & Food Safety Mastery",
    category="Cooking",
    description=(
        "The professional foundation in culinary arts and commercial kitchen management. "
        "Master classical French knife cuts, heat transfer science, the Maillard reaction, "
        "HACCP food safety compliance, seasoning formulas, and baker's percentages."
    ),
    color="#F97316",
    days=DAYS
)
