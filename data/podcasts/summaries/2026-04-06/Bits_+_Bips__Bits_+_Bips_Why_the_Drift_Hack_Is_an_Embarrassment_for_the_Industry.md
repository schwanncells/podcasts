---
podcast: Bits + Bips
date: 2026-04-06
source_transcript: data/podcasts/transcripts/Bits_+_Bips/2026-04-06_Bits_+_Bips_Why_the_Drift_Hack_Is_an_'Embarrassment_for_the_Industry'.md
---

# Bits + Bips — "Why the Drift Hack Is an 'Embarrassment for the Industry'"

**Hosts:** Austin Campbell (Zero Knowledge Group); Ram Ahluwalia (CEO, Lumida); Chris Perkins (founder, 250 Digital, soon to be head of Franklin Crypto).

## TL;DR

- **$285 million drained from Drift Protocol on April 1st** — the biggest DeFi hack of 2026 so far and the second-largest Solana hack ever, behind Wormhole's $326 million in 2022. Funds were bridged to Ethereum via Circle's CCTP within 12 minutes.
- **North Korea's Apple JS group executed a 6-month social engineering campaign** — attackers posed as a quant trading firm, met Drift contributors in person at conferences across multiple countries via paid proxies, deposited over $1 million to build credibility, then struck via a VS Code Cursor zero-day and a malicious TestFlight app. Attribution assessed at "medium to high, growing toward very high" confidence by SE911; on-chain flows also link to the Radiant Capital hack.
- **Circle faced backlash for not freezing $232 million in USDC** — ZachXBT argued Circle's inaction enabled laundering through its own CCTP bridge; Circle responded it only freezes when legally required. Austin argues post-GENIUS Act rules will likely impose monitoring and freeze obligations on stablecoin issuers, and that Circle may face money transmitter liability for the roughly six-hour window during which funds were visibly moving.
- **The Drift 2-of-5 multi-sig raises an unlicensed money transmitter question** — Austin argues that a protocol where specific parties hold upgrade keys and can seize control at any time is functionally "pretty bank-like" and not meaningfully decentralized, which could expose founders to regulatory liability.
- **Iran's IRGC has built a crypto toll booth in the Strait of Hormuz** — operators can pay $1 per barrel to $2 million per super tanker in yuan or stablecoins via Tron to transit the strait. The IRGC moved $3 billion through crypto in 2025 per Chainalysis; Iran's Ministry of Defense now accepts crypto for arms exports. Chris argues stablecoins are actually a trap for bad actors: freeze and seize capabilities make USDT a surveillance vector, not a safe haven.
- **The hosts disagree sharply on the Iran war campaign** — Ram calls it a "C minus execution effort," citing missed timelines, repeated delays, Iran setting negotiation terms, and 10 years of Tomahawk inventory burned. Chris defends the tactical military execution and compares the situation to the 1995 Scott O'Grady rescue. Austin notes a disconnect between Trump's negotiating rhetoric and the military's strategy of eliminating Iranian leadership.
- **The token fundamentals thesis is in crisis** — token count has grown from ~5,000 in 2020 to ~75,000 today; the median token is down 80% from its peak. Revenue has decoupled from token prices since 2021, and protocol founders are accused of not being honest about valuations. Chris disputes the framing, arguing tokens are wrappers and the issue is whether there's real value underneath, not how many exist.
- **Franklin Templeton acquired 250 Digital** — Chris Perkins's liquid crypto fund will become the foundation of Franklin Crypto, with Perkins as head. The deal was partly funded using Franklin's own BENJI tokenized money market fund. The goal is institutional-grade, scalable crypto investment solutions for pensions, endowments, and corporations.

---

**The Drift Hack: Nation-State Social Engineering at Scale**

The Drift Protocol hack, which drained $285 million on April 1st, stands as the largest DeFi exploit of 2026 and second-largest in Solana history. What distinguished it from previous hacks was the degree of operational sophistication: attackers spent six months building in-person trust at conferences across multiple countries, using paid proxies so that no North Korean nationals were directly present. They deposited over $1 million and built a functioning ecosystem vault to establish credibility before striking. The technical attack vectors included a VS Code Cursor zero-day that silently executes code on file open with no click or warning, and a malicious TestFlight app. By the time the exploit completed, the group's Telegram chats and malicious software had been fully scrubbed.

Attribution points to the DPRK's Apple JS group, with confidence characterized as "medium to high, growing toward very high" based on analysis by SE911 and on-chain fund flow tracing that links the hack to the Radiant Capital breach attributed to the same group. Mandiant was engaged. Most of the funds were bridged to Ethereum via Circle's CCTP within roughly 12 minutes.

Chris Perkins frames the situation plainly: "When a nation state attacks a startup, the nation state's going to win every single time." He argues the industry needs what he calls "neo-privateers" — licensed private citizens who can respond immediately to on-chain exploits in the way that on-chain investigators like ZachXBT already operate informally, but with legal authority and a policy framework to act. He sees the CLARITY Act as a potential vehicle and says recovery policy capabilities should be included in the bill.

**Circle's Liability and the Stablecoin Freeze Debate**

ZachXBT publicly criticized Circle for not moving faster to blacklist wallets after the hack, claiming that inaction enabled $232 million in USDC to be laundered through Circle's own CCTP cross-chain bridge. Circle's stated position, as reported by Coindesk, is that it freezes only when legally required — a stance that highlights, as Austin puts it, "a core tension between on-chain speed and legal norms."

Austin argues the legal picture will clarify substantially post-GENIUS Act. Under the Bank Secrecy Act framework, banks are already permitted — and often required — to temporarily hold funds when suspicious activity is flagged, in the same way that a large wire transfer triggers a "was this you?" verification text. He suggests it would not be surprising if US dollar stablecoin issuers end up with similar monitoring and freeze obligations once GENIUS rulemaking is complete.

More pointed is Austin's argument about money transmitter liability. Circle holds money transmission licenses in most US states, and money transmitters have a duty of care toward user funds. He draws an analogy to MoneyGram: if someone shows up claiming to be a customer with no ID and receives funds meant for someone else, the transmitter shares liability. The Drift case is notable because the exploit became publicly visible on social media quickly, and funds continued moving through CCTP for approximately six hours — making it difficult for Circle to argue it lacked adequate notice or time to act.

**Protocol Decentralization and the 2-of-5 Multi-Sig Problem**

Austin raises a structural question about Drift's 2-of-5 multi-sig governance: if protocol contributors hold private keys that allow them to upgrade the smart contracts and effectively seize control at any time, how is that meaningfully different from a centralized financial intermediary? He contrasts this with truly immutable smart contracts where keys are burned after deployment, arguing that upgradable protocols with identifiable key holders look "pretty bank-like" and may qualify as unlicensed money transmitters under existing law. Had regulators made this determination clear in 2021, Austin argues, it might have preempted the Drift situation entirely by forcing protocol teams to choose between genuine decentralization and proper licensing.

Ram frames the broader tension: security and centralization tend to go together because centralized systems have gate points and supervisory actors, while permissionless trustless systems are inherently more porous. DeFi has been building complex, decentralized protocols without the security infrastructure that complexity demands. His verdict: "It's an embarrassment for the industry." Protocol audits proved insufficient; social engineering bypassed technical safeguards. He argues VCs spent too much capital on L1 and L2 infrastructure chasing quick flips rather than investing in the core security and trust infrastructure DeFi needs to attract institutions. Austin summarizes the dynamic: "Crypto is speed running the history of finance. The thing they're speed running here is why financial regulation exists."

**Iran's Crypto Toll Booth and Stablecoin as Surveillance Vector**

The IRGC has reportedly established a live payment system at the Strait of Hormuz: tanker operators can pay $1 per barrel or up to $2 million per super tanker in yuan or stablecoins via Tron to transit the strait. Chainalysis estimates the IRGC moved $3 billion through crypto in 2025, and Iran's Ministry of Defense has begun accepting crypto for arms exports.

Austin frames it sardonically — the dollar now on both sides of the conflict — but Chris turns it around: from a national security standpoint, stablecoins are a poor choice for bad actors. The underlying treasuries are held by centralized, accountable entities that can be pressured. Freeze and seize capabilities mean the US government could, in principle, allow adversaries to accumulate large stablecoin positions and then interdict them overnight. Chris argues this gives US intelligence "a very good vector, not only to freeze and seize, but sometimes maybe they just watch it a little bit and see where it goes." His conclusion: bad actors using stablecoins are taking on significant operational risk they may not fully appreciate.

Austin adds that the public ledger aspect is consistently underestimated: "People greatly underestimate the public part of public blockchains."

**The Iran War: Tactical Execution vs. Strategic Drift**

Ram is pointed in his criticism: the campaign has delivered repeated deadline delays (March 26th, then April 1st, then further extensions), Iran is setting negotiation terms rather than accepting them, the Pentagon burned roughly 10 years of Tomahawk inventory, and the US has not secured Iran's uranium. His assessment: "C minus execution." He argues the public is being misled and that Trump's Monday claim of "12 points of negotiation and alignment with Iran" was contradicted within days by Iran issuing its own demands.

Chris defends the tactical military record, citing the recovery of a downed F-15 weapon system officer as an example of American values and operational capability. He draws on his experience aboard the USS Kearsarge during the 1995 Scott O'Grady rescue to describe the complexity of such missions. He separates tactical execution from strategic outcomes, arguing the fighting forces — commanded by Admiral Cooper, not the relieved Army chief of staff — have performed well, and that the broader situation, while bad, was worse before action was taken: Iran was accelerating toward nuclear capability.

Austin identifies the central contradiction: the military's actions — systematically eliminating Iranian leadership — are the actions of a force trying to exhaust an enemy into surrender, not the actions aligned with Trump's stated goal of a quick negotiated settlement and an open strait. He raises two explanations: either there is a coordination failure within the US government, or Trump's public rhetoric is deliberately calibrated to manage market expectations rather than describe operational reality.

The Polymarket controversy surfaces briefly: Representative Seth Moulton condemned the platform for listing a market on whether the downed F-15 pilots would be rescued, calling it "disgusting." Polymarket removed the market and apologized, citing a failure of internal safeguards. Chris notes that as prediction markets decentralize, enforcing content limits will become structurally harder.

**Token Fundamentals Crisis: Too Many Tokens, Broken Transmission Mechanism**

The episode addresses a widely circulated thread arguing that the token ecosystem is in structural distress. The numbers: roughly 5,000 tokens existed in 2020; today there are approximately 75,000. The median token is down 80% from its peak; the average coin is only slightly above 2020 levels and down 50% from 2021. Revenue growth has decoupled from token price performance — even in periods of strong on-chain revenue, token appreciation has not followed. The proposed explanation: "revenue growth rarely became token holder returns," and investors can no longer trust that protocol success flows to them.

Chris pushes back on the framing. A token is a wrapper, he argues — like an ETF — and the fact that most wrappers contain nothing of value does not indict the wrapper format itself. The question is always what's underneath: real users, real revenue, meaningful governance rights, and clear value accrual mechanisms. He sees the 99% of tokens trending toward zero as noise, not signal. Ram agrees in substance but adds that genuine product-market-fit names are identifiable, the list is short, and many have been indiscriminately sold off in the macro drawdown — creating selective opportunities for investors willing to do the work.

Austin introduces a finer-grained critique: many protocol tokens fail not because tokens are bad wrappers but because the underlying promise was hollow — no legal ownership, unclear governance rights, and cash flows being redirected away from token holders. He also questions the FAT protocol thesis: if layer-one block space is a commodity, value may accrue to applications rather than infrastructure, and the L1 heavy allocations of the last cycle may have been systematically mispriced.

Chris confirms this view is becoming consensus: apps are where value discovery will concentrate, L1 competition has become Hobbesian, and the handful of protocols with genuine product-market fit are the ones worth underwriting. Ram adds that the macro backdrop still has a "boot on the throat" of these projects, suggesting patience over urgency: do the research now, size the short list, and deploy when the macro picture clears.

**Franklin Templeton Acquires 250 Digital**

Chris Perkins announced that Franklin Templeton acquired 250 Digital Asset Management — his liquid crypto strategies fund spun out of CoinFund — to form the foundation of Franklin Crypto, with Perkins as head and Seth as CIO. The transaction was announced April 1st and is pending close. Notably, Franklin Templeton used its BENJI tokenized money market fund — one of the earliest and largest tokenized MMFs in the industry — to help fund transaction costs.

Chris describes the opportunity as serving institutional clients — pensions, endowments, corporations — who know they need crypto exposure but lack the infrastructure to execute. Franklin Templeton's CEO Jenny Johnson, who came up through a technology background, has driven the firm's crypto and tokenization strategy from the top since 2018. Sandy Kaul, whom Chris describes as "one of the biggest brains on Wall Street," is also joining the effort. The stated goal is to be the leading active investor in crypto for the institutional market, leading with controls as the primary differentiator. Chris envisions AI-powered, customizable vault-based solutions as a medium-term product direction.

Austin notes that BENJI's use as a transaction funding mechanism is emblematic of a broader shift: a regulated 40 Act government money market fund being used as a money instrument on-chain is not DeFi — it is traditional financial activity migrated onto a blockchain, which Austin describes as the core institutional tokenization thesis in practice.
