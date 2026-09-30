---
podcast: Unchained
date: 2026-09-30
source_transcript: data/podcasts/transcripts/Unchained/2026-09-30_How_Bitget_Is_Chasing_$388_Million_in_Stolen_Funds_After_a_Zero-Day_Hack.md
---

# Unchained — "How Bitget Is Chasing $388 Million in Stolen Funds After a Zero-Day Hack"

**Host:** Laura Shin. **Guests:** Gracie Chen (CEO, Bitget).

## TL;DR

- **A zero-day vulnerability in a third-party, non-crypto-specific security tool gave attackers backend access to Bitget's wallet servers** — letting them inject fraudulent withdrawal commands entirely outside normal user-facing risk controls, then delete all traces to obstruct forensic analysis.
- **Two waves on September 24: $361 million stolen between 6:58–9:23 PM UTC in 17 large transfers, then a deliberate second exposure of $30 million** — Bitget opened hot wallets to rescue larger balances still inside, knowingly accepting the second-round loss.
- **Only $632,000 of $388 million has been frozen** — Tether, Circle, and Near Intend are the only organizations to have helped; Chen cited the Bybit precedent of just 3.5% frozen after one year and said she doesn't have much hope for significantly better recovery.
- **ThorChain publicly refused to block hacker-associated addresses**; Near Intend froze ~$500,000 and published the position that "permissionless doesn't mean neutral" — the clearest divergence of DeFi philosophy to emerge from the incident.
- **Bitget's $464 million user protection fund covered the full $388 million stolen with no user losses** — the fund has since grown to $556 million and the company plans to replenish it to above $300 million using company capital within one week.
- **Zach XBT initially declined to investigate**, citing Bitget's lack of support for his work; days later he published on-chain findings identifying five aliases used by Chinese intermediaries laundering DPRK funds from the hack — his prior public accusations against Bitget's leadership about pump-and-dump activity were unresolved in the interview.
- **Social engineering attempts against Chen began the day after the hack** — a team of impostors posing as a well-known investment firm approached her with multiple named "team members" taking distinct roles, exploiting the post-incident window of rapid outreach.
- **Withdrawal reopening was smoother than expected**: one hour after Ethereum withdrawals resumed, Bitget recorded a net ETH inflow of 9,674 ETH in versus approximately 9,023 ETH out.

---

**The Attack: Zero-Day Exploit and Two Waves**

The hack began on September 24 with two test transactions at 6:31 PM UTC — 0.48 ETH from an ETH hot wallet and 93 TRX from a Tron hot wallet — both calculated to fall below Bitget's risk control thresholds. At 6:58 PM, attackers initiated 17 large transfers across Ethereum, XRP, Arbitrum, Avalanche, Optimism, BSC, Base, Zcash, and Tron, stealing approximately $361 million. Seven minutes after the first large transfer, Bitget's reconciliation system detected a balance discrepancy and automatically blocked all user-initiated withdrawals. That block did not stop the hack.

The attackers had exploited a zero-day vulnerability — previously unknown to anyone — in a third-party security product Bitget used. The vendor is described as a general-purpose provider not specific to crypto. Through this vulnerability, attackers accessed a critical internal management system, impersonated an internal identity, and directly inserted fraudulent withdrawal commands into backend wallet servers. The wallet servers executed those transfers as legitimate instructions. After completing the transfers, the attackers deleted all traces of the fraudulent commands, specifically to obstruct root-cause analysis and delay Bitget's response. Due to the absence of direct evidence, the security team had to examine a much broader range of systems to find the entry point.

A second wave occurred between 8:55 and 9:23 PM UTC, stealing approximately $30 million. This was not a security failure but a deliberate decision under uncertainty: unable to rule out a private key compromise, Bitget's team opened wallets to move funds from hot and warm storage to cold wallets. That temporary window allowed attackers a second, smaller incursion. Chen described the calculus directly: the funds rescued from the hot and warm wallets were far more than $30 million, making the exposure an acceptable cost.

**Recovery: $632K Frozen Out of $388 Million**

Recovery has been extremely limited. Tether and Circle responded fastest, freezing stablecoins from the stolen addresses early. Near Intend subsequently froze approximately $500,000 in crypto that had passed through its swap protocol after detecting the addresses. As of the interview, the total frozen is $632,000 across all three organizations. Chen drew the Bybit comparison directly: after one year, only 3.5% of more than $1.4 billion stolen from Bybit had been frozen, and actual recovery was a fraction of that. She said she hoped Bitget could do better but acknowledged low expectations.

Bitget is offering a 5% bounty for voluntarily freezing attacker funds and a 5% bounty for recovery, modeled on Bybit's approach. The company has maintained a live public dashboard tracking all stolen fund addresses at trace.bgblockchain.xyz/v2/explorer, patterned after the Lazarus bounty site Bybit created after its own hack. Bitget formally engaged SlowMist and Mandiant for independent forensics and is working through legal procedures required by Near Intend before any frozen funds can be transferred back.

**ThorChain vs. Near Intend: Diverging Stances on Permissionlessness**

Bitget publicly asked ThorChain to refuse service to hacker-associated addresses. ThorChain declined publicly. Chen noted what she saw as inconsistency: ThorChain has shut down its own system during previous hacks where it was itself the victim, but declined to act when the victim was a third party. Chen also referenced competitors who publicly criticized ThorChain for this position, observing that their stance differed when they themselves were hacked. She reached out to ThorChain privately through intermediaries but had not secured a direct conversation with its core developers by the time of the interview.

Near Intend took the opposing position. Its CEO Alex published a piece describing Near Intend's "shell" risk-intelligence layer — a system aggregating KYT signals, transaction-flow anomaly detection, and inputs from external researchers to automatically determine whether to permit individual transactions. Near Intend's stated principle: "permissionless doesn't mean neutral." Chen cited this approvingly, arguing that easy money laundering creates more hacking incentives across the industry, and called on DeFi protocols to build compliance and detection layers even atop permissionless architectures.

**Zach XBT and On-Chain Research**

Zach XBT's response to the hack was publicly complicated by his prior history with Bitget. Months earlier, he had accused Bitget leadership — naming both Gracie Chen and chairman Sean Liu by name — of allowing pump-and-dump schemes to operate on the platform, and announced plans to increase public pressure on the exchange. Separately he traced $500 million in withdrawals from suspected insiders of a token he called a market manipulation scheme. When the hack was announced, he initially posted that he had "no current plans to monitor the BitGet exploit" given the lack of support from Bitget's leadership. Days later, he published findings identifying five aliases used by Chinese illicit actors attempting to launder DPRK funds from the hack, reaching out in Discord channels with wallet-level transaction evidence. Chen confirmed Bitget's team had spoken to Zach and other on-chain researchers as part of broad industry outreach, but said no formal engagement or payment was made with him specifically, and she was not directly involved in those conversations. On his prior pump-and-dump allegations, Chen declined to respond substantively, noting the flagged tokens were listed across all major exchanges.

**User Protection Fund and Withdrawal Reopening**

Bitget established its user protection fund in mid-2022 after observing a wave of smaller exchange failures and bankruptcies. The fund is held in three publicly verifiable open wallets, with a publicly stated minimum threshold of $300 million (raised from an original $200 million). At the time of the hack, the fund held $464 million — more than the entire $388 million stolen. All user assets were fully covered and no user losses occurred.

Following the hack, Bitget moved some protection fund assets to hot wallets to meet withdrawal demand, and the fund's stated value has since risen to $556 million. The company plans to inject additional company capital within one week to restore the fund to above the $300 million threshold. Chen said the fund performed exactly as intended and she would not change anything about it; changes going forward would be to the security infrastructure, not the reserve structure.

On withdrawal reopening: Bitcoin withdrawals resumed the day before the interview; Ethereum withdrawals opened at 8:00 AM UTC the morning of the interview. One hour after Ethereum withdrawals opened, Bitget recorded 9,674 ETH inflow against approximately 9,023 ETH outflow — a net inflow. Chen described the lower-than-expected withdrawal volume as evidence of user confidence and expressed gratitude to users who stayed, while acknowledging significant work ahead to win back those who left.

**Security Changes and Industry-Wide Advice**

Post-incident security actions include: full network isolation of affected servers and systems to prevent further compromise and preserve forensic evidence; revocation and reissuance of all internal credentials; revocation of privileged system access; and restructuring critical operations to require multiple approvals. Chen acknowledged the central lesson: insufficient due diligence on the third-party vendor. The vendor is a general-purpose provider — "if you are not a crypto company, you might have used their service as well" — and Bitget will change how thoroughly it vets such vendors going forward.

Chen offered industry-wide advice: conduct thorough due diligence on every third-party service provider; assume social engineering will accompany or immediately follow any major incident; verify unfamiliar meeting or collaboration platforms before using them (she noted that even the video platform used for the Unchained interview gave her a brief moment of suspicion); maintain KYC, KYT, and KYB programs as a baseline; and build or join an industry alliance of top exchanges, security firms, and intelligence providers to systematically combat DPRK and other state-sponsored hacking operations.

**Ongoing Social Engineering Post-Hack**

The day before the interview, Chen was targeted by impostors posing as a prominent investment firm. The attack was sophisticated: multiple fake team members took different roles, each impersonating known figures from the real organization, approaching her with offers of help and requests for action. She detected the fraud by verifying through a separate, trusted channel with the organization's actual leadership. She attributed the timing explicitly to attackers knowing the post-hack recovery window creates pressure to engage many new counterparties rapidly, reducing normal verification diligence. She described this as a known DPRK playbook: study the target's public profile, identify who they would plausibly contact, and impersonate those people.

**IPO Timeline**

Bitget's IPO remains on the roadmap. Chen stated the hack does not change major financial plans. The company is actively communicating with law enforcement and regulators and framing itself as a victim that responded with transparency and competence.
