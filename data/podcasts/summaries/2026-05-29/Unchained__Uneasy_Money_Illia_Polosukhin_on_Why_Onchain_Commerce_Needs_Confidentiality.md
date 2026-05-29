---
podcast: Unchained
date: 2026-05-29
source_transcript: data/podcasts/transcripts/Unchained/2026-05-29_Uneasy_Money_Illia_Polosukhin_on_Why_Onchain_Commerce_Needs_Confidentiality.md
---

# Unchained — "Uneasy Money: Illia Polosukhin on Why Onchain Commerce Needs Confidentiality"

**Host:** Laura Shin (extract exact host from transcript intro). **Guests:** Illia Polosukhin (co-founder, NEAR Protocol; co-author, "Attention Is All You Need," the foundational transformer paper that enabled modern LLMs).

## TL;DR

- **Confidentiality is the unlock for mainstream onchain commerce** — Businesses cannot operate on public blockchains where competitors and suppliers can see revenue, costs, and salaries via block explorers; NEAR's confidential intents solve this with execution confidentiality, enabling stablecoins and fiat payments in 600ms block times.
- **150+ assets now in confidential intents** — Including several million USDC, 8 million NEAR, and multiple million Zcash; the system runs a full, private NEAR shard with intent-based infrastructure for privacy-preserving transactions.
- **Privacy requires active crime prevention, not neutrality** — NEAR deployed Shield, an AI anomaly-detection system that scans transactions in real time, flags illicit activity, and alerts exchanges and partners without revealing underlying identities; this defends against money launderers while maintaining privacy.
- **Litecoin's Mimble Wimble vulnerability shows governance failure** — Core developers found a critical flaw two months before launch, patched only miners without warning exchanges or bridges, leading to a double-spend attack that exploited both Mimble Wimble bug + DDoS attack; this exposed the importance of coordinated incident response.
- **Decentralization is a tool, not a goal** — Polosukhin argues that "don't be evil" and "smaller EF" are non-goals; what matters is building a flourishing decentralized ecosystem with clear incentives, redundancy, and cooperation—not disorganization; NEAR's model uses shared infrastructure (HR, finance) + market principles to align incentives.
- **Ethereum Foundation faces a crisis of purpose** — Multiple employees leaving, no clear mission beyond "smaller" and "don't be evil"; Polosukhin sees the EF's job as organizing and enabling builders, not doing the work itself—similar to how Google or a local municipality provides services and frameworks.
- **AI agents and blockchain enable p2p markets** — NEAR AI Marketplace tests disaggregated work: individuals package expertise into agent workflows and offer them on a marketplace where quality is verified by AI judges and escrow; this replaces traditional corporate functions (e.g., insurance claim filing, background checks) with trustless transactions.
- **Credit assignment is the fundamental organizational problem** — Whether in gradient descent or in hierarchies, knowing who contributed what is hard; AI and blockchain (intent-based, verifiable execution) make credit assignment feasible, unlocking DAOs and distributed organizations where incentives are transparent and merit-driven.

---

**The Transformer Paper Origin and NEAR's AI Roots**

Polosukhin explains that he has been interested in AI and AGI since childhood, building his first neural network at age 14. At Google, he worked on question-answering systems and recognized that recurrent neural networks (RNNs) had a fundamental bottleneck: they process language one word at a time, maintaining only about 100–1,000 floats of context. For a search engine expecting 200-millisecond response times, reading the entire internet sequentially was impossible.

The transformer architecture solved this by removing the recurrence and leveraging GPU parallelism. Instead of reading one word at a time, transformers process the entire input (a full Wikipedia page or search results) in parallel, using the attention mechanism to focus on relevant context. A team of eight people spent six to seven months bringing this to production state-of-the-art. Polosukhin emphasizes that this foundational breakthrough came not from a new mechanism alone, but from recognizing that machines are highly parallel and rethinking the entire approach.

NEAR itself started as an AI company. Polosukhin and his team explored using AI to write smart contracts correctly (not break them). They saw blockchain as a natural application for this work and eventually launched NEAR as a scalable, user-friendly blockchain with WebAssembly and account abstraction—features Ethereum had discussed but not shipped.

**Intents and Cross-Chain Communication**

The core of NEAR's intent system is enabling cross-chain control of assets. In conversations with Ken (the host) two years prior, Polosukhin described intents as confusing "gobbledygook"; Ken later realized Polosukhin had been explaining how intents allow one chain to control another. The initial product-market fit was enabling Bitcoin and Dogecoin holders to trade without central exchanges—especially important for assets like Zcash, which were being delisted.

Intents scale beyond single-chain trading. NEAR can now run complex logic on its own chain and push only the execution onto other chains (Solana, for example). This solves Solana's constraint of small contract size and low runtime capacity by offloading heavy computation to NEAR while executing lean transactions on Solana itself.

**Confidential Intents and Privacy for Business**

In 2022, NEAR built a private shard using confidential execution but shelved it due to regulatory uncertainty. Now, with broader market acceptance of privacy and clearer regulatory positioning, NEAR has launched confidential intents—a private shard running full NEAR features with intent-based infrastructure. The system supports 150+ assets, all of which can be private by default. Current holdings include several million USDC, 8 million NEAR, and several million Zcash.

The motivation is clear: no business can operate on a public blockchain where suppliers, competitors, and customers see all financial flows. Even a Zcash-friendly merchant using confidential intents can accept Zcash, cross-pay through NEAR's system, and have the transaction settled to Bitcoin or stablecoins without the merchant knowing the source—maintaining both privacy and regulatory clarity. Block times are 600 milliseconds, allowing near-real-time settlement with fiat coming soon.

**Crime Prevention Through Active Defense**

A critical tension is that confidentiality enables both legitimate privacy and money laundering. NEAR took an explicit stance: privacy protocols that become havens for criminals serve neither legitimate users nor the broader vision of onchain commerce at scale. NEAR deployed Shield, an AI system that scans other blockchains and intents transactions in real time using anomaly detection. If an account suddenly receives $100 million with no historical balance, that is flagged as suspicious. NEAR's detection actually identified a Litecoin Mimble Wimble vulnerability before it was exploited.

Taylor Monahan (co-host and security expert) emphasized the importance of not letting criminals dominate a protocol's user base and feedback loop. Thieves and money launderers have different needs than legitimate users—they do not care about UX, user experience details, or long-term product-market fit. If a protocol optimizes for criminals first, it shapes all downstream features in the wrong direction. NEAR chose to build tools for legitimate commerce, which required active crime prevention as a core feature.

Shield also operates as an information network. Partners (exchanges, bridges, other chains) can subscribe to advisories of varying severity without NEAR revealing underlying identities. NEAR uses Bloom filters and cryptography to allow partners to check deposits against suspicious address hashes without exposing the underlying data.

**Litecoin's Disclosure Failure and Incident Response**

An example of what not to do came from Litecoin's handling of a critical Mimble Wimble vulnerability. Litecoin core developers discovered it themselves, patched it, and sent it to miners two months before disclosure. They did not warn exchanges, bridges (like ThorChain), or NEAR—only the miners. The old protocol version had the Mimble Wimble bug; the new version introduced a DDoS vulnerability as a side effect. An attacker exploited this window by withdrawing fake money from the privacy pool (not even double-spending, but withdrawal of funds they did not possess), then DDoSed the network to keep only old nodes online, and attempted to withdraw the stolen funds across exchanges.

This incident exposed the danger of privileged disclosure. In the age of AI finding vulnerabilities alongside humans, a two-month lead time becomes a zero-day in disguise. The real failure was not warning all parties who could be potential off-ramps. NEAR's approach, by contrast, includes an information network and rapid incident response—multiple organizations working together to detect, contain, and recover from incidents.

**Decentralization as a Tool, Not an Ideology**

A broader argument emerges: decentralization is not itself a goal. It is a tool that enables redundancy, resilience, and preventing single points of failure. NEAR's ecosystem includes dozens of companies working in close coordination, with shared communication infrastructure (Slack connects across organizations). When NEAR had a hack (the Ria incident), five companies coordinated, traced the attacker, gathered forensic evidence, and recovered funds. This happened because leadership could organize response and teams had incentive alignment.

Polosukhin critiques the Ethereum Foundation's framing of its role. Vitalik recently posted a 1,500-word thread on X arguing for a smaller EF, citing "don't be evil" and decentralization as values. But these are non-goals. "Don't be evil" is a constraint, not a strategy. The goal should be a flourishing decentralized ecosystem of builders with clear incentives—not an EF that stays small by staying uninvolved. Polosukhin pitched the EF multiple times to build sharding, WebAssembly, and account abstraction as features. The EF's response: "We're not paying you anything for this; you get no upside." The EF is well-funded and can afford to organize, but instead retreats into neutrality, refusing to tweet about product builders or have favorites, leading to neglect of the very ecosystem it should be cultivating.

Compare this to Google, which has organizational structure, incentive alignment, and clear missions despite internal complexity. Or a municipality with fire departments, police, courts, and municipal services all working together. The function of leadership is not to do everything yourself; it is to set a vision, align incentives, and provide a framework within which others can execute.

**AI, Blockchain, and Organizational Markets**

Looking ahead, Polosukhin sees a shift from corporations and foundations holding people to organizations operating on market principles. AI makes credit assignment tractable—you can now estimate how much an individual's contribution affected the organization's bottom line. Simultaneously, each individual becomes more productive, able to work on multiple projects.

NEAR's Ironclaw system (mentioned briefly) supports multi-tenant operation and experiment with a commitment system: when you agree to ship a feature in a meeting, it automatically creates a task, surfaces it to the team, and updates documentation. Workflows scan meeting notes to extract decisions made and decisions not made (where organizations leak value through indecision).

The endgame is a NEAR AI Marketplace where individuals package expertise into agent workflows (e.g., insurance claim filing, background checks) and offer them for a price. Quality is verified by AI judges, escrow is handled onchain, and humans loop in for taste and final judgment. This disaggregates work that traditionally required a corporate function (five employees doing insurance claims manually) into a trustless marketplace where a single expert can codify a workflow and offer it as a service, paid per use.

**Credit Assignment and the Future of DAOs**

Polosukhin's core thesis is that credit assignment is the fundamental organizational problem. In gradient descent, the optimization is about assigning credit to each weight in the network. In organizations, it is about knowing who contributed what. When you cannot assign credit, hierarchies become necessary: you bundle people together and promote the bundle collectively. But with AI and blockchain (intent-based, verifiable execution), credit assignment becomes feasible.

This unlocks true DAOs. Current DAOs fail because they lack the infrastructure to track who did what and why. With AI-assisted credit assignment and onchain intent execution with verification, you can have a truly distributed organization where each person's contribution is traceable, their incentives are transparent, and they can move freely between projects without losing upside. This is where AI and blockchain fit together most naturally.

