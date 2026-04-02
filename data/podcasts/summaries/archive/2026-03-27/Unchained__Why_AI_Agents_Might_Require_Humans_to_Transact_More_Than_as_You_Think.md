---
podcast: Unchained
date: 2026-03-27
source_transcript: data/podcasts/transcripts/Unchained/2026-03-27_Why_AI_Agents_Might_Require_Humans_to_Transact_More_Than_as_You_Think.md
---

# Unchained — "Why AI Agents Might Require Humans to Transact More Than as You Think"

**Host:** Laura Shin. **Guests:** Noah Levine (partner, a16z); Robbie Peterson (junior partner, Dragonfly).

## TL;DR

- **Robbie argues 95%+ of agentic activity will be commercial agents** — deployed top-down within businesses, analogous to how 95%+ of software today runs in enterprises and governments, and most of these agents will automate without actually transacting.
- **"Headless merchants" are a new class of B2B commerce** — Noah's term for small, developer-built merchants that agents discover and pay on a per-transaction basis via protocols like X402 and MPP, without ever visiting a website or signing a subscription.
- **Stablecoins win for micro-transactions and permissionless experimentation; cards win everywhere else** — Noah paid 30–40 cents in stablecoins via X402 to pull data from Allium for a report; traditional card networks retain the advantage for consumer-facing, higher-value purchases due to chargeback protection and customer familiarity.
- **Card networks and blockchains are each insufficient in different ways** — cards have solved risk-scoring and fraud authentication but lack instant settlement; blockchains offer real-time global settlement but have built no equivalent fraud-scoring layer, creating a potential opening for chain-based systems to build new agent-specific risk graphs.
- **The real bottleneck to agentic commerce adoption is not the payment rails** — Robbie identifies human trust/behavioral inertia, bureaucratic resistance inside organizations, government adoption timelines, and legal/regulatory structures as the primary obstacles. Noah adds that discoverability — how agents find and vet thousands of new headless endpoints — is the unsolved problem on the merchant side.
- **Robbie's "Fat Wallet Thesis" holds that whoever owns the end user captures the most value** — he argues agents won't abstract away trading interfaces because preferences are revealed in the act of browsing and chart-reading, not just stated upfront. Noah counters that AI is making the front end increasingly modular while the back end becomes the defensible asset.
- **Tempo is the early front-runner for agentic settlement infrastructure** — Stripe's merchant distribution via MPP plus key partners gives it a head start, though Stripe also integrated X402 before the MPP announcement, leaving the final winner unclear.

---

**Three Types of Agents and the Scope of Agentic Commerce**

Robbie frames agentic activity in three categories. Commercial agents are deployed within businesses to automate internal workflows — a Salesforce agent doing sales outreach, or a finance agent handling back-office functions — and represent 95% or more of all near-term agentic activity. Consumer agents assist individuals with tasks like research and recommendation but, in Robbie's view, stop short of autonomous purchasing because consumer preferences are not static: they emerge through the process of discovery itself. Someone asking an agent to book a Tokyo trip will want to see hotel photos, read reviews, and weigh tradeoffs that the agent cannot fully anticipate. The third category, which Robbie calls "bottom-up agents," are genuinely autonomous, procuring their own resources and potentially interfacing with other agents. These were catalyzed by the emergence of coding agents like Claude Code and what participants repeatedly call the "OpenClaw phenomenon."

Noah broadly agrees on direction but is more optimistic about the pace at which humans will grow comfortable delegating to agents. He draws a parallel to early internet adoption, where initial fears about data security gave way to widespread trust as guardrails improved. The key distinction he emphasizes is that even if an agent is doing the research, it is often still the human who authorizes the final transaction — a pattern he describes as functionally similar to an Apple Pay tap.

**Headless Merchants and the New Developer Economy**

Noah's central thesis is that the rise of coding platforms has created a large new class of developers who need services on a project-by-project basis — a domain name, a server, a proprietary data pull — and currently must leave their terminal to acquire them. He coins the term "headless merchants" for the small, vibe-coded services springing up to serve these developers: a couple of people standing up an API endpoint in a day or two, discoverable and payable per transaction through protocols like X402. His own report-building session, where he paid 30–40 cents to an Allium X402 server for data without needing an account, is his concrete illustration of this model.

This new merchant class is unlikely to be underwritten by traditional payment processors, which is where stablecoins function as the digital equivalent of cash — accessible to the street vendor who cannot accept cards. Noah notes that creative services, image generation, and music tools are early examples, but he expects the category to expand broadly into developer infrastructure.

**Stablecoins vs. Cards: Different Lanes, Not a Zero-Sum Race**

Both guests see stablecoins and card networks coexisting in distinct segments rather than competing directly. Robbie points to a historical parallel: stablecoin-linked cards became the preferred form for consumer-to-merchant payments because of the Lindy effect — consumers have used cards for decades, merchants have accepted them for decades, and that inertia is powerful. The same dynamic favors cards for traditional agentic commerce use cases: booking flights, purchasing consumer goods, any transaction where the user wants fraud protection, chargebacks, and points.

Where cards fall short is in servicing the permissionless, nascent headless-merchant layer. Traditional acquirers cannot easily underwrite a two-person company that stood up an API yesterday. Stablecoins fill that gap. Robbie observes that another reason blockchains win for bottom-up agents is structural rather than technical: blockchain protocols have no shareholders, no institutional counterparties, and no regulatory exposure that would force them to decline risk. Visa and Mastercard simply cannot take the same chances.

**The Fraud Problem and Why Agents Change It**

Robbie identifies a subtle but important gap in the card-network advantage. Card networks have spent years building fraud graphs and risk-scoring models calibrated to human behavioral patterns — idiosyncratic transaction sequences that reveal a person's identity and habits. An agent's behavioral fingerprint looks fundamentally different from a human's. Robbie raises the open question of whether agents will require entirely new fraud-scoring infrastructure, and suggests this may actually be blockchain's wedge into higher-stakes agentic transactions: if no existing system has solved agent-specific risk scoring, a blockchain-native solution built from the ground up for machines could compete on ground where cards have no incumbent advantage.

Noah notes that for micro-transactions — fractions of a cent to a few cents — fraud is largely a non-issue. If an agent hits a bad endpoint and loses 30 cents, the loss is tolerable. Fraud concerns scale in importance with transaction size, which is precisely the segment where card networks are already positioned.

**Competing Payment Protocols**

Laura describes the main standards in play. MPP (Merchant Payments Protocol), developed by Stripe and Tempo, introduces a "sessions" construct — analogous to opening a tab at a bar — that sets a spending budget for a run rather than requiring a separate transaction for each API call. It currently settles only on Tempo, requires Stripe, and connects to traditional card rails; LightSpark (a Bitcoin Lightning company) is also integrated. The developers say it will eventually become chain-agnostic. X402, an open standard from Coinbase, is fully permissionless, supports any ERC-20 token, is gasless for users, but has no sessions layer — every request is a discrete payment. Visa's CLI is a card-default wallet that can be downloaded into coding agents and comes pre-loaded with a directory of endpoints. Google's Agent Payments Protocol (AP2) was also noted.

Noah is optimistic on both X402 and MPP. MPP's advantage is distribution: existing Stripe merchants can enable agentic payments with a button click. X402 demands more bespoke integration. He notes that Stripe integrated X402 before announcing MPP, so the interplay between them remains unresolved. His broader point is that the rails question is largely solved — the open problem is on the merchant side: who builds compelling services worth paying for?

**Value Capture and the Fat Wallet Debate**

Robbie returns to a thesis he wrote roughly two years ago: whoever owns the end user captures the most value, a pattern consistent across every major technology cycle. He argues this will hold in crypto and agentic commerce alike — specifically, he does not believe agents will abstract away trading interfaces, because chart-reading and browsing are themselves the process by which preferences form. He also frames value capture as a barbell: whoever owns the end user on one side, and whoever owns the settlement layer on the other. He identifies Tempo as the current front-runner on the settlement side, given its Stripe merchant distribution and strategic partner mix.

Noah pushes back with a structural observation: AI is decoupling front ends from back ends more aggressively than any prior technology. In crypto, a user can export their private keys and import them into a new wallet — same back end, entirely different interface. The same dynamic is emerging in AI products: the back end is increasingly static and hard to replicate, while front ends become modular and cheap to build. His implication is that competitive moats will increasingly live in back-end infrastructure and unique data, while the front-end layer remains fluid.
