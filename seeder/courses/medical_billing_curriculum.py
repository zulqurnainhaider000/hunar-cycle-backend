"""
Medical Billing & Clinical Coding Curriculums
Contains:
1. Medical Billing & Revenue Cycle Management (RCM) (15 Days)
2. ICD-10-CM & CPT Coding Clinical Crosswalks (15 Days)
"""

from seeder.curriculum_builder import make_day, make_course

# =========================================================================
# COURSE 1: Medical Billing & Revenue Cycle Management (RCM) (15 Days)
# =========================================================================
RCM_DAYS = []

rcm_titles = {
    1: ("The Healthcare Revenue Cycle: Patient Intake to Zero Balance", "RCM manages administrative and clinical functions from initial appointment registration to final balance collection.", "An airport baggage system; passenger check-in (demographics), luggage screening (eligibility), flight transit (claim submission), and baggage carousel retrieval (payment posting)."),
    2: ("The Health Insurance Landscape: Commercial, Medicare & Medicaid", "Navigate fee-for-service versus managed care rules across Medicare Part A/B/C/D and Medicaid state plans.", "A multi-lane toll highway; commercial trucks, federal government vehicles, and local commuters each follow distinct automated toll passes and rules."),
    3: ("Patient Registration & Real-Time Eligibility Verification (EDI 270/271)", "Verify active coverage, copayments, deductibles, and out-of-pocket maximums before clinical service.", "Checking a customer's passport validity at the border gate before allowing them to board the international flight."),
    4: ("Prior Authorization (PA) Workflows & Medical Necessity Rules", "Secure insurer pre-approval for specialized procedures and medications to avoid automatic claim denials.", "Submitting architectural blueprints to the city zoning board before breaking ground on an apartment complex."),
    5: ("Box-by-Box Mastery of the CMS-1500 (HCFA) Claim Form", "Master the universal claim form for outpatient medical doctors, therapists, and nurse practitioners.", "A standardized tax return; every single box (Box 1a Insured ID, Box 21 Diagnoses, Box 24 Services) must match official registry data."),
    6: ("UB-04 (CMS-1450) Institutional Claims for Inpatient Hospital Care", "UB-04 captures revenue codes, DRGs, and room/board charges for acute care hospital admissions.", "A commercial hotel itemized invoice combining room stay, room service, conference hall, and concierge charges into a master bill."),
    7: ("Clearinghouse Operations & Electronic Claim Submission (EDI 837P)", "Clearinghouses scrub claims against thousands of payer-specific edits before forwarding ANSI 837 files.", "An automated mail sorting facility with laser scanners that return envelopes with missing stamps or invalid postal zip codes."),
    8: ("The Adjudication Process: Deductibles, Coinsurance & Copays", "Insurers apply contract fee schedules and split payment responsibility between payer and patient.", "A dinner bill split between two friends; one pays the predetermined coupon discount, the other covers the remaining tip and drinks."),
    9: ("Electronic Remittance Advice (EDI 835 ERA) & Payment Posting", "Reconcile electronic payments and write-offs against the patient's billing ledger automatically.", "Scanning a bank deposit slip into the accounting ledger to mark pending customer invoices as fully paid."),
    10: ("Claim Adjustment Reason Codes (CARC) & Remittance Remarks (RARC)", "Decode standardized denial codes (PR-1, PR-2, CO-16, CO-29) to determine next financial steps.", "A traffic citation stating the exact code violated (speeding vs running a red light) and the exact remedy required."),
    11: ("Denial Management: Root Cause Analysis & Appealing CO-16/CO-29", "Overturn rejected claims with targeted appeal letters and supporting clinical documentation.", "Filing a formal legal appeal with an appellate court, citing precedent and submitting sworn evidence to reverse a ruling."),
    12: ("Timely Filing Limits & Proof of Timely Electronic Submission", "Payers enforce strict 90, 180, or 365-day filing deadlines; electronic EDI 999 acknowledgments prove submission.", "Postmarking tax returns before midnight on April 15th; the postmark timestamp proves you met the legal deadline."),
    13: ("Patient Billing: Balance Billing, Statements & Collections", "Issue clear patient statements and navigate ethical payment plans without violating No Surprises Act rules.", "A friendly, itemized retail receipt that clearly shows what insurance paid and what remains due without hidden surprise fees."),
    14: ("HIPAA Privacy & Security Rules: Protecting PHI in Healthcare", "Safeguard Protected Health Information (PHI) through end-to-end encryption, role-based access, and BAAs.", "An armored bank vault with biometric scanners; medical records can only be viewed by authorized personnel with a legitimate business need."),
    15: ("Capstone: Full-Scale Practice Revenue Cycle Audit & Recovery", "Audit accounts receivable (A/R) aging buckets, overturn stale denials, and optimize practice cash flow.", "You are a professional Revenue Cycle Management specialist and certified medical billing expert.")
}

for day_num in range(1, 16):
    t_info = rcm_titles.get(day_num, (f"Day {day_num}: Revenue Cycle Management", "Manage healthcare billing.", "Medical claim processing."))
    RCM_DAYS.append(make_day(
        order=day_num,
        title=f"Day {day_num}: {t_info[0]}",
        concept=t_info[1],
        analogy=t_info[2],
        sections=[
            (f"Operational Framework of {t_info[0]}", f"Mastering {t_info[0]} allows medical practices and hospital systems to minimize claim denials, accelerate reimbursement velocity, and remain fully compliant with HIPAA regulations."),
            ("Payer Scrubbing Rules & Adjudication Workflows", "Audit claim line items against national coding edits, manage electronic remittance postings, and recover aging accounts receivable (A/R > 90 days).")
        ],
        snippets=[
            (f"{t_info[0]} Claim Adjudication Logic (Python)", f"""def adjudicate_medical_claim_{day_num}(charge: float, allowed: float, copay: float) -> dict:
    contractual_writeoff = round(charge - allowed, 2)
    insurance_paid = round(allowed - copay, 2)
    return {{'day': {day_num}, 'allowed': allowed, 'writeoff': contractual_writeoff, 'insurance_paid': insurance_paid, 'patient_copay': copay}}

print(adjudicate_medical_claim_{day_num}(250.0, 160.0, 30.0))""", "python"),
            ("A/R Aging Days Calculator", """def calculate_ar_days(total_ar: float, avg_daily_charges: float) -> float:
    return round(total_ar / avg_daily_charges, 1) if avg_daily_charges > 0 else 0.0

print("A/R Days ($120k AR, $3k daily charges):", calculate_ar_days(120000.0, 3000.0), "days")""", "python")
        ],
        challenge=(f"RCM Challenge Day {day_num}", "Write a function `calculate_patient_coinsurance(allowed_amount, coinsurance_pct)` that returns the patient responsibility rounded to 2 decimal places.",
                   "def calculate_patient_coinsurance(allowed_amount: float, coinsurance_pct: float) -> float:\n    pass",
                   "def calculate_patient_coinsurance(allowed_amount: float, coinsurance_pct: float) -> float:\n    return round(allowed_amount * (coinsurance_pct / 100.0), 2)", "32.0"),
        quizzes=[
            (f"What is the primary role of {t_info[0]} in the healthcare revenue cycle?", [f"To execute {t_info[0]} to ensure clean claim submission, compliant billing, and timely reimbursement", "To delete patient electronic medical records", "To bill patients for procedures that were never performed", "To cancel physician hospital privileges"], f"To execute {t_info[0]} to ensure clean claim submission, compliant billing, and timely reimbursement", f"Day {day_num} focuses on {t_info[0]}."),
            ("What does CARC stand for on an Electronic Remittance Advice (ERA)?", ["Claim Adjustment Reason Code: standardized codes explaining why a claim was adjusted or denied", "Clinical Assessment Record Check", "Central Authorization Review Committee", "Certified Accounting Resource Code"], "Claim Adjustment Reason Code: standardized codes explaining why a claim was adjusted or denied", "CARCs explain why a claim was not paid in full according to standardized national codes."),
            ("What standard form is used by physicians to submit outpatient claims to insurance payers?", ["CMS-1500 (HCFA)", "UB-04", "W-2", "Form 1040"], "CMS-1500 (HCFA)", "The CMS-1500 is the universal paper and electronic claim standard for outpatient professional services."),
            ("Under HIPAA, what constitutes Protected Health Information (PHI)?", ["Any individually identifiable health information created, stored, or transmitted by a covered entity", "Only public demographic statistics published by the census", "The doctor's college diploma", "The hospital cafeteria menu"], "Any individually identifiable health information created, stored, or transmitted by a covered entity", "PHI includes names, SSNs, medical diagnoses, and billing accounts tied to an individual."),
            ("What is an 'EDI 835' transaction in healthcare electronic data interchange?", ["Electronic Remittance Advice (ERA) detailing payer adjudication, write-offs, and payment vouchers", "A patient appointment reminder text message", "A drug prescription sent to a pharmacy", "A hospital floor plan schematic"], "Electronic Remittance Advice (ERA) detailing payer adjudication, write-offs, and payment vouchers", "The 835 transaction communicates payment voucher and adjustment reasoning back to the clinic.")
        ]
    ))

MEDICAL_RCM_BLUEPRINT = make_course(
    title="Medical Billing & Revenue Cycle Management (RCM)",
    category="Medical Billing",
    description=(
        "The comprehensive 15-Day masterclass on healthcare billing, insurance adjudication, and revenue cycle management. "
        "Master CMS-1500 completion, UB-04 inpatient claims, eligibility verification (EDI 270/271), clearinghouse scrubbing (EDI 837P), "
        "remittance reconciliation (EDI 835), CARC denial management, timely filing limits, and HIPAA compliance."
    ),
    color="#EF4444",
    days=RCM_DAYS
)


# =========================================================================
# COURSE 2: ICD-10-CM & CPT Coding Clinical Crosswalks (15 Days)
# =========================================================================
CODING_DAYS = []

cod_titles = {
    1: ("ICD-10-CM Structure: Alpha Characters, Codes & 7th Characters", "Diagnostic coding requires 3 to 7 alphanumeric characters specifying etiology, anatomy, and encounter status.", "A library catalog Dewey Decimal number; 610 is medical science, 610.7 is nursing, and decimals pinpoint the exact shelf."),
    2: ("ICD-10-CM Coding Guidelines: Sequencing & Primary Diagnosis", "Sequence the condition established after study to be chiefly responsible for the encounter as primary.", "Naming the main star of a movie in the opening credits before listing the supporting character actors."),
    3: ("Endocrine & Metabolic Coding: Type 1 vs Type 2 Diabetes", "Navigate combination coding for diabetes with manifestations (neuropathy, nephropathy, retinopathy).", "A tree branch dividing into sub-twigs; the root is diabetes (E11), and twigs define organ complications."),
    4: ("Cardiovascular Coding: Hypertension, CHF & Myocardial Infarction", "Document acute vs chronic coronary syndrome and understand causal links between hypertension and heart disease.", "A plumbing system under high water pressure; sustained high pressure over years causes pump failure (heart failure)."),
    5: ("Respiratory Conditions: Acute vs Chronic Bronchitis & Asthma", "Distinguish between acute infective exacerbations and baseline chronic obstructive pulmonary disease.", "A calm river experiencing an unexpected flash flood; code the underlying riverbed and the sudden flood surge."),
    6: ("Musculoskeletal & Injury Coding: Fractures, Sprains & Laterality", "Code specific anatomical laterality (Right vs Left) and episode of care (Initial 'A', Subsequent 'D', Sequela 'S').", "A police accident report noting whether the driver's side door or passenger side was struck and if it's the first scene report."),
    7: ("CPT Coding Manual Architecture: Categories I, II, & III", "CPT Category I covers standard medical procedures; Category II tracks quality metrics; Category III covers emerging tech.", "A national building code book with separate chapters for plumbing, electrical wiring, and experimental solar panels."),
    8: ("Evaluation & Management (E/M) Coding: Medical Decision Making (MDM)", "Select E/M codes (99212-99215) based on the number and complexity of problems addressed and risk.", "An emergency room triage desk sorting patients by case severity: minor scratch vs complex heart arrhythmia."),
    9: ("E/M Time-Based Coding & Prolonged Services", "Bill based on total face-to-face and non-face-to-face physician time on the date of the encounter.", "A professional attorney billing clients based on billable minutes spent reviewing documents and consulting in court."),
    10: ("CPT Modifiers Part 1: -25 (Significant Separate E/M Service)", "Append modifier -25 when a physician performs a preventive visit and a separate sick visit on the same day.", "A mechanic doing an annual safety inspection who also replaces worn brake pads during the same garage visit."),
    11: ("CPT Modifiers Part 2: -59, -50, -51 (Surgical & Anatomical Edits)", "Modifier -59 indicates a distinct, independent procedural service that is not normally reported together.", "A dentist filling two completely separate teeth on opposite sides of the mouth during a single dental appointment."),
    12: ("HCPCS Level II: Durable Medical Equipment (DME) & J-Codes", "HCPCS Level II codes describe medical supplies, wheelchairs, prosthetics, and injectable pharmaceuticals.", "The hardware store catalog listing specialized bolts, surgical crutches, and injectable medicines not found in standard CPT."),
    13: ("National Correct Coding Initiative (NCCI) Edits & Unbundling", "NCCI Column 1/Column 2 edits prevent unbundling components that are already included in comprehensive codes.", "Ordering a combo value meal at a diner; you cannot bill separately for the burger, the bun, the fries, and the ketchup."),
    14: ("Clinical Documentation Improvement (CDI) & Physician Queries", "Bridge clinical charts and coder understanding by submitting compliant, non-leading queries to physicians.", "A translator asking a diplomat for clarification on an ambiguous phrase before publishing an official treaty."),
    15: ("Capstone: Complex Outpatient Chart Coding & Audit Defense", "Abstract ICD-10 and CPT codes from multi-specialty operative notes and defend coding choices against audit.", "You are a master clinical coder capable of passing AAPC (CPC) and AHIMA certification examinations.")
}

for day_num in range(1, 16):
    t_info = cod_titles.get(day_num, (f"Day {day_num}: Clinical Coding", "Code clinical diagnoses.", "CPT/ICD-10 crosswalks."))
    CODING_DAYS.append(make_day(
        order=day_num,
        title=f"Day {day_num}: {t_info[0]}",
        concept=t_info[1],
        analogy=t_info[2],
        sections=[
            (f"Clinical Methodology of {t_info[0]}", f"Mastering {t_info[0]} ensures clinical services are abstracted with anatomical precision and diagnostic necessity, eliminating compliance penalties and payer rejections."),
            ("Audit Defense & Coding Accuracy Standards", "Apply official coding guidelines, attach appropriate CPT modifiers, and navigate NCCI mutually exclusive edits with 100% precision.")
        ],
        snippets=[
            (f"{t_info[0]} Crosswalk Model (Python)", f"""def crosswalk_coding_rule_{day_num}(icd10: str, cpt: str) -> dict:
    has_medical_necessity = len(icd10) >= 3 and len(cpt) == 5
    return {{'day': {day_num}, 'icd10': icd10, 'cpt': cpt, 'valid_crosswalk': has_medical_necessity}}

print(crosswalk_coding_rule_{day_num}("E11.9", "99214"))""", "python"),
            ("ICD-10 Laterality Validator", """def check_laterality(code: str) -> str:
    if code.endswith('1'): return 'Right Side'
    if code.endswith('2'): return 'Left Side'
    if code.endswith('3'): return 'Bilateral'
    return 'Unspecified'

print("M25.561 laterality:", check_laterality("M25.561"))""", "python")
        ],
        challenge=(f"Coding Challenge Day {day_num}", "Write a function `is_valid_cpt(code)` that returns True if code is a string of exactly 5 digits.",
                   "def is_valid_cpt(code: str) -> bool:\n    pass",
                   "def is_valid_cpt(code: str) -> bool:\n    return len(code) == 5 and code.isdigit()", "True"),
        quizzes=[
            (f"What is the clinical function of {t_info[0]}?", [f"To apply {t_info[0]} to capture diagnostic specificity, medical necessity, and procedural accuracy", "To replace doctors with automated robots", "To guess medical codes randomly", "To eliminate patient charts"], f"To apply {t_info[0]} to capture diagnostic specificity, medical necessity, and procedural accuracy", f"Day {day_num} focuses on {t_info[0]}."),
            ("What does CPT Modifier -25 represent when appended to an E/M code?", ["A significant, separately identifiable evaluation and management service on the same day as a procedure", "The patient canceled their appointment", "The doctor was 25 minutes late", "The procedure was performed by a resident"], "A significant, separately identifiable evaluation and management service on the same day as a procedure", "Modifier -25 allows reimbursement for an E/M visit performed alongside a minor procedure."),
            ("What does the 7th character 'A' in an ICD-10-CM fracture code indicate?", ["Initial encounter for active medical treatment of the fracture", "Subsequent healing encounter", "Sequela late effect years later", "An accidental laboratory finding"], "Initial encounter for active medical treatment of the fracture", "Character 7 'A' is used while the patient is receiving active treatment for the acute injury."),
            ("What is 'Unbundling' in procedural medical coding?", ["Illegally reporting multiple component codes separately when a single comprehensive CPT code covers the entire service", "Unwrapping surgical bandages", "Discarding paper medical records", "Opening an email attachment"], "Illegally reporting multiple component codes separately when a single comprehensive CPT code covers the entire service", "Unbundling artificially inflates billing and violates National Correct Coding Initiative rules."),
            ("What does HCPCS Level II primarily code that is absent from CPT Category I?", ["Durable medical equipment (DME), prosthetics, ambulance rides, and injectable pharmaceuticals (J-codes)", "Inpatient surgery procedures", "Heart transplant operations", "Doctor office visits"], "Durable medical equipment (DME), prosthetics, ambulance rides, and injectable pharmaceuticals (J-codes)", "HCPCS Level II captures non-physician medical supplies, medications, and durable equipment.")
        ]
    ))

CLINICAL_CODING_BLUEPRINT = make_course(
    title="ICD-10-CM & CPT Coding Clinical Crosswalks",
    category="Medical Billing",
    description=(
        "The definitive 15-Day guide to professional clinical coding and audit defense. "
        "Master ICD-10-CM alphanumeric structures, diabetes combination coding, laterality, "
        "E/M Medical Decision Making (MDM), CPT modifiers (-25, -59), HCPCS Level II J-codes, NCCI bundling edits, and physician CDI queries."
    ),
    color="#B91C1C",
    days=CODING_DAYS
)
