---
podcast: Unchained
date: 2026-06-07
source_transcript: data/podcasts/transcripts/Unchained/2026-06-07_What_Two_DOJ_Cases_Reveal_About_the_Legal_Risks_of_Prediction_Markets_Bits_+_Bips.md
---

# Unchained — "What Two DOJ Cases Reveal About the Legal Risks of Prediction Markets: Bits + Bips"

**Host:** Steve Ehrlich (head of research, Sharplink). **Guest:** Sam Enders (partner, K Hill; founder, K Hill Next; former DOJ prosecutor, Southern District of New York).

## TL;DR

- **Two historic insider trading prosecutions on Polymarket:** US v. Spagnuolo (Google engineer traded on confidential search results, profiting ~$1.2M) and US v. Van Dyke (military officer traded on classified information about Venezuela/Maduro invasion), both filed by SDNY.
- **Insider trading charges reframed as commodities fraud, not securities fraud:** Because Polymarket is a CFTC-regulated derivatives exchange trading swaps (binary contracts), prosecutors charged wire fraud and commodities fraud rather than traditional securities insider trading.
- **Three legal preconditions for a prosecution:** material non-public information, received in confidence from a duty-bound source (Google, the government), and trading on that information with knowledge of the duty violation.
- **George Santos case opens "scalping" angle:** Santos bet against his own attendance at the State of the Union after publicly committing to attend, potentially exposing him to pump-and-dump or market manipulation charges rather than insider trading.
- **Prediction markets preemption debate: CFTC vs. state gambling laws.** Chair Selic argues commodities futures contracts on events (including sports) fall under federal jurisdiction; states claim gaming regulation applies. Third Circuit (2-judge majority) sided with CFTC; Ninth Circuit signals the opposite at oral argument.
- **Clarity Act does not resolve prediction markets.** The pending crypto regulatory bill explicitly excludes prediction markets, leaving resolution to courts or requiring separate legislation.
- **MicroStrategy Bitcoin sale resolution dispute:** A Polymarket binary contract on whether MicroStrategy would sell Bitcoin by end-May resolved based on SEC filing disclosure (June), not the actual sale date (May), costing tens of millions in disputed payouts and raising oracle/resolution-rule risks.
- **Retail traders face asymmetric risks:** Most participants lose money to professional market makers; additionally, traders must diligence contract specifications, oracle providers (UMA's ~9 top token holders have outsized voting power), and whether resolution terms are unambiguous before placing bets.

---

**Prosecution Theory: From "Insider Trading" to Commodities Fraud**

Enders explains that "insider trading" is a colloquial term, not a legal charge. The actual crime is a breach of fiduciary duty: receiving material non-public information in confidence from a source and trading on it for personal gain. In traditional securities cases, prosecutors charge wire fraud or securities fraud. Polymarket operates as a CFTC-designated contract market trading binary commodities swaps, so both the Spagnuolo and Van Dyke prosecutions are charged as commodities fraud and wire fraud rather than securities insider trading. This distinction matters because it sidesteps debates about whether an asset is a security—Polymarket is unambiguously a commodities exchange under CFTC oversight.

**The Spagnuolo Case: Google Confidential Information**

Spagnuolo, a Google engineer, had access to internal tools showing the year's top searches. He found a mismatch between what Polymarket traders expected and what Google's data showed, placing a bet on Kalshi (a different prediction market) that effectively locked in a risk-free profit from his perspective (setting aside legal risk). The complaint alleges he knew the information was marked confidential, and Google employees have a fiduciary duty to their employer. He profited approximately $1.2 million.

**The Van Dyke Case: Classified National Security Information**

Van Dyke, a member of the U.S. armed forces, allegedly traded on classified information about an imminent invasion and arrest of Nicolás Maduro in Venezuela before that operation occurred. He had signed confidentiality agreements binding him to protection of classified material. This case raises national security implications: if adversaries monitor prediction markets to anticipate U.S. military operations, those markets become intelligence gathering tools, jeopardizing operational security and potentially lives.

**The Three Legal Elements of Insider Trading**

Enders distills the test to three elements: (1) material non-public information, (2) received in confidence from someone who expects you to keep it secret, (3) trading on that information knowing you have a duty to keep it confidential. Unlike securities markets where the unfairness-to-other-traders framing dominates casual discussion, the law focuses on breach of a fiduciary relationship. Overheard tips at a bar don't count because there is no duty; a farmer hedging his orange crop based on his own knowledge of yield doesn't violate the law; an algorithmic trader beating the market with proprietary analysis infringes no duty.

**The George Santos Prediction Market Case**

Santos publicly stated he would attend the State of the Union address in February 2026, then canceled hours before it began while having bet heavily against his attendance. This fact pattern does not fit traditional insider trading because Santos is the source and definer of the information (his attendance plans), not a betrayer of someone else's confidence. However, two alternative prosecutorial theories emerge. First, if Santos lied when he said he would attend and then bet against himself, it resembles a "scalping" or pump-and-dump scheme—making a public misrepresentation to move the market in your favor before revealing the truth. Enders prosecuted John McAfee for similar behavior (recommending coins while secretly selling). Second, if Santos initially intended to attend but later decided not to and then placed the bet, prosecutors might argue market manipulation under commodities or wire fraud statutes, though this is a harder case because there are legitimate reasons to trade even as circumstances change. Prosecutors generally prefer cases with clear deception and specific intent (mens rea).

**The Chastain Precedent: Property-Based Limits on Wire Fraud**

The OpenSea case (US v. Chastain) involved an employee trading on inside information about which NFTs would be featured on the homepage. The Second Circuit reversed Chastain's conviction, holding that the information and property at issue were not proper subjects of wire fraud prosecution. Enders notes that defense counsel in Spagnuolo will likely cite Chastain, and a separate precedent (Blaszczak) raises questions about whether government-held information counts as "property" that can be stolen and traded on. These doctrinal limits create uncertainty for commodities fraud prosecutions.

**CFTC vs. State Gaming Regulation: The Preemption Battle**

Prediction markets have grown to billions of dollars in transaction volume, with projections of multi-trillion-dollar markets. Chair Selic of the CFTC and the Trump administration argue that when a CFTC-regulated designated contract market (DCM) such as Kalshi or Polymarket offers a binary futures contract on an event—including sporting events—it falls under exclusive federal jurisdiction under the Commodity Exchange Act. This preempts state gaming and gambling laws, meaning operators like Kalshi and Polymarket do not need state gambling licenses. FanDuel and DraftKings, by contrast, have obtained state gaming licenses because they operated under the assumption that sports betting requires state regulation. Enders represents prediction market operators and sides with CFTC preemption.

The courts are split. The Third Circuit issued a preliminary ruling (2-judge majority, 1 dissent) signaling CFTC preemption in a Kalshi case. The Ninth Circuit, at oral argument in a pending case, signaled it would likely rule the opposite way. Trial courts in other circuits have reached different outcomes. Unless Congress legislates clearly, the U.S. Supreme Court will eventually decide the question. The stakes are enormous: state regulators in gaming-dependent states like New Jersey and Nevada stand to lose significant tax revenue if sports betting on prediction markets escapes state licensing.

**Clarity Act Silence on Prediction Markets**

The pending Clarity Act, which would grant regulatory clarity to crypto markets, explicitly excludes prediction markets from its scope. This means no legislative pathway is imminent, and courts will determine the federalism question.

**The MicroStrategy Bitcoin Sale and Oracle Risk**

Polymarket hosted a binary contract on whether MicroStrategy would sell Bitcoin by the end of May. MicroStrategy disclosed in an SEC filing in June that a sale had occurred in May. The resolution dispute hinges on whether the controlling date is when the sale actually occurred (May) or when it became public (June filing). This dispute involves tens of millions of dollars and raises two systemic risks: (1) contract specification ambiguity—what exactly triggers a resolution?—and (2) oracle risk—how are disputes resolved? Polymarket uses UMA, a relatively small oracle provider. Ehrlich reports that roughly 9 top token holders on UMA control sufficient voting power to decide most outcomes, concentrating risk in a handful of parties rather than achieving true decentralization.

**How Binary Contracts Can Spiral Into Ambiguity**

Enders notes that contract language must be concrete and unambiguous. Ehrlich recalls a previous Polymarket resolution dispute over Volodymyr Zelenskyy's attire when he met President Trump (whether he wore a "suit"). Definitions that seem obvious in English become contested when real money is on the line. The resolution mechanism depends on an oracle—in this case, UMA token holders voting on the outcome. There are no universally accepted standards yet for how such contracts should be written to avoid disputes, though the CFTC expects designated contract markets (DCMs) to self-certify guidelines ensuring contracts are sufficiently precise and markets are not susceptible to manipulation.

**Retail Trader Diligence and Risk Factors**

Enders advises retail participants to (1) understand the bet specifications and how the outcome is determined, (2) assess their edge—why do they believe they have better information or analysis than the market?—and (3) verify the edge is legal (not based on inside information). Beyond prosecutorial risk, traders face multiple layers of counterparty and structural risk: professional market makers consistently beat retail traders; leverage products are expanding; oracle governance is concentrated; and resolution terms can be interpreted multiple ways. Enders personally views prediction markets primarily as a data source, not a trading venue—observing market prices to infer crowd beliefs rather than betting. Retail traders should not risk money they cannot afford to lose, especially as leverage trading becomes available.

**Unresolved Legal Questions**

Enders flags several open doctrinal issues: Do these criminal statutes apply extraterritorially to offshore trading (Polymarket and Kalshi operate outside the U.S. but accept U.S. traders)? What types of property can be regulated under insider trading and wire fraud statutes? (Chastain and Blaszczak create ambiguity.) The government signaling that Polymarket trades are commodities, not securities or gambling, has implications for ongoing SEC-crypto debates (Howey test) but does not resolve them uniformly. The landscape is evolving rapidly, driven by prosecutorial action rather than legislation.
