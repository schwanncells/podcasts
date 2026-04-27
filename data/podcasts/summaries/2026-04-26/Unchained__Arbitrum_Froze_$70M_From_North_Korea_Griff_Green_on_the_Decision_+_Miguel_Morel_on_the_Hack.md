---
podcast: Unchained
date: 2026-04-26
source_transcript: data/podcasts/transcripts/Unchained/2026-04-26_Arbitrum_Froze_$70M_From_North_Korea_Griff_Green_on_the_Decision_+_Miguel_Morel_on_the_Hack.md
---

# Unchained — "Arbitrum Froze $70M From North Korea? Griff Green on the Decision + Miguel Morel on the Hack"

**Host:** Laura Shin. **Guests:** Griff Green (Arbitrum security council member, leader of the DAO Security Fund, co-founder of GiveItBack, white hat incident response veteran since the 2016 DAO hack).

## TL;DR

- **North Korean hackers stole ~$70M in rsETH tokens via LayerZero exploit** — Kelp DAO's bridge had vulnerability; attackers moved stolen tokens across chains, borrowed additional ETH on Aave and Arbitrum, then left funds in a single address for ~48 hours, creating the recovery window.
- **Arbitrum Security Council froze the funds using a Layer 1 transaction** — Using forced inclusion mechanics (a Stage 1 rollup feature), the council executed a transaction on Ethereum that sent the stolen funds to address 0x0 DAO, where no one controls them, without requiring a node upgrade that would have caused network disruption.
- **Seal 911 coordinated the response and blocked exits** — The security organization coordinated with law enforcement, exchanges, and bridges to freeze UI access and prevent laundering; all bridges except the 7-day-delay native bridge were blocked, creating the conditions for recovery.
- **The decision was controversial internally, narrowly technical, and philosophically weighted** — Green initially rejected the plan because early solutions required node upgrades that risked network disruption; he approved only when the technical team found an "ingenious" Layer 1 solution; security council deliberations are confidential, but his view: "If you can stop North Korea, you do it."
- **This is only the third major fund recovery Green has orchestrated** — After the 2016 DAO hack and the Parity multisig recovery (~$200M), this represents a rare precedent-setting action; Green argues social consensus, not immutability, is blockchain's true property.
- **Arbitrum DAO governance will decide the final use of the frozen funds** — The 12-member security council (elected by ARB token holders, six new per year) is now tasked with emergency response only; the $70M in the dead address requires vote from all ARB holders; three entities must coordinate: Kelp DAO, Lido, and Layer Zero.
- **Risk is narrative, not legal; precedent is set at the token-holder level** — Green sees minimal legal risk ("no one's ever sued me") and argues the accountability layer is market dynamics—if ARB holders disapprove, the token price reflects it; precedent applies only to L2s with similar security council structures, not Bitcoin or Ethereum mainnet (though he notes it's technically possible there too).
- **The DAO Security Fund launches a $1M quadratic funding round with ~100 vetted security projects** — The round aims to coordinate Ethereum security as a public good, shifting from individual project defense to ecosystem-wide tooling; projects were strictly vetted for prior public benefit and actual security focus, not general crypto.

---

**The LayerZero Exploit and the Stolen Funds**

The hack began with a vulnerability in Kelp DAO's bridge on LayerZero. North Korean hackers exploited the system to withdraw approximately $70 million in rsETH tokens—a staked ether token collateralized by ETH on mainnet. The attackers moved the stolen tokens across multiple Layer 2 networks, using them as collateral to borrow additional ETH on Aave (on mainnet) and on Arbitrum. After executing these exploitative transactions, the hackers unexpectedly left their stolen funds in a single address and did not move them for roughly 48 hours. This pause, as Green and Shin both emphasize, was critical: "North Korea never sits and lets that money just sit for two days." It was "lightning striking," an unusual mistake that created the recovery window.

**Seal 911's Coordination Effort**

Behind the scenes, Seal 911—a white-hat security organization—played the decisive role in making recovery possible. The organization immediately coordinated with law enforcement, exchanges, and bridge operators to block the stolen funds' exit routes. Seal 911 blocked UI access for the attacker's address across multiple platforms and froze access to all bridges except Arbitrum's native bridge, which has a 7-day settlement delay and cannot be censored by the security council in normal operation. Green credits Seal 911 as "the hero here," describing years of infrastructure work that made coordinated response possible: "This infrastructure of Seal 911 is really the hero here. The security council is getting a lot of credit for executing, but the real execution happened at layer zero."

**The Technical Solution: Forced Inclusion and Layer 1 Transactions**

When the Arbitrum Security Council considered freezing the funds, it faced a technical problem. The obvious solution—upgrading Arbitrum node software to rewrite the blockchain state—would have caused network-wide disruption: oracles could fail, liquidations could cascade, and other platforms could suffer collateral damage. Green initially opposed this approach: "If we end up stopping North Korea but then we have a lot of other people lose money because of liquidations or something," the benefit would not justify the harm.

The breakthrough came from Arbitrum's Stage 1 rollup design: forced inclusion. Because Layer 2 rollups rely on a centralized sequencer (a single ordering authority), they need a mechanism to prevent censorship. Arbitrum's answer is forced inclusion—the ability to submit a transaction on Layer 1 Ethereum that the sequencer must eventually include on Arbitrum. After a 15-minute delay, the transaction becomes final. The security council leveraged this to craft an elegant solution: instead of upgrading the network, they submitted a transaction on Ethereum that, 15 minutes later, automatically moved the attacker's funds from an address they controlled to address 0x0 DAO, an address no one controls. The funds remained frozen without any node software change.

**The Security Council's Decision-Making Process**

The Arbitrum Security Council comprises 12 independent members, six elected annually by ARB token holders, with terms moving from six-month to two-year cycles. Green is one such member, elected both for his white-hat incident-response experience (including leading fund recovery during the 2016 DAO hack and the Parity multisig recovery of ~$200M) and his active participation in ARB governance as a high-ranking delegate.

Green cannot disclose the council's deliberations, which are confidential. However, he describes his own process: initial skepticism based on network risk, consultation with multiple stakeholders (particularly Taylor Monahan at Seal 911, who proposed the idea), and eventual approval once the Layer 1 solution eliminated network disruption concerns. His position on precedent and accountability is direct: "If you can recover users' funds, you do it. If it's in your power, you take the power to do what's right."

When asked about objections, Green declined to name them but emphasized that legitimate philosophical concerns exist. The fear is that if arbitum can freeze north Korean funds, it can freeze anyone's funds. Green counters that this reveals a fundamental truth about blockchains: they are open-source code run on servers and social consensus. Immutability is not a property of the code; social consensus is. He notes that the same capability exists in Bitcoin and Ethereum. If Bitcoin's largest mining pools—which control >51% of the network—had pressure applied, they could theoretically freeze Satoshi Nakamoto's coins. The accountability for such actions lies not in the multisig or the security council, but in market dynamics: "All the people who are holding or might want to hold Bitcoin—those reasons, those market dynamics, provide the accountability for these systems." ARB holders can sell or hold based on whether they approve of the council's actions.

**Precedent and Philosophical Implications**

Green emphasizes that this action sets precedent only for Layer 2s with similar security council structures. For Bitcoin and Ethereum mainnet, the action would be far more difficult, though he maintains it remains technically possible. The real lesson for North Korea, and other attackers, is behavioral: they will likely move funds as quickly as possible in future attacks rather than pausing to exploit additional chains. Green predicts that the only reason Arbitrum succeeded is the specific window of inaction. "This basically is like a replay of the DAO, because the only reason it worked was because there was this moment where they weren't moving the funds."

The criticism Green sees on social media is more often "disappointment in the narrative of blockchain tech" than objection to the action itself. Most people who are "real" and not "crazy monkeys" (his phrase for anonymous online commenters) support the move. The most substantive critique comes from Gabe Shapiro, who agrees the action was justified but argues that security councils should have clearer legal underpinning and stated rules for when they will and will not act. Green partially agrees: he does not support additional legal frameworks but sees merit in future elections requiring council candidates to state their principles in advance. However, he also values the difficulty of reaching consensus among independent entities, viewing the council as a "rarely used Supreme Court" that should remain deliberately constrained.

**Redistribution and Governance**

The $70 million in the 0x0 DAO address now awaits a vote by arbitrum DAO token holders. This situation mirrors the resolution of the original DAO hack in 2016, when the white-hat group (led by Green) recovered two-thirds of the stolen funds. The DAO governance then decided to redistribute those funds to token holders via a contract mechanism. In the current Arbitrum case, multiple parties must coordinate: Kelp DAO, Lido (which likely holds collateral in the attack), and Layer Zero. Green expects all three to propose distribution mechanisms that will be voted on by ARB holders. "Rescuing funds is way easier than redistributing them," he notes. "That's always the hardest part." The public discourse and multi-party coordination should lead to a better outcome than any single entity deciding unilaterally.

**The DAO Security Fund and Ecosystem-Wide Approach**

Beyond the immediate recovery, Green announced the launch of the DAO Security Fund, a coordinated effort to address what he sees as a chronic problem: Ethereum is extremely secure (highly decentralized with well-distributed staking, far more so than Bitcoin or other blockchains), but it is not safe to use. "We have the technology to be better than PayPal, better than banks, and yet I don't know anyone who has their bank account fished or accidentally sends money to the wrong person on the wrong chain." The fund aims to shift security from individual project defense to ecosystem-wide public goods.

The first major initiative is a $1 million quadratic funding round launching the day of the episode. Approximately 100 security projects have been vetted and included—far fewer than typical rounds because Green and the curators applied strict criteria: projects must have demonstrated public benefit in the past and must actively advance security, not just peripheral security-related work like privacy tools or newsletters. Through quadratic funding, which uses a square root formula to favor projects with more unique donors, "the more people you get to donate to, the more of the matching pool you get." The round lasts three weeks, and additional rounds are planned quarterly (depending on ETH price, since the fund is financed through staking yield).

Green articulates the philosophy underlying the fund: security is a public good and benefits from economies of scale. Currently, "everybody is securing their own house, but they're in a war zone." UniSwap and other major protocols spend heavily on security for themselves. If ecosystem-wide tools and coordination could secure all platforms collectively, every project would spend less while achieving better results. The fund's real strategy is coordination—using the money to "bring everybody together" so that the Ethereum ecosystem defends as one rather than as isolated fortresses.

