---
podcast: Unchained
date: 2026-03-19
source_transcript: data/podcasts/transcripts/Unchained/2026-03-19_DEX_in_the_City_Why_the_Binance_Case_Against_the_WSJ_'Is_Probably_Not_a_Winner'.md
---

# Unchained — "DEX in the City: Why the Binance Case Against the WSJ 'Is Probably Not a Winner'"

**Hosts:** Katherine Kirkpatrick Bos, Jessi Brooks. **Guest:** Jane Khodarkovsky (partner at Arktouros; former federal prosecutor; sanctions and anti-money laundering expert).

## TL;DR

- **Binance sues WSJ for defamation over $1.7 billion Iran allegations** — Wall Street Journal reported that $1.7 billion in crypto flowed through Binance tied to Iran and the Islamic Revolutionary Guard Corps (IRGC); Binance disputes this and claims WSJ disregarded Binance's rebuttal.
- **Defamation case faces "actual malice" standard, likely difficult to win** — As a public figure, Binance must prove the Journal knew the reporting was false and acted with reckless disregard; this is one of the hardest standards in media law and rarely succeeds.
- **Sanctions evasion allegations predate 2023 settlement** — The 2023 DOJ/FinCEN/OFAC/CFTC resolution covered 2017-2020 activity; the WSJ allegations concern 2022-2024 activity, meaning new investigation timeline and potential parallel DOJ investigation.
- **CFTC issues Phantom no-action letter on self-custodial wallets** — Crypto wallet Phantom can allow users to trade CFTC derivatives through regulated partners without registering as an introducing broker, because Phantom's role is passive (no order discretion, no trading signals).
- **AAVE user loses $50 million in single slippage event** — User converted $50 million to stablecoin in one liquidity pool, received only $36,000 due to catastrophic slippage despite warning of liquidity constraints; raises best-execution questions for DeFi.
- **SEC-CFTC memorandum of understanding aims for clearer regulatory lanes** — The two agencies formalized commitment to collaborate on jurisdiction boundaries; success depends on personal relationships between leadership and may be temporary.
- **Stripe integrates HTTP 402 (Coinbase protocol) for AI agent payments** — Machine-to-machine micropayments enable AI agents to pay for resources like paywalled articles; raises unresolved money-transmission questions for crypto facilitators.
- **Custom cancer vaccine developed via ChatGPT saves dog's life** — Australian data scientist used AI tools and Google DeepMind's AlphaFold to design personalized vaccine for rescue dog with terminal cancer; tumor shrank 75% after first injection.

---

**Binance's Defamation Suit Against the Wall Street Journal**

In February 2026, the Wall Street Journal reported that $1.7 billion in cryptocurrency flowed through Binance and was tied to Iran, specifically the Islamic Revolutionary Guard Corps (IRGC). Iran is a "comprehensively sanctioned jurisdiction" under U.S. sanctions law, meaning no U.S. person or company is permitted to provide services there. Binance disputes the allegations as "categorically false" and sued the Journal for defamation in civil court.

The hosts and Khodarkovsky discuss the legal standard required for the suit. Under defamation law for public figures, Binance must prove "actual malice"—that the Journal knew the information was false or acted in reckless disregard of its truth. Binance has stated it rebutted the Journal's claims before publication, and Khodarkovsky notes this defamation case will be "very difficult to win." Catherine adds that "every defamation case is hard because you have to prove that someone really knew that what they were publishing was going to be false."

A critical distinction for the investigation: the 2023 settlement and monitors covered activity from 2017-2020. The WSJ allegations concern 2022-2024 activity, meaning a potential new DOJ investigation would address different time periods. Congressional pressure on DOJ to investigate already exists, though it remains unclear whether FinCEN or other agencies will launch parallel investigations alongside any DOJ effort.

Khodarkovsky emphasizes the operational reality of sanctions evasion in crypto: sophisticated actors in Iran need "middlemen" with access to platforms willing to move money and misrepresent its source. The alleged scheme involved Chinese actors opening Binance accounts and routing funds to Iran, making it difficult for Binance to claim ignorance given the compliance flags such activity should raise.

**Sanctions Enforcement, Money Transmission, and OFAC's Limited Reach**

Catherine explains that OFAC (Office of Foreign Assets Control), which enforces sanctions, is "a tiny office" with enormous power—it can seize assets and cut off access to the U.S. financial system. However, OFAC moves slowly; it took years to designate the first crypto address, and new addresses defeat that strategy instantly. Prosecuting sanctions violations is harder than OFAC enforcement because it is not "strict liability"—prosecutors must prove the defendant knew the sanctions law existed, "the highest standard of cases" that Khodarkovsky had to prove as a federal prosecutor. This decoupling means OFAC action and DOJ prosecution operate at different speeds.

**CFTC Provides Clear Runway for Phantom Wallet**

The CFTC issued a no-action letter to Phantom, a self-custodial crypto wallet, permitting it to allow users to trade derivatives through regulated partner exchanges without registering as an introducing broker. The distinction matters: an introducing broker solicits or accepts orders for derivatives, but Phantom's role is "passive"—no discretion over individual orders, no buy or sell signals. The CFTC essentially articulated that if a front end remains sufficiently passive, it avoids certain registration requirements.

Khodarkovsky notes that crypto Twitter misinterpreted this as blanket approval for all front ends, when the guidance is much narrower. The letter also emphasizes identity verification, which connects back to sanctions compliance: regulators want to know that AI agents and agentic payments cannot bypass KYC and AML requirements.

The CFTC additionally reaffirmed existing guidance on prediction markets, stressing that Designated Contract Markets (DCMs) must police contracts for manipulation—described as "really a nothing burger" by Catherine, as it merely restates existing rules. The CFTC did signal strong territorial claims, specifically noting that sports-related event contracts fall under CFTC jurisdiction, essentially telling states to "get off our lawn."

**The AAVE Slippage Catastrophe and the DeFi Best-Execution Gap**

A user attempted to swap $50 million into a liquidity pool, receiving only $36,000 due to extreme slippage. Despite warnings about liquidity constraints and instructions to acknowledge the risk, the transaction executed. AAVE CEO Stani defended the protocol, arguing that warnings were provided and the user checked the box. Separately, AAVE and CoW Swap issued conflicting postmortems: AAVE blamed liquidity constraints and price impact; CoW Swap blamed infrastructure failure.

Catherine frames this as a "best execution" problem. In traditional finance, brokers are required by FINRA and SEC regulation to find the most favorable terms for clients and are prohibited from executing obviously destructive trades. The EU's MiFID 2 framework similarly requires brokers to act in clients' best interests. DeFi protocols, being unregulated, face no such duty; they offer only warnings and user acknowledgment.

Jessi criticizes the industry's double-speak: DeFi advocates claim it is safer than centralized finance and demand regulatory clarity that excludes DeFi, while simultaneously defending $50 million losses as user error. She argues that "we can't have a holistic conversation about DeFi when things like this are happening in the background."

Khodarkovsky advocates for technical and software solutions—not regulation—that mitigate user harm, such as built-in safeguards against catastrophic slippage. She notes that institutional adoption of DeFi requires confidence that large transactions will not be decimated by illiquidity, and that the gap between DeFi's aspirations and its current user experience must narrow for mainstream adoption.

Catherine previews a forthcoming academic paper co-authored with Jessi on programmable risk management for autonomous agents, signaling that legal and technical frameworks for emerging tech remain underdeveloped.

**SEC-CFTC Memorandum of Understanding on Regulatory Coordination**

The two agencies formalized an MOU committing to clearer collaboration and jurisdiction-sharing. In Khodarkovsky's experience, inter-agency coordination has historically been "very random and pretty much entirely relationship based." This MOU is consistent with public statements from both agency heads supporting a "whole of government approach" and clearer "rules of the road."

However, success is contingent on leadership relationships and may not outlast personnel changes. Khodarkovsky notes that the 2023 Binance settlement itself involved DOJ, FinCEN, OFAC, and the CFTC working in concert, so precedent for joint enforcement exists. The hosts agree that even a "nothing burger" MOU is preferable to agency conflict, especially given that Chair see (SEC) came from the CFTC and has preexisting relationships with the agency's leadership.

**HTTP 402 and Agentic Commerce: Unresolved Money-Transmission Questions**

Stripe integrated HTTP 402, an open-source protocol developed by Coinbase and Cloudflare, enabling AI agents to pay for resources on a per-use basis (e.g., two cents to read a paywalled article). The pitch is seductive: the Internet finally has a native payment layer for machine-to-machine commerce, and crypto provides the settlement layer.

However, actual adoption remains minimal. Daily volume is approximately 30,000; monthly volume over the past 30 days is roughly 1.6 million, despite broader industry claims of 24 million. Competitors including Visa (Intelligent Commerce), MasterCard (Agent Pay), and PayPal offer similar functionality without requiring crypto.

Jessi highlights the legal tension: 402 transactions involve "facilitators" that verify and settle payments on-chain, but the facilitators' operational scope is not standardized. Coinbase is properly licensed; however, the protocol is open-source, and many builders are integrating it without necessarily understanding money-transmission licensing requirements. The central unresolved question: will FinCEN classify facilitators as money transmitters, and if so, who bears the licensing burden—the protocol layer, the integration layer, or individual nodes?

Khodarkovsky frames the issue as one of identity and control. Money transmission is defined by taking custody and control of others' funds; if a facilitator holds funds or can redirect them, money-transmission rules apply. Conversely, if an AI agent retains unambiguous control of its own funds and merely signals payment intent to the facilitator, the question becomes murkier. She emphasizes the need to "see the flow" of funds and identify "points of control" to determine whether money transmission is genuinely occurring.

The unresolved question will likely drive future academic papers, policy debate, and possibly enforcement, mirroring the legal complexity that surrounded Tornado Cash and 1960 statute interpretation. Developer protections and the boundary between software provision and money transmission remain contested terrain.

**AI-Driven Personalized Medicine: Dog Cancer Vaccine**

A Sydney-based tech entrepreneur and data scientist with no vaccine expertise used ChatGPT to research cancer treatment, then collaborated with Google DeepMind's AlphaFold to design a custom vaccine for his rescue dog, Rosie, who was diagnosed with terminal cancer. Conventional treatments (chemotherapy and surgery) failed, and veterinarians predicted only months of survival.

Within two months, the entrepreneur developed and administered a personalized vaccine. After the first injection, Rosie's tumor shrank 75%, significantly extending her expected lifespan. While not a cure, the result demonstrates a tangible example of AI augmenting expertise in healthcare, enabling a non-specialist to leverage machine learning and expert tools to save an animal's life.

The hosts celebrate this as "technology for good," contrasting the positive potential of AI with media narratives of AI risk. The story also underscores a broader theme: emerging technologies (crypto, AI agents, personalized medicine) will outpace legal and regulatory frameworks, and their ultimate impact depends on how thoughtfully the industry balances innovation with risk mitigation.
