---
podcast: Unchained
date: 2026-03-19
source_transcript: data/podcasts/transcripts/Unchained/2026-03-19_DEX_in_the_City_Why_the_Binance_Case_Against_the_WSJ_'Is_Probably_Not_a_Winner'.md
---

# Unchained — "DEX in the City: Why the Binance Case Against the WSJ 'Is Probably Not a Winner'"

**Hosts:** Katherine Kirkpatrick Bos (general counsel, StarkWare); Jessi Brooks (web3 prosecutor turned web3 protector). **Guest:** Jane Khodarkovsky (partner, Arktouros; former federal prosecutor specializing in sanctions, AML, and illicit finance).

## TL;DR

- **Binance sued the Wall Street Journal for defamation** after a February 2026 WSJ report alleged $1.7 billion in crypto flowed through Binance tied to Iran's IRGC — Binance calls the allegations "categorically false," but the hosts and guest say the defamation case is "probably not a winner."
- **The defamation bar is actual malice** — because Binance is a public figure, the WSJ must have knowingly published false information to lose; that standard is nearly impossible to meet, especially for reporting on a legitimately contested factual claim.
- **The new allegations fall outside the 2023 settlement window** — the DOJ/FinCEN/OFAC/CFTC resolution covered conduct from 2017 to 2020; the WSJ's allegations describe more recent activity, meaning a parallel DOJ investigation is possible, and the agencies may not coordinate the way they did last time.
- **OFAC's power in crypto is structural but slow** — OFAC can sever a company from the entire US financial system via the SDN list, but designating crypto addresses has limited practical impact because new addresses can be created instantly; sanctions prosecution also requires proving the defendant knew the law existed, one of the highest criminal standards.
- **CFTC issued a no-action letter for Phantom's self-custodial wallet** — Phantom can route users to regulated derivatives partners (futures, perps, event contracts) without registering as an introducing broker, so long as its role remains passive with no discretion over individual orders; the hosts call this genuinely useful regulatory clarity.
- **A single DeFi transaction turned $50 million USDT into $36,000** — AAVE and Cowswap published conflicting postmortems (liquidity/price impact vs. infrastructure failure), renewing debate over whether DeFi can credibly court institutional partners while resisting best-execution standards that apply in TradFi.
- **X402 agentic payment protocol is generating hype but thin volume** — Stripe integrated the Coinbase/Cloudflare standard; daily volume is roughly $30K and 30-day volume is about $1.6 million, not the $24 million figure circulating on social media; competing options from Visa, Mastercard, and PayPal all let AI agents transact without crypto, raising questions about whether X402 offers a durable advantage.
- **Money transmission risk for X402 facilitators is unresolved** — the "facilitator" role in X402 (receiving payment, verifying on chain, settling) may constitute money transmission depending on how much custody and control the facilitator actually exercises; Jane Khodarkovsky says the answer requires seeing each specific implementation's flow of funds.

---

**Binance vs. the Wall Street Journal: The Defamation Claim**

In February 2026 the Wall Street Journal reported that approximately $1.7 billion in cryptocurrency flowed through Binance and was tied to Iran's Islamic Revolutionary Guard Corps, a comprehensively sanctioned jurisdiction and entity under US law. Binance disputed the allegations as categorically false and filed a civil defamation suit against the Journal. Senators subsequently called on the DOJ to investigate.

Khodarkovsky explains that Iran is one of a small number of "comprehensively sanctioned" countries where US persons and companies are prohibited from providing any services at all, distinct from the more targeted entity-by-entity sanctions that apply to, for example, Russia. The WSJ's allegations center on a scheme in which Chinese and Hong Kong-based actors allegedly opened Binance accounts, moved crypto through them, and routed funds to the IRGC. The theory is not that Binance's accounts were Iranian-held directly, but that Binance was willfully blind to transaction patterns that basic compliance review should have flagged as sanctions evasion or money laundering.

On the defamation suit itself, Kirkpatrick Bos notes that because Binance is almost certainly classified as a public figure, the WSJ would only be liable if it published with "actual malice," meaning it knew the allegations were false and published anyway. All three participants agree the case is "probably not a winner." Khodarkovsky notes that every defamation case is difficult and that even proving knowledge of falsity in a contested factual dispute is an extremely high bar. Brooks adds that there may be a PR rationale even absent legal merit: Binance has invested heavily in compliance personnel and wants to signal that it will no longer absorb reputational attacks silently.

**The 2023 Settlement and the Risk of a New Investigation**

The 2023 resolution with DOJ, FinCEN, OFAC, and the CFTC covered Binance's conduct between 2017 and 2020. Khodarkovsky flags that the WSJ's new allegations relate to a more recent timeframe, which means they fall entirely outside what was resolved. She notes there is no guarantee that a new investigation, if one is opened, would be a joint multi-agency effort the way the first one was — that collaboration was partly relationship-dependent, and agencies may move at different speeds or independently. The CFTC's involvement in the original resolution also means the new story touches yet again on an exchange subject to multiple US regulatory authorities simultaneously.

**How OFAC Works — and Why It Has Limits in Crypto**

Kirkpatrick Bos clarifies common misconceptions about OFAC. Adding a company to the Specially Designated Nationals (SDN) list freezes US assets and prohibits any US person or bank from transacting with it, effectively cutting off access to the global dollar system and even foreign banks with US correspondent relationships. That makes an OFAC action economically lethal. But Khodarkovsky points out that OFAC is a small office that moves slowly, and designating specific crypto wallet addresses — which OFAC began doing roughly five years ago — has limited operational impact because a new address can be generated in seconds. Criminal sanctions prosecution under IIPA and related statutes is also unusually demanding: unlike strict liability offenses, the government must generally prove the defendant knew the sanctions law existed, which is a high standard rarely seen in white-collar cases.

**CFTC Regulatory Moves: Prediction Markets and the Phantom No-Action Letter**

Kirkpatrick Bos covers two CFTC developments released around the time of the episode. The first, guidance on prediction markets, reaffirmed that designated contract markets (DCMs) must follow existing rules against manipulation and police their contracts accordingly. She calls it "a nothing burger" that largely restated current law, with the only notable element being specific reference to sports-related event contracts and potential coordination with leagues. The guidance also continued to signal that the CFTC views prediction markets as squarely within its jurisdiction.

The second action, a no-action letter for Phantom's self-custodial wallet, she considers more substantive. Phantom sought confirmation that it could allow users to access CFTC-regulated derivatives (futures, perps, event contracts) through partner exchanges without registering as an introducing broker. The CFTC said it would not take action because Phantom's role is entirely passive — no discretion, no involvement in individual order routing, no buy or sell signals. Kirkpatrick Bos emphasizes this is not a blanket clearance for all front ends, but it does provide a meaningful roadmap for the kind of passive interface role that escapes introducing broker registration.

**SEC-CFTC Memorandum of Understanding**

The episode briefly covers a new MOU between the SEC and CFTC committing to interagency collaboration on crypto oversight. Khodarkovsky calls the whole-of-government approach generally positive, citing her DOJ experience, and notes the 2023 Binance resolution as proof that joint enforcement is already precedent. She and the hosts temper enthusiasm by noting the arrangement is heavily dependent on the personal relationships of current leadership — CFTC Chair Brian Quintenz previously worked at the SEC, giving him built-in ties — and that durability beyond the current administration is uncertain.

**The AAVE Slippage Incident and the Best Execution Gap in DeFi**

The hosts discuss an incident in which a user lost nearly all of a $50 million USDT position in a single AAVE/Cowswap transaction, receiving approximately $36,000 due to catastrophic price impact from insufficient liquidity. The user had been warned by the interface before proceeding and clicked through anyway. AAVE's postmortem framed the event as a liquidity and price impact problem; Cowswap's framed it as an infrastructure failure. The conflicting accounts drew significant attention.

Kirkpatrick Bos frames the legal issue around best execution: in regulated TradFi environments, FINRA requires broker-dealers to use "reasonable diligence to find the most favorable price for the customer," and MiFID 2 imposes similar fiduciary obligations in the EU. Neither standard applies to DeFi. Brooks argues that the incident undermines DeFi's concurrent pitch to institutional partners, since it is difficult to simultaneously claim DeFi is consumer-safe and argue against regulation. Khodarkovsky pushes toward solutions: she argues the more productive question is what technical guardrails can be built natively into protocols so that events like this are mitigated without imposing CeFi-style intermediary requirements. She acknowledges that regulated institutions considering DeFi exposure will need credible answers on exactly these failure modes.

**X402 Agentic Payments: Real Use Case, Unresolved Legal Risk**

Brooks covers the X402 machine-to-machine payment protocol, originally developed by Coinbase and Cloudflare, which Stripe recently integrated. X402 enables AI agents to pay for gated resources (a paywalled article, an API call) automatically in crypto, with a "facilitator" verifying payment on chain and settling the transaction. The concept is genuine: it represents a potential native payment layer for agentic web commerce that existing HTTP infrastructure lacks, with micropayments as a credible advantage.

However, Brooks notes the actual numbers are modest: daily volume is around $30,000 and 30-day volume is approximately $1.6 million, well below the $24 million figure circulating on social media. She also notes that Visa (Intelligent Commerce), Mastercard (Agent Pay), and PayPal (agent-ready infrastructure) are all building non-crypto agentic payment options, meaning crypto is one path among many rather than a default.

The unresolved legal question is whether X402 facilitators constitute money transmitters. Facilitators take payment from one party, verify it on chain, and settle — a flow that resembles money transmission in that someone is taking custody and control of funds on behalf of others. Khodarkovsky says there is no settled answer yet and that it depends on the specific implementation: the key question is whether a given facilitator has meaningful discretion and custody over user funds or is simply executing a predetermined instruction. She also flags an identity dimension: World's integration of its identity verification kit into X402 signals that the industry recognizes that knowing who is actually initiating agentic payments will matter for sanctions compliance and consumer protection purposes.
