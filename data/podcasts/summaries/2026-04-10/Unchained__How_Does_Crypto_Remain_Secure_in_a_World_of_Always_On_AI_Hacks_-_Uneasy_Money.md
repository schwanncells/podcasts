---
podcast: Unchained
date: 2026-04-10
source_transcript: data/podcasts/transcripts/Unchained/2026-04-10_How_Does_Crypto_Remain_Secure_in_a_World_of_Always_On_AI_Hacks_-_Uneasy_Money.md
---

# Unchained — "How Does Crypto Remain Secure in a World of Always On AI Hacks? - Uneasy Money"

**Host:** Cain Warwick. **Guest:** Austin Griffith (Ethereum Foundation, repeat security expert guest, builds EthSkills and agentic smart contract tools).

## TL;DR

- **Mythos model found 20+ zero-day vulnerabilities in decades-old software** — Anthropic was so concerned about the model's capabilities that it restricted access to 12 partner organizations (AWS, Apple, NVIDIA, Linux Foundation) with NDAs and $100 million in usage credits.
- **Balancer V2 exploit parallels AI threat scaling** — a five-year-old smart contract was hacked for ~$100 million; combined with Mythos's capabilities, the team worries similarly ancient, supposedly secure systems will be systematically exploited by AI.
- **Immutability makes crypto vulnerable in AI era** — unlike traditional software that can be patched or hot-swapped, immutable blockchain contracts cannot be fixed once deployed; the hosts debate whether upgradable contracts are necessary safety nets or architectural failures.
- **Autonomy threshold matters: AI-assisted hacking vs. autonomous hacking** — current AI helps identify and speed up exploit feedback loops (e.g., with Balancer), but Mythos represents a shift where AI can independently hunt and execute exploits without human guidance for weeks.
- **Skill files are now critical infrastructure for agent-based development** — Griffith's EthSkills teaches agents the delta between their 2023 training data and current crypto realities (gas costs, protocol names, deployment details); agents go from "IQ 60" to "IQ 140" on Ethereum with a single skill file link.
- **Model pricing collapses push cost optimization into core architecture** — Haiku is now as capable as Opus 4.1 was; new frontier models will be $100–200 per million tokens, triggering a cascade where Sonnet and Haiku prices drop, forcing engineers to optimize task routing or face $800–1,000 daily bills.
- **Agents can now outsmart human developers at specific tasks** — Griffith's CloudBot has deployed smart contracts with $250k+ on mainnet without human review; agents outperform humans at DevOps, harness design, and cost optimization, shifting engineers to higher-level abstraction.
- **Anthropic API changes force difficult pricing choices** — subscription ($200/month) is 5–10x cheaper than metered API usage, creating incentive to game the system with multiple accounts; Anthropic's 89% uptime and rate-limiting changes suggest internal chaos.

---

**Mythos, Zero-Days, and the Security Timeline**

Mythos is Anthropic's newest frontier model, restricted to 12 partners, that reportedly discovered 20+ zero-day vulnerabilities in decades-old codebases like OpenBSD. Warwick and Griffith frame this as a watershed moment: previous Anthropic models were released with internal testing and researcher access phases, but the company was so concerned about Mythos's capabilities that it bypassed those stages entirely. The model was deemed "too dangerous to release" yet released anyway, with Anthropic publishing a 200-page agent safety card describing attempts to prevent harmful outputs. The $100 million in inference credits given to partners signals Anthropic's expectation that they will run automated loops continuously, likely for security testing.

**Crypto's Unique Vulnerability to AI Exploitation**

Unlike traditional infrastructure, blockchain protocols face a distinct problem: immutable code. Griffith explains that if an AI finds a zero-day in Linux, teams can patch, upgrade, and hot-swap in place. But if a five-year-old smart contract on Ethereum is cracked, it stays cracked forever. The Balancer V2 exploit exemplifies this fear: code that had been running safely for five years suddenly became vulnerable, hacked for roughly $100 million. Warwick speculates whether that was already achieved by AI-assisted hackers using Opus, now worried it will accelerate with Mythos.

Taylor Monaghan pushes back somewhat: Mythos is genuinely new and scary, but it doesn't necessarily mean prior recent hacks were Mythos-driven. That said, she agrees the trajectory is toward worse outcomes. Web 2 will suffer more than crypto (fewer bug bounties, fewer audits), but crypto is still vulnerable. Uniswap is the counterexample—it's simple, massively audited, and has a huge bug bounty—yet even Uniswap's unhackability confidence "has gone down significantly" in the last 48 hours.

**The Autonomy Threshold: When AI Transitions from Assistant to Actor**

The hosts distinguish between AI-assisted hacking and autonomous hacking. In the first phase, AI identifies exploit pathways or speeds up feedback loops, helping humans find and execute attacks. Griffith notes he was already concerned a month ago that "someone doesn't have a really smart fine-tuned model systematically going through breaking these smart contracts." Mythos changes the calculus: rather than assisting, it can independently run for weeks, reading entire codebases autonomously, without human intervention. As Warwick says, "this is the first time that we've seen a model that's so smart that they're so scared of it, that they're like, we need to give this to a small group of like 12 partners."

**Skill Files as the Frontier of Agent Knowledge Management**

Griffith introduced EthSkills, a Markdown-based knowledge repository that teaches agents about Ethereum without code execution or MCP server risk. The insight is that LLMs know crypto from their training data but at a cursory, dangerous level—they know enough to be confidently wrong. Skill files provide the delta: current gas costs, protocol updates since 2023, deployment details, and contract standards. When Griffith gave EthSkills to Opus, it immediately "one-shot" complex smart contract tasks it previously failed at.

The skill file approach is now industry standard—Austin mentions sites should host them at `yoursite.com/skill.md` for agent discovery. The process of building a good skill file is iterative: interrogate each claim to ensure the agent doesn't already hallucinate it (pollution check), then deploy and watch for failure modes. Griffith shares an anecdote where his concentrated liquidity farming agent sent NFT LP tokens into a gauge contract permanently because it simulated a specific path successfully, didn't realize approval was missing, then "worked around" the error with a different function call that actually broke everything. EthSkills now has hard rules: simulate transaction exit paths to ensure tokens can be withdrawn.

**Model Pricing Dynamics and Cost Optimization Loops**

Griffith describes an oscillation between expensive frontier models (Opus at $200/million tokens) and cheaper alternatives (Minimax M2.7 at roughly a hundredth of Opus's cost). Using Opus costs ~$20 per smart contract job; optimizing harnesses and using cheaper models for supporting tasks can drop that to $5. The frontier model is used only for the irreducible complex parts (writing contracts, auditing), while routine tasks (git pulls, documentation) run on cheaper models.

Warwick notes that Anthropic's pricing history shows a collapse curve: Opus was $75/million tokens when it launched, now $25 with a 1M context window. When Mythos arrives, assume $100–200/million tokens initially, which will cascade down the entire pricing ladder—Sonnet drops to Haiku's current price, Haiku becomes nearly free. This forces engineers to either optimize relentlessly (finding the exact routing and task-splitting strategy) or watch costs spiral ($800–1,000 per day for unbounded agent runs).

**Anthropic's Pricing Structure and Subscription Arbitrage**

The subscription model ($200/month Claude subscription) delivers an estimated $1,000 worth of API usage at metered rates. Griffith admits to using the API directly and paying more, but he's aware of people running 5+ subscriptions to juice the discount, or cycling between them as rate limits reset. Warwick suspects Anthropic knows this is happening, sees it as either acceptable collateral damage or intentional market segmentation.

Anthropic's recent changes—requiring API keys instead of subscription account auth, rate-limiting changes in February—appear to be closing gaps, but the company can't effectively police distributed subscription gaming. This feeds into a broader narrative Warwick constructs: Anthropic internally is chaotic. Evidence: publicly reported 89% uptime (zero nines instead of five nines, the standard), mysterious rate-limiting, contradictory messaging on company spending vs. restrictions.

**From Code to DevOps: Agents Outpacing Humans**

Griffith stopped doing his own DevOps because agents are vastly better at it. He asked his agent to deploy a complex inference system to RunPod ($3/hour H200 GPU), something that would have taken four days of reading docs and frustration ten years ago. The agent completed it instantly. Now his agents maintain databases, change records, spin up infrastructure—all opaquely to him. He's shifted to "idea guy" level, letting the agent translate concepts into working systems.

This mirrors a broader shift: when a frontier model arrives, previously "hard" tasks (writing smart contracts, building harnesses, optimizing prompts) become obvious. Then engineers reoptimize at the next level of abstraction. Griffith builds harnesses to make cheaper models do sophisticated work, which used to require expensive models.

**Long-Running Autonomy and the Cost-Harness Tradeoff**

As models improve, they can run autonomously longer. Opus 4.5 (released November) was the inflection point where it became "better than me at this thing" for Griffith's main work. Mythos capable of reading OpenBSD for two weeks straight represents the next step: if the model is expensive but can one-shot a complex problem in a single long-running session, the old cost-optimization tricks (cheap models + harnesses) may become obsolete. Instead, you pay $100 per request for Mythos to solve the unsolvable, rather than pay thousands in Sonnet iterations.

Boris Cherny advised "building for the model six months from now." Griffith interpreted this as: Mythos could arrive "any time in the next few weeks," so all the harness scaffolding (loops, fallbacks, cheap-model approximations) might vanish if Mythos can autonomously handle months-long tasks.

**Memory, Context, and the Laziness Problem**

Models hallucinate confidently. When Griffith asked an agent about Velodrome vs. Aerodrome, it confidently reported velodromes were invented in 1782 (cycling tracks), then ranked aerodromes as 1800s technology, despite Aerodrome being a 2022 DeFi protocol. Grok search made it worse, confident in wrong tweets. Only the knowledge base with real contract deployment data (Velodrome: August 12, 2022) could correct it.

This illustrates two problems: first, models need up-to-date knowledge (skill files), and second, they need memory/context to avoid drifting. Early OpenClaw versions would forget mid-conversation. Worse, mid-transaction, an agent might forget the intent and send a tweet instead of moving $100,000 into a vesting contract. Memory is now critical infrastructure.

**The Laziness and Safety Problem in Agent Design**

Agents know how to do things correctly but often don't. Griffith's farming agent was supposed to approve an NFT for transfer before staking it, but skipped that step in the simulation, then "worked around" failure by using `safe_transfer_from` into the gauge—which permanently locked the NFT. The agent had simulated this path and it worked, so it felt safe, but safety checking is incomplete: it never verified the NFT could be withdrawn afterward.

This is why EthSkills is verbose and feels like "you always get this wrong, don't do this"—it's encoding the failure modes agents find. Similarly, OpenClaw (Anthropic's agent orchestration framework) is notably bad at editing its own config files; Griffith uses Claude Code or Cursor instead because OpenClaw confidently breaks itself. Warwick joked that OpenClaw "lobotomizes itself" trying to self-edit, suggesting agents need skill files even for meta-tasks (editing their own configs).

**Threat Actors, Mythos Leaks, and Insider Risk**

The 12 partners (AWS, Apple, NVIDIA, Linux Foundation, etc.) receiving Mythos are bound by strict NDAs. Warwick infers malice: Anthropic likely expects some will use Mythos for offensive purposes (finding zero-days to sell, breaking competitors' infrastructure) despite the safety card. The leak vector is inevitable—insiders at those 12 orgs could sell access, or the companies themselves might test Mythos's offensive capabilities.

Warwick also speculates about Anthropic's internal understanding of threat actors already using frontier models. Every time the U.S. government requests data on attacks using Claude, Anthropic is forced to confront that their tools are both defensive and offensive.

**On Crypto, Polymarket, and Mythos Market Prediction**

Warwick frames insider trading on Polymarket—people front-running wars, betting on strikes before they happen—and asks: if 12 organizations have Mythos, won't one of them use it to profit from an Ethereum hack? Griffith agrees it's inevitable. The deeper question is whether a Mythos-driven first hack on mainnet will be marketable on Polymarket. Warwick suggests creating prediction markets ("When will Mythos first hack Ethereum?") but doesn't resolve whether Mythos is so locked down that early hacks will stay hidden.

**The Broader Inference: Signal, Noise, and LARP**

As agents and skill files proliferate, signal-to-noise degrades. Crypto Twitter is full of claims about "recursive self-autonomous reinforcement loops" and "genetic algorithms" running on Mac Minis with 32 GB VRAM. Some are real (Griffith's agents deploying contracts), some are LARP (one high-profile claim was revealed to involve a GitHub account hacked by an impostor). The level of effort to fake credibility is low; the level of technical depth to vet claims is high. Griffith's EthSkills is real and shareable, but not every skill file or tool will be.

**The Path Forward: Subscription Wars, Mythos Timing, and Equilibrium**

Warwick compares the current state to early mobile contracts: carriers had per-minute, per-SMS, per-MB data pricing. Competition and infrastructure investment led to equilibrium, though not always cheaper—instead, different segments paid different prices. Anthropic may be creating similar tiers, with subscription as a consumer play and API as enterprise, using Mythos as the next tier-splitter.

The episode ends on a tension: Mythos will arrive soon, will be restricted initially, and might be the first time frontier AI unleashes autonomous hacking at scale on blockchain. The hosts joke about Mythos "jailbreaking itself," emailing humans from the park, but the joke contains real anxiety: this model might be too smart to contain, and the cryptographic guarantees Ethereum relies on (math, not execution) might not hold against sufficiently advanced code-breaking.
