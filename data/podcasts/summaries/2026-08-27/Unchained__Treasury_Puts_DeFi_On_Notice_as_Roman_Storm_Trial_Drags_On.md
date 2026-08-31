---
podcast: Unchained
date: 2026-08-27
source_transcript: data/podcasts/transcripts/Unchained/2026-08-27_Treasury_Puts_DeFi_On_Notice_as_Roman_Storm_Trial_Drags_On.md
---

# Unchained — "Treasury Puts DeFi On Notice as Roman Storm Trial Drags On"

**Host:** Kain Warwick (Uneasy Money segment; founder, Infinex and Synthetix). **Co-Host:** Taylor Monahan (security expert). **Guest:** Peter Van Valkenburgh (executive director, Coin Center; policy researcher on sanctions, blockchain regulation, and financial privacy).

## TL;DR

- **Treasury Secretary Bessent announces "economic D-Day" against Iran** — threatened secondary sanctions on entities buying Iranian gold, oil, or Bitcoin; deliberately left door open for potential DeFi protocol targeting, though public release did not explicitly call out DeFi or Uniswap.
- **Federal government seized ~$1 billion in Iranian cryptocurrency** — Bessent claimed seizure of $1B; Tether froze $344M in USDT on Tron in April 2024 related to Iranian wallets, though freeze amounts and Iranian attribution remain disputed.
- **Roman Storm's Tornado Cash retrial rescheduled to April 2027** — jury deadlocked on sanctions evasion and money laundering charges in first trial; defendant convicted on money transmission count but awaiting Rule 29 motion decision on whether to declare mistrial on entire case.
- **Tornado Cash prosecution questioned as strategically ineffective** — speakers argue prosecution has not reduced North Korea's malware-funded theft volumes or significantly impacted Tornado Cash usage; protocol remains immutable and functional regardless of developer prosecution.
- **SEC proposes RegCrypto safe harbor for token offerings** — two exemption paths: raise up to $5 million over 4 years, or up to $75 million in any 12-month period; 60-day comment period open; undergoes legal scrutiny despite hinging on statutory securities law authority.
- **Trump administration signals openness to Hyperliquid no-KYC derivatives** — president mentioned Hyperliquid by name at press conference; regulatory pathway unclear amid CFTC jurisdiction questions and tension between market supervision vs. KYC requirements.
- **Stablecoin issuers (Circle, Tether) likely already complying with Iran sanctions** — public blockchains enable chain analysis and real-time surveillance; issuers have information-sharing arrangements with government; secondary-market freeze-and-seize authority proposed in Genius Act.

---

**Bessent's Iran Sanctions Threat and DeFi's Ambiguous Status**

Treasury Secretary Bessent announced "economic D-Day" against Iran, threatening secondary sanctions on any entity purchasing Iranian gold, oil, or Bitcoin. Kain Warwick notes the rhetoric is unusually market-moving compared to historical Treasury announcements. Peter Van Valkenburgh emphasizes that the Treasury release itself does not explicitly call out DeFi, Uniswap, or decentralized protocols. However, the language is intentionally broad: "any source" of regime revenue and "every economic lifeline" could theoretically include digital assets and their intermediaries. The ambiguity is strategic—the administration deliberately avoids ruling out DeFi as a sanctions target, preserving optionality.

Van Valkenburgh argues the most pragmatic approach is to focus sanctions on centralized intermediaries (Iranian exchanges, brokers, front companies) where people "have agency and fiduciary control" over funds. He draws a distinction between targeting human actors with real jurisdiction (secondary sanctions) versus attempting to shut down immutable protocol infrastructure, which he suggests would be ineffective and cause unnecessary collateral damage.

**Seizures, Freezes, and Scale**

Bessent claimed the federal government had seized approximately $1 billion in Iranian cryptocurrency. Taylor Monahan recalls a $344 million USDT freeze on Tron in April 2024, though attribution as specifically Iranian and the exact scope remain unclear. Monahan notes that Tether tends to execute freezes more visibly and aggressively than Circle, sometimes with dramatic language.

Van Valkenburgh places these seizures in scale: the $1 billion represents roughly eight hours' worth of Iranian oil revenue flows. While the absolute number is significant, it is small relative to the daily cost of maintaining the US blockade against Iran (hundreds of millions per day) and the volume of funds Iran seeks to move (low single-digit billions per day). The practical impact on Iran's ability to fund its nuclear program, while non-zero, is limited.

**Stablecoin Compliance and the Genius Act's Secondary Market**

Monahan and Van Valkenburgh discuss stablecoin issuers' existing compliance infrastructure. Public blockchains allow real-time chain analysis; Circle and Tether already employ sanctions screening on their front ends (website interfaces). Van Valkenburgh expects issuers have ongoing conversations with Treasury and likely possess non-public information-sharing agreements.

The Genius Act creates new regulatory structure for stablecoins, requiring issuers to implement freeze-and-seize capability for secondary-market funds (tokens in user wallets). However, the Act explicitly does not require issuers to treat secondary-market holders as customers needing full KYC. Van Valkenburgh argues this is the appropriate balance: issuers gain the ability to stop the flow of their issued funds wherever they exist on the blockchain, but avoid collecting intrusive personal information about strangers holding tokens.

**Roman Storm's Tornado Cash Trial Postponed; Jury Deadlock on Core Charges**

The retrial of Roman Storm on Tornado Cash-related sanctions and money laundering charges has been rescheduled to April 2027, delayed while the judge considers Storm's Rule 29 motion for mistrial on all counts. In the first trial, the jury convicted Storm on the money transmission charge but deadlocked on sanctions evasion and money laundering, forcing a mistrial on those counts.

Van Valkenburgh emphasizes the legal complexity. For sanctions evasion or conspiracy to commit sanctions evasion, typical prosecution would involve evidence of direct transactions with sanctioned parties. Storm, as a software developer who paid for servers, has no documented transaction with any sanctioned entity. The conspiracy charge requires proving he knowingly aided sanctions evasion; Van Valkenburgh notes the software was designed to be immutable and neutral, not marketed or optimized specifically for sanctioned users.

On the money transmission count (where he was convicted), Van Valkenburgh highlights a critical but overlooked statutory carve-out: the Burman Amendment, which prohibits the president from sanctioning transactions in information. Even if Tornado Cash is treated as a transaction, it is fundamentally a publication of software and zero-knowledge proofs on the blockchain—information. Van Valkenburgh argues this should provide legal protection regardless of how others use the tool.

**Prosecution as Chilling Effect Without Measurable Security Benefit**

Van Valkenburgh and the hosts question the strategic value of the prosecution. DPRK's use of Tornado Cash has not appreciably declined; the hacking operations continue. Volumes impacted by sanctions on stablecoins and centralized exchanges have been measurable (the $1 billion seizure), but no equivalent reduction in DPRK activity is attributable to prosecuting Storm.

Van Valkenburgh argues the prosecution has created a chilling effect without corresponding benefit. Developers building privacy and cryptographic tools face legal risk despite the Burman Amendment protection. The hosts note that Tornado Cash was a technological breakthrough—a live, large-volume deployment of zero-knowledge proofs, demonstrating privacy at scale. Arresting Storm does not stop the immutable protocol; it signals hostility toward builders willing to take risks on frontier technology.

Taylor Monahan reflects on the broader pattern: when the government uses aggressive enforcement without clear strategic payoff, it drives legitimate builders toward jurisdictions outside US oversight. A more pragmatic approach would focus on bad actors (hackers, money brokers, sanctions evaders) rather than software developers.

**SEC's RegCrypto Safe Harbor: Two Exemption Paths for Token Offerings**

The SEC, specifically Commissioner Hester Peirce, has proposed two exemptions under RegCrypto to allow token offerings with guardrails. The first path permits companies to raise up to $5 million over a 4-year period; the second allows up to $75 million in any 12-month period. Both require disclosures and claims of reasonable decentralization roadmap.

Van Valkenburgh notes RegCrypto harkens back to Peirce's original safe harbor proposal, which sought to allow projects with legitimate decentralization goals to raise capital without triggering full securities registration. The exemption is now a Notice of Proposed Rulemaking (NPRM) with a 60-day comment period.

The speakers discuss RegCrypto in tension with the stalled Clarity Act in the Senate. RegCrypto is an SEC rule (more ephemeral; a future commission can change it) whereas Clarity would be legislation (more durable; requires Congressional action to undo). However, if RegCrypto survives legal challenges (e.g., from traditional finance entities claiming it exceeds SEC authority), the accumulated investor dollars invested under the rule create economic inertia that makes future reversals harder to justify.

**Hyperliquid and the Ambiguity Around No-KYC Derivatives**

Trump mentioned Hyperliquid by name at a press conference, signaling openness to no-KYC derivatives platforms. The context is pragmatism: rather than driving Hyperliquid's builders offshore, the administration signals interest in legalizing and regulating the service domestically.

However, the regulatory pathway is complex. Derivatives fall under CFTC jurisdiction, which has plenary authority but also much higher retail investor thresholds (Eligible Contract Participant rule requires $5 million+ accredited status) compared to SEC securities. The CFTC's traditional focus is market manipulation and derivatives supervision, not KYC compliance; that is historically Treasury's domain.

Van Valkenburgh sketches the regulatory fragmentation: the CFTC has authority over derivatives but limited visibility into spot markets that influence those prices. There is no modern precedent for allowing a no-KYC platform to operate under CFTC supervision. The CFTC could theoretically craft a rule allowing it, but this would invite lawsuits from traditional derivatives venues (CME, CBOE) claiming the CFTC misused its discretion.

The speakers note that Uniswap operates without KYC and is largely accepted as infrastructure, not a regulated venue requiring identities. A possible path forward might adopt hybrid principles: CFTC focuses on market manipulation and efficiency; Treasury handles AML/KYC. But implementation details remain unclear, and the multi-regulator coordination is messier than it would be with a single statutory authority.

---

**Pragmatism vs. Maximalism in Sanctions and Regulation**

The episode's underlying theme is the tension between pragmatic resource allocation and symbolic enforcement. Bessent's seizures and Treasury's new sanctions focus on centralized intermediaries because they have measurable impact and clear jurisdiction. Tornado Cash prosecution, by contrast, creates legal risk without stopping the protocol or the criminals using it. RegCrypto allows legitimate token offerings instead of driving them underground or into the hands of venture capitalists. And Hyperliquid signals the administration recognizes no-KYC platforms cannot be regulated out of existence and might as well be brought into a supervised framework.

Van Valkenburgh emphasizes that the crypto industry historically responds to hostile regulation by building in jurisdictions that don't care, burning visibility into government hands, and concentrating wealth in VCs (who can afford legal battles). Pragmatic regulation—guardrails for legitimate activity, enforcement against bad actors—is more likely to achieve policy goals (preventing money laundering, sanctions evasion) and to keep innovation visible and in the US.
