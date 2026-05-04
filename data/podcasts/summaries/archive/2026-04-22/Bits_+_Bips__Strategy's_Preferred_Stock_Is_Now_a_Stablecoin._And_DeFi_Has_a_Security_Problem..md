---
podcast: Bits + Bips
date: 2026-04-22
source_transcript: data/podcasts/transcripts/Bits_+_Bips/2026-04-22_Strategy's_Preferred_Stock_Is_Now_a_Stablecoin._And_DeFi_Has_a_Security_Problem..md
---

# Bits + Bips — "Strategy's Preferred Stock Is Now a Stablecoin. And DeFi Has a Security Problem."

**Host:** Austin Campbell (High Scholar, Zero Knowledge Group). **Guests:** Parker White (founding contributor, Apex), Chris Perkins (CEO, 250 Digital Asset Management; former investor and liquid fund manager), Ram Alawalia (Maester of Wealth, leader, Lumina), Michael Bentley (Lord Protector, Euler).

## TL;DR

- **MicroStrategy's STRC preferred is yielding 11.5-13% on-chain via Apex** — the largest preferred stock ever issued ($8.5B instrument, $100M in tokenized STRC) now pays double-digit yields on Ethereum after Apex launched APXUSD/APYUSD, attracting capital rotation from private credit redemptions.
- **Yield-bearing stables are NOT genius-regulated** — they're unregulated securities wrapped as stablecoins; Apex's product is geo-blocked to non-US persons under Reg S, but secondarily trades on Kraken, creating regulatory ambiguity.
- **Apex's moat is packaging, not pure STRC exposure** — a diversified basket (STRC + SEDA + cash), two-token yield model, and over-collateralization deliver lower volatility (~2.5% vs 5% raw) while capturing leverage through preferential yield distribution; crypto modifications like Pendle yields and tranching create a "DeFi Lego."
- **$290 million KelpDAO hack exposed infrastructure vulnerabilities** — attackers (attributed to North Korea's Lazarus Group) compromised RPC nodes, swapped OPGETH binaries, and DDoS'd clean nodes to force failover to poisoned validators; attack proceeded despite 46-minute response and $100-200M additional losses prevented.
- **Layer 0 single-verifier default was the attack vector** — 40% of protocols use the one-of-one DVN configuration out of the box; the other 60%, including Euler, use multiple independent DVNs and were unaffected. Security experts blame both Kelp's choice and Layer 0's defaults.
- **DeFi TVL collapsed from $99.5B to $86.3B in 48 hours** — market signaling that current security costs (undetected $600M in hacks this month alone) exceed acceptable levels; fundamental shift toward immutability-vs-security trade-offs required.
- **Three paths forward discussed:** (1) add slowness/checkpoints/delays to interdiet attacks; (2) simplify protocols to remove attack surface (Uniswap model); (3) accept targeted centralization (audits, monitoring, pools) while preserving code transparency and immutability.
- **Bitcoin and equities rallying despite Iran geopolitics** — positioning (private credit redemptions, BlackRock hedge exits) and AI momentum (Claude productivity narrative) drive catch-up trades; Iran risk largely priced; markets expect growth, not drawdown.

---

**Apex: On-Chain Yield from MicroStrategy's Preferred Stock**

Parker White explains that Apex creates a stablecoin backed by MicroStrategy's STRC (Strategy preferred equity), the largest and most liquid preferred stock ever issued, which trades on the NASDAQ. STRC itself carries no yield, but MicroStrategy issues it as a capital-raising instrument and uses the proceeds to buy Bitcoin—they've accumulated ~$100M worth through Apex alone, and ~$2.5B company-wide over recent weeks. Because of this structure, STRC trades at a premium reflective of the company's Bitcoin holdings and leverage profile.

Apex tokenizes STRC into APXUSD (non-staked, liquid trading) and APYUSD (staked, yield-bearing). The product is over-collateralized and includes a mix of STRC, SEDA, and some cash. Over 7.5 weeks, Apex hit $180M in supply with the staked version yielding approximately 12%, targeting 13%. The two-token model allows yield to be concentrated: currently 50% of issued assets are staked, meaning the entire collateral base pays yield to half the holders, creating yield leverage. Apex also listed on Kraken this week—unusual for a pre-token-generation event.

White emphasizes that Apex's advantage over a direct STRC holding isn't just accessibility. The product offers diversification (other preferred stocks will join SEDA in the basket), lower volatility through over-collateralization, and DeFi composability. Users can farm yields on Pendle (farming the yield tranche), participate in tranching protocols to split into senior/junior tranches, or use it as a building block. Comparing raw STRC volatility of roughly 5% to Apex's 2.5% shows the smoothing effect of diversification and reserves.

Chris Perkins questions whether calling it a stablecoin makes sense and notes that when a security is wrapped on-chain, securities law arguably still applies. White clarifies that Apex's front end is geo-blocked to non-US persons (Reg S exemption for foreign investors), though the token subsequently trades freely on secondary markets like Kraken—a regulatory gray zone. He also notes Apex already holds STRCX (tokenized STRC via the xDox platform) but chose not to build on that because liquidity is poor and the platform adds no value. Apex's packaging, by contrast, is far more liquid than all tokenized stock platforms combined.

**The Risk Profile and Regulatory Ambiguity**

Perkins and the group discuss the core risk: this is not a stablecoin regulated under USDx, but a basket of securities and yield instruments wrapped on-chain. The name matters for US regulatory clarity. The actual risk is twofold: (1) impairment in STRC if MicroStrategy falters or Bitcoin crashes, and (2) standard DeFi protocol risks. Ram points out the amusing irony that humans love yield and are drawn to leverage without reading the fine print.

Parker acknowledges that DeFi security incidents (particularly recent hacks like KelpDAO) are slowing Apex's roadmap. The team has added multiple safeguards: manual minting/redemption via multi-sig, time locks on all contracts, and daily limits on cross-chain bridging (using Chainlink CCIP) to mitigate bridge exploits. He credits Apex's ex-Kraken team (dating to 2013) for institutional security discipline.

The conversation shifts to regulatory runway. Austin asks whether Apex is effectively betting on US regulatory stasis—i.e., that direct STRC-on-chain trading remains restricted, preserving the value of Apex's wrapper. Parker counters that secondary market availability (Kraken listing) is beyond Apex's control, and that the real moat is packaging and DeFi features, not regulatory arbitrage. Over time, as more companies issue preferred stocks, the diversified basket and crypto composability will become the differentiator, not restriction alone.

**Macro: Market Positioning and Iran Risk**

Ram Alawalia frames the current rally as a positioning story. Private credit has been crushed by redemptions; hedge funds are offside; BlackRock (the world's largest asset manager) went to neutral on equities and is now scrambling to re-enter. Additionally, Claude's recent product launches (multiple per week) shifted narrative from "AI will cause deflationary disruption" to "the world is short compute, semis and industrials must rally." This is a catch-up trade with non-consensus positioning.

On Iran: the geopolitical risk is priced. The US can handle oil at $85–95 (not 120), and there's been no further escalation. US blockade of the Strait of Hormuz, plus increased production and tanker queues at Houston, show containment. Ram references a Wall Street Journal article with behind-the-scenes Trump decision-making, though details aren't fully explored in the episode.

Parker, structurally long Bitcoin personally, notes that Bitcoin decoupled from equities during the Iran crisis—a "real interesting moment." He sees a catch-up trade ahead: Bitcoin is still well off all-time highs relative to equities, and MicroStrategy's aggressive buying (~$2.5B recent) signals accumulation by a large, leveraged entity. The setup from relative value is compelling. The limiting factor is how long MicroStrategy can continue raising capital (via STRC issuance) before hitting balance-sheet constraints. Parker estimates ~$8.5B for the STRC instrument, a "drop in the bucket" compared to global financial products, leaving room for growth.

---

**The KelpDAO Hack: Technical Details and Attribution**

Michael Bentley summarizes the attack. On April 20, attackers (attributed to North Korea's Lazarus Group) drained 116,500 rsETH (~$290M) from KelpDAO via its Layer 0 bridge. The mechanics: compromise two RPC nodes feeding Layer 0's single DVN (Decentralized Verifier Network), swap the OPGETH binary for a malicious one, DDoS the clean nodes to force failover to the poisoned ones, then selectively lie to approve a fraudulent cross-chain mint. The monitoring queue failed because the nodes were compromised. Blockade's analysis suggests sophistication comparable to nation-state operations.

Bentley confirms this is a sophisticated attack—binary swaps, DDoS timing, RPC node compromise—all hallmarks of high-level threat actors. He notes that "last rest attribution" to Lazarus Group is likely correct.

Austin points out a blame debate: Layer 0 claims KelpDAO chose a one-of-one DVN setup (default out-of-the-box), and 40% of protocols follow that pattern. Kelp countered that Layer 0's own GitHub defaults and recommendations point to this setup. Third-party analysts (Zach Rind from Chainlink, OX NGMI, the Defiant, Dune analysis, Euler) largely blame Layer 0 for the dangerous default. Meanwhile, 60% of protocols (including Euler, Oiler) use multiple independent DVNs and were unaffected.

Chris Perkins reframes the conversation: instead of blaming Layer 0 or Kelp, the real culprits are the attackers. He emphasizes that we lack an adequate government response to Lazarus Group operations. ("When I'm walking down the street with my wallet and someone steals it, those are the persons that need to be held accountable.") He calls for whole-government accountability and clarity on crypto policy to enable innovation and defense.

Bentley adds that in earlier DeFi (2020–2023), exploits were primarily smart-contract code flaws, which are public and auditable. Now attacks are infrastructure-level: key leaks, RPC node compromises, binary swaps. These are materially different threat vectors.

---

**DeFi Security: Systemic Fragility and Proposed Solutions**

Austin raises the central tension: KelpDAO responded in 46 minutes—preventing an additional $100–200M in losses—but this reveals that latency is everything. Current DeFi models assume transactions are legitimate. After a string of $600M in hacks this month alone (plus earlier incidents like Cetus and Bybit), is this assumption tenable?

Chris Perkins emphasizes that investor confidence depends on operational and cyber risk, not just market risk. He advocates for "agentic" AI-based defense and recommends looking to Claude (Anthropic's model) for vulnerability discovery—Claude recently identified bugs in 26-year-old BSD Linux that has been "battle-tested for decades." If a model can find flaws in legacy code at that scale, the tools are available. The issue is that DeFi must harden *at scale and with urgency*.

Michael Bentley proposes insurance and reinsurance as market mechanisms. If protocols price insurance (30% per annum premiums are feasible, though punitive), that's a transparent, market-driven risk signal. Alternatively, guarantee funds (socialized losses in tail-risk scenarios, as exist in derivatives markets) could provide a backstop without imposing centralized control.

Austin suggests two complementary paths: (1) introduce slowness—delays, checkpoints, multi-signature confirmations—that give time to interdict attacks, and (2) simplify—isolate pools so failures don't cascade. Chris pushes back: if you delay or introduce friction, you're moving toward centralization. Immutability doesn't require instant finality; a transparent, delayed finality (checking transactions during a hold period before committing) preserves the immutable history while reducing attack surface.

Michael observes that credit markets (lending protocols) are harder to secure than AMMs (like Uniswap) because they depend on external oracles, volatility data, and liquidity conditions. Uniswap is self-contained; Compound and Aave depend on the outside world. He's "resigned to the fact" that truly immutable, fully decentralized credit protocols may be impossible. The trade-off: either (a) accept some centralized oversight (Tether and Drift partnership), (b) sacrifice efficiency for security (peer-to-peer isolated lending, like early SushiSwap), or (c) accept contagion risk as the price of liquidity.

Austin floats a corporate model: rate-limiting on deposits (new capital added at 10% per day max) would prevent flash-loan abuse and give time for monitoring. Chris extends this: bilateral lending offers (like an AMM for borrowing/lending pairs) would eliminate contagion but sacrifice the liquidity that users demand. Michael agrees that the peer-to-peer model is "so clunky" that it never scales compared to pooled liquidity—users want to deposit, borrow huge sums, and withdraw whenever they like. That's the killer feature of Compound and Aave.

The consensus: DeFi cannot have it all. **Trade-offs are mandatory.** Michael's view: accept "the minimum amount of centralizing force" required to prevent spectacular collapses while maintaining composability, code transparency, and disintermediation. Chris's closing: the current paradigm is not sustainable. $86.3B TVL (down from $99.5B in 48 hours) reflects market rejection of the risk/yield equation.

---

**Bitcoin Narrative and Quantum Money**

Parker reiterates his structural Bitcoin bullish case: the setup is compelling on relative value (Bitcoin still well off highs) and accumulation (MicroStrategy buying billions weekly). The constraint is not Bitcoin or STRC demand but MicroStrategy's balance sheet and leverage ratios.

Austin closes with an existential joke: when humanity encounters non-human intelligence (UAPs), the first three questions are "Who is your leader?", "What are your intentions?", and crucially, "How do you manage money?" The fourth will be "Is there quantum money?" (A tongue-in-cheek reminder that money and trust mechanisms matter even in sci-fi scenarios.)

The episode ends with a teaser: Laura will moderate a debate/allegedly heated fistfight between Yuval Hasib (Dragonfly) and Alex Krofsky (Matter Labs) on Canto, pre-recorded and promised to be intense.
