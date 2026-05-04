---
podcast: Unchained
date: 2026-04-22
source_transcript: data/podcasts/transcripts/Unchained/2026-04-22_Is_Canton_Permissionless_CEO_Says_Yes,_but_SuperValidators_Need_Approval.md
---

# Unchained — "Is Canton Permissionless? CEO Says Yes, but SuperValidators Need Approval"

**Host:** Laura Shin. **Guests:** Yuval Ruz (co-founder and CEO, Digital Asset; formerly DRW and Citadel); Hasib Qureshi (managing partner, Dragonfly; venture investor in crypto infrastructure); Alex Glukowski (co-founder and CEO, Matterlabs; building Previdium private institutional blockchain on Ethereum).

## TL;DR

- **Canton aims to bring capital markets on-chain** — Digital Asset's goal is to enable issuers to move books and records natively on-chain while maintaining privacy and settlement finality, solving problems stablecoins and traditional finance can't address on permissionless infrastructure.
- **At the heart of the debate: Is Canton a blockchain or a database?** — Alex argues it's a "mediated messaging network" that cannot prevent double spend without relying on centralized issuers; Yuval counters that Canton's UTXO model with encrypted UTXOs allows multi-party validation and decentralized composability, unlike account-based chains.
- **Canton relies on issuer signatures to prevent double spend** — In the DAML (Digital Asset Modeling Language) contract system, issuers must co-sign every state transition as a multi-party requirement. If an issuer is compromised by a state-level actor, they could mint unlimited assets undetectably (e.g., minting billions of tokens, diluting existing holders).
- **Previdium offers visibility; Canton trades it for privacy** — Previdium (a ZK-rollup on Ethereum) shows all state changes on mainnet—attackers cannot hide a compromise. Canton's design hides transaction details from non-participants, making unauthorized asset creation undetectable without the issuer's self-report.
- **"Permissionless" on Canton means different things** — Yuval defines it as: anyone can build apps, participate, and apply to become a super validator (a 46-node quorum that orders and timestamps transactions). Approval requires super-majority vote. Alex argues this is not permissionless in the crypto sense—it requires explicit permission from existing validators, unlike staking-based networks where anyone meeting a minimum can participate objectively.
- **Super validators do not validate business logic; issuers do** — Yuval explains that super validators act as an ordering and timestamping layer (like ISPs) without seeing transaction contents. The issuer is the party that prevents double spend. Canton coin (the native asset) is fully permissionless; RWAs (real-world assets) rely entirely on issuer integrity.
- **Most controversies trace to market success and tribal resentment, not technical flaws** — Yuval notes that other L2s and L1s have far more centralized sequencers and higher staking barriers, yet face no scrutiny. Canton's partnerships (Mizuho, Nomura, JPX, Hanwha, Visa, JP Morgan, HSBC) sparked criticism online because execution and adoption became undeniable; competitors building on other chains are called heroes; those choosing Canton become villains.

---

**The Premise: Bringing Capital Markets On-Chain**

Yuval Ruz opens by framing Digital Asset's goal: to convince institutional issuers to move their books and records on-chain natively. The core problem is that existing permissionless blockchains don't solve for institutional requirements: privacy (not all transactions should be visible to the whole world), settlement finality, and composability. Yuval draws a parallel to the internet—permissionless infrastructure (TCP/IP) doesn't mandate permissionless applications (websites can be private). Digital Asset built Canton to solve capital markets infrastructure at the protocol layer, enabling institutions to build confidential, composable transactions.

Yuval also corrects the record on funding: neither DRW nor Citadel founded Digital Asset. DRW is an investor, but Yuval and his co-founder Eric left DRW to start the company independently, joined by a third co-founder with a cryptography background. This distinction matters because it addresses early confusion about corporate backing.

**The Central Technical Dispute: Is Canton a Blockchain?**

Alex Glukowski launches the core criticism: Canton is not a blockchain in the Bitcoin sense. Blockchains solve double spend without relying on trusted third parties. Alex frames the question: "What is the actual innovation? What's the invention? What's the breakthrough that Canton has built that was not possible 10 years ago?"

Yuval responds that Canton uses a UTXO model (like Bitcoin) with encrypted UTXOs, enabling multi-party validation and decentralized composability that "message-based architecture" cannot achieve. Unlike Previdium (a single RPC source controlled by one entity), Canton allows atomic composition of smart contracts with privacy.

The debate hinges on what "composability" means. Yuval claims privacy-preserving atomic composition is unique to Canton; without a third-party reliance, parties cannot compose transactions. Alex counters that traditional finance (SWIFT) already uses atomic messaging between parties. Yuval argues that SWIFT requires trust in intermediaries; Canton removes that reliance.

**The Double-Spend Problem and Issuer Dependency**

As the debate sharpens, the architecture becomes clear: In Canton's DAML contract model, each UTXO is encrypted so only designated parties see its contents. When a transaction is proposed, it functions like a multi-signature arrangement requiring multiple parties (including the issuer) to approve the state transition. The super validators (Canton's 46-node consensus layer) order and timestamp transactions but do NOT validate the business logic.

This creates a critical vulnerability: **the issuer is the sole party that prevents double spend.** If the issuer is compromised—hacked by a nation-state actor—they can authorize unlimited minting of that asset without detection. Alex cites real-world precedent: Layer Zero's DVN hack where a single 1-of-1 multisig approved invalid transactions; and Parity/PolkaDot, where unauthorized asset inflation propagated through the network.

Yuval's counter-argument: this is not unique to Canton. Any stablecoin issuer (USDC, USDT) on Ethereum or Solana, if compromised, could mint a billion dollars. The issuer is a trusted intermediary in both cases. However, Alex points out the crucial difference: **on public blockchains, the mint would be immediately visible on-chain.** Everyone observing the ledger would see the unauthorized issuance. On Canton, it remains hidden—undetectable without the issuer's voluntary disclosure.

Yuval pushes back: Previdium users depend on an RPC from closed-source software and a ZK proof they didn't participate in creating. A Previdium issuer could upgrade a contract within a block, drain accounts, downgrade the contract, and hide the damage with a proof that EVM processed correctly. On Canton, at least every participant in the contract would know about the change because they validate it themselves. Alex counters that on Ethereum and Previdium, the change is visible to the public; on Canton, it propagates unseen through the system.

**Architecture Comparison: Privacy vs. Auditability**

A key distinction emerges: Canton prioritizes privacy and composability for institutions; Previdium prioritizes auditability and public visibility. Previdium is built on Ethereum as a ZK-rollup, with all state transitions written to mainnet—transparent and immutable. Canton is a separate ledger where encrypted UTXOs mean only parties to a transaction see its details. If an asset issuer is compromised, the compromise spreads through the network undetectably until someone (ideally the issuer or an auditor) notices balance discrepancies.

Yuval frames this as acceptable for institutional use: traditional finance institutions have other monitoring and governance mechanisms (audits, compliance checks, hot/cold wallet limits) that don't exist in open blockchains. But Alex argues that Canton claims to offer blockchain-like properties (decentralization, integrity, composability) while actually offering neither—it's a database with a governance token and messaging layer.

**The Permissionless Debate**

The final major clash focuses on permissionlessness. Canton requires super validators, and becoming one requires applying and receiving super-majority approval from existing super validators. Yuval defines permissionless as: anyone can build apps on the infrastructure, participate by connecting, and apply to become a super validator. He notes that the 46 super validators include small wallet providers, DeFi protocols, and institutions like Broadridge, TradeWeb, SBI, DRW, and Visa—but notably, no traditional banks yet.

Yuval argues his critics are inconsistent: other L1s and L2s have far more centralized sequencers or require tens of millions in staking capital. Solana and Ethereum validators require 32 ETH or more—a tens-of-millions-dollar barrier for average users. Hedera is a closed network of a few validators, yet faces no public outcry. Canton allows anyone to propose becoming a super validator, with governance deciding merit; it's no more permissioned than chains that can fork or change protocol rules.

Alex and Hasib counter that there's a material difference between a minimum-requirement (staking 32 ETH) and **explicit permission from existing validators.** One is an objective threshold anyone can meet; the other is subjective gatekeeping. Hasib reframes: "You come and ask for permission, and then if it's granted, you can participate." That's not permissionless in the crypto meaning of the word—it's permissioned with a voting gate.

Yuval concedes the semantics debate but argues the substance is sound: every blockchain's validators could vote to censor others tomorrow; Ethereum and Solana are only "permissionless" until they aren't. The practical difference between Canton and other chains is one of degree, not kind.

**Attribution and Market Dynamics**

Hasib notes that the controversy is tied to Canton's market success. "You guys are winning, which is why there is this spotlight." Yuval agrees: Digital Asset executed quietly for years with partnerships (Mizuho, Nomura, JPX, Hanwha, Visa, JP Morgan, HSBC), and criticism erupted once adoption became undeniable. He suspects tribalism: competitors building on other chains are hailed as innovators, but those choosing Canton become villains. If the same institutions chose Ethereum L2s for RWA settlement, they'd be called heroes and knights of on-chain capital markets. Yuval attributes much of the noise to market position defense, not technical substance.

---

**Summary**

The episode exposes a fundamental tension in blockchain philosophy: Can permissionless infrastructure serve institutional capital markets? Yuval argues yes—Canton trades public transparency and decentralized consensus for privacy and composability, accepting issuer-level trust assumptions as a tradeoff. Alex and Hasib argue that this is precisely why Canton isn't a blockchain—blockchains solve trust at the infrastructure layer; Canton relocates it to issuers, offering no improvement over traditional databases plus governance tokens.

Both sides agree on facts (how DAML, super validators, and encryption work), but disagree on whether these properties constitute a blockchain or merely masquerade as one. The underlying question is whether the industry's definition of "blockchain" should evolve to include privacy-first institutional platforms, or remain bound to the Bitcoin white paper's goal of removing trusted third parties entirely.
