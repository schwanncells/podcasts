---
podcast: Unchained
date: 2026-04-24
source_transcript: data/podcasts/transcripts/Unchained/2026-04-24_DEX_in_the_City_KelpDAO_vs._LayerZero_Who_Is_Liable_When_a_DeFi_Protocol_Is_Hacked.md
---

# Unchained — "DEX in the City: KelpDAO vs. LayerZero: Who Is Liable When a DeFi Protocol Is Hacked?"

**Host:** Catherine KK (fluent in TradFi and conversant in deep tech, Starkware). **Guests:** Jesse (Web3 prosecutor turned Web3 protector, Rivet Capital); V (former SEC, now Web3-focused attorney).

## TL;DR

- **$300M KelpDAO/LayerZero exploit:** Attackers compromised infrastructure tied to KelpDAO's Layer Zero bridge, forged cross-chain messages, minted restaked ETH, and used it as collateral on Aave to withdraw real assets with no backing—turning a single bridge exploit into a system-wide crisis.
- **Liability unclear in DeFi:** Unlike traditional products where duties are well-defined, DeFi lacks clear responsibility chains. Neither KelpDAO nor Layer Zero wants to be blamed, but courts haven't yet established who had a duty and failed to meet it—negligence may not apply; gross negligence suits could become common.
- **47% of Layer Zero teams chose one-of-one verifier setup:** This single point of failure became the attack vector. The question: Is Layer Zero liable for offering this risky default? Is it like selling a car with optional airbags, or should teams bear responsibility for their config choices?
- **DeFi's core values—permissionlessness and decentralization—enable contagion:** KelpDAO's composability across protocols meant the exploit spread beyond a simple bridge hack. Protocols may need to rethink constraints like rate limits or asset restrictions without re-intermediating the system.
- **Ninth Circuit grilled prediction markets on gambling vs. derivatives:** Three Trump-appointed judges appeared skeptical of the CFTC's federal preemption argument in Kalshi vs. Nevada. A split circuit decision makes Supreme Court review in 2027–2028 likely.
- **Agentic commerce liability is being solved outside crypto:** Amex launched agent purchase protection—covering losses when AI agents make transaction errors. Crypto hasn't addressed identity, mandate, and accountability in agentic systems; blockchain is the natural habitat but isn't closing the gap fast enough.
- **DeFi user base is shifting:** As retail investors enter (including non-builders), lawsuits and liability become inevitable. If your mom loses $15, she will call the SEC. The industry can't rely on "degen phase" excuses anymore.

---

**The Run of Exploits and KelpDAO's Bridge Hack**

V reports that in recent weeks, DeFi has suffered a cascade of attacks: Resolve (minting function manipulation), Drift (oracle manipulation), and KelpDAO (bridge exploit). Within the last three months, losses exceed all of 2025 combined. KelpDAO was the largest this year. Almost 300 million restaked ETH was drained after attackers compromised infrastructure tied to KelpDAO's bridge connection to Layer Zero. Attackers were able to forge a cross-chain message, mint restaked ETH without underlying collateral, and use the newly minted asset as collateral on Aave to borrow or withdraw real assets. This turned what could have been an isolated bridge exploit into a potential system-wide crisis.

V emphasizes accountability is essential: questioning poor operational security, governance design, or security practices is not grave-dancing; it is necessary to prevent future incidents. KK draws a parallel to gun violence discourse—silence prevents improvement and disrespects victims.

**Liability and the Question of Duty**

Catherine KK, a former litigator, explains that litigation hinges on establishing duty: who had a responsibility to do X and failed to meet it. In DeFi, this is murky. Negligence suits are common in litigation, but they require showing breach of a duty—which is often unclear in DeFi. Gross negligence (a higher bar) may become more common as plaintiffs' lawyers sue everyone involved. KK notes that contemporaneous communications matter; taking ownership of an incident in internal comms can create liability.

V frames the core legal question: Is Layer Zero liable for even offering a one-of-one verifier setup when 47% of teams selected this configuration? The comparison is to a carmaker offering optional airbags. If a large portion of the ecosystem adopts one configuration, does it stop looking like individualized choice and start looking like an industry standard? When that choice leads to a $300M loss, who bears responsibility?

**Defaults, Design, and DeFi's Coming Reckoning**

V argues that defaults matter. Offering an option shapes behavior. If you have a large portion of your user base gravitating toward one setup, it's no longer just a choice—it's an architecture. Courts will eventually have to wrestle with when saying "we provided the tools" is insufficient as a defense.

KK adds that DeFi is moving past its degen phase. Everyday retail users are entering the space. If a non-builder loses $15, they will call the SEC. The industry has to be responsible and understand that lawsuits will become common.

V draws a parallel to fintech and banking-as-a-service (BaaS) crises. Community banks relied on BaaS providers, which weren't correctly accounting for client funds. The outcome: if you have a relationship with the customer, you are liable. Your users shouldn't have to know the entire underlying stack. DeFi teams need to understand they have a relationship with their users and that liability comes with it.

**Composability as Strength and Vulnerability**

Catherine emphasizes that the strengths of DeFi—composability, permissionlessness, interoperability—are also its vulnerabilities. Open systems empower bad actors. The industry must ask itself hard questions about constraints. Permissionlessness and decentralization are conflated but distinct. A protocol can restrict asset types or impose rate limits without requiring KYC. New users shouldn't be able to deposit and borrow $300M in one shot, and protocols should consider mechanisms that don't re-intermediate the system. DeFi is at an inflection point.

Jesse pushes back: regulators already have enough reason to overreact; DeFi's Twitter statements won't change that calculus. But Catherine argues for reasoned conversations distinguishing between different DeFi types. Not every protocol needs circuit breakers, but some should consider mechanisms.

**Prediction Markets and the Ninth Circuit**

Catherine explains the prediction market litigation landscape. Designated Contract Markets (DCMs) are the exchanges themselves; Futures Commission Markets (FCMs) are intermediaries. The Ninth Circuit, one level below the Supreme Court, heard oral arguments from Kalshi (prediction markets) against Nevada's attempt to regulate them. Three Trump-appointed judges sounded openly skeptical of the CFTC's federal preemption argument—one judge said of a specific rule interpretation, "This can't be a serious argument."

Catherine notes that when judges ask pointed, leading questions, it signals they've already made up their minds about the ruling. Kalshi faces an uphill climb. The decision will take 60–120 days (sometimes six to 18 months) from the Ninth Circuit. If that court rules against prediction markets and another circuit rules for them, the Supreme Court is likely to take the case. Catherine predicts the Supreme Court will weigh in during 2027–2028.

**Paris Blockchain Week and Versailles**

Jesse shares that all three were at Paris Blockchain Week and attended a dinner at Versailles itself. They were escorted through the palace in black tie, given a private tour with period-costumed actors, and received champagne with a custom label while watching fireworks from a room next to the Hall of Mirrors. Jesse calls it an out-of-world experience, though disorienting given the hacks and user losses happening simultaneously in DeFi.

Catherine notes that while the event was beautiful and well-organized—all three praised the organizers—it highlighted the disconnect between celebrating DeFi's potential and grappling with its failures. The conference had strong European regulatory and institutional participation.

**Agentic Commerce: Lessons from Amex**

Jesse pivots to AI and agentic commerce. Amex just launched agentic commerce experiences where an AI agent can book United flights and charge your Amex card. If the agent books the wrong date, Amex covers the loss. This is called agent purchase protection. Delta, Expedia, Hilton, Stripe, and PayPal are all partners.

The key: Amex answered three hard questions in agentic commerce. First, identity—how do you know an agent is who it says it is? Amex built agent registration, giving each AI agent a tokenized credential. Second, mandate—how do you constrain what an agent can do? Book a flight is not the same as book the most expensive first-class flight. Amex built programmable guardrails. Third, accountability—when the agent screws up, who pays? Amex says: we will. And that accountability is what unlocks adoption.

Jesse argues this is the gap crypto hasn't closed. Blockchain should be leading here—it's agentic commerce's natural habitat. Smart contracts, composability, on-chain micropayments, and settlement without intermediaries make blockchains ideal for AI agents. But TradFi is racing ahead. Amex's guardrails live inside Amex's system; the liability framework is whatever Amex says it is and can change anytime. Crypto has the building blocks—agent wallets, on-chain micropayments, programmable spend limits—but composability is a double-edged sword. If one protocol is compromised, contagion spreads. The opportunity is now, but crypto needs to act.

**DeFi's Mirror Moment**

Catherine stresses that crypto should not only replicate Amex but build something programmable and durable, independent of terms-of-service changes. The architecture should be on-chain, cryptographic, and lasting. Crypto's real window is closing; Amex's solution works today.

V reflects on the broader moment: one day DeFi feels like the top of the world with institutions hiring crypto talent. The next day, there are exploits and offshore prediction market death markets. Good and bad mixed together. The industry is at a fork.

**Prediction Markets Aside**

Catherine appeared on a prediction markets panel at Eve Wealth, titled "Are Prediction Markets Gambling?" She will also speak on a prediction markets panel at Consensus.

**Robotics and Human Good News**

Jesse shares uplifting robotics stories. In China, after a high-rise fire, elderly residents couldn't retrieve belongings from top floors. Robotics with leg-like appendages helped them climb dozens of stairs to recover items that meant everything to them. In Europe, robots are chasing wild boars out of civilian neighborhoods. And robots recently won a half marathon. For all the fear around AI, real-world applications are touching lives positively.

**Chris Giancarlo and Intergenerational Innovation**

Catherine highlights Chris Giancarlo, former CFTC chair and known for innovation-oriented leadership, who interviewed his daughter—an oncology nurse practitioner with research in women's health—at Eve Wealth. They discussed intergenerational finance and the importance of talking to children about innovation in all forms. Catherine advocates teaching children about crypto and AI early, not so they live on screens but so they're armed to navigate a changing world. She also emphasizes educating across socioeconomic spectra. This kind of non-traditional conference programming, focusing on families and broader knowledge-sharing, is what the industry needs more of.
