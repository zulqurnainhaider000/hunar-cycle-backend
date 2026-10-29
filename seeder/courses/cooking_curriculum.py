"""
Culinary Arts & Food Science Curriculums
Contains:
1. Culinary Arts, Knife Skills & Flavor Science (15 Days)
2. Commercial Baking & Food Safety (HACCP) Mastery (15 Days)
"""

from seeder.curriculum_builder import make_day, make_course

# =========================================================================
# COURSE 1: Culinary Arts, Knife Skills & Flavor Science (15 Days)
# =========================================================================
CULINARY_DAYS = []

cul_titles = {
    1: ("Kitchen Knife Anatomy, Sharpening & The Claw Grip", "Mastering the chef's knife and guide-hand claw grip is the foundation of kitchen speed and safety.", "A samurai master maintaining their katana; a dull blade requires dangerous brute force, while a razor-sharp edge glides effortlessly."),
    2: ("Classical Knife Cuts: Brunoise, Julienne & Batonnet", "Uniform knife cuts ensure all ingredients cook at the exact same rate while elevating visual presentation.", "Cutting standard puzzle pieces; if all pieces are cut to uniform mathematical dimensions, they fit together seamlessly in the pan."),
    3: ("Mise en Place: Station Organization & Workflow", "Prepare, measure, and position all ingredients before turning on the heat to eliminate kitchen panic.", "A surgeon in an operating room; scalpel, gauze, and clamps are lined up neatly on the sterile tray before the first incision."),
    4: ("Heat Transfer Science: Conduction, Convection & Radiation", "Understanding the physics of heat transfer allows chefs to control surface crusts and internal doneness.", "Tanning on a sunny beach (radiation), sitting in a hot sauna (convection), or touching a warm stone (conduction)."),
    5: ("The Maillard Reaction: Searing, Fond & Pan Sauces", "Amino acids and reducing sugars react at 280°F-330°F to create hundreds of complex roasted flavor compounds.", "Developing a photographic print under warm chemical wash; the invisible potential flavors emerge into rich golden-brown depth."),
    6: ("French Mother Sauces Part 1: Béchamel & Velouté", "A roux of equal parts butter and flour thickens dairy or rich stock into silky, velvety mother sauces.", "The concrete foundation of a home; master the basic mortar, and you can build fifty different architectural extensions on top."),
    7: ("French Mother Sauces Part 2: Espagnole, Hollandaise & Tomato", "Master warm butter emulsification and rich brown veal reductions for classic culinary sauces.", "Suspension cables holding up a bridge; whisking egg yolks and clarified butter creates a delicate molecular emulsion suspension."),
    8: ("Flavor Balancing: The 5 Basic Tastes (Sweet, Salty, Sour, Bitter, Umami)", "Balance dish profiles by countering rich or salty flavors with acidity and umami depth.", "An audio soundboard equalizer; you adjust the bass (rich fat), midrange (salt & umami), and treble (acid & herbs) until the track sounds perfect."),
    9: ("Acid & Fat: Using Citrus and Vinegars to Cut Richness", "Acid cuts through dense fats and dairy, brightening the palate and making heavy dishes feel light.", "Squeezing fresh lime juice over rich street tacos; the citrus acts like a sharp knife slicing through the heavy animal fat."),
    10: ("Herb & Spice Extraction: Toasting & Blooming in Oil", "Fat-soluble flavor compounds in spices must be bloomed in hot oil to release their essential aromatic oils.", "Steeping a high-grade tea leaf in hot water; dry spices remain dormant until awakened by warm fat."),
    11: ("Roasting, Braising & Stewing: Collagen to Gelatin Breakdown", "Low, slow moist heat melts tough connective tissue (collagen) into unctuous, fork-tender gelatin.", "Carving an ice sculpture under warm water; hard, tough fibers slowly soften and transform into rich, melting silk."),
    12: ("Soups and Stocks: Clear Consommé to Rich Bone Broth", "Simmering roasted bones extract mineral richness and gelatin for deeply restorative broths.", "Brewing a fine single-malt whiskey; slow extraction over hours yields liquid gold with complex aromatic layers."),
    13: ("Starch and Grain Science: Risotto, Polenta & Al Dente Pasta", "Manage starch gelatinization through precise water temperature and mechanical agitation.", "Weaving silk threads; continuous gentle stirring releases amylose starch from arborio rice to create a luxurious natural cream."),
    14: ("Plating Aesthetics: Negative Space, Contrast & Textures", "Present food with height, clean rims, contrasting colors, and complementary textures (crunch vs smooth).", "An abstract art canvas in a gallery; the empty white space around the subject gives the food breathing room and dignity."),
    15: ("Capstone: Executing a Professional 5-Course Tasting Menu", "Synthesize knife cuts, mother sauces, flavor balancing, and plating into a restaurant service simulation.", "You have graduated from home cooking to running a professional culinary kitchen.")
}

for day_num in range(1, 16):
    t_info = cul_titles.get(day_num, (f"Day {day_num}: Culinary Mastery", "Cook with precision.", "Culinary chemistry."))
    CULINARY_DAYS.append(make_day(
        order=day_num,
        title=f"Day {day_num}: {t_info[0]}",
        concept=t_info[1],
        analogy=t_info[2],
        sections=[
            (f"Culinary Science of {t_info[0]}", f"Mastering {t_info[0]} allows chefs to manipulate flavor chemistry, heat dynamics, and ingredient structures with effortless professional mastery."),
            ("Commercial Kitchen Execution & Technique", "Execute proper station hygiene, temperature logging, and tasting protocols to deliver Michelin-standard consistency every service.")
        ],
        snippets=[
            (f"{t_info[0]} Formulation Formula (Python)", f"""def calculate_culinary_ratio_{day_num}(flour_g: float, fat_g: float) -> dict:
    roux_weight = flour_g + fat_g
    ratio = '1:1 CLASSICAL' if flour_g == fat_g else 'CUSTOM'
    return {{'day': {day_num}, 'roux_weight': roux_weight, 'ratio': ratio}}

print(calculate_culinary_ratio_{day_num}(50.0, 50.0))""", "python"),
            ("Cooking Temperature Guide", f"""def get_target_temp(meat_type: str) -> int:
    temps = {{'poultry': 165, 'ground_beef': 160, 'steak_medium': 145, 'pork': 145}}
    return temps.get(meat_type.lower(), 165)

print("Target Temp Poultry:", get_target_temp('poultry'), "°F")""", "python")
        ],
        challenge=(f"Culinary Challenge Day {day_num}", "Write a function `scale_ingredient(base_g, original_servings, new_servings)` that returns the scaled ingredient weight rounded to 1 decimal place.",
                   "def scale_ingredient(base_g: float, original_servings: int, new_servings: int) -> float:\n    pass",
                   "def scale_ingredient(base_g: float, original_servings: int, new_servings: int) -> float:\n    if original_servings <= 0: return 0.0\n    return round(base_g * (new_servings / original_servings), 1)", "150.0"),
        quizzes=[
            (f"What is the foundational principle of {t_info[0]}?", [f"To apply {t_info[0]} to achieve consistent flavor balance, texture, and culinary excellence", "To burn food to ashes", "To never use salt or seasoning", "To throw away the cutting board"], f"To apply {t_info[0]} to achieve consistent flavor balance, texture, and culinary excellence", f"Day {day_num} focuses on {t_info[0]}."),
            ("What does 'Mise en Place' mean in professional French culinary tradition?", ["Everything in its place: organizing all prep, chopped items, and tools before cooking", "Cooking everything on the highest possible flame", "Eating before your guests arrive", "Cleaning the dining room floor"], "Everything in its place: organizing all prep, chopped items, and tools before cooking", "Mise en place ensures seamless, stress-free execution during fast-paced restaurant service."),
            ("What temperature range is required for the Maillard reaction to occur?", ["280°F to 330°F (140°C to 165°C)", "32°F to 40°F (0°C to 4°C)", "450°F to 600°F (232°C to 315°C)", "It only happens in liquid water"], "280°F to 330°F (140°C to 165°C)", "The Maillard reaction requires dry heat above boiling point to brown proteins and sugars."),
            ("Why is acid (lemon juice, vinegar) used when a dish tastes too heavy or fatty?", ["Acid brightens flavors by stimulating saliva production and chemically cutting through dense fats", "Acid turns all food into sugar", "Acid completely dissolves the meat", "Acid decreases the temperature of the dish"], "Acid brightens flavors by stimulating saliva production and chemically cutting through dense fats", "Acidity balances rich lipid coatings on the tongue, creating harmony and freshness."),
            ("What is the classical French roux ratio for thickening sauces?", ["Equal parts fat (butter) and all-purpose flour by weight (1:1)", "10 parts sugar to 1 part salt", "1 part flour to 5 parts water", "Roux does not contain any flour"], "Equal parts fat (butter) and all-purpose flour by weight (1:1)", "A classic roux uses equal weights of fat and flour cooked to white, blond, or brown stages.")
        ]
    ))

CULINARY_ARTS_BLUEPRINT = make_course(
    title="Culinary Arts, Knife Skills & Flavor Science",
    category="Cooking",
    description=(
        "The professional 15-Day culinary academy on kitchen technique, food science, and flavor balancing. "
        "Master classical knife cuts (brunoise, julienne), mise en place workflow, heat transfer physics, "
        "the Maillard reaction, French mother sauces, acid/fat balancing, and restaurant plating aesthetics."
    ),
    color="#F97316",
    days=CULINARY_DAYS
)


# =========================================================================
# COURSE 2: Commercial Baking & Food Safety (HACCP) Mastery (15 Days)
# =========================================================================
BAKING_DAYS = []

bak_titles = {
    1: ("Food Safety Regulations & The Danger Zone (40°F-140°F)", "Pathogenic bacteria multiply exponentially between 40°F and 140°F; food must not linger in this zone for > 2 hours.", "A highway where speed limits are ignored; bacteria doubles every 20 minutes in the Danger Zone until food becomes a biohazard."),
    2: ("Cross-Contamination Prevention & Sanitation Protocols", "Segregate raw poultry, meats, seafood, and ready-to-eat produce with color-coded systems.", "A hospital quarantine ward; doctors never touch infected patients and newborn babies without washing hands and switching gloves."),
    3: ("Internal Meat Cooking Temperatures for Commercial Kitchens", "Poultry must reach 165°F, ground meats 160°F, and whole steaks 145°F to ensure pathogen destruction.", "A security firewall; if the temperature threshold isn't reached, biological pathogens can slip past the defense."),
    4: ("HACCP Systems: Critical Control Points & Temp Logs", "Hazard Analysis Critical Control Point systems systematically identify, monitor, and prevent food hazards.", "A nuclear plant safety checklist; automated alarms and hourly logs ensure valves remain within strict safety tolerances."),
    5: ("Commercial Storage Protocols: FIFO & Date Labeling", "First In, First Out (FIFO) guarantees older stock is rotated forward and consumed before expiration.", "A grocery store shelf; new milk cartons are placed at the back so customers naturally buy the nearest expiration date first."),
    6: ("Baker's Percentages: Scaling Recipes From Flour Weight", "In professional bakeries, flour is always 100%, and all other ingredients are expressed as a percentage of flour weight.", "A mathematical coordinate system; setting total flour as the origin point (100%) allows recipes to scale from 1 loaf to 1,000 loaves instantly."),
    7: ("Gluten Science: Protein Strands, Hydration & Kneading", "Gliadin and glutenin proteins bond in water to form elastic gluten sheets that trap gas bubbles.", "A spiderweb or trampoline net; the stronger and more elastic the mesh, the higher the bread dough can rise without collapsing."),
    8: ("Yeast Fermentation: Proofing & Bulk Fermentation Ratios", "Yeast metabolizes simple sugars into carbon dioxide gas (rise) and ethanol (flavor complexity).", "Tiny biological air pumps working inside the dough, inflating millions of microscopic balloons that expand in the oven."),
    9: ("Sourdough Microbiology: Wild Starters & Lactic Acids", "Wild yeasts and lactobacillus bacteria create natural leavening and distinctive tangy flavor.", "A thriving biodiverse forest ecosystem where trees (yeast) and moss (bacteria) live in perfect symbiotic harmony."),
    10: ("Laminated Doughs: Croissants & Puff Pastry Layering", "Alternate layers of cold butter and dough create hundreds of flaky, steam-inflated pastry sheets.", "A deck of cards separated by thin butter sheets; in a hot oven, water in the butter flashes to steam, pushing the pastry layers apart."),
    11: ("Chemical Leaveners: Baking Soda vs Baking Powder", "Baking soda requires an acid to react; double-acting baking powder reacts once with liquid and again under oven heat.", "A science fair volcano; baking soda and vinegar erupt instantly, while baking powder has a delayed secondary fuse."),
    12: ("Custards and Emulsions: Pastry Cream & Curd Stability", "Egg proteins coagulate between 160°F and 180°F; temper hot liquids into eggs slowly to prevent curdling.", "Gently acclimating swimmers to cold ocean water one splash at a time rather than throwing them into an icy lake."),
    13: ("Chocolate Tempering: Controlling Beta Crystal Structures", "Melt and cool chocolate to specific temperatures so cocoa butter forms glossy, snappy Beta V crystals.", "Arranging dominoes in a perfect line; when crystals align into Beta V, chocolate snaps sharply with a mirror gloss."),
    14: ("Recipe Costing: Food Cost Percentage & Menu Pricing", "Keep food costs between 28% and 32% of retail menu prices to ensure profitable restaurant margins.", "A retail price tag formula; every dollar of raw ingredients must generate at least three dollars of menu sales to cover overhead."),
    15: ("Capstone: Commercial Bakery Launch & Full HACCP Audit", "Formulate recipes, scale production batches, and draft a compliant HACCP food safety audit.", "You are a professional commercial baker and food safety certified kitchen manager.")
}

for day_num in range(1, 16):
    t_info = bak_titles.get(day_num, (f"Day {day_num}: Baking & Safety", "Master commercial baking.", "Food safety standards."))
    BAKING_DAYS.append(make_day(
        order=day_num,
        title=f"Day {day_num}: {t_info[0]}",
        concept=t_info[1],
        analogy=t_info[2],
        sections=[
            (f"Food Science of {t_info[0]}", f"Mastering {t_info[0]} guarantees that commercial baked goods rise with flawless structural integrity while complying with strict FDA and health department sanitation codes."),
            ("Commercial Operations & Hygiene Controls", "Maintain temperature logs, implement color-coded cross-contamination prevention, and calculate baker's formulas with mathematical accuracy.")
        ],
        snippets=[
            (f"{t_info[0]} Formula Model (Python)", f"""def calculate_baker_pct_{day_num}(flour_weight: float, hydration_pct: float) -> dict:
    water_weight = round(flour_weight * (hydration_pct / 100.0), 1)
    return {{'flour_g': flour_weight, 'water_g': water_weight, 'hydration': f"{{hydration_pct}}%"}}

print(calculate_baker_pct_{day_num}(1000.0, 72.0))""", "python"),
            ("HACCP Safe Temperature Checker", """def verify_safe_holding_temp(temp_f: float, is_hot_holding: bool) -> bool:
    if is_hot_holding:
        return temp_f >= 135.0  # Must be above danger zone
    return temp_f <= 41.0       # Must be cold below danger zone

print("Hot Holding 140°F Safe:", verify_safe_holding_temp(140.0, True))""", "python")
        ],
        challenge=(f"Baking Challenge Day {day_num}", "Write a function `calculate_food_cost_pct(cost_of_ingredients, selling_price)` that returns food cost percentage rounded to 1 decimal place.",
                   "def calculate_food_cost_pct(cost_of_ingredients: float, selling_price: float) -> float:\n    pass",
                   "def calculate_food_cost_pct(cost_of_ingredients: float, selling_price: float) -> float:\n    if selling_price <= 0: return 0.0\n    return round((cost_of_ingredients / selling_price) * 100, 1)", "28.5"),
        quizzes=[
            (f"What is the critical rule of {t_info[0]}?", [f"To leverage {t_info[0]} to ensure commercial food safety, proper hydration, and culinary consistency", "To leave raw chicken on warm countertops overnight", "To guess all recipe weights by sight", "To turn off the refrigerator at night"], f"To leverage {t_info[0]} to ensure commercial food safety, proper hydration, and culinary consistency", f"Day {day_num} focuses on {t_info[0]}."),
            ("What temperature range defines the FDA Temperature Danger Zone?", ["40°F to 140°F (4°C to 60°C)", "0°F to 32°F (-18°C to 0°C)", "180°F to 212°F (82°C to 100°C)", "350°F to 400°F (175°C to 204°C)"], "40°F to 140°F (4°C to 60°C)", "Bacteria grows most rapidly in the Danger Zone; keep hot food hot and cold food cold."),
            ("What does FIFO stand for in commercial food inventory management?", ["First In, First Out: use the oldest inventory first to prevent spoilage", "Fast Ingredients For Orders", "Fixed Internal Food Operations", "Free Ice For Overnight"], "First In, First Out: use the oldest inventory first to prevent spoilage", "FIFO ensures ingredients are consumed well before their expiration dates."),
            ("In Baker's Math, what ingredient is always designated as 100%?", ["Total Flour Weight", "Total Water Weight", "Total Yeast Weight", "Total Salt Weight"], "Total Flour Weight", "Flour is the baseline 100%, and all other ingredients are calculated as a percentage of flour."),
            ("What causes laminated dough (croissants) to rise into dozens of flaky layers in the oven?", ["Water in the cold butter turns to steam, pushing the alternating flour sheets upward before evaporating", "Baking soda and vinegar reaction", "Blowing air into the dough with a straw", "Adding heavy cornstarch"], "Water in the cold butter turns to steam, pushing the alternating flour sheets upward before evaporating", "Steam expansion from butter layers creates the light, honeycomb texture of croissants.")
        ]
    ))

BAKING_SAFETY_BLUEPRINT = make_course(
    title="Commercial Baking & Food Safety (HACCP) Mastery",
    category="Cooking",
    description=(
        "The complete 15-Day professional masterclass on commercial pastry science and food safety engineering. "
        "Master the Temperature Danger Zone, HACCP critical control points, cross-contamination prevention, "
        "baker's percentages, gluten network development, sourdough wild cultures, laminated doughs, and recipe costing."
    ),
    color="#EA580C",
    days=BAKING_DAYS
)
