---
podcast: Unchained
date: 2026-03-20
source_transcript: data/podcasts/transcripts/Unchained/2026-03-20_Bitcoin_DeFi_Has_Been_Elusive._Can_Mysten_Labs_Bring_$1.4_Trillion_Onchain.md
---

# Unchained — "Bitcoin DeFi Has Been Elusive. Can Mysten Labs Bring $1.4 Trillion Onchain?"

**Host:** Laura Shin. **Guest:** Adani Abiodun (co-founder and chief product officer, Mysten Labs; formerly led Libra/Meta blockchain project; cryptographer).

## TL;DR

- **Hashi: native Bitcoin lending without wrapping** — Mysten Labs announced Hashi, a decentralized protocol for borrowing and lending using Bitcoin directly on the Sui blockchain without creating taxable wrapped-asset events. No wrapping means no tax liability, addressing a major barrier to adoption.
- **24 institutional partners launching immediately** — BitGo, Ledger, Bullish, Wave Digital, Navi, FalconX, and others controlling hundreds of billions in Bitcoin are integrating Hashi on day one, designed for custodians, exchanges, hedge funds, and sovereign wealth funds rather than retail users.
- **Over 125 Sui validators secure Bitcoin via multi-sig** — The protocol uses Sui's validator set as signatories on a Bitcoin network multi-sig wallet, with a Guardian backstop layer for added collusion protection. Majority signature required to move funds; same cryptographic primitives that secure the Sui blockchain now secure Bitcoin collateral.
- **Formal verification + on-chain insurance = institutional-grade security** — All smart contracts undergo formal verification (mathematical proof of correctness), and Soto Insure will offer the first native Bitcoin-denominated insurance, with premiums and claims settled in Bitcoin itself.
- **Wave Digital issuing rated Bitcoin bonds on-chain** — The first professionally rated, Bitcoin-backed bonds will trade live on Sui, enabling institutions to raise capital against Bitcoin collateral with real-time settlement and ratings from major rating agencies.
- **Unlocking $1.4 trillion in Bitcoin yield** — WBTC achieved only 1% penetration due to tax friction; Hashi's trust-minimized design, tax-free structure, and institutional backing aim to move far beyond that ceiling and make Bitcoin the collateral engine for DeFi.

---

**The Problem: Bitcoin Collateral Trapped Outside DeFi**

Nearly 60% of crypto's market cap has remained locked in Bitcoin holdings with no access to yield. Bitcoin ETFs launched in 2024 but could not generate returns—they were held in custodial wallets with no on-chain lending mechanism. Abiodun frames 2026 as the year Bitcoin becomes a true collateral instrument in DeFi rather than just a store of value. The challenge is that existing solutions impose friction: wrapped Bitcoin (WBTC) gained only 1% adoption because the wrapping process itself creates a taxable event, dissuading institutional and individual holders from putting their Bitcoin to work.

**Hashi: A Trust-Minimized Native Approach**

Unlike WBTC and similar wrapped solutions, Hashi keeps Bitcoin on the Bitcoin blockchain itself. Users lock Bitcoin into a multi-signature wallet controlled by Sui validators, then originate loans directly on Sui without ever creating a derivative asset. This structure avoids the tax burden that has kept billions in Bitcoin sidelined.

The protocol allows users to mint stablecoins (USDC, USDT, Sui Dollar) or Bitcoin-denominated bonds directly against Bitcoin collateral. A self-custodial user with a hardware wallet can generate yield; so can an institution like BitGo managing client Bitcoin. The design is intentionally agnostic to custody model, enabling both DeFi-native and traditional finance use cases simultaneously.

**Institutional Demand Drove the Design**

Abiodun reveals that Hashi emerged from direct partner feedback. Large banks, sovereign wealth funds, and nation-states approached Mysten with billions in Bitcoin reserves they wanted to deploy in DeFi, but every existing L2 and wrapped-asset solution failed institutional due diligence. Partners could not articulate or trust the chain of trust assumptions required. They asked for a minimal-trust, single-step solution. Mysten built Hashi specifically to meet those requirements, which explains why the launch includes 24 established institutional partners from day one—this is a purpose-built tool for large Bitcoin holders, not a retail product.

**Security Architecture: Validators, Guardians, and Formal Verification**

Hashi's security rests on three layers. The primary layer uses all 125+ Sui validators as signatories on a Bitcoin multi-sig address; a majority must approve any fund movement. Sui's cryptographic security model—proven at billions of dollars in transaction volume—now directly secures Bitcoin collateral.

The second layer is the Guardian model: a multi-sig between validators themselves that activates only if validators collude, providing a fallback to protect users against loss. This has never been triggered in production but exists as backstop against an unlikely extreme scenario.

The third layer is formal verification. Every smart contract governing the Bitcoin-to-Sui bridge undergoes mathematical proof that it behaves exactly as coded with no side effects. Abiodun notes this is the strongest guarantee in computer science for smart contracts and not all chains can perform it.

**Insurance Backed by Bitcoin**

Soto Insure is providing institutional-grade coverage specifically for Hashi. Critically, premiums and claims are denominated and settled in Bitcoin, not dollars. This on-chain insurance is priced low by demonstrating formal verification, validator security, and the Guardian model all reduce loss probability to acceptable levels. Users can purchase insurance at the point of deposit, with premiums deducted in Bitcoin and coverage automatically applied. This is described as an industry first.

**Stablecoins and Bitcoin-Backed Bonds**

Users can mint multiple stablecoins against Bitcoin collateral. Sui Dollar, Mysten's native stablecoin, is backed one-to-one by US Treasuries and distributes yields from Treasury holdings back to the Sui network. This means a user borrowing against Bitcoin can receive a lower borrowing rate because the stablecoin's Treasury yield reduces the cost.

Wave Digital will issue the first institutionally rated Bitcoin bonds entirely on-chain. These bonds are rated by major rating agencies and can be traded in real-time on Sui's decentralized exchange (Deep Book), AMMs, and perpetual protocols. This enables large Bitcoin holders to raise capital against their reserves without selling, and investors to access Bitcoin-backed fixed-income instruments with professional credit ratings.

**Oracle and Pricing Infrastructure**

CF Benchmarks, a leading cryptocurrency index provider, will supply Bitcoin pricing data alongside other oracle sources. Strong, diverse oracles ensure collateral pricing is accurate for loan calculations and DeFi risk management.

**Differentiation from Competitors**

Abiodun identifies three key differences from other Bitcoin L2 and yield solutions. First, minimal trust assumptions: users trust only the Sui validator set, the Guardian model, and formal verification—a small, explainable set of factors. Competitor solutions require understanding multiple bridged protocols.

Second, no wrapped asset means no tax event. Mysten obtained legal opinions confirming that Hashi does not trigger taxable events in many US jurisdictions and internationally, directly addressing the friction that limited WBTC to 1% penetration.

Third, the team's pedigree. Mysten was founded by former Meta (Libra) blockchain researchers and world-leading cryptographers. The formal verification capability comes from this research background and sets Hashi apart from simpler wrapped-asset models.

**Ambitions**

Abiodun states the goal explicitly: unlock the $1.4 trillion in Bitcoin for DeFi yield generation. If successful, this would far exceed WBTC's 1% penetration by removing tax friction, enabling institutional participation, and providing insurance guarantees that traditional intermediaries cannot match.
