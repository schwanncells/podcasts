---
podcast: Unchained
date: 2026-03-27
source_transcript: data/podcasts/transcripts/Unchained/2026-03-27_Uneasy_Money_How_the_Resolv_Hack_Shows_an_Audit_Doesn't_Mean_'Secure'.md
---

# Uneasy Money — "How the Resolv Hack Shows an Audit Doesn't Mean 'Secure'"

**Host:** Cain Warwick. **Guests:** Taylor Monaghan (security expert and co-host); Luca (CEO, Pudgy Penguins and Abstract); Omerik Goldberg (CEO, Chaos Labs — risk management firm, Aave's primary risk manager).

## TL;DR

- **$54 million lost in the Resolv hack** — an attacker compromised Resolv's AWS-hosted private key for ~$300K, minted $80 million in unbacked USR stablecoins, dumped them on Curve, and walked away with 24 million in ETH. USR crashed from $1 to roughly $0.025.
- **The root cause was a single AWS key with uncapped mint authority** — gaining access to the AWS account gave the attacker unlimited, unilateral minting power. The key was never exported; the attacker simply commanded it from inside AWS.
- **Protocol paused three hours after the exploit began** — the delay suggests no pager duty or real-time alerting infrastructure was in place, despite Resolv having undergone 14 security audits.
- **Audits don't cover operational security** — the 14 audits were each narrowly scoped to separate components; none examined the AWS key setup. Monaghan calls it "security theater": auditors can only audit what they're engaged to review, and OPSEC is never in scope.
- **Contagion spread through Morpho's public allocator feature** — initial Morpho exposure was ~$5K at hack time; automated liquidity routing to high-interest markets inflated losses to roughly $8–10M. Fluid and Venus each lost over $20M through direct collateral drains.
- **The oracle on USR Morpho markets was hard-coded to $1.00** — because Morpho markets are immutable once deployed, the price stayed at $1 even as USR crashed, allowing the attacker to borrow 100 cents of real assets for every near-worthless USR deposited.
- **Aave V4 advances out of governance deadlock** — the new hub-and-spoke architecture replaces monolithic pools with segregated risk tiers, more granular asset onboarding, and easier off-boarding. Goldberg sees it as the most highly configurable lending experience Ave has built.
- **DeFi systematically misprices risk** — the hosts argue that high yields are the market's signal of real risk, and the industry's habit of treating all risk as equally unknowable enables repeated, preventable losses.

---

**How the Resolv Hack Worked**

At approximately 2:20 UTC on Sunday, an attacker gained access to Resolv's AWS account and used it to command the protocol's hosted private key to mint $80 million in USR stablecoins. Resolv stores its minting key in AWS Secrets Manager — a step up from keeping it in a MetaMask wallet on a laptop, but still a single key with unlimited authority. The attacker did not need to export the key; once inside AWS, they could instruct the key to mint directly. The attacker executed several separate minting transactions rather than one atomic operation, suggesting either limited planning or caution about triggering alerts.

From there the attacker dumped USR on Curve pools against other stablecoins, then converted proceeds to ETH. USR depegged from $1 to around $0.025 — a 266:1 ratio of minted supply to actual backing at the hack's peak. Resolv paused the protocol three hours after the exploit began, a delay Goldberg and Monaghan attribute to inadequate alerting infrastructure. Goldberg notes that basic incident response tools like PagerDuty — standard practice under frameworks like SOC2 — appear to have been absent or unmonitored.

**Why AWS Doesn't Equal Security**

Monaghan and Goldberg emphasize that moving a key from a local machine to AWS changes the attack surface but does not eliminate the underlying risk. An attacker who compromises an AWS account gains the same effective power as one who steals a MetaMask private key — the attack just looks different. Goldberg notes that within AWS, there are additional layers that Resolv did not appear to use: multi-factor authentication on the AWS account itself, biometric access controls, and critically, per-mint velocity limits or multi-party authorization requirements. A minting function capped at 10 million tokens per hour would have made the $80 million mint take at least eight hours — dramatically increasing detection time.

Interestingly, other parts of the Resolv system did require multi-sig and had a more rigorous operational security model. The infinite-mint function being a single-key operation appears to have been an inconsistency within the protocol's own design, not a global posture.

**The Security Audit Problem**

The team addresses the widely circulated figure of 14 audits: Goldberg notes that no component was apparently reviewed more than twice, and each audit covered a separate module of the system. Monaghan argues this represents "security theater." Smart contract auditors review what they are explicitly engaged to examine — smart contract logic, not AWS configurations, key management practices, or operational procedures. Auditors are not in a position to ask whether a team's infinite-mint password is stored in Apple Notes unless that is within scope.

Monaghan's proposed alternative: start with a threat model before engaging any auditor. Identify the worst-case scenarios, prioritize by severity, and then bring in the appropriate specialists to address each risk. Without that foundation, teams end up hiring an available auditor at a desired price point for a brand-name badge to put on a website. The result is comprehensive-sounding audit counts that leave the highest-severity vectors unexamined.

**Contagion: Curve, Fluid, Venus, and Morpho**

Once USR was minted, the attacker moved through several DeFi venues. Curve pools holding USR against other stablecoins were the initial exit point, with the attacker swapping USR for real assets before ultimately converting to ETH. Fluid and Venus, which both listed USR as collateral, each suffered losses exceeding $20 million as the attacker deposited USR and borrowed out legitimate assets at high loan-to-value ratios.

The Morpho situation was more unusual. At the time the hack began, Morpho's USR-collateral vaults had very little liquidity — roughly $5K of exposure. That exposure should have stayed small as liquidity dried up. But Morpho's "public allocator" feature — designed to route capital toward markets experiencing interest rate spikes — interpreted the sudden high borrowing demand in USR markets as a legitimate yield opportunity and automatically funneled fresh capital into those markets. Real stablecoins kept flowing in to meet attacker-driven borrow demand for 90 minutes to two hours in the hardest-hit (Gauntlet-curated) vaults, and up to ten hours across other curators. Total Morpho losses reached roughly $8–10 million.

Compounding the Morpho problem: the USR oracle in those markets was hard-coded to $1.00 at market creation. Because Morpho markets are immutable once deployed, the oracle could not be updated as USR crashed. The attacker was effectively borrowing at full dollar value against collateral worth a fraction of a cent.

**The Timing and Attacker Behavior**

The hosts speculate about the attacker's profile. The multi-step execution — mint, mint again, swap on Curve, then move to lending protocols — suggests partial planning rather than a fully scripted automated attack. Goldberg notes that most sophisticated crypto hacks are "hands-on keyboard" operations where a human adapts in real time, citing the DPRK/Lazarus Group's UX Link infinite-mint incident as an example: the Lazarus operators were dumping minted tokens across front ends, got phished by an Inferno drainer wallet, lost some funds to that, and two minutes later minted another 900 trillion tokens and kept going.

For Resolv, one interpretation is that the attacker expected the team to rotate the key immediately upon compromise detection, so moved quickly despite the 2 p.m. UTC Sunday timing. Another is that the attacker knew from the team's security posture that no real-time alerting existed. Goldberg frames a key takeaway: teams managing money need to operate as if someone is always attempting entry — "you have to expect that hacks happen at 3 a.m. wherever you are."

**Curator Accountability and Risk Pricing**

A broader theme of the episode is the accountability gap in DeFi's curator model. Cain and Monaghan argue that the principal-agent problem for vault curators is misaligned: curators are rewarded for maximizing yield, not for minimizing tail risk, and there is no mechanism to hold them accountable when downstream composability causes losses. Goldberg notes that unlimited credit lines — allowing any amount of any collateral to be deposited without a debt ceiling — are not standard practice even in traditional finance, and that debt ceilings proportional to demand would have contained the Morpho losses.

Monaghan's broader critique is that DeFi "does not know how to reason about risk." The industry treats all risk as effectively unknowable and equivalent, which allows the false inference that 25% APY could be risk-free. The hosts note that high yields are the market's own signal that meaningful risk exists, and that the industry's psychological adaptation to constant danger has led to a "false equivocation" where alien-impact risk and a known single-key mint vulnerability get treated the same way.

**Aave V4: Hub-and-Spoke Architecture**

The second major topic is Aave V4's passage through governance. Goldberg, whose firm Chaos Labs serves as Aave's risk manager, describes V4's core innovation as a hub-and-spoke architecture replacing V3's monolithic pool model. In V3, assets listed in the main pool were extremely difficult to delist — once in, largely permanent. During the post-FTX bear market, Aave held a number of DeFi tokens that had lost 90%+ of their value and created ongoing risk management burdens.

V4 introduces multiple hubs with different risk profiles: a core hub for blue-chip, conservatively underwritten assets, and additional hubs for more experimental lending experiences. Each market within a hub can have its own interest rate model and collateral configuration. This allows Chaos Labs to be more granular about trade-offs — specifying parameters at the asset-pair level rather than making binary listing decisions. Asset teams can still apply for the core hub, but the bar remains high; experimental assets start in isolated configurations before any consideration for elevation.

Goldberg also notes V4 arrives as institutional capital enters DeFi in meaningful volume. Coinbase and Kraken have launched vault products, and enterprise allocators prioritize principal protection over maximum yield — a different incentive structure than retail degens. He argues this should improve overall market quality, because institutions will demand the kind of baseline security posture that protocols like Resolv skipped.

**Forcing Functions and Market Power**

Luca describes a real-world example of Aave's market power acting as a security forcing function: a token project had to upgrade its smart contracts because Aave flagged weak mint functionality as a precondition for listing. Monaghan generalizes the point — Aave is one of the few DeFi protocols with enough market power to enforce baseline security standards, similar to how exchanges require emissions documentation before listing. He argues that if Aave and similar protocols consistently required multi-party minting controls, proof-of-reserve oracles, or velocity limits as prerequisites for integration, the industry would adopt those practices far faster than any regulatory mandate could achieve.

Goldberg notes that exchanges are also waking up to this: a recent Binance incident where Athena's token had low liquidity on a weekend caused the exchange to pay hundreds of millions out of pocket after discovering from first principles why accurate oracle pricing matters.
