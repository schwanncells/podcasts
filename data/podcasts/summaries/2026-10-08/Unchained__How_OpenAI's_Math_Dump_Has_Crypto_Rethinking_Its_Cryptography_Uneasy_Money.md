---
podcast: Unchained
date: 2026-10-08
source_transcript: data/podcasts/transcripts/Unchained/2026-10-08_How_OpenAI's_Math_Dump_Has_Crypto_Rethinking_Its_Cryptography_Uneasy_Money.md
---

# Unchained — "How OpenAI's Math Dump Has Crypto Rethinking Its Cryptography: Uneasy Money"

**Host:** Kane Wark. **Guests:** Taylor Monahan (security expert; formerly MetaMask); Austin Griffith (builder enablement, DEF); Ben DiFrancesco (founder and CEO, Scopelift; builder of Umbra and Cactus; formerly Tally DAO).

## TL;DR

- **OpenAI released 722 math papers, some formalized in Lean, raising fears of faster elliptic curve brute-forcing** — Ethereum researcher Justin Drake tweeted "don't panic" while suggesting holders with 50+ BTC migrate funds to wallets protected by alternative hash functions.
- **ECC isn't solved, but the window for action may be measured in months** — Ben DiFrancesco argued worst-case scenarios still require massive compute and long timescales; Austin Griffith noted Chinese models are "not far behind" if OpenAI's frontier model unlocked this capability.
- **MetaMask/Consensys Staking rotated validator keys after just 0.36 ETH was redirected from fee-recipient addresses** — Taylor Monahan explained withdrawal keys stay with users; the rotation was proactive containment before any real funds were at risk.
- **NEAR's $4M hacker returned all funds at 0% bounty** — the attacker sent dust to the Lazarus/Ronin address (same misdirection as the Euler hacker), was identified publicly by Aurora's Alex, and returned everything.
- **Zach XBT spent $350K of his own money to map a DPRK money laundering network** — he befriended operative "Jimmy Green," uncovering a Chinese laundering operation that moved over $1 billion post-Bybit; the launderers invoke DeFi ideology as cover.
- **Gnosis/Safe investors petitioned a Swiss foundation court over foundation governance** — Safe TVL fell from $66B to $30B; Ben DiFrancesco argued DAO dysfunction largely stemmed from regulatory fears that prevented governance tokens from returning any value to holders.
- **Blast and Abstract L2s shut down; "never build a wallet" emerged as the episode's lesson** — Abstract's wallet integration was cited as its fatal flaw in a market with 180+ L2s.

---

**OpenAI's Math Dump and the Cryptography Scare**

Kane Wark opened from Singapore reacting to Ethereum researcher Justin Drake's "don't panic" tweet, which warned that OpenAI's release of 722 formalized math papers — some in the Lean proof assistant — may contain findings enabling faster brute-forcing of elliptic curve private keys. Drake's specific concern: wallets holding more than 50 BTC are early targets, since the original Bitcoin block reward created many wallets at exactly that threshold. His advice was to migrate such holdings behind wallets using a different hash function.

The hosts framed the moment as unprecedented. Austin Griffith drew a direct comparison to early COVID — "terminally online" people are first to notice the beginning of an exponential process that the mainstream hasn't registered. He was careful not to frame AI progress as inherently catastrophic, but stressed that bad human intuition about exponential curves creates a widening gap between crypto-native observers and everyone else. The specific trigger: reports that OpenAI used a single model in a single session to work through the Erdős problem, spending a reported $10 million in compute.

Ben DiFrancesco added important nuance. Even in the worst case, breaking ECC would not mean private keys are instantly derivable. It would still require massive compute over significant time, and compute is expensive. He also noted the broader stakes: HTTPS and the global banking system run on the same cryptographic primitives, meaning the first real-world exploitation would look like nation-state espionage, not Bitcoin theft. Weth's $5.5 billion concentrated in a single smart contract address was flagged as a particularly alarming example. Kane's practical takeaway from Drake's tweet: don't panic and hastily rotate cold wallets — doing so is far more likely to cause a self-inflicted loss than any GPU farm attack in the near term.

**MetaMask Staking Validator Key Rotation**

Taylor Monahan explained the architecture of Consensys Staking's non-custodial validator product: users retain their withdrawal keys (the keys that actually move funds), while validator keys — which perform attestation work — live on servers. A third element, the fee-recipient address (determining where MEV fees and block rewards go), is a server-side configuration rather than a signed transaction. In the incident, 0.36 ETH was redirected from specified fee addresses to new addresses. Monahan characterized the immediate proactive key rotation as a sign of strong security hygiene: an unusual config change triggered an alarm, and the team rotated everything before any meaningful funds were at risk. Kane admitted he isn't entirely sure where all his own validator keys are.

**NEAR Protocol Hack: Full Return at 0% Bounty**

In the week since the show last covered the NEAR hack, the attacker returned all $4 million of stolen funds. Monahan explained the pattern: the attacker sent dust to the Lazarus Group's Ronin bridge address — the same misdirection tactic used by the Euler hacker — hoping investigators would attribute the theft to North Korea. Aurora's Alex identified the attacker publicly on Twitter with direct, unambiguous language: they'd been identified. The attacker returned everything immediately. The hosts were emphatic that no bounty should be paid: the industry's practice of offering 10-20% returns to hackers who return funds creates perverse incentives, and the only appropriate response is zero-percent and maximum accountability.

**Zach XBT's Undercover DPRK Laundering Investigation**

Taylor Monahan walked through Zach XBT's multi-year investigation that culminated in a detailed public thread. Starting from a pattern Monahan had long flagged — loud, outraged users appearing in DeFi discords to complain about frozen transactions are nearly always money launderers — Zach went deeper after the Bybit hack. He befriended an operative Monahan identified as "Jimmy Green," a Chinese money launderer working on behalf of DPRK, and spent $350K of his own money building a comprehensive map of the laundering operation. The network moved over $1 billion in roughly four to five months post-Bybit.

The investigation revealed a key intelligence gap: the launderers are fully conscious of their role, completely shameless, and fluent in crypto ideology — invoking decentralization principles to pressure DeFi frontends into processing their transactions. Monahan had spent years trying to convince centralized exchanges (many Chinese-operated) that accounts with strong Chinese-language indicators were nevertheless laundering for DPRK, which the exchanges found counterintuitive. Zach's public thread created accountability pressure that quiet sharing with law enforcement had not. Kane discussed the burnout dynamic Zach had experienced — years of people approaching him only when they needed something — and observed this investigation felt like Zach operating from genuine purpose again.

**Safe/Gnosis Foundation Dispute and DAO Governance**

Kane outlined the situation: a group of investors filed a petition with a Swiss foundation authority (not a formal lawsuit) arguing the Gnosis foundation is not fulfilling its obligations. Safe TVL dropped from $66 billion to $30 billion — likely at least partly a reflection of asset price movements. Investors including Mike Dudas called for replacing "lazy unaccountable foundation boards."

Ben DiFrancesco offered a structural defense. Swiss foundations, like most crypto foundations, are intentionally designed to owe no duties to token holders — a deliberate legal structure to avoid securities law exposure. He argued a large share of DAO dysfunction over the past decade was a direct consequence of regulatory fear: teams couldn't implement fee switches, buybacks, or dividends without risking SEC action, so governance tokens were structured to avoid any appearance of economic returns. Now that the regulatory environment is shifting, protocols will be held to a higher standard — Ben pointed to Uniswap's programmatic fee distribution as the emerging benchmark, and argued that the speculative premium on governance tokens is gone, so token economic security must be real.

On Safe's monetization challenges, Kane acknowledged the bind: charging fees would likely trigger a fork, and a forked Safe would inevitably lose people's money. Enterprise security tiers were tried and largely rejected by crypto teams unwilling to pay for security available for free. Ben's broader conclusion was that governance isn't supposed to eliminate contention — it's supposed to resolve it. The original belief that DAOs would transcend human nature was the mistake; the experiments themselves were worth running.

**L2 Shutdowns and the Wallet Curse**

Blast and Abstract both shut down during the week. Kane read the shutdowns as a bullish capitulation signal — end-of-cycle cleanup before the next move. He also acknowledged some personal responsibility for the L2 proliferation, noting he'd tried to meme one or two L2s into existence and instead got 180 of them. Abstract was credited with genuinely interesting account-abstraction UX work, but its wallet integration was identified as the fatal flaw. The episode closed on "never build a wallet" as explicit life advice: wallets combine the highest user expectations, the most hostile fee sensitivity, and the greatest security liability of any product in crypto.
