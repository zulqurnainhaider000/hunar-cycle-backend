"""
Crypto, DeFi & Financial Markets Mastery Blueprint
Comprehensive curriculum covering blockchain architecture, smart contracts, decentralized finance (DeFi),
portfolio risk management, technical analysis indicators, liquidity pools, and market cycles.
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
        title="Day 1: Blockchain Fundamentals & Cryptographic Proofs",
        concept="Blockchains are decentralized, immutable ledgers secured by cryptographic hashing and consensus mechanisms.",
        analogy="Think of a traditional bank like a single accountant sitting in a locked office writing transactions in a private notebook. If that accountant is bribed or makes a mistake, the ledger is compromised. In a blockchain, 10,000 accountants across the world all hold identical notebooks. Every new transaction is shouted out loud, verified by mathematical proof, and recorded into everyone's notebook simultaneously.",
        theory_sections=[
            {
                "heading": "The Anatomy of a Block & Hash Pointer",
                "body": "Every block in a blockchain contains a block header with a cryptographic hash of the previous block, a timestamp, a nonce, and a Merkle root of all transactions included in that block. Altering even a single character in a past transaction changes its hash, breaking the hash chain and invalidating all subsequent blocks."
            },
            {
                "heading": "Consensus Mechanisms: Proof of Work (PoW) vs Proof of Stake (PoS)",
                "body": "Proof of Work relies on computational energy (hashrate) to solve difficult cryptographic puzzles (e.g. Bitcoin). Proof of Stake relies on economic collateral (validators locking capital) to propose and validate blocks (e.g. Ethereum), achieving 99.9% lower energy consumption."
            }
        ],
        code_snippets=[
            {
                "title": "SHA-256 Block Hashing Demonstration (Python)",
                "explanation": "Illustrates how altering transaction data completely changes the resulting cryptographic block hash.",
                "language": "python",
                "code": """import hashlib

def calculate_block_hash(prev_hash: str, transactions: str, nonce: int) -> str:
    payload = f"{prev_hash}{transactions}{nonce}".encode('utf-8')
    return hashlib.sha256(payload).hexdigest()

h1 = calculate_block_hash("00000abc", "Alice->Bob: 5 BTC", 42)
h2 = calculate_block_hash("00000abc", "Alice->Bob: 5.01 BTC", 42) # Tiny 0.01 change!

print(f"Original Block Hash: {h1[:32]}...")
print(f"Tampered Block Hash: {h2[:32]}... (Completely Different!)")"""
            },
            {
                "title": "Proof of Work Mining Simulation",
                "explanation": "Demonstrates the computational difficulty of finding a hash with leading zeros.",
                "language": "python",
                "code": """import hashlib

def mine_block(prev_hash: str, data: str, difficulty: int = 4) -> tuple:
    target = '0' * difficulty
    nonce = 0
    while True:
        candidate = f"{prev_hash}{data}{nonce}".encode()
        h = hashlib.sha256(candidate).hexdigest()
        if h.startswith(target):
            return nonce, h
        nonce += 1

nonce, block_hash = mine_block("00001234", "Tx: Reward Miner 3.125 BTC", difficulty=3)
print(f"Mined Nonce: {nonce} | Hash: {block_hash}")"""
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Satoshi to Bitcoin Converter",
            description="Write a function `satoshis_to_btc(sats)` that converts Satoshis into BTC as a float (1 BTC = 100,000,000 Satoshis).",
            starter_code="""def satoshis_to_btc(sats: int) -> float:
    # Your code here
    pass""",
            solution_code="""def satoshis_to_btc(sats: int) -> float:
    return sats / 100_000_000.0""",
            expected_output="0.5"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What makes a blockchain ledger 'immutable'?",
                options=[
                    "Each block includes a cryptographic hash of the previous block, making tampering immediately detectable",
                    "A single central bank manages and locks all passwords",
                    "Transactions can be edited with permission from the server administrator",
                    "All computers on the network must be physically located in the same data center"
                ],
                correct_answer="Each block includes a cryptographic hash of the previous block, making tampering immediately detectable",
                explanation="Modifying any historical transaction changes its hash, which invalidates the hash pointers of all subsequent blocks across the network."
            ),
            QuizQuestionBlueprint(
                question="How many Satoshis equal one full Bitcoin (1 BTC)?",
                options=[
                    "100,000,000 (100 million)",
                    "1,000 (1 thousand)",
                    "1,000,000 (1 million)",
                    "10,000,000,000 (10 billion)"
                ],
                correct_answer="100,000,000 (100 million)",
                explanation="Bitcoin is divisible up to 8 decimal places; the smallest unit is 1 Satoshi (0.00000001 BTC)."
            ),
            QuizQuestionBlueprint(
                question="What is the primary difference between Proof of Work (PoW) and Proof of Stake (PoS)?",
                options=[
                    "PoW uses computational energy/mining; PoS uses staked capital/validators",
                    "PoW is for smartphones; PoS is for supercomputers",
                    "PoS does not use any cryptographic keys or digital signatures",
                    "PoW allows unlimited inflation; PoS has a hard cap of 10 coins"
                ],
                correct_answer="PoW uses computational energy/mining; PoS uses staked capital/validators",
                explanation="PoW secures networks through proof of expended computing energy, while PoS secures networks through economic collateral staked by validators."
            ),
            QuizQuestionBlueprint(
                question="What is a 'Merkle Root' in a block header?",
                options=[
                    "A cryptographic summary hash of all transactions included in that block",
                    "The username of the miner who discovered the block",
                    "The electricity cost in kilowatt hours used to mine the block",
                    "A physical hardware chip installed inside a Bitcoin ATM"
                ],
                correct_answer="A cryptographic summary hash of all transactions included in that block",
                explanation="A Merkle tree hierarchically hashes pairs of transactions into a single root hash representing the entire transaction set."
            ),
            QuizQuestionBlueprint(
                question="What does 'Non-Custodial' mean regarding cryptocurrency wallets?",
                options=[
                    "You control your private keys and have sole authority over your funds without third-party intermediaries",
                    "An exchange holds your password and can freeze your account at any time",
                    "The government insures your deposit up to $250,000",
                    "You are not allowed to make transactions over $500"
                ],
                correct_answer="You control your private keys and have sole authority over your funds without third-party intermediaries",
                explanation="'Not your keys, not your coins'—non-custodial wallets give users absolute sovereign control over cryptographic key pairs."
            )
        ]
    ),
    DayBlueprint(
        order=2,
        title="Day 2: Decentralized Finance (DeFi) & Automated Market Makers (AMM)",
        concept="DeFi replaces financial middlemen with self-executing smart contracts and mathematical liquidity pools.",
        analogy="Think of a traditional stock exchange like a crowded trading pit where specialist brokers match buyers with sellers for a commission. An Automated Market Maker (AMM like Uniswap) replaces the brokers with a robot holding two buckets of coins (e.g. ETH and USDC) that always enforces the formula: x * y = k. Anyone can trade with the robot 24/7 without asking permission.",
        theory_sections=[
            {
                "heading": "The Constant Product Formula: x * y = k",
                "body": "In an AMM liquidity pool, `x` is the reserve of Token A, `y` is the reserve of Token B, and `k` is a constant product. When a trader deposits Token A to withdraw Token B, `x` increases and `y` decreases. To keep `k` constant, the relative price shifts automatically based on supply and demand."
            },
            {
                "heading": "Impermanent Loss & Liquidity Provision",
                "body": "Liquidity Providers (LPs) deposit pairs of tokens into pools to earn trading fee shares. However, if the price ratio between the two tokens diverges significantly from when they were deposited, the LP suffers 'Impermanent Loss' compared to simply holding the tokens in a wallet."
            }
        ],
        code_snippets=[
            {
                "title": "Uniswap Constant Product AMM Simulator (Python)",
                "explanation": "Calculates swap output amount and price impact according to x * y = k.",
                "language": "python",
                "code": """def simulate_amm_swap(reserve_in: float, reserve_out: float, amount_in: float, fee_pct: float = 0.3) -> dict:
    # 0.3% LP fee
    effective_amount_in = amount_in * (1.0 - (fee_pct / 100.0))
    # dy = (y * dx) / (x + dx)
    amount_out = (reserve_out * effective_amount_in) / (reserve_in + effective_amount_in)
    
    initial_price = reserve_out / reserve_in
    exec_price = amount_out / amount_in
    slippage_pct = round(((initial_price - exec_price) / initial_price) * 100, 2)
    
    return {
        'amount_out': round(amount_out, 4),
        'slippage_pct': slippage_pct,
        'new_reserve_in': round(reserve_in + amount_in, 2),
        'new_reserve_out': round(reserve_out - amount_out, 2)
    }

# Pool: 100 ETH & 300,000 USDC (ETH price = 3,000 USDC)
res = simulate_amm_swap(reserve_in=100.0, reserve_out=300000.0, amount_in=5.0)
print("Swap Result (Selling 5 ETH):", res)"""
            },
            {
                "title": "Position Sizing & Risk Management Calculator",
                "explanation": "Determines maximum safe position size based on account risk tolerance.",
                "language": "python",
                "code": """def calculate_position_size(portfolio_value: float, risk_pct: float, stop_loss_pct: float) -> float:
    # Maximum dollar risk allowed on this trade
    max_risk_dollars = portfolio_value * (risk_pct / 100.0)
    # Position size = Risk Dollars / Stop Loss %
    position_size = max_risk_dollars / (stop_loss_pct / 100.0)
    return round(position_size, 2)

# $10,000 portfolio, risking max 1% ($100), with a 4% stop loss:
pos = calculate_position_size(10000.0, risk_pct=1.0, stop_loss_pct=4.0)
print(f"Max Position Size: ${pos:,.2f} (Restricts total risk to $100)")"""
            }
        ],
        coding_challenge=CodingChallengeBlueprint(
            title="Risk-to-Reward Ratio Calculator",
            description="Write a function `risk_to_reward_ratio(entry_price, stop_loss, target_price)` that returns the R:R ratio rounded to 2 decimal places.",
            starter_code="""def risk_to_reward_ratio(entry_price: float, stop_loss: float, target_price: float) -> float:
    # Your code here
    pass""",
            solution_code="""def risk_to_reward_ratio(entry_price: float, stop_loss: float, target_price: float) -> float:
    risk = abs(entry_price - stop_loss)
    reward = abs(target_price - entry_price)
    if risk <= 0:
        return 0.0
    return round(reward / risk, 2)""",
            expected_output="3.0"
        ),
        quizzes=[
            QuizQuestionBlueprint(
                question="What mathematical formula powers Automated Market Makers (AMM) like Uniswap v2?",
                options=[
                    "x * y = k (Constant Product)",
                    "E = mc^2",
                    "a^2 + b^2 = c^2",
                    "PV = nRT"
                ],
                correct_answer="x * y = k (Constant Product)",
                explanation="The constant product formula `x * y = k` maintains the invariant product of token reserves in a liquidity pool."
            ),
            QuizQuestionBlueprint(
                question="What is 'Impermanent Loss' in decentralized finance?",
                options=[
                    "The difference in value between holding tokens in a wallet versus depositing them into a liquidity pool",
                    "Losing your wallet recovery seed phrase in a house fire",
                    "A transaction fee paid to validators when sending funds",
                    "A temporary internet outage on a centralized exchange"
                ],
                correct_answer="The difference in value between holding tokens in a wallet versus depositing them into a liquidity pool",
                explanation="Impermanent loss occurs when the price divergence of paired tokens reduces pool value compared to holding them individually."
            ),
            QuizQuestionBlueprint(
                question="What does 'Slippage' mean when swapping crypto tokens on an AMM?",
                options=[
                    "The difference between the expected price of a trade and the actual executed price due to pool depth",
                    "When your phone slides off the desk while making a trade",
                    "When an exchange freezes all user withdrawals during high volatility",
                    "The gas fee refund returned to your wallet"
                ],
                correct_answer="The difference between the expected price of a trade and the actual executed price due to pool depth",
                explanation="Large trade sizes relative to pool liquidity shift the reserve ratio, resulting in slippage and less favorable execution prices."
            ),
            QuizQuestionBlueprint(
                question="In professional risk management, what is the recommended maximum capital to risk on a single trade?",
                options=[
                    "1% to 2% of total portfolio value",
                    "50% to 75% of total portfolio value",
                    "100% (all-in on leverage)",
                    "Risk management is unnecessary in bull markets"
                ],
                correct_answer="1% to 2% of total portfolio value",
                explanation="Restricting risk to 1-2% per trade protects traders against prolonged drawdowns and catastrophic account wipeouts."
            ),
            QuizQuestionBlueprint(
                question="What is a 'Smart Contract' in decentralized finance?",
                options=[
                    "Self-executing code deployed on a blockchain that enforces contractual logic without human intermediaries",
                    "A legal document written on parchment paper and signed by a judge",
                    "An artificial intelligence model that predicts future stock prices",
                    "A password manager used to store website credentials"
                ],
                correct_answer="Self-executing code deployed on a blockchain that enforces contractual logic without human intermediaries",
                explanation="Smart contracts automatically execute predetermined logic (e.g. collateral liquidation, token swaps) on the blockchain."
            )
        ]
    )
]

FINANCE_CRYPTO_MASTERY_COURSE_BLUEPRINT = CourseBlueprint(
    title="Crypto, DeFi & Financial Markets Mastery",
    category="Finance & Crypto",
    description=(
        "The comprehensive curriculum for decentralized finance, blockchain protocols, and capital management. "
        "Master cryptographic hashing, consensus algorithms, Automated Market Makers (x*y=k), "
        "liquidity pools, impermanent loss, and quantitative risk management."
    ),
    color="#8B5CF6",
    days=DAYS
)
