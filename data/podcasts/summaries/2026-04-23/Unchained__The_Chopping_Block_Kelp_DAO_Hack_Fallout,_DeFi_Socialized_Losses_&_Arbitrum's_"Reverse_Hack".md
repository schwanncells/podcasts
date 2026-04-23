---
podcast: Unchained
date: 2026-04-23
source_transcript: data/podcasts/transcripts/Unchained/2026-04-23_The_Chopping_Block_Kelp_DAO_Hack_Fallout,_DeFi_Socialized_Losses_&_Arbitrum's_"Reverse_Hack".md
---

# Unchained — "The Chopping Block: Kelp DAO Hack Fallout, DeFi Socialized Losses & Arbitrum's 'Reverse Hack'"

**Host:** Hasib (head of business development, Dragonfly; early-stage crypto investor). **Guests:** Tom (DeFi maven and operator, Chopping Block); Tarun (risk researcher, Gauntlet); Monet Supply (governance specialist, Spark Protocol, formerly MakerDAO; led risk consulting for 5 years).

## TL;DR

- **$200+ million stolen via forged bridge message** — North Korea exploited KelpDAO's Unichain bridge (secured by a single validator) to mint unbacked liquid restaking tokens, post them as collateral on Aave and Compound, and borrow $200M+ in ETH.
- **Three parties blame each other in a "Spider-Man meme"** — KelpDAO chose a one-of-one validator setup; Layer Zero (which ran that validator) calls it non-standard but collected payment; Aave/Compound set risk parameters that allowed 300M borrow cap on a pegged derivative without sufficient guardrails.
- **Lending protocols are fractured into L1/L2 with unclear loss allocation** — Aave depositors on L2s took larger losses than mainnet; the protocol is locked (100% utilization) until someone injects capital or decides if losses are socialized per-chain or pan-protocol.
- **Arbitrum's security council executed a "reverse hack" via 9-of-12 multi-signature** — they modified state to confiscate ~$70M of stolen funds from North Korea and moved it to a burn address for governance to decide its use; North Korea immediately laundered the remaining funds post-seizure.
- **Arbitrum's action received broader public support than expected** — compared to past precedents like dYdX's SWE hack recovery (sentiment 2:1 against), the sentiment here was more positive; people view it as governance exercising legitimate emergency powers with high security threshold.
- **DeFi needs rate limits, collateral consolidation, and realistic peg risk modeling** — low-hanging fruit includes per-asset borrow/deposit caps (Spark and Fluid already deploy these); longer-term fixes involve acknowledging that pegged assets can break and building isolation.

---

**The KelpDAO Hack: Mechanics and the Bridge Failure**

KelpDAO is a liquid restaking protocol that had just over $1 billion in TVL, mostly deployed in looping trades on Aave, Compound, and MorphoBlue—borrowing ETH at 2% to amplify returns on collateral earning 3%. The vulnerability originated in KelpDAO's use of Layer Zero's OFT (Omnichain Fungible Token) framework to issue their token across multiple chains and L2s.

The hack worked through Unichain, an L2 where KelpDAO had almost no liquidity. A forged message purported to show 100,000 KelpDAO tokens burned on Unichain. The bridge validator—run by Layer Zero, the same company that built the bridge infrastructure—signed this false state update. Without actually holding any tokens on Unichain, North Korea effectively unlocked $200+ million in valid KelpDAO tokens on Ethereum mainnet. The attacker then posted these fake tokens as collateral across lending protocols and borrowed hundreds of millions of dollars in ETH. When the fraud became public, no lender would buy the stolen tokens on open markets (any sale would crater the price), so the attacker simply defaulted on all loans.

Layer Zero's postmortem blamed KelpDAO for choosing a one-of-one validator setup, claiming their documentation advises against this. KelpDAO shot back: Layer Zero collected payment to run the validator and got hacked, making Layer Zero responsible. The attack surface remains murky—Tarun flagged that the compromise method (an RPC injection rather than a direct validator compromise) has not been fully disclosed, making it unclear whether simply switching to a two-of-two or multi-sig setup would have prevented it.

**Blame, Liability, and the Precedent Question**

The debate hinges on duty of care and who bears the cost when a multi-party system fails. Tom argues Layer Zero looks worst because it collected payment to run the service; accepting that payment implies a standard of care, much like hiring a mechanic. Monet takes a legal view: Layer Zero likely disclaimed liability in their terms, making KelpDAO the most culpable party in writing—yet KelpDAO is worth only ~$100 million in equity value, nowhere near enough to compensate victims.

Hasib emphasizes that this is the first major hack where responsibility is genuinely unclear, breaking crypto's unwritten norm that losses are always made whole. The industry is watching to see if this creates a precedent: Do parties accept liability and pay, or do they lawyer up and refuse? Monet notes that whoever sets the precedent will shape future behavior for decades, as DeFi is now deeply interconnected and future cascading failures are nearly inevitable.

Aave, the largest impacted protocol, faces additional complexity: mainnet depositors took smaller losses than L2 depositors because different collateral chains had different exposures. The question of whether losses are socialized across the entire protocol or segregated by chain (L1 versus L2s) has no precedent.

**Arbitrum's "Reverse Hack" and the Governance Question**

Arbitrum's security council—a 9-of-12 multi-signature of independent validators—took extraordinary action. They deployed a special transaction to upgrade the L1 bridge contract, allowing them to modify L2 state and move $70 million of stolen funds to a burn address for later governance decision-making. This confiscation was neither a rollback nor a traditional hack—it used the documented governance mechanism, just in an emergency fashion.

Hasib notes that public sentiment was surprisingly positive compared to past recoveries. Tom attributes this to the high threshold (9 of 12) and the moral clarity: North Korea bad, recovery good. Hasib embraced this as an example of how L2s can compete on governance values—some L2s may offer rapid response to state-level emergencies, others may prioritize censorship resistance. Monet played devil's advocate, arguing that setting precedent for emergency seizure opens the door to more questionable requests in the future (government orders, regulator demands). He also noted that Hyperliquid, another project using Arbitrum, might view this action as a competitive advantage (the chain will defend them if hacked), which could increase Arbitrum's market share.

**What Went Wrong: The Peg Assumption**

Tarun highlighted the deepest vulnerability: the entire DeFi ecosystem treats pegged or pseudo-pegged assets (liquid staking tokens, L2 derivatives, stable coins) as equivalent to their underlying, despite tail risk that breaks the peg. Lending protocols set high LTVs on KelpDAO because it was "backed by ETH somewhere." The assumption failed. He noted that nearly every major hack since 2019 traces back to an implicit peg breaking: bridge assets treated as one-to-one with their underlying, synthetic assets treated as equivalent to spot, staking derivatives treated as safely replicating the base asset.

Tom noted that competitive pressure drives these high LTVs—protocols that offer more generous borrowing capacity on pseudo-pegged assets attract yield-seeking traders, and protocols that tighten parameters lose market share. Monet countered that rate limits and collateral concentration can break this dynamic.

**Remediation: Rate Limits, Collateral Focusing, and Peg Honesty**

Monet outlined low-hanging fruit: per-asset deposit and borrow rate limits (how much of a new asset can enter the system per block/day), already deployed by Spark and Fluid. This would have capped the damage—there is no legitimate reason for a user to post $300 million of collateral in a single transaction.

Monet also advocates for collateral consolidation: rather than listing 4-5 similar liquid restaking tokens, focus on one or two with bulletproof bridges and strong operations. Market forces may naturally drive this consolidation as confidence in smaller LRTs evaporates.

Tarun emphasized the deeper issue: stop implicitly pegging things. Audit and document which assets are treated as one-to-one with their underlying, which can de-peg, and what happens when they do. Build isolation accordingly. The diamond has many facets—oracle pegs, bridge pegs, L1/L2 pegs, loop-dependency pegs—and most hacks exploit a facet that went unacknowledged. This problem is inherent to permissionless systems where anyone can fork a successful pegged asset design into ten new variants, but it is manageable through honest accounting and risk discipline.
