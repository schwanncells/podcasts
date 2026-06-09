---
podcast: Unchained
date: 2026-05-16
source_transcript: data/podcasts/transcripts/Unchained/2026-05-16_Bits_+_Bips_The_Interview_—_The_$16_Trillion_Repo_Market_Is_TradFi's_Central_Nervous_System._Its_Finally_Coming_Onchain.md
---

# Unchained — "Bits + Bips: The Interview — The $16 Trillion Repo Market Is TradFi's Central Nervous System. Its Finally Coming Onchain"

**Host:** Steve Erlic (head of research at Sharplink). **Guests:** Craig Burchil (head of lending at Falcon X, a top prime broker in crypto); Matteo Pendalfi (CEO and co-founder of Pareto, an onchain credit infrastructure provider).

## TL;DR

- **The repo market stands at $16 trillion** — at end of 2024, ~$16 trillion in government bond-backed repo was outstanding globally (~80% of total repo positions), serving as the core mechanism for institutional balance sheet management and short-term liquidity.
- **The 2019 repo crisis was a distribution failure, not a cash shortage** — overnight rates spiked from ~2% to over 20% in a single day because concentrated reserves couldn't be redistributed fast enough; the Fed intervened and created a permanent standing repo facility.
- **Onchain credit has $5.13 billion deployed but is still in infrastructure-building phase** — across 2,000+ onchain credit assets; borrowers and underwriting have matured (Falcon X, Apollo's ACred, Maple Finance's syrup USDC among top participants), but the market structure isn't yet scaling.
- **Stablecoin repo is an emerging near-term use case** — as new stablecoins proliferate, repo could let prime brokers swap stablecoins (e.g., USDC for USDT) temporarily without burn-and-mint cycles.
- **RWA illiquidity is the bigger near-term driver** — onchain repo could bridge quarterly-redemption RWAs and daily-liquidity investors without forcing secondary market sales at a discount.
- **Forced selling cascades (e.g., Morpho vault stress events) could largely be avoided** — a mature onchain repo market would let holders access liquidity by posting collateral rather than selling, absorbing the cascade before it starts.
- **Matteo forecasts $1 trillion in onchain repo within 5 years** — Craig's bear case: standardization on a common repo agreement is a "gargantuan challenge" and the single biggest barrier to a scaled, interoperable market.

---

**What the Repo Market Is and Why It Matters**

Craig Burchil described repos — repurchase agreements — as short-term secured loans in which one party sells an asset and agrees to buy it back later, often overnight. At the end of 2024, roughly $16 trillion in government bond-backed repo was outstanding globally, representing about 80% of total repo activity. The market serves three distinct functions: short-term liquidity for firms bridging temporary cash gaps; leverage (as with hedge funds running basis trades); and balance sheet management for banks, where post-Basel regulations incentivize swapping certain assets at period-end to optimize risk-weighted asset treatment. Burchil compared open-term repos to the crypto industry's familiar "open-term loans" in CeFi lending markets, noting the structural equivalence.

**The 2019 Repo Seizure**

Matteo Pendalfi described the September 2019 episode as a "destructive stress test." Overnight repo rates spiked from ~2% to over 20% in a single day — not because cash was absent, but because reserves were too concentrated at a few large banks and couldn't be redistributed fast enough due to post-crisis balance sheet constraints and settlement timing pressures. The Fed intervened with emergency cash injections for the first time since the 2008 financial crisis and subsequently created a standing repo facility as a permanent backstop. Pendalfi drew a direct parallel to onchain credit's current structural gaps: fragmented infrastructure, uneven liquidity distribution across protocols, and no standing backstop are the same problems repo market evolution was designed to fix. "You have to build the plumbing before you need it, not when you need it."

**Centrally Cleared vs. Bilateral/Triparty Repo**

Centrally cleared repo standardizes all terms — settlement, collateral management, pricing — so participants only negotiate on price. Bilateral repo offers more flexibility (analogous to trading derivatives under a custom ISDA) but requires each participant to maintain their own operational infrastructure per counterparty. Triparty repo emerged as a middle path: a custodian like BNY Mellon or JP Morgan acts as triparty agent, handling collateral selection, substitution, daily valuation, and settlement on behalf of both parties. Burchil noted that one of the core reasons institutions prefer repo over standard loans — bankruptcy remoteness — requires very specific documentation. A true repurchase agreement gives the lender the right to sell collateral directly without going through a bankruptcy proceeding, a legally meaningful distinction that must be preserved in the paperwork even when the underlying mechanics are moved onchain.

**Current State of Onchain Credit**

Pendalfi noted that the $5+ billion deployed across onchain credit represents real progress but still reflects an infrastructure-building phase. What has matured: institutional borrowers like Falcon X are accessing credit onchain with clear terms, defined collateral arrangements, and legally enforceable structures — a sharp contrast from early onchain credit where borrowers were often crypto-native entities with thin credit histories and limited accountability. Professional underwriting with traditional credit discipline has also entered the space. Composability is beginning to demonstrate real value: using an onchain credit facility or RWA asset as collateral in a DeFi overcollateralized protocol is a meaningful proof of concept for the next phase of the market.

**The Legal Friction Around Smart Contract Repo**

Smart contracts are not legal contracts, and the documentation requirements to achieve bankruptcy remoteness are difficult to satisfy programmatically. Burchil's view: onchain repo doesn't have to be fully programmatic. A hybrid model — where contractual paperwork is signed off-chain while smart contracts execute and manage the actual position — is both valid and likely necessary to attract larger, traditionally-oriented participants. He framed the choice between bilateral (customizable, bespoke, higher operational burden) and centrally cleared (standardized, automated, easier to scale) as the same tradeoff that already exists in TradFi repo — and argued there is no one-size-fits-all answer. Forcing full on-chain execution could exclude the very counterparties needed to build market depth.

**Stablecoin Repo and RWA Illiquidity**

Burchil identified two near-term drivers for onchain repo. First, the proliferation of new stablecoins creates demand for fast, cost-efficient stablecoin swaps (e.g., needing USDT when holding USDC for a client settlement) without going through burn-and-mint cycles. A liquid repo market would let prime brokers swap stablecoins temporarily and unwind. Second — and Burchil considered this potentially more significant — many RWAs currently offer quarterly or gated liquidity, while investors want daily liquidity. Onchain repo facilities could bridge that gap: an investor posts the RWA as collateral and gets instant liquidity, paying interest rather than selling at a discount on secondary markets.

**Deleveraging Use Case and Morpho Dynamics**

Burchil pointed to stress events in Morpho vault markets as the clearest real-world demonstration of why onchain repo matters. During liquidity crunches, participants are forced to sell positions they would have preferred to keep — triggering a cascade of price declines, spiking interest rates, additional liquidations, and depeg risk across LSTs. A mature repo facility would have let holders access liquidity by posting assets as collateral rather than selling. For Morpho vault curators specifically, repo backstops would allow higher LTVs and larger allocations to assets currently limited by illiquid redemption windows. Falcon X already offers deleveraging facilities against various assets, not only their own credit token, because of this dynamic.

**Five-Year Outlook**

Pendalfi expressed high confidence that onchain repo will reach at least $1 trillion within five years, driven by the pipeline of traditional finance players actively exploring onchain applications, and said he wouldn't be surprised to see it happen sooner. Burchil's bull case: the need is real, the facilities are already being built, and the market participants are already engaged. Bear case: standardization — getting the ecosystem onto a common repo agreement with uniform terms, analogous to how centrally cleared TradFi repo works — is a "gargantuan challenge." Efforts to create a standardized onchain repo form (he referenced former colleagues at Membrane working toward something analogous to GIMRA in TradFi) face massive barriers. Onchain infrastructure is, in his view, probably the best starting point for building such a standard, but it remains the single biggest obstacle to a truly scaled and interoperable onchain repo market.
