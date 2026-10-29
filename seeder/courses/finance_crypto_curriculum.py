"""
Finance & Crypto Curriculums
Contains:
1. Technical Analysis & Candlestick Trading Mastery (15 Days)
2. DeFi Protocols, Smart Contracts & Crypto Investing (15 Days)
"""

from seeder.curriculum_builder import make_day, make_course

# =========================================================================
# COURSE 1: Technical Analysis & Candlestick Trading Mastery (15 Days)
# =========================================================================
TA_DAYS = []

ta_titles = {
    1: ("Anatomy of Japanese Candlesticks (OHLC & Wicks)", "Candlesticks reveal the psychological battle between buyers (bulls) and sellers (bears) over a fixed timeframe.", "Think of a candle like a boxing round. The bell rings at Open, boxers trade blows reaching High and Low extremes, and the round ends at Close. The wick shows where one side pushed forward but was driven back."),
    2: ("Support, Resistance & Horizontal Key Levels", "Key horizontal levels represent historical institutional order clusters and liquidity zones.", "Support is like a reinforced concrete floor that bounces a falling basketball. Resistance is the hard ceiling that stops it from rising higher."),
    3: ("Trendlines, Market Structure & Breakouts", "Market structure defines whether an asset is in an uptrend (HH/HL), downtrend (LH/LL), or consolidation.", "A moving train maintains forward momentum until a derailment occurs; trends stay intact until structure breaks."),
    4: ("Reversal Patterns: Doji, Hammer, Engulfing & Pin Bars", "Reversal candles signal exhaustion of the prevailing momentum and impending trend changes.", "A marathon runner collapsing just yards from the finish line signals they cannot maintain the pace, opening the door for a competitor to pass."),
    5: ("Continuation Patterns: Bull Flags, Triangles & Wedges", "Continuation patterns represent brief pauses where institutions accumulate before the next explosive trend leg.", "A diver bending their knees on the springboard before launching into the air; price contracts before expanding violently."),
    6: ("Volume Spread Analysis & Order Flow Mechanics", "Volume validates price action; price movement without institutional volume is a trap.", "A high-speed racecar needs fuel; a breakout without massive volume is a car rolling downhill on neutral—it will stall."),
    7: ("Moving Averages (EMA 20, 50, 200) & Golden Crosses", "Exponential moving averages smooth out market noise to reveal dynamic institutional support.", "The moving average is the gravitational pull of the planet; price can rocket away temporarily, but gravity inevitably pulls it back."),
    8: ("RSI (Relative Strength Index) & Hidden Divergences", "RSI measures the velocity and magnitude of directional price movements to detect overbought/oversold extremes.", "A car's speedometer revving into the redline; it indicates the engine is overheating and cannot sustain top speed much longer."),
    9: ("MACD (Moving Average Convergence Divergence) Momentum", "MACD tracks the relationship between two moving averages of an asset's price to gauge momentum shifts.", "Watching two waves collide in the ocean; when the fast wave crosses above the slow wave, a surge of momentum follows."),
    10: ("Fibonacci Retracements & The Golden Pocket (0.618)", "Natural geometric ratios describe how deeply price pulls back before continuing its primary trend.", "A bow being drawn back; pulling it back 61.8% stores the maximum kinetic energy to propel the arrow forward."),
    11: ("Multi-Timeframe Analysis (Daily Trend, 4H Setup, 15M Execution)", "Aligning higher-timeframe context with lower-timeframe precision optimizes risk-to-reward entries.", "A military general uses satellite maps for strategy, drone feeds for battlefield maneuvers, and binoculars for the sniper rifle."),
    12: ("The 1% Risk Management Rule & Position Sizing", "Capital preservation is rule #1; risking more than 1-2% on any single trade leads to ruin.", "A submarine has watertight bulkheads; if one compartment floods (a losing trade), the ship seals it off and stays afloat."),
    13: ("Risk-to-Reward (R:R) Ratios & Mathematical Expectancy", "You can be wrong 60% of the time and still be wildly profitable with a 3:1 R:R ratio.", "A business that loses $100 on bad inventory but makes $400 on good inventory prints cash even if half the items fail."),
    14: ("Trading Psychology, FOMO & Revenge Trading Defense", "The biggest enemy in trading is not the market, but your own emotions and dopamine loops.", "A seasoned pilot follows the pre-flight checklist blindly during turbulent storms rather than panicking on emotion."),
    15: ("Capstone: Constructing a Rule-Based Quantitative Trading Plan", "Synthesize indicators, risk parameters, and execution rules into an algorithmic trade journal.", "You have graduated from gambling to running a systematic, quantitative trading desk.")
}

for day_num in range(1, 16):
    t_info = ta_titles.get(day_num, (f"Day {day_num}: Technical Strategy", "Master market analysis.", "Analytical precision."))
    TA_DAYS.append(make_day(
        order=day_num,
        title=f"Day {day_num}: {t_info[0]}",
        concept=t_info[1],
        analogy=t_info[2],
        sections=[
            (f"Theory & Mechanics of {t_info[0]}", f"Analyzing {t_info[0]} provides objective mathematical edges in high-volatility financial and cryptocurrency markets. Professional traders rely on strict probability rather than emotional intuition."),
            ("Practical Chart Execution & Edge Definition", "Understand how institutional market makers exploit retail liquidity at these levels, and position your orders alongside institutional flow.")
        ],
        snippets=[
            (f"{t_info[0]} Indicator Calculation (Python)", f"""def calculate_ta_metric_{day_num}(price: float, volume: float) -> dict:
    signal = 'BULLISH' if price > 100 and volume > 1000 else 'NEUTRAL'
    return {{'day': {day_num}, 'price': price, 'volume': volume, 'signal': signal}}

print(calculate_ta_metric_{day_num}(105.5, 1500.0))""", "python"),
            ("Risk Sizing Formula", f"""def position_size_calculator(account: float, risk_pct: float, stop_pct: float) -> float:
    risk_dollars = account * (risk_pct / 100.0)
    return round(risk_dollars / (stop_pct / 100.0), 2)

print("Position size ($10k acct, 1% risk, 3% stop):", position_size_calculator(10000.0, 1.0, 3.0))""", "python")
        ],
        challenge=(f"TA Challenge Day {day_num}", "Write a function `calculate_profit_factor(total_gains, total_losses)` that returns the profit factor rounded to 2 decimal places.",
                   "def calculate_profit_factor(total_gains: float, total_losses: float) -> float:\n    pass",
                   "def calculate_profit_factor(total_gains: float, total_losses: float) -> float:\n    if total_losses <= 0: return 0.0\n    return round(total_gains / total_losses, 2)", "2.25"),
        quizzes=[
            (f"What is the foundational concept of {t_info[0]}?", [f"To leverage {t_info[0]} to establish objective risk-defined trading edges", "To predict the exact future with 100% certainty", "To trade with 100x leverage on all savings", "To abandon stop losses completely"], f"To leverage {t_info[0]} to establish objective risk-defined trading edges", f"Day {day_num} establishes {t_info[0]} as a risk-defined edge."),
            ("Why is the 1% risk rule standard practice for professional traders?", ["It guarantees survival through long losing streaks without blowing up the account", "It forces you to trade only 1 penny per day", "It is legally mandated by the United Nations", "It prevents you from paying capital gains tax"], "It guarantees survival through long losing streaks without blowing up the account", "Even with 10 consecutive losses, risking 1% preserves over 90% of total capital."),
            ("What does a 3:1 Risk-to-Reward ratio mean in practice?", ["Your profit target is 3 times larger than your maximum stop loss distance", "You trade 3 times per day", "You risk $3 to make $1", "You must win 3 trades out of 3"], "Your profit target is 3 times larger than your maximum stop loss distance", "A 3:1 R:R allows a trader to be profitable with only a 30% win rate."),
            ("Why does volume confirm a genuine breakout?", ["High volume proves institutional money is participating and absorbing supply", "Volume decreases server latency", "It changes the color of the candlesticks", "Volume has zero significance in modern markets"], "High volume proves institutional money is participating and absorbing supply", "Without institutional volume, breakouts are easily reversed by market makers."),
            ("What is the primary danger of revenge trading after a loss?", ["Trading on emotional anger and bypassing risk rules, leading to rapid capital destruction", "Your broker will give you an interest-free loan", "Your computer will restart automatically", "You will instantly earn back all losses"], "Trading on emotional anger and bypassing risk rules, leading to rapid capital destruction", "Revenge trading replaces disciplined strategy with emotional gambling.")
        ]
    ))

TECHNICAL_ANALYSIS_BLUEPRINT = make_course(
    title="Technical Analysis & Candlestick Trading Mastery",
    category="Finance & Crypto",
    description=(
        "The complete 15-Day masterclass on reading financial and crypto charts with institutional precision. "
        "Master OHLC candlesticks, support/resistance, market structure, EMA dynamic ribbons, RSI divergences, "
        "Fibonacci golden pockets, and quantitative 1% risk management."
    ),
    color="#8B5CF6",
    days=TA_DAYS
)


# =========================================================================
# COURSE 2: DeFi Protocols, Smart Contracts & Crypto Investing (15 Days)
# =========================================================================
DEFI_DAYS = []

defi_titles = {
    1: ("Blockchain Architecture & Distributed Ledgers", "Blockchains combine cryptographic hashing and consensus to achieve Byzantine fault-tolerant ledgers.", "A public town square bulletin board where anyone can post transactions, but no one can erase what was already carved in stone."),
    2: ("The Ethereum Virtual Machine (EVM) & Gas Economics", "The EVM is a decentralized world computer executing deterministic bytecode funded by gas fees.", "A public toll road where every mile of road traveled and computational hill climbed costs a specific amount of fuel."),
    3: ("Non-Custodial Wallets, Private Keys & Mnemonic Phrases", "Sovereign custody gives users sole authority over cryptographic asset access.", "A master bank vault with a mathematical combination lock where you are the only human on earth who knows the code."),
    4: ("Smart Contract Standards: ERC-20 & ERC-721", "Standardized smart contract interfaces enable frictionless composability across the entire ecosystem.", "Standard USB-C ports that allow devices from any manufacturer to plug and play with zero custom adapters."),
    5: ("Decentralized Exchanges (DEXs) vs Centralized Exchanges (CEXs)", "DEXs allow trustless peer-to-contract trading directly from personal wallets.", "Trading apples for oranges directly at a farmer's market stall without handing your fruit to an exchange vault."),
    6: ("Constant Product Automated Market Makers (Uniswap x*y=k)", "Algorithmic pricing balances token pools mathematically without human market makers.", "A balance scale with gold on one side and silver on the other; removing gold automatically increases silver's relative value."),
    7: ("Liquidity Provision & Demystifying Impermanent Loss", "LPs earn protocol swap fees while taking on divergence risk between paired assets.", "Running a currency exchange booth at an airport; you earn fees on every trade, but currency swings can affect inventory value."),
    8: ("DeFi Lending Protocols (Aave, Compound & Health Factor)", "Over-collateralized lending enables trustless loans without credit checks or bank managers.", "Pawning a gold watch worth $1,000 to borrow $700 in cash; if gold drops to $750, the pawn shop liquidates the watch to protect itself."),
    9: ("Stablecoin Architectures: Fiat-Backed vs Over-Collateralized", "Stablecoins maintain purchasing power pegs through centralized reserves or algorithmic debt vaults.", "A casino chip that the cashier guarantees will always swap back for exactly one dollar at the cashier cage."),
    10: ("Layer 2 Scaling Solutions: Optimistic & ZK-Rollups", "Rollups process transactions off-chain and post compressed cryptographic proofs to Layer 1.", "A bus carrying 50 passengers paying a single highway toll together instead of 50 individual cars clogging the road."),
    11: ("Cross-Chain Bridges & The Interoperability Trilemma", "Bridges wrap or lock assets to communicate across disparate state machines.", "A currency exchange booth on a border crossing between two countries that speak different languages."),
    12: ("Smart Contract Security, Audits & Preventing Exploits", "Immutability means code bugs are permanent; thorough testing and audits prevent re-entrancy hacks.", "Installing a state-of-the-art bank vault door with biometric sensors so thieves cannot use a crowbar to pry it open."),
    13: ("Liquid Staking Derivatives (LSDs like Lido)", "Liquid staking unlocks capital efficiency for proof-of-stake validation assets.", "Depositing gold in a vault and receiving an official bearer certificate you can trade around town while earning vault interest."),
    14: ("Crypto Portfolio Allocation & Dollar-Cost Averaging (DCA)", "Disciplined systematic purchasing outperforms emotional market timing in volatile cycles.", "Investing a set percentage of your paycheck on the 1st of every month regardless of whether the weather is sunny or stormy."),
    15: ("Capstone: Deploying a Multi-Protocol Yield & Risk Strategy", "Synthesize wallets, DEXs, lending, and hedging into a production-grade crypto portfolio.", "You are fully equipped as a sovereign Web3 investor and decentralized finance practitioner.")
}

for day_num in range(1, 16):
    t_info = defi_titles.get(day_num, (f"Day {day_num}: DeFi Mechanics", "Protocol fundamentals.", "Decentralized systems."))
    DEFI_DAYS.append(make_day(
        order=day_num,
        title=f"Day {day_num}: {t_info[0]}",
        concept=t_info[1],
        analogy=t_info[2],
        sections=[
            (f"Architecture of {t_info[0]}", f"Analyzing {t_info[0]} unlocks deep institutional understanding of Web3 and decentralized finance protocols. Smart contracts enable trust-minimized financial services that run 24/7."),
            ("Risk Analysis & On-Chain Mechanics", "Audit on-chain smart contract data to verify liquidity depth, contract ownership privileges, and collateralization health factors.")
        ],
        snippets=[
            (f"{t_info[0]} Smart Contract Logic (Solidity/Python)", f"""def evaluate_defi_state_{day_num}(collateral_usd: float, debt_usd: float) -> dict:
    health_factor = round(collateral_usd / debt_usd, 2) if debt_usd > 0 else 999.0
    status = 'HEALTHY' if health_factor >= 1.5 else 'LIQUIDATION_RISK'
    return {{'day': {day_num}, 'health_factor': health_factor, 'status': status}}

print(evaluate_defi_state_{day_num}(15000.0, 8000.0))""", "python"),
            ("AMM Swap Output Calculation", f"""def calculate_amm_output(reserve_a: float, reserve_b: float, delta_a: float) -> float:
    # dy = (y * dx) / (x + dx)
    return round((reserve_b * delta_a) / (reserve_a + delta_a), 4)

print("Tokens received:", calculate_amm_output(100.0, 300000.0, 2.0))""", "python")
        ],
        challenge=(f"DeFi Health Factor Challenge Day {day_num}", "Write a function `calculate_health_factor(collateral_usd, debt_usd, liquidation_threshold=0.8)` that returns `(collateral * threshold) / debt` rounded to 2 decimal places.",
                   "def calculate_health_factor(collateral_usd: float, debt_usd: float, liquidation_threshold: float = 0.8) -> float:\n    pass",
                   "def calculate_health_factor(collateral_usd: float, debt_usd: float, liquidation_threshold: float = 0.8) -> float:\n    if debt_usd <= 0: return 999.0\n    return round((collateral_usd * liquidation_threshold) / debt_usd, 2)", "1.6"),
        quizzes=[
            (f"What is the core function of {t_info[0]}?", [f"To enable {t_info[0]} in a trust-minimized, decentralized financial ecosystem", "To allow governments to censor private wallets", "To slow down internet connections", "To eliminate the need for computers"], f"To enable {t_info[0]} in a trust-minimized, decentralized financial ecosystem", f"Day {day_num} covers {t_info[0]}."),
            ("What does the 'Health Factor' represent in DeFi lending protocols like Aave?", ["The safety margin of collateral relative to borrowed debt; below 1.0 triggers liquidation", "The physical health of the protocol founder", "The speed of the network's internet connection", "The number of active Twitter followers"], "The safety margin of collateral relative to borrowed debt; below 1.0 triggers liquidation", "A health factor above 1.5 protects against market volatility and automated liquidation."),
            ("Why is 'Not your keys, not your coins' a golden rule in Web3?", ["If a third-party centralized exchange holds your private keys, they control your assets", "Keys are made of physical brass", "Keys can only be kept in a safety deposit box", "It is a slogan used to promote credit cards"], "If a third-party centralized exchange holds your private keys, they control your assets", "Non-custodial custody ensures only the owner can authorize transactions."),
            ("What is the primary benefit of Layer 2 Rollups like Arbitrum and Base?", ["They bundle hundreds of transactions off-chain, drastically reducing Ethereum gas fees", "They replace the internet with radio waves", "They make all cryptocurrencies free", "They delete past blockchain history"], "They bundle hundreds of transactions off-chain, drastically reducing Ethereum gas fees", "Rollups provide high throughput and low fees while inheriting L1 security."),
            ("What causes Impermanent Loss for Liquidity Providers in an AMM?", ["Price divergence between the two deposited tokens compared to simply holding them in a wallet", "A physical power failure at the server farm", "Paying too much income tax", "The exchange running out of paper money"], "Price divergence between the two deposited tokens compared to simply holding them in a wallet", "Whenever the ratio between token prices shifts, arbitrageurs adjust pool reserves.")
        ]
    ))

DEFI_MASTERY_BLUEPRINT = make_course(
    title="DeFi Protocols, Smart Contracts & Crypto Investing",
    category="Finance & Crypto",
    description=(
        "The comprehensive 15-Day guide to decentralized finance, smart contract architecture, and on-chain investing. "
        "Master EVM gas mechanics, non-custodial security, Uniswap AMMs (x*y=k), liquidity farming, Aave lending health factors, "
        "Layer 2 rollups, and disciplined portfolio risk management."
    ),
    color="#7C3AED",
    days=DEFI_DAYS
)
