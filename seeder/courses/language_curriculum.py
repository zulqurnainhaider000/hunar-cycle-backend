"""
Language & Global Communication Curriculums
Contains:
1. Professional English & Global Workplace Fluency (15 Days)
2. Executive Communication & Business Negotiation (15 Days)
"""

from seeder.curriculum_builder import make_day, make_course

# =========================================================================
# COURSE 1: Professional English & Global Workplace Fluency (15 Days)
# =========================================================================
ENGLISH_DAYS = []

eng_titles = {
    1: ("High-Frequency Core Vocabulary & Sentence Skeletons", "Fluency is built on instant recall of core verbs and connecting structures, not obscure dictionary words.", "Learning guitar chords; you only need 4 fundamental chords to play 80% of all popular songs."),
    2: ("The Art of Collocations & Natural Phrase Chunking", "Native speakers speak in multi-word chunks; memorize collocations rather than translating word by word.", "Pre-assembled Lego blocks that snap together instantly rather than melting raw plastic on the floor."),
    3: ("Mastering English Verb Tenses in Professional Contexts", "Present Perfect vs Past Simple defines accuracy when discussing project status and career achievements.", "A camera lens focusing: past simple is a photograph taken yesterday; present perfect connects that photo to what is happening right now."),
    4: ("Active Voice vs Passive Voice: Writing With Authority", "Active voice identifies the actor immediately, creating punchy, accountable executive writing.", "A direct, firm handshake in a boardroom meeting compared to a limp, hesitant wave from across the room."),
    5: ("Executive Email Etiquette & The BLUF Framework", "Put the Bottom Line Up Front so busy executives instantly grasp your request and deadline.", "A billboard on a highway; drivers traveling at 70 mph need a bold headline and a single exit sign."),
    6: ("Connecting Words & Cohesive Discourse Markers", "Transition words guide the reader's brain smoothly between arguments and evidence.", "Train tracks that guide high-speed carriages smoothly across mountain ravines without jolts."),
    7: ("Prepositions of Time, Place, and Direction Made Simple", "Master the 'In, On, At' pyramid from broad general concepts to pinpoint specifics.", "A pyramid: 'In' is the broad base (years, cities); 'On' is the middle (days, streets); 'At' is the pinpoint tip (hours, addresses)."),
    8: ("Modal Verbs for Polite Workplace Requests (Could, Would, Should)", "Softening directives with modal verbs preserves professional relationships while maintaining standards.", "A shock absorber in a luxury car; it delivers the same forward propulsion without jarring the passengers."),
    9: ("Professional Meetings: Voicing Opinions & Diplomatic Disagreement", "Disagree with ideas without attacking people using diplomatic framing phrases.", "Fencing with padded foils; you score points on the argument without causing bodily harm to your partner."),
    10: ("Accent Reduction, Word Stress & The Schwa Sound (/ə/)", "English is a stress-timed language; stressing the correct syllables creates effortless comprehension.", "A musical rhythm section; the drummer hits the accented beat with power while passing lightly over the unaccented notes."),
    11: ("Paraphrasing, Active Listening & Clarification Questions", "Confirm mutual understanding by reflecting the speaker's thoughts back in your own words.", "A sonar ping returning from a submarine; it verifies location and removes misunderstandings."),
    12: ("Business Reports, Executive Summaries & Bullet Points", "Distill 50-page complex data into a 1-page high-impact briefing.", "A bullion gold bar refined from tons of raw unrefined river silt."),
    13: ("Cross-Cultural Nuances in Global Remote Teams", "Navigate direct vs indirect communication styles across multinational workplaces.", "A universal electrical adapter that lets your laptop plug cleanly into outlets in Tokyo, London, and New York."),
    14: ("Idiomatic Expressions and Phrasal Verbs in Corporate English", "Demystify common workplace idioms ('touch base', 'move the needle', 'hit the ground running').", "Learning the insider handshakes of a community so you speak like a true insider rather than a tourist."),
    15: ("Capstone: Delivering a Flawless Virtual Executive Presentation", "Deliver an engaging, persuasive 10-minute presentation with structured slide transitions.", "You have achieved professional fluency, confidence, and executive presence in the global workplace.")
}

for day_num in range(1, 16):
    t_info = eng_titles.get(day_num, (f"Day {day_num}: Workplace English", "Communicate fluently.", "Professional clarity."))
    ENGLISH_DAYS.append(make_day(
        order=day_num,
        title=f"Day {day_num}: {t_info[0]}",
        concept=t_info[1],
        analogy=t_info[2],
        sections=[
            (f"Linguistic Foundations of {t_info[0]}", f"Mastering {t_info[0]} allows international professionals to communicate with confidence, precision, and executive gravitas in competitive remote environments."),
            ("Real-World Workplace Scenarios", "Apply these communication frameworks across emails, Slack messages, team standups, and high-stakes client reviews.")
        ],
        snippets=[
            (f"{t_info[0]} Phrasing Models (Python)", f"""def analyze_communication_tone_{day_num}(phrase: str) -> dict:
    is_polite = any(w in phrase.lower() for w in ['could', 'would', 'appreciate', 'thank you', 'please'])
    tone = 'EXECUTIVE & DIPLOMATIC' if is_polite else 'DIRECT / INFORMAL'
    return {{'day': {day_num}, 'phrase': phrase, 'tone': tone}}

print(analyze_communication_tone_{day_num}("Could we review the timeline by Thursday?"))""", "python"),
            ("Word Stress & Readability Calculator", f"""def calculate_readability_words(text: str) -> dict:
    words = text.split()
    return {{'word_count': len(words), 'avg_length': round(sum(len(w) for w in words) / len(words), 1)}}

print(calculate_readability_words("We are pleased to confirm that the project milestones have been completed."))""", "python")
        ],
        challenge=(f"Language Challenge Day {day_num}", "Write a function `is_passive_voice(sentence)` that returns True if 'was ' or 'were ' or 'been ' is in the lowercase sentence.",
                   "def is_passive_voice(sentence: str) -> bool:\n    pass",
                   "def is_passive_voice(sentence: str) -> bool:\n    s = sentence.lower()\n    return 'was ' in s or 'were ' in s or 'been ' in s", "True"),
        quizzes=[
            (f"What is the primary benefit of {t_info[0]}?", [f"To apply {t_info[0]} to communicate with clarity, diplomacy, and executive authority", "To speak so fast that nobody understands", "To use ancient vocabulary that confuses colleagues", "To avoid answering all emails"], f"To apply {t_info[0]} to communicate with clarity, diplomacy, and executive authority", f"Day {day_num} focuses on {t_info[0]}."),
            ("What does the BLUF framework dictate in professional emails?", ["Bottom Line Up Front: state the primary conclusion, decision, or request in sentence #1", "Bury the main point in the final footnote", "Never include a call to action", "Write in all capital letters"], "Bottom Line Up Front: state the primary conclusion, decision, or request in sentence #1", "BLUF respects the recipient's time and guarantees immediate clarity."),
            ("How does the 'Schwa' sound (/ə/) function in natural English pronunciation?", ["It is the most common, relaxed vowel sound, used on unstressed syllables (e.g. 'about', 'problem')", "It is a loud shouting sound used only in military commands", "It is never pronounced by native speakers", "It only exists in the German language"], "It is the most common, relaxed vowel sound, used on unstressed syllables (e.g. 'about', 'problem')", "The schwa creates the natural rhythm and timing of conversational English."),
            ("What is a diplomatic way to disagree during a business meeting?", ["'I see where you're coming from, however, have we considered the impact on Q3 budget?'", "'That is completely wrong and makes no sense.'", "'You should be fired for suggesting that.'", "Remaining silent and complaining on social media"], "'I see where you're coming from, however, have we considered the impact on Q3 budget?'", "Diplomatic framing addresses the idea thoughtfully without insulting colleagues."),
            ("Why is active voice preferred in executive business writing?", ["It clearly identifies who is responsible for the action and creates concise, direct sentences", "It takes up more words to make reports longer", "It hides the name of the project manager", "It is required for international copyright"], "It clearly identifies who is responsible for the action and creates concise, direct sentences", "Active voice ('The team hit the target') is clearer than passive ('The target was hit by the team').")
        ]
    ))

ENGLISH_FLUENCY_BLUEPRINT = make_course(
    title="Professional English & Global Workplace Fluency",
    category="Language",
    description=(
        "The comprehensive 15-Day masterclass on mastering workplace English for multinational and remote teams. "
        "Master high-frequency vocabulary, natural collocations, verb tenses, active voice, BLUF email etiquette, "
        "diplomatic meeting disagreement, accent reduction, and executive presentations."
    ),
    color="#F59E0B",
    days=ENGLISH_DAYS
)


# =========================================================================
# COURSE 2: Executive Communication & Business Negotiation (15 Days)
# =========================================================================
NEGOTIATION_DAYS = []

neg_titles = {
    1: ("The Foundations of Persuasive Rhetoric (Ethos, Pathos, Logos)", "Aristotelian rhetoric balances credibility, emotional resonance, and logical rigor to persuade stakeholders.", "A three-legged stool; if you rely only on logic (Logos) without credibility (Ethos) or empathy (Pathos), the stool falls over."),
    2: ("Non-Verbal Communication, Video Presence & Vocal Dynamics", "Over 70% of communication is vocal tone, eye contact, pacing, and open posture.", "A symphony conductor; the tempo and volume of the baton communicate nuance long before the words are spoken."),
    3: ("Framing Arguments & The Anchoring Effect in Business", "The first number or perspective introduced into a conversation anchors all subsequent negotiations.", "Throwing a heavy ship anchor into the harbor mud; all floating vessels now drift relative to that fixed point."),
    4: ("The Harvard Principled Negotiation Method", "Separate the people from the problem, focus on interests rather than positions, and invent options for mutual gain.", "Two siblings fighting over an orange; one wants the juice to drink, the other wants the peel for a cake; understanding interests gives both 100%."),
    5: ("BATNA (Best Alternative to a Negotiated Agreement)", "Your BATNA is your ultimate source of negotiating power; never enter a negotiation without knowing your walkaway point.", "An emergency parachute strapped to your back; having a functioning parachute gives you total confidence during the flight."),
    6: ("Tactical Empathy & Chris Voss's Mirroring Techniques", "Repeat the last 1 to 3 critical words spoken by your counterpart with an upward inflection to gather intelligence.", "A mirror reflecting an image back; it invites the other person to expand, clarify, and reveal hidden information."),
    7: ("Labeling Emotions: 'It seems like you're hesitant about the timeline...'", "Diffusing negative emotions by naming them disarms defensiveness and builds deep rapport.", "Turning on a bright flashlight in a dark basement; once the monster is illuminated, the irrational fear evaporates."),
    8: ("Calibrated Questions: Shifting From 'Yes' to 'How'", "Ask 'How' and 'What' questions that force the other party to solve your problem for you.", "Handing the steering wheel of the car to the passenger and asking: 'How do you recommend we navigate this roadblock?'"),
    9: ("Handling High-Stakes Objections With Poise", "Welcome objections as signs of engagement rather than rejection; an objection is an invitation to collaborate.", "A martial artist using an opponent's incoming momentum to execute a gentle, controlled throw without absorbing the blow."),
    10: ("Storytelling Frameworks for Founders and Executives", "Humans remember stories 22x more than dry bullet points; use the Hero's Journey to communicate vision.", "A campfire where elders pass down vital tribal wisdom through memorable allegories that survive for generations."),
    11: ("Pitching to Investors & Mastering the Tough Q&A", "Answer investor questions directly in the first 5 words, then substantiate with metrics.", "A tennis champion returning a 130 mph serve with a crisp, centered backhand rather than fumbling the racket."),
    12: ("Crisis Communication & Executive Damage Control", "Take radical ownership immediately, state what happened objectively, and outline the immediate 3-step fix.", "A pilot announcing engine turbulence calmly over the intercom with a clear flight reroute plan."),
    13: ("Salary, Equity & Contract Negotiations", "Negotiate total compensation packages across equity, bonuses, flexible hours, and severance.", "Building a gourmet sandwich; if the client won't add more turkey (salary), negotiate for avocado, cheese, and gourmet sourdough (equity & perks)."),
    14: ("Managing Upward & Cross-Functional Alignment", "Align with senior executives by understanding their personal OKRs and solving their biggest headaches.", "A chief of staff who prepares briefings before the general even realizes a logistical issue arose."),
    15: ("Capstone: Live High-Stakes Business Negotiation Simulation", "Synthesize BATNA, tactical empathy, calibrated questions, and anchoring in an enterprise deal simulation.", "You have mastered the art and science of high-stakes executive communication and negotiation.")
}

for day_num in range(1, 16):
    t_info = neg_titles.get(day_num, (f"Day {day_num}: Executive Negotiation", "Influence stakeholders.", "Principled negotiation."))
    NEGOTIATION_DAYS.append(make_day(
        order=day_num,
        title=f"Day {day_num}: {t_info[0]}",
        concept=t_info[1],
        analogy=t_info[2],
        sections=[
            (f"Strategic Dynamics of {t_info[0]}", f"Mastering {t_info[0]} gives executives and entrepreneurs the psychological tools to navigate conflict, protect enterprise value, and close win-win agreements."),
            ("Tactical Application & Behavioral Psychology", "Deploy tactical empathy, calibrate questions, and anchor positions to turn high-tension disputes into collaborative problem-solving sessions.")
        ],
        snippets=[
            (f"{t_info[0]} Negotiation Logic (Python)", f"""def evaluate_batna_deal_{day_num}(offered_deal: float, batna_value: float) -> str:
    if offered_deal > batna_value * 1.15:
        return 'STRONG ACCEPT: Exceeds BATNA by > 15%'
    if offered_deal >= batna_value:
        return 'ACCEPTABLE: Meets BATNA baseline'
    return 'WALK AWAY: BATNA is superior'

print(evaluate_batna_deal_{day_num}(120000.0, 100000.0))""", "python"),
            ("ZOPA (Zone of Possible Agreement) Calculator", f"""def calculate_zopa(buyer_max: float, seller_min: float) -> dict:
    has_zopa = buyer_max >= seller_min
    zopa_size = max(0.0, buyer_max - seller_min)
    return {{'has_agreement_zone': has_zopa, 'spread': zopa_size}}

print("ZOPA ($90k min seller, $110k max buyer):", calculate_zopa(110000.0, 90000.0))""", "python")
        ],
        challenge=(f"Negotiation Challenge Day {day_num}", "Write a function `is_in_zopa(offer, seller_reservation, buyer_reservation)` that returns True if seller_reservation <= offer <= buyer_reservation.",
                   "def is_in_zopa(offer: float, seller_reservation: float, buyer_reservation: float) -> bool:\n    pass",
                   "def is_in_zopa(offer: float, seller_reservation: float, buyer_reservation: float) -> bool:\n    return seller_reservation <= offer <= buyer_reservation", "True"),
        quizzes=[
            (f"What is the foundational strategy of {t_info[0]}?", [f"To apply {t_info[0]} to negotiate collaboratively while preserving maximum strategic leverage", "To shout louder than the counterpart until they surrender", "To sign whatever the other side puts in front of you", "To threaten physical violence"], f"To apply {t_info[0]} to negotiate collaboratively while preserving maximum strategic leverage", f"Day {day_num} emphasizes {t_info[0]}."),
            ("What does BATNA stand for in negotiation theory?", ["Best Alternative to a Negotiated Agreement", "Basic Agreement Tax Notification Act", "Business Administration Technical Network Association", "Buyer Automated Trade Notification Asset"], "Best Alternative to a Negotiated Agreement", "Your BATNA is your walkaway alternative; knowing it prevents accepting bad deals."),
            ("What is a 'Calibrated Question' as taught by former FBI hostage negotiator Chris Voss?", ["An open-ended question starting with 'How' or 'What' that prompts the other party to solve the issue", "A closed question that can only be answered with 'Yes'", "An insulting question meant to anger the counterpart", "A multiple choice test question"], "An open-ended question starting with 'How' or 'What' that prompts the other party to solve the issue", "'How am I supposed to do that?' shifts the problem-solving burden back to the other party."),
            ("What does the 'Anchoring Effect' describe in pricing discussions?", ["The tendency for the first number introduced to heavily influence all subsequent bids and counter-offers", "Dropping metal into a lake", "Forgetting the price of goods", "Paying in foreign paper currency"], "The tendency for the first number introduced to heavily influence all subsequent bids and counter-offers", "The initial anchor sets the mental benchmark against which all adjustments occur."),
            ("In Harvard principled negotiation, why should you focus on interests rather than positions?", ["Positions are what people say they want; interests are the underlying needs that can be satisfied in multiple ways", "Positions are legally binding in federal court", "Interests are irrelevant to business", "Positions allow you to avoid signing contracts"], "Positions are what people say they want; interests are the underlying needs that can be satisfied in multiple ways", "Uncovering underlying interests enables creative win-win solutions that satisfy both parties.")
        ]
    ))

EXECUTIVE_COMMUNICATION_BLUEPRINT = make_course(
    title="Executive Communication & Business Negotiation",
    category="Language",
    description=(
        "The complete 15-Day masterclass on executive influence, high-stakes negotiation, and rhetorical persuasion. "
        "Master Ethos/Pathos/Logos, BATNA walkaway power, Chris Voss's tactical empathy and calibrated questions, "
        "investor pitch delivery, crisis communications, and C-suite salary negotiations."
    ),
    color="#D97706",
    days=NEGOTIATION_DAYS
)
