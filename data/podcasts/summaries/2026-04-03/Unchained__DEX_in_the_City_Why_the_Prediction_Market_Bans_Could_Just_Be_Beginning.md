---
podcast: Unchained
date: 2026-04-03
source_transcript: data/podcasts/transcripts/Unchained/2026-04-03_DEX_in_the_City_Why_the_Prediction_Market_Bans_Could_Just_Be_Beginning.md
---

# Unchained — "DEX in the City: Why the Prediction Market Bans Could Just Be Beginning"

**Hosts:** Vee Lee and Jesse Brooks (co-hosts, DEX in the City). **Guest:** Ryan Miller (partner, Morrison & Forrester financial services group; former CFTC staff counsel to Chairman Gary Gensler during Dodd-Frank; former commodities and derivatives partner at Sullivan & Cromwell; former General Counsel of FTX US).

## TL;DR

- **CFTC Chairman Michael Selig is running the agency alone** — no other commissioners have been nominated, and he's pushing an aggressive agenda covering digital assets, prediction markets, and Dodd-Frank cleanup, signaling a shift from "regulation by enforcement" to proactive rulemaking.
- **Joint CFTC-SEC interpretive guidance (March 17) formally categorized most major digital assets as commodities** — Miller calls it "the first real, tangible joint agency pronouncement" on token classification, giving traditional financial firms the regulatory certainty they need to enter the space.
- **Prediction market insider trading is already illegal under Dodd-Frank** — a provision enacted during that rulemaking bans using government information to trade derivatives; Miller says cases where someone trades on confidential employer information are "low-hanging fruit for the CFTC," and corporate compliance teams should update personal trading policies to cover prediction markets now.
- **The NFL may be the decisive force in where prediction markets land** — the league came out supporting federally regulated CFTC markets while pushing for stricter insider-trading enforcement; Miller says the NFL "decides where we go as a country" on this question.
- **Institutional prediction markets are coming, beyond sports** — smarter clients are focused on using prediction markets to express views on economic developments and hedge idiosyncratic risks; most current contracts are binary, but multi-range settlement products are beginning to emerge.
- **Canton Network's permissioned blockchain design is a choice, not a regulatory requirement** — critics at the DAF conference argued Reg SCI and PFMI principles don't mandate that unauthorized inputs be blocked from entering the system, only that unauthorized transactions not be processed; the deeper risk is that issuers retain full admin control, making enforcement dependent on operator good faith.
- **The Meta/YouTube product design liability verdict has direct implications for crypto** — a jury found that design choices (infinite scroll, gamified engagement) were the harm itself rather than the hosted content; the hosts argue the logic maps directly onto prediction market platforms, Pump.fun-style token launchpads, and potentially DeFi protocols.
- **A CFTC-SEC harmonization MOU signals joint crypto regulation is coming** — dual-registered entities currently face duplicative exam programs and reporting requirements; perpetuals on equities are cited as a product category that will require joint rulemaking if the U.S. wants a domestic parallel to on-chain global markets.

---

**CFTC Under Chairman Selig: From Enforcement to Rulemaking**

Ryan Miller frames the current CFTC moment around Chairman Michael Selig, confirmed by the Senate and now running the agency without any other commissioners — none have been nominated. Selig has flagged three priorities: cleaning up traditional Dodd-Frank over-the-counter swaps rulemakings, digital assets, and prediction markets. Stylistically, the transition from the prior era's regulation-by-enforcement approach is intentional and visible: the agency is putting out guidance, proposed rules, and advance notices of proposed rulemaking that invite market comment before action is taken.

Miller compares the expected output to the Dodd-Frank era under Chairman Gensler, when the agency produced 50 to 60 major rulemakings in a single year — far above the historical baseline of four or five. He says the CFTC is open to industry briefings and actively soliciting input on how on-chain markets work, particularly in DeFi. The agency's constraint is structural: it's funded by Congress rather than fees, giving it far smaller staff than the SEC despite derivatives markets that are comparable in notional size to equities markets.

The CFTC also announced an Innovation Task Force on March 24, led by the chairman's staffer Michael Pasolacqua. Its mandate covers digital assets and DeFi, AI, and prediction markets, and it includes private industry members who will help identify where rulemaking is needed.

**Token Taxonomy: The First Joint CFTC-SEC Categorization**

Miller describes the March 17 joint CFTC-SEC interpretive guidance on token taxonomy as a landmark event. For the first time in a concrete, actionable way, both agencies jointly pronounced how they will categorize crypto tokens for regulatory purposes. The headline outcome: most major digital assets are now clearly on the commodity side of the regulatory ledger. Miller says this is the level of certainty that lets market participants build new products and allocate capital in the United States — and specifically, it's the signal that traditional financial services firms have needed before diving in in a meaningful way.

**CFTC-SEC Harmonization and Dual-Jurisdiction Challenges**

The agencies signed a Memorandum of Understanding formalizing a joint harmonization effort, which Miller says is a significant signal. He points to decades of pain for dual-registered entities — entities like hedge funds that are simultaneously registered as investment advisors with the SEC and commodity trading advisors with the CFTC, facing duplicative examination cycles and reporting requirements for the same underlying activity.

Jesse Brooks notes that the practical stakes are high: many portfolio companies are trying to build in both the securities and commodities spaces simultaneously because crypto doesn't separate cleanly into those categories. She adds that products like tokenized equities and one-stop trading platforms — referencing Robinhood's planned L1 — are inherently cross-jurisdictional. Miller highlights perpetuals on equities as a specific near-term pressure point: once the CFTC establishes a framework for crypto perpetuals, demand for equity perpetuals will follow, and the U.S. currently has zero of this product because the existing dual-exchange regime was too burdensome to be commercially viable.

**Prediction Markets: Existing Law, Insider Trading, and the NFL**

Miller argues that the wave of legislative proposals to ban government officials from trading prediction markets is "politically charged" bill-waving rather than necessary new law. Dodd-Frank already includes a provision banning the use of government information to trade derivatives. If a government employee trades prediction markets based on confidential information obtained through their role, that's already a Dodd-Frank violation. The parallel to corporate insider trading is even more direct: employees who learn nonpublic information at work and trade on it are already subject to misappropriation law, and enforcement actions with fines exist in that space.

The hosts push back on whether laws are sufficient without enforcement. Miller agrees that some egregious cases will need to be brought before the frameworks feel real to market participants, noting "there's going to be some comically horrible fact patterns" in the early cases. Vee Lee adds that national security implications compound the problem — she references Israeli military officials arrested for trading on advance knowledge of military strikes. The panel agrees that corporate compliance teams should be updating personal trading policies to explicitly cover prediction market participation, the same way hedge funds already regulate employees' personal accounts with restricted lists.

On the institutional trajectory, Miller says the "smarter clients" he works with are looking past sports toward prediction markets as tools for expressing views on economic data and hedging idiosyncratic risks. Most current contracts are simple binaries, but multi-range settlement structures are emerging and expected to unlock significantly more institutional use. The NFL's public support for federally regulated CFTC prediction markets — while pushing platforms to get serious about insider-trading enforcement — is, in Miller's view, potentially decisive: "The NFL decides where we go as a country on this."

**Canton Network and the Permissioned vs. Permissionless Debate**

Vee Lee introduces the Canton Network debate by noting that Canton uses a permissioned architecture with sub-transaction privacy, centralized authorization, and gated membership. Canton's proponents frame this as a regulatory necessity, arguing that securities markets require privacy and authorization controls that public chains cannot provide, citing Reg SCI and the PFMI principles.

Lee disputes this framing directly. She argues those frameworks require that unauthorized transactions not be processed, but contain nothing that requires unauthorized inputs to be blocked from entering the system at all — Canton is making a design choice and claiming it's mandated. The deeper problem she identifies, citing Alex Glukowski of ZKsync at the DAF conference, is that Canton requires issuers to retain full admin control. On a public blockchain, enforcement is guaranteed by open-source code that anyone can audit. On Canton, enforcement depends on the operator acting in good faith, which she argues every investor on the other side of a trade should treat as a risk rather than a feature.

Miller offers a counterpoint focused on institutional incentives. Regulated financial institutions like Goldman Sachs and DTCC have their entire enterprise — investment banking operations representing trillions in exposure — at stake. Connecting to a permissionless chain with active hack and code-exploit vulnerabilities is not a risk they can accept just to experiment with distributed ledger technology. He views Canton as an intermediate step: "not a test net, but a very constrained environment where they get to control everything." His expectation is that the two worlds eventually connect, at which point the bifurcated liquidity problem forces cross-chain interoperability between Canton and public chains — just as cross-chain activity has emerged between Ethereum and Solana. Lee raises a fundamental question about whether that interoperability is even achievable if the public side cannot verify state on the permissioned side.

**The Meta/YouTube Verdict and Product Design Liability**

Jesse Brooks walks through the Meta/YouTube verdict in which a jury found both companies negligent not for hosting harmful content — Section 230 shields platforms from liability as publishers — but for designing products that predictably caused harm. The ruling signals that courts are willing to treat product architecture itself as the source of liability: infinite scroll, gamified engagement, notifications, reward loops that reduce friction and nudge behavior toward harmful outcomes.

Brooks argues the logic maps directly onto crypto. Prediction market platforms wrapping contract trading in real-time notifications, trending markets, and retail-friendly UX start to look like "engineered wagering" rather than neutral infrastructure. Pump.fun is cited as a clearer case: it collapsed token issuance, social virality, and retail speculation into a single loop, rewarding attention in ways structurally similar to social media — and producing some genuinely harmful outcomes in the process. DeFi protocols face the same question: even if a protocol claims it is infrastructure rather than a platform, someone made the design choices that made it frictionless and scalable.

Miller draws the financial services parallel: Wall Street has always offered arguably addictive products — options, complex derivatives — but has managed the exposure through disclosure requirements, suitability standards, and marketing restrictions aimed at retail investors. The new question is whether platforms must now embed suitability thinking into the product design process itself, not just into disclosures. He concludes that the outcome will land somewhere between outright bans and fully unregulated free markets, and that litigation is the mechanism by which that middle ground gets defined.
