---
podcast: Unchained
date: 2026-11-24
source_transcript: data/podcasts/transcripts/Unchained/2026-11-24_How_Pearl_Could_Turn_AI_Data_Centers_Into_a_Challenger_to_Bitcoin.md
---

# Unchained — "How Pearl Could Turn AI Data Centers Into a Challenger to Bitcoin"

**Host:** Laura Shin. **Guest:** Ryan Watkins (co-founder, Synchocy Capital; investor in Pearl; formerly OSR researcher; cryptocurrency and blockchain strategist).

## TL;DR

- **Bitcoin's security model is broken long-term** — mining rewards halve every four years, requiring Bitcoin's price to nearly double every four years to maintain miner incentives. At $1.5 trillion market cap, the asset cannot sustain 19% annualized growth indefinitely without either perpetual inflation (rejected by community), a functional fee market (hasn't developed), or government central-bank holdings (not cyberpunk). This creates a fundamental vulnerability.
- **Pearl solves Bitcoin's security problem with useful work** — instead of useless SHA-256 hashing, Pearl miners prove matrix multiplication (the core of AI inference). AI data centers can mine Pearl with near-zero incremental overhead, creating a security budget funded by the economic value of GPU computation rather than price appreciation alone.
- **Pearl Day could arrive before 2030** — Watkins' modeling shows that if 12.5% of projected global data-center capacity mines Pearl by 2030, Pearl's compute-energy footprint would surpass Bitcoin's, making it theoretically more secure. This feasible threshold could arrive in 3–5 years, reshuffling "monetary premium" value flows.
- **Early adoption starts with aligned operators, then broadens** — Pearl's mining progression: community believers and independent data centers (willing to accept high overhead) → serverless inference providers → hyper-rational AI clouds (mining solely for economics once overhead nears zero). Together AI ($8B valuation) adopted Pearl within weeks of mainnet, signaling real-world traction.
- **FP8 upgrade (January 2027) is critical** — expands GPU compatibility and enables "duplex miners" (entities mining Pearl *while* serving inference workloads), creating better unit economics than synthetic-only miners and shifting the network toward genuine useful work.
- **Pearl's tokenomics: hard supply cap (2.1 billion) and credible censorship resistance** — a 21M-unit Bitcoin equivalent with predictable halving schedule. Privacy via zero-knowledge cryptography and post-quantum resistance address gaps in Bitcoin's design. Pearl replicates Bitcoin's store-of-value attributes while solving long-term security-budget risk.
- **Pearl is not a business or competitor to AI platforms** — it's a cryptocurrency speculative asset bootstrapping GPU supply. Venice (privacy-wrapped AI) and Pearl are symbiotic, not rivals; Venice workloads could run on Pearl-mining data centers. Pearl's current 80% synthetic-mining phase reflects early-stage capital subsidizing network build-out.
- **Founding team has deep credibility** — Omri Weinstein (NVIDIA senior researcher), Elon Komar Goski (Chudnovsky Professor at some university, cryptography researcher), and Eden Sugarman derived Pearl from a 2025 academic paper; mainnet launched April 2026. Their connections in Silicon Valley and AI communities drive institutional adoption beyond crypto.

---

**Bitcoin's Long-Term Security Budget Crisis**

Watkins opens by positioning Pearl not as a price bet but as a hedge against Bitcoin's most fundamental vulnerability: its decaying security budget. Bitcoin's white paper envisioned "electronic cash" funded long-term by transaction fees. Early on, block rewards (newly minted Bitcoin) subsidized miners, but the protocol halves rewards every four years. Watkins argues that no meaningful fee market has emerged despite years of network activity. As a result, Bitcoin's entire security model rests on the assumption that price will rise perpetually—specifically, nearly 19% annually to offset each halving's reward cut. At $1.5 trillion, this becomes increasingly implausible.

The community has rejected the obvious alternatives: perpetual inflation contradicts Bitcoin's core value proposition (hard money), widespread transaction fees threaten its cash-system character (which Bitcoin abandoned for digital gold anyway), and expecting governments to hold Bitcoin on balance sheets and subsidize mining contradicts the decentralized ethos. Watkins does not claim Bitcoin will fail—he emphasizes the base case is Bitcoin figures it out. But he argues that if Bitcoin does not solve this, capital will flow to alternatives that do, creating the opportunity Pearl addresses.

**Pearl's Core Innovation: Useful Proof of Work**

Pearl replaces Bitcoin's useless SHA-256 hashing with matrix multiplication—the foundational operation of all AI inference. This is not a minor difference. When a GPU mines Pearl, it simultaneously proves the computation AND provides real inference capacity: a ChatGPT query, a coding agent, any neural-network workload. Bitcoin's ASIC hardware has zero utility outside mining; Pearl's GPU hardware drives a multi-trillion-dollar AI industry. This decoupling of mining from dedicated hardware is crucial to Pearl's thesis.

The key innovation is "near-zero incremental overhead." Today, running Pearl mining on an AI data center imposes overhead—compute cycles that could serve paying inference customers instead go to proof generation. Watkins stresses this overhead is *not* zero overnight; it's a progression. Pearl's team is aggressively optimizing the kernel (the low-level GPU program performing matrix multiplication) to lower this cost. Two technical achievements Watkins highlights are the Blackwell-optimized GEM implementation and PerlQuant, both evidence the team is making measurable progress. The FP8 upgrade (January 2027) will expand which GPU architectures can mine Pearl, significantly broadening the pool of data centers that can participate.

The economic logic is brutal: once overhead drops low enough, an AI cloud choosing *not* to mine Pearl is leaving money on the table. At that point, adoption shifts from ideological alignment to rational economic self-interest. Early adopters—independent operators, Silicon Valley-connected neoclouds—accept higher overhead to build a position. As overhead falls, hyper-rational operators with no particular loyalty to Pearl are forced to mine or lose competitive position (because competitors mine and pass savings to customers). This ratcheting dynamic is Pearl's adoption engine.

**The Path to Pearl Day and Compute-Energy Parity**

Watkins projects "Pearl Day"—when Pearl's compute-energy footprint surpasses Bitcoin's—could arrive before 2030. This is the most bold and controversial claim. He frames it in terms of energy rather than raw hash rate because Pearl's hash function (matrix multiplication) is not directly comparable to Bitcoin's SHA-256; normalizing to energy expended permits apples-to-apples comparison of network security.

His model estimates 12.5% of projected 2030 global AI data-center capacity would need to mine Pearl to exceed Bitcoin's energy consumption. This is *not* a fringe assumption; it reflects infrastructure buildout already underway. The fact that the threshold is achievable without moonshot premises is what shifted Watkins from skepticism to conviction. He also notes that Bitcoin miners, many of whom are pivoting to AI cloud operations, retain mining DNA and familiarity with crypto. If Pearl's overhead falls low enough, recruiting them is plausible.

Watkins explicitly *does not* claim Pearl will flip Bitcoin's price in three to five years. P-Day is about compute-energy parity, not market cap. He argues that reaching compute-energy parity would likely trigger repricing (a Pearl holder's confidence would rise if the network provably secured as much compute as Bitcoin) and potentially encourage Bitcoin developers to respond. He also emphasizes this is a multi-cycle, multi-year thesis—not a speculative cycle play.

**Adoption Trajectory and Duplex Mining**

The network's progression is strategic. Today, ~80% of Pearl's GPUs mine synthetically—performing matrix multiplication to no end, purely to generate proofs and earn mining rewards. No real inference workload is served. This phase subsidizes network bootstrap and attracts aligned capital. The upcoming FP8 upgrade will enable "duplex miners": operators simultaneously serving real inference workloads *and* mining Pearl. Game-theoretically, duplex miners have superior unit economics (dual revenue streams) and will eventually outcompete pure synthetic miners as network overhead falls. This creates a forcing function: either serve real customers or get priced out.

Watkins projects adoption will begin with serverless inference providers and independent data centers (willing to tolerate high overhead for early positioning), then broaden to larger neoclouds as overhead drops. Eventually, indifferent cloud operators will adopt Pearl not for ideology but to match competitors. The fact that Together AI (a $8 billion valuation AI cloud) added Pearl support within weeks of mainnet demonstrates that Pearl's team has real relationships in the AI space outside crypto.

**Tokenomics and Store-of-Value Attributes**

Watkins is careful to distance Pearl's value proposition from tokenomics gimmicks. Many crypto projects claim novel "tokenomic structures" generate demand; Watkins argues this is cargo-cult economics. What makes Bitcoin a store of value is not its token supply curve but its attributes: cheap verification (a user with a laptop can fully verify Bitcoin), censorship resistance (high hash rate makes 51% attacks prohibitively costly), immutability, and the credible expectation of these properties persisting into perpetuity.

Pearl replicates these attributes: a 2.1-billion-unit hard cap (100x Bitcoin's 21M-unit cap, but a unit distinction only), predictable halving schedule, cheap light-client verification, and planned privacy features (zero-knowledge cryptography) that Bitcoin lacks. Pearl's censorship resistance is *different* than Bitcoin's—GPUs have residual value outside Pearl (for AI inference), whereas ASICs have zero value outside Bitcoin. But Watkins argues that at scale, Pearl mining becomes a meaningful portion of GPU economics (perhaps 5–10%), creating a financial incentive to defend the network against attacks similar to Bitcoin's.

The core value proposition is that Pearl solves Bitcoin's long-term security-budget problem. If Pearl achieves sufficient hash rate and maintains that through dual utility (useful computation), it offers a credible long-term store of value—a hedge against Bitcoin failing to address its core vulnerability.

**Counterarguments and Risk Assessment: 51% Attacks and Fair-Launch Critique**

Critics have raised two main objections. First, the 51% attack surface: Bitcoin's ASICs are worthless outside mining, so attacking Bitcoin destroys the attacker's hardware value as well. Pearl's GPUs retain value for AI inference, creating superficial asymmetry. Watkins counters that the actual attack incentive is proportional to the future block-reward stream, which is true for both systems. Early on, Pearl mining is a small fraction of GPU economics, so the attack incentive is negligible. At scale, if Pearl becomes 5–10% of GPU value, the financial disincentive grows proportionally. Renting GPUs for a 51% attack faces legal barriers (hyperscaler contracts prohibit arbitrary workload reassignment) and fuzzy motivation (why attack a network that makes you money?).

Second, critics (including researcher "Zero Knowledge" at a1 Research, October 2026) flagged that Pearl raised $55M+ in equity from Lightspeed and Ribbit, plus $75M for the team's own GPU array. The comparison point was Venice, which locked investor tokens and burned revenue; Pearl locked neither. Watkins rejects the comparison: Pearl Research is not a business extracting value—it's a cryptocurrency project. Pearl holders (community and early investors alike) do not get enterprise revenue; they hold an asset, like Bitcoin holders. Insider ownership (team + early investors ~5% of supply) matches Satoshi's holdings and is below Zcash's 20% founder reward. Watkins notes there is no such thing as a "fair launch" post-Bitcoin; every crypto project attracts speculative capital with expectations of gains.

**Pearl vs. Bitcoin: Long-Term Dynamics**

Watkins is asked what happens to Bitcoin if Pearl Day arrives and Pearl's hash rate surpasses Bitcoin's. He resists claiming Bitcoin becomes worthless. Bitcoin has 17 years of proven network security; a competitor needs to earn that same credibility. Even in a highly bullish Pearl scenario, Bitcoin likely remains a top-tier asset for years—the "monetary religion" around Bitcoin takes decades to shift. But Watkins does see a scenario in which slowly, over 10–15 years, if Bitcoin fails to address quantum, privacy, and long-term security issues while Pearl succeeds in recruiting critical GPU mass, capital gradually flows to Pearl. This would not be a catastrophic flip but a gradual reshuffling of "monetary premium" in the crypto asset class.

He emphasizes Pearl is a *venture bet* on this uncertainty—not an assertion that Pearl definitely flips Bitcoin. The base case remains Bitcoin solves its problems. But the base case also had non-trivial probability prior to Pearl's elegant solution, and Pearl's existence changes that calculation. For Watkins, the investment thesis is that if Bitcoin stumbles, Pearl is well-positioned to capture that value.

**Future Development and Current Limitations**

Pearl is currently a pure store-of-value play. It has no built-in utility beyond its speculative/monetary premium. This is intentional and appropriate for the bootstrap phase. Watkins envisions long-term expansion: Pearl Polymath (the research roadmap) suggests future upgrades to prove training and fine-tuning workloads, not just inference. If Pearl can prove arbitrary AI computation, it becomes a verifiable ledger of all compute transactions—a historical record. This foundation could support secondary markets (compute marketplaces) or verification use cases (proving an inference workload was performed as specified). But Watkins is clear: these are future possibilities, not current features. The immediate focus is getting GPU overhead low enough for real data centers to mine at scale.

The FP8 upgrade (January 2027) is the gating item. It expands GPU compatibility, enabling duplex mining and shifting more of the network toward genuinely useful work. Beyond that, Pearl's team could expand GPU support to TPUs and other accelerators, further broadening adoption surface. Watkins stresses he is not focused on near-term token utility; he is focused on the prerequisite: getting the supply side online.

**Watkins' Conviction and Investment Rationale**

Watkins' essay and investment in Pearl stem from two converging signals. First, Zcash's second rally (2024–2025) demonstrated market demand for alternatives to Bitcoin rather than pure speculation. Second, repeated peer interest and institutional momentum (Lightspeed, Ribbit backing) flagged Pearl as credible. When he dug in and realized Pearl actually *solved* Bitcoin's long-term security problem—a gap he had long assumed was unsolvable—he committed. This is not a price-speculation bet; it is a venture thesis on whether useful proof-of-work can achieve scale and thereby become a credible hedge against Bitcoin's structural vulnerability.

