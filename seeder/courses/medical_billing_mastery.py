"""
Medical Billing, Coding & Revenue Cycle Management (RCM) Blueprint
Comprehensive curriculum covering ICD-10-CM diagnosis coding, CPT procedure codes,
HCPCS Level II, CMS-1500 claim forms, EDI 837 transmission, denial management, and HIPAA compliance.
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
        title="Day 1: Foundations of Medical Billing & ICD-10-CM Coding",
        concept="Medical billing bridges healthcare services and insurance reimbursement through standardized diagnostic (ICD-10) and procedure (CPT) codes.",
        analogy="Think of medical billing like international airport baggage handling. A flight ticket has standardized airport IATA codes (JFK, LHR). If a tag has a typo, the luggage gets lost. In healthcare, if an ICD-10 diagnostic code doesn't support the medical necessity of a CPT procedure, the claim is rejected by the insurance payer.",
        theory_sections=[
            {
                "heading": "The Structure of ICD-10-CM Codes",
                "body": "ICD-10-CM (International Classification of Diseases, 10th Revision, Clinical Modification) contains 3 to 7 alphanumeric characters. Character 1 is always an alphabetic letter (except U). Characters 2 and 3 are numeric, followed by a decimal point. Characters 4-6 specify etiology, anatomic site, and severity. Character 7 represents the encounter type (A = Initial, D = Subsequent, S = Sequela)."
            },
            {
                "heading": "Medical Necessity and Code Linkage",
                "body": "Reimbursement requires 'Medical Necessity'. The physician's diagnosis (ICD-10) must medically justify why the procedure or diagnostic test (CPT) was performed. For instance, billing an MRI of the brain for a sprained ankle is flagged as medical necessity fraud."
            }
        ],
        code_snippets=[
            {
                "title": "ICD-10 Format Validator (Python)",
                "explanation": "Validates the syntactic structure of an ICD-10-CM diagnostic code.",
                "language": "python",
                "code": """import re

ICD10_REGEX = re.compile(r'^[A-TV-Z][0-9][0-9A-B](\\.[0-9A-TV-Z]{1,4})?$')

def validate_icd10_code(code: str) -> bool:
    clean_code = code.strip().upper()
    return bool(ICD10_REGEX.match(clean_code))

print("J01.90 (Acute Sinusitis):", validate_icd10_code("J01.90"))   # True
print("123.45 (Invalid Format):", validate_icd10_code("123.45"))   # False"""
            },
            {
                "title": "CMS-1500 Diagnostic Pointer Crosswalk",
                "explanation": "Maps CPT service lines to the appropriate diagnosis code pointers (Box 24E).",
                "language": "python",
                "code": """def build_claim_line(cpt_code: str, charge: float, dx_pointers: list) -> dict:
    valid_pointers = ['A', 'B', 'C', 'D']
    for p in dx_pointers:
        if p not in valid_pointers:
            raise ValueError(f"Invalid diagnosis pointer: {p}")
    return {
        'procedure_cpt': cpt_code,
        'billed_amount': charge,
        'diagnosis_pointers': "".join(dx_pointers)
    }

line_item = build_claim_line(cpt_code="99213", charge=150.00, dx_pointers=['A', 'B'])
print("Clean CMS-1500 Line Item:", line_item)"""
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Clean Claim Reimbursement Estimator",
            description="Write a function `calculate_allowed_amount(billed_amount, allowed_fee_schedule, coinsurance_pct)` that returns the patient responsibility amount rounded to 2 decimal places.",
            starter_code="""def calculate_allowed_amount(billed_amount: float, allowed_fee_schedule: float, coinsurance_pct: float) -> float:
    # Your code here
    pass""",
            solution_code="""def calculate_allowed_amount(billed_amount: float, allowed_fee_schedule: float, coinsurance_pct: float) -> float:
    allowed = min(billed_amount, allowed_fee_schedule)
    return round(allowed * (coinsurance_pct / 100.0), 2)""",
            expected_output="24.0"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What does ICD-10-CM stand for?",
                options=[
                    "International Classification of Diseases, 10th Revision, Clinical Modification",
                    "Internal Clinical Documentation for Hospitalized Patients, 10th Protocol",
                    "Integrated Coding Database for 10 Common Medical Conditions",
                    "Insurance Claim Directory for Outpatient Care Management"
                ],
                correct_answer="International Classification of Diseases, 10th Revision, Clinical Modification",
                explanation="ICD-10-CM is the official diagnostic classification system maintained by WHO and CMS for American clinical healthcare."
            ),
            QuizQuestionBlueprint(
                question="In ICD-10-CM coding, what does the 7th character 'A' signify?",
                options=[
                    "Initial encounter for active treatment",
                    "Subsequent encounter during routine recovery",
                    "Sequela (late effect of a previous injury)",
                    "Adverse drug interaction"
                ],
                correct_answer="Initial encounter for active treatment",
                explanation="Character 7 'A' indicates the initial encounter where the patient is receiving active care from the provider for the injury."
            ),
            QuizQuestionBlueprint(
                question="What is the concept of 'Medical Necessity' in healthcare billing?",
                options=[
                    "The diagnostic ICD-10 code must clinically justify why the CPT procedure was performed",
                    "The patient must be transported to the hospital exclusively in an ambulance",
                    "The medical bill must exceed $5,000 to be eligible for insurance payment",
                    "The physician must have graduated from medical school within the last 5 years"
                ],
                correct_answer="The diagnostic ICD-10 code must clinically justify why the CPT procedure was performed",
                explanation="Insurers only reimburse procedures that are recognized as medically necessary and appropriate for the patient's diagnosed condition."
            ),
            QuizQuestionBlueprint(
                question="Which standard form is used to submit professional claims to insurance companies for outpatient services?",
                options=[
                    "CMS-1500 (HCFA)",
                    "UB-04 (CMS-1450)",
                    "W-2 Tax Statement",
                    "I-9 Employment Authorization"
                ],
                correct_answer="CMS-1500 (HCFA)",
                explanation="The CMS-1500 form is the universal claim form for outpatient medical doctors, therapists, and professional healthcare providers."
            ),
            QuizQuestionBlueprint(
                question="What does CPT stand for in procedural coding?",
                options=[
                    "Current Procedural Terminology",
                    "Clinical Patient Transmission",
                    "Central Payment Transaction",
                    "Certified Prescription Treatment"
                ],
                correct_answer="Current Procedural Terminology",
                explanation="CPT codes are published and copyrighted by the American Medical Association (AMA) to identify healthcare procedures."
            )
        ]
    ),
    DayBlueprint(
        order=2,
        title="Day 2: The Revenue Cycle (RCM), EDI 837/835 & Denial Management",
        concept="The Revenue Cycle is the administrative pipeline that captures, scrubs, adjudicates, and recovers patient and insurance revenue.",
        analogy="Think of RCM like an electronic toll booth system on a turnpike. If a car's transponder has an unlinked credit card (eligibility error) or incorrect license plate (typo), the gate doesn't open. In RCM, automated clearinghouse scrubbers catch errors before sending electronic claims to payers.",
        theory_sections=[
            {
                "heading": "Electronic Data Interchange (EDI 837 & 835)",
                "body": "Modern billing transmits claims electronically via HIPAA-mandated ANSI ASC X12 EDI standards. The EDI 837P (Professional) transacts claim data from the provider to the payer. The EDI 835 ERA (Electronic Remittance Advice) returns the adjudication explanation and payment details."
            },
            {
                "heading": "Claim Adjustment Reason Codes (CARC) & Denial Workflows",
                "body": "When a claim is denied, the ERA contains Claim Adjustment Reason Codes (CARCs) and Remittance Advice Remark Codes (RARCs). Common codes include PR-1 (Deductible Amount), PR-2 (Coinsurance), CO-16 (Claim lacks required information), and CO-29 (Time limit for filing has expired)."
            }
        ],
        code_snippets=[
            {
                "title": "EDI 837 Payload Parser (Python)",
                "explanation": "Extracts patient, provider, and procedure segments from an electronic claim transaction.",
                "language": "python",
                "code": """def parse_edi_claim(claim_str: str) -> dict:
    segments = claim_str.split('~')
    data = {}
    for seg in segments:
        parts = seg.strip().split('*')
        if parts[0] == 'NM1' and parts[1] == '85':
            data['billing_provider'] = parts[3]
        elif parts[0] == 'NM1' and parts[1] == 'IL':
            data['insured_patient'] = f"{parts[3]}, {parts[4]}"
        elif parts[0] == 'SV1':
            data['cpt_code'] = parts[1].split(':')[1]
            data['amount'] = float(parts[2])
    return data

sample = "NM1*85*2*METRO CLINIC*****XX*1234567890~NM1*IL*1*DOE*JOHN****MI*987654~SV1*HC:99214*175.00*UN*1~"
print("Parsed EDI 837:", parse_edi_claim(sample))"""
            },
            {
                "title": "CARC Denial Action Triage",
                "explanation": "Routes denied claims to the appropriate billing specialist based on reason codes.",
                "language": "python",
                "code": """CARC_ROUTING = {
    'CO-16': 'Front Desk: Collect missing clinical records/eligibility',
    'CO-29': 'Appeals: Review proof of timely electronic submission',
    'CO-97': 'Billing Lead: Unbundle/appeal inclusive service',
    'PR-1': 'Patient Accounts: Bill patient deductible balance',
}

def triage_denial(carc_code: str) -> str:
    return CARC_ROUTING.get(carc_code, 'General Accounts Receivable Follow-up')

print("Denial CO-16:", triage_denial('CO-16'))
print("Denial PR-1:", triage_denial('PR-1'))"""
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Clean Claim Rate Calculator",
            description="Write a function `clean_claim_rate(paid_first_pass, total_submitted)` that computes the Clean Claim Percentage rounded to 1 decimal place.",
            starter_code="""def clean_claim_rate(paid_first_pass: int, total_submitted: int) -> float:
    # Your code here
    pass""",
            solution_code="""def clean_claim_rate(paid_first_pass: int, total_submitted: int) -> float:
    if total_submitted <= 0:
        return 0.0
    return round((paid_first_pass / total_submitted) * 100, 1)""",
            expected_output="95.5"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What is the electronic transaction standard for submitting professional medical claims?",
                options=[
                    "EDI 837P",
                    "EDI 835",
                    "HTTP GET 404",
                    "CSV Tab-Delimited"
                ],
                correct_answer="EDI 837P",
                explanation="EDI 837P (Professional) is the HIPAA-mandated electronic transaction format for submitting healthcare claims."
            ),
            QuizQuestionBlueprint(
                question="What electronic document does an insurance payer send back to detail payment and claim adjustment reasons?",
                options=[
                    "EDI 835 Electronic Remittance Advice (ERA)",
                    "W-4 Tax Exemption Form",
                    "Federal Reserve Bank Statement",
                    "Annual 10-K Stock Report"
                ],
                correct_answer="EDI 835 Electronic Remittance Advice (ERA)",
                explanation="The EDI 835 transaction details allowed amounts, contractual write-offs, copays, deductibles, and denial reason codes."
            ),
            QuizQuestionBlueprint(
                question="What does denial code 'CO-16' indicate on an Explanation of Benefits (EOB)?",
                options=[
                    "Claim lacks information or has billing errors needed for adjudication",
                    "The patient's health insurance policy is active and fully paid",
                    "The doctor has been chosen as physician of the year",
                    "The claim has been paid in full without any deductions"
                ],
                correct_answer="Claim lacks information or has billing errors needed for adjudication",
                explanation="CO-16 requires supplemental medical records or corrected diagnostic pointers before the claim can be paid."
            ),
            QuizQuestionBlueprint(
                question="What is a 'Clean Claim' in medical revenue cycle management?",
                options=[
                    "A claim submitted with complete, accurate information that is paid on the first pass without rejection",
                    "A paper bill that has been sanitized with isopropyl alcohol",
                    "A bill that has zero copay or deductible assigned to the patient",
                    "A claim that is under $10 in total billed fees"
                ],
                correct_answer="A claim submitted with complete, accurate information that is paid on the first pass without rejection",
                explanation="A clean claim meets all payer scrubbing guidelines and passes through adjudication to payment on the first submission."
            ),
            QuizQuestionBlueprint(
                question="Under HIPAA, what constitutes Protected Health Information (PHI)?",
                options=[
                    "Any individually identifiable health data, including patient names, SSNs, medical records, and billing details",
                    "Only public statistics published by the CDC without any patient names",
                    "The brand of computers used by the hospital IT team",
                    "The physical address of the insurance company headquarters"
                ],
                correct_answer="Any individually identifiable health data, including patient names, SSNs, medical records, and billing details",
                explanation="PHI encompasses all health information linked to patient identifiers created, used, or transmitted by a covered entity."
            )
        ]
    )
]

MEDICAL_BILLING_MASTERY_COURSE_BLUEPRINT = CourseBlueprint(
    title="Medical Billing & RCM Fundamentals",
    category="Medical Billing",
    description=(
        "The complete guide to medical billing, diagnostic and procedural coding, and healthcare revenue cycle management. "
        "Learn ICD-10-CM structures, CPT coding, CMS-1500 completion, clearinghouse EDI 837/835 transmissions, "
        "CARC denial management, and HIPAA regulatory compliance."
    ),
    color="#EF4444",
    days=DAYS
)
