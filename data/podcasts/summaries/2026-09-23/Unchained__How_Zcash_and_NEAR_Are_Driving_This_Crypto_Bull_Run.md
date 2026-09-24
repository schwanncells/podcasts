---
podcast: Unchained
date: 2026-09-23
source_transcript: data/podcasts/transcripts/Unchained/2026-09-23_How_Zcash_and_NEAR_Are_Driving_This_Crypto_Bull_Run.md
---

# Unchained — "How Zcash and NEAR Are Driving This Crypto Bull Run"

**Host:** Laura Shin. **Guests:** Ilia Polisukin (co-founder, Near Protocol; co-inventor in LLM research); Mert Mumtas (co-founder and CEO, Helas; Zcash influencer and advisor).

## TL;DR

- **Zcash up 32% in one week, Near up 69%** — Zcash now ranks #9 on CoinGecko, Near ranks #23; both cryptocurrencies are outperforming broader market gains as institutional and individual interest in privacy-enabled DeFi grows.
- **Near Intense connects all chains privately** — A cross-chain settlement layer that aggregates liquidity and enables swaps across Ethereum, Solana, Zcash, and others without requiring users to bridge assets or expose transaction amounts; TVL now exceeds $260 million, with Zcash comprising $71 million.
- **Privacy vs. confidentiality serve different use cases** — Zcash uses zero-knowledge proofs for maximum privacy (no shared state, limited smart contracts); Near Intense uses multi-party computation and secure enclaves for programmable confidentiality (full DeFi but some computation visibility to nodes).
- **Zcash's counterfeit vulnerability was fixed and formally verified** — The Orchard pool flaw (which could have enabled minting) was patched via forced migration to Ironwood, formally verified three times, making undetectable counterfeit "mathematically impossible."
- **Privacy is a retention tool, not just adoption** — Once users experience private transactions, they experience reduced anxiety about financial surveillance; privacy becomes a psychological benefit, not just regulatory compliance.
- **Quantum-proof Zcash with 3x faster blocks coming** — The Zcash upgrade (referred to as NU7) will reduce block times from 75 seconds to 25 seconds, add a new simpler ZK circuit (reducing attack surface), achieve quantum proofing (no recovery needed), and enable private governance voting.
- **Business and travel use cases drive privacy demand** — Institutions cannot disclose customer information; travelers need opsec when booking flights/hotels in high-kidnapping jurisdictions; merchants accept Zcash via Near Intense without seeing sender balances.

---

**Market Performance and Bullish Sentiment**

Zcash has gained 32% in a single week and now ranks #9 on CoinGecko—near all-time highs. Near has appreciated 69% in the same timeframe, ranking #23. Both tokens are significantly outperforming Bitcoin (up roughly 10% on the week) and broader crypto market gains. Laura Shin notes the price action aligns with what she describes as "the dream of Bitcoin DeFi actually coming true, just not on Bitcoin"—a positioning where Zcash functions as a privacy-enhanced store of value and Near Intense acts as the DeFi layer connecting it to other ecosystems.

**Zcash as an Alternative Bitcoin**

Mert Mumtas argues that Zcash should be understood as having different trade-offs rather than being strictly superior to Bitcoin. Like Bitcoin, Zcash aims to be a store of value, but with the added advantage of shielded transactions. He compares it to how Ethereum positioned itself as a scaling solution via sharding—a goal Near Protocol actually achieved. The similarity to Bitcoin is what makes Zcash easy to pitch ("it's encrypted Bitcoin"), but Mumtas emphasizes that privacy alone does not explain the price performance; the full story includes quantum proofing, scale, and the ability to hold value without revealing holdings.

**Privacy as a Prerequisite for Institutional Adoption**

Ilia Polisukin stresses that as blockchain moves beyond speculation toward real business use, privacy becomes essential for regulatory and operational reasons. Banks and fintech firms have been "sitting on the sidelines" waiting for a way to participate in on-chain finance without exposing customer information and internal transaction flows. A financial institution cannot disclose how much it paid suppliers or received from customers; these are material, competitive secrets. Privacy solves this adoption blocker for institutions. Mumtas frames this as a "minority rule" necessity—when certain actors (institutions, regulated entities) have a hard requirement for privacy, the entire system must support it to onboard them, benefiting all users through optionality.

**Distinction: Privacy vs. Confidentiality**

Polisukin explains that Zcash uses zero-knowledge proofs—specifically, users generate proofs and submit them to the network. Only the user knows their balance; they prove they can spend funds without revealing amounts. This approach has a critical limitation: there is no shared state, making traditional smart contract computation (which requires observing state) difficult. Near Intense, by contrast, uses a combination of multi-party computation, secure enclaves, and zero-knowledge proofs to create a "shared private computer." Near nodes run inside secure enclaves (hardware-enforced isolation), and all communication between them is encrypted and proven via zero-knowledge proofs. This "confidentiality" model allows programmable DeFi (yield farming, perpetuals, complex financial primitives) while keeping balances and transaction amounts hidden from outside observers.

Mumtas adds that the choice depends on user need. For a store of value, maximum privacy (Zcash) is appropriate. For programmable DeFi (Near Intense), you need to balance privacy with the ability to run order books and execute contracts—a less extreme but still strong privacy model. He notes regulatory implications: confidentiality (where to/from are hidden but amounts are not) suits individual transparency requirements; full anonymity suits jurisdictions permitting it but risks "being roman stormed" (targeted by regulators).

**Near Intense: Technical Architecture**

Polisukin walks through a Near Intense swap. A user broadcasts an intent—"I want Zcash for Solana"—to the network. Solvers bid on the quote. Once matched, both parties sign an intent, creating a "signed intent" that goes to a settlement system. Near Intense runs a multi-party computation network (part of its validator set) that can sign transactions on multiple blockchains. Near controls addresses on Solana, Ethereum, Zcash, and others. When a user deposits to a Near-controlled address on Solana, the Near smart contract (which lives in a private shard on Near) knows the deposit occurred. The verifier contract—a ledger tracking all balances and signed intents—updates accordingly. The settlement then releases funds either to the user's Near balance or directly to a Zcash shielded address, keeping the transaction confidential. Near thus replicates what centralized exchanges do (custodying funds across chains) but does so programmatically and decentrally.

The TVL in Near Intense now exceeds $260 million, with $71 million in Zcash (Polisukin notes that Dune Analytics is missing the confidential balance in its tracking, so the true figure may be higher).

**The Zcash Vulnerability and Formal Verification**

In June 2026, a critical vulnerability was discovered in Zcash's Orchard pool: the protocol could theoretically allow anyone to mint counterfeit coins within that pool. Because Zcash is fully anonymous, no observer could detect such minting. Mumtas and Polisukin stress that they have no evidence the bug was exploited, but the vulnerability highlights a unique risk in extremely private systems: if an exploit occurs, nobody may ever know.

The solution involved forced migration from Orchard to Ironwood. Over 90% of funds migrated voluntarily; any transaction on Orchard automatically triggers migration. Additionally, Zcash formally verified the Ironwood pool three times, using mathematical proof to demonstrate that undetectable counterfeit bugs "mathematically cannot exist." Mumtas adds that Zcash's response, while technical, points to a broader evolution: smart people reviewing code no longer qualifies as security in the age of AI. Formal verification—using mathematically sound proof checkers—is becoming a must for critical software. Near and Zcash have published results showing they can perform verification 250 times cheaper than traditional approaches, making this defense practical.

**Privacy: Psychological Safety and Retention**

Polisukin argues that privacy is not just an adoption tool but a retention tool. Surveys show people say they care about privacy, then choose convenience—but that contradicts the lived experience of users of private systems. Once someone uses truly private finance (no one can see their balance or transactions), they experience reduced anxiety. There's a "psychological safety" in knowing that nobody can track you, stop you, or take your money based on visibility. People won't return to transparent systems once they've experienced that. The retention effect means privacy is actually orthogonal to convenience: good product design delivers privacy without friction (as Near Intense and Zcash shielded pools do).

**Real-World Use Cases: Travel and Business**

Mumtas describes using Zcash via Near Intense while traveling—specifically booking flights and hotels. He notes that France, for example, has very high rates of crypto-related kidnappings; knowing that no one watching the blockchain can see his net worth is a significant operational security (opsec) win. Zcash wallets have a "pay" feature integrating Near Intense, allowing him to swap Zcash to USDC on any chain and pay merchants, all without the travel concierge seeing his balance or the merchant seeing where funds came from.

Shin adds her own perspective: public transaction visibility (like Venmo's broadcast-by-default model) has led to embarrassing or weaponizable information leaks. She appreciates the ability to pay for things—especially speculative trades or losses—without creating a public record.

**Upcoming Zcash Upgrades**

Mumtas outlines several improvements coming in NU7 (or the broader upgrade roadmap):

1. **Faster blocks** — Block time reduces from 75 to 25 seconds, improving confirmation times and making Near Intense swaps settle faster.
2. **Quantum proofing** — Today Zcash is "quantum recoverable" (if quantum computers break the underlying math, users can recover funds). NU7 adds "quantum proof"—complete security even if quantum computers emerge, with no recovery process needed.
3. **New shielded pool** — A simpler ZK circuit with fewer moving parts, reducing attack surface and risk. Simpler circuits also mean lower latency on mobile and resource-constrained devices.
4. **Private governance voting** — Coin holders will be able to vote on network changes privately, expressing their preference on policy with "skin in the game" while maintaining anonymity—a cyberpunk ideal rarely implemented.

**Security Monitoring: Beyond Code Review**

Both speakers emphasize that security now requires more than "smart people reviewed it." Polisukin notes that Near Intense runs nodes inside secure enclaves and has "alert, detection, and prevention systems" (called "Shield") monitoring the entire infrastructure. If a fork or anomaly (like the Litecoin double-spend via Nimble Limbo pool) occurs, Shield detects it and disconnects that network rather than processing potentially fraudulent transactions. This proactive security is more defensive than hoping bugs don't exist.

