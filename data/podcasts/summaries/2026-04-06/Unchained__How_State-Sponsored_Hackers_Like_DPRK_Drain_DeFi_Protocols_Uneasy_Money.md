---
podcast: Unchained
date: 2026-04-06
source_transcript: data/podcasts/transcripts/Unchained/2026-04-06_How_State-Sponsored_Hackers_Like_DPRK_Drain_DeFi_Protocols_Uneasy_Money.md
---

# Uneasy Money — "How State-Sponsored Hackers Like DPRK Drain DeFi Protocols"

**Host:** Cain Warwick (host, Uneasy Money; crypto founder). **Guests:** Taylor Monahan (security expert; core member of SEAL 911; known for crypto incident response and DPRK malware research); Luca Netz (founder, Pudgy Penguins).

## TL;DR

- **Drift Protocol hacked for $250M+** — attacker compromised an admin key, created a new CBT market, overrode withdrawal thresholds, and drained all pools; Monahan flagged DPRK timing as "sus" given the Axios supply chain attack the day before, though attribution at the time of recording was still uncertain.
- **Axios npm supply chain attack was DPRK** — hackers compromised a package maintainer (likely via Teams/Zoom call), pushed malicious code to a dependency downloaded by an estimated ~100 million computers per week, replicating the same payload they normally get victims to run manually.
- **DPRK malware bypasses MFA entirely** — session tokens saved on a compromised device are stolen and reused; malware pings DPRK command-and-control servers every 60 seconds awaiting instructions and can lie dormant for weeks or months before acting.
- **Antivirus won't catch DPRK malware** — even Sentinel One (enterprise EDR) failed to detect it in recent cases; CrowdStrike is the only recommended defense; the operational baseline for crypto founders is multiple separate MacBooks rotated by purpose.
- **USDC/Circle refuses to freeze without a court order** — Monahan argues this policy "begs the government to enter your stuff" and is useless in fast-moving hacks; Tether makes its own policy-driven decisions and can act quickly when theft address and funds are still visible on-chain.
- **Claude Code source code sat unnoticed on GitHub for ~3 months** — an agent apparently checked in the entire codebase, possibly because Sonnet was used where Opus should have been; Bar Levy claimed no line of code in Claude Code is more than 6 months old across a 14-month-old product.
- **The Claude Code leak is not existential for Anthropic** — the model weights (the "math ball") are the real asset; the harness code is valuable mainly for its hard-won prompting tricks, which will now accelerate open-source model quality.
- **SEAL 911 is a volunteer crypto emergency response group** — donation-funded, covers malware, smart contracts, on-chain tracing, phishing, and drainers; anyone in crypto can reach out for guidance after an incident.

---

**The Drift Protocol Hack — Active Incident**

The episode opens mid-incident: Drift Protocol, a Solana-based derivatives protocol, has just been drained for over $250 million. Warwick and Monahan discuss it while it's still unfolding, cautioning that details are speculative. The attacker compromised an admin multi-sig key, used it to create a new market (CBT), and then raised the protocol's withdrawal limits — which are normally capped — to extract funds from all pools. Monahan notes that this required more steps than a typical key compromise hack: the attacker had to understand Drift's architecture well enough to know that a withdrawal cap existed and that updating it via the admin key was the path to draining at scale. "As far as key compromise hacks go, they had to do more work than normal," she says. This is also Drift's second major hack; a 2022 incident involved collateral inflation to drain vaults.

On contagion risk, Monahan explains the primary concern would be if stolen tokens are dumped, driving down prices for assets used as collateral elsewhere — potentially triggering insolvency cascades. She assesses Jupiter Lend and JLP as likely fine given their liquidity depth, and notes that Solana's DeFi layer has stronger liquidity controls than is commonly assumed.

**DPRK and the Axios Supply Chain Attack**

The Drift timing coincides with a major DPRK supply chain attack on the Axios npm package the previous day. Monahan explains that a group within DPRK's cyber operations — normally focused on Zoom/Teams-based social engineering — compromised a maintainer of the Axios JavaScript library, which is a dependency in a vast number of software projects. They pushed a malicious version of the package containing the same payload they normally get crypto founders to run manually during fake VC calls. Because Axios is downloaded by an estimated ~100 million computers per week, the reach was vastly larger and fully automated.

Monahan describes why open-source maintainers are especially vulnerable: they typically have strong deployment security (code review, build pipelines, careful key management) but are not conditioned to expect adversarial social contact. A convincing message from what appears to be a VC or collaborator, then a Teams or Zoom call with a subtle technical prompt, is enough. "They just are not used to people bashing your door down to try and steal your shit," Warwick adds.

**How DPRK Malware Works — Session Tokens, Heartbeats, Dormancy**

Once DPRK gains access to a developer's machine through a Zoom or Teams call, the victim rarely notices anything immediately. The malware installs silently and does not attempt visible logins. Instead, it establishes what Monahan calls a "heartbeat ping" — the device calls out to DPRK command-and-control infrastructure every 60 seconds asking for instructions. If no instructions come, it waits and pings again. It can sit dormant for two weeks, two months, or longer before activation.

The reason MFA provides no protection is that authentication session tokens — the short-lived credentials that web apps issue after a successful login — are stored on the device and reused by the malware directly. If a developer has a GitHub, npm, or CI/CD token active on their laptop, the attackers take that token and act as the developer without triggering any new login event. Hardware 2FA on the account is irrelevant once the token has been harvested.

For supply chain defense, Monahan recommends "pinning" dependencies rather than auto-updating, and enforcing a minimum age threshold (e.g., seven days) before any package can be merged into a repository. Some teams have internal tooling that blocks a pull request if a dependency is newer than the minimum age, creating friction that buys time for the community to detect malicious versions.

**Device Security — Mac vs. Windows, EDR, and Operational Separation**

Monahan is direct: standard antivirus, including Malwarebytes and even enterprise tools like Sentinel One, will not detect DPRK malware. "In the past couple months, that hasn't even been detected," she says of Sentinel One. EDR (Endpoint Detection and Response) tools like CrowdStrike are the recommended floor for anyone with significant crypto exposure or who runs a company, because they monitor behavior and process patterns rather than hash-matching against known malware signatures.

On Mac versus Windows, the historical advantage of Mac has eroded. Because most crypto founders and developers now use Macs, DPRK has invested specifically in Mac-native malware. Monahan says DPRK is "probably one of the most sophisticated" writers of Mac-native malware. That said, the ultimate defense is operational separation: maintain multiple MacBooks assigned to different categories of activity, so that a compromise on one device does not expose keys or tokens used in another context.

**Phishing Mechanics and Business Email Compromise**

Monahan explains that simply clicking a phishing link rarely causes immediate harm — additional steps are typically required. The most common current vector is "click-fix": a page claims the user's system is broken and instructs them to copy and paste a command into Terminal to fix it. The command installs the malware. The deeper danger of clicking a phishing link is that it switches the victim into autopilot mode, making subsequent steps feel natural and reducing skepticism.

Netz shares a firsthand account of a $2 million business email compromise during a fundraising round. An attacker — later traced to Nigeria — got into an email chain between Netz's company and a VC, changed one letter in an email address (replacing a capital "I" with a lowercase "l"), redirected wire instructions, and received the funds. The VC had insurance. Monahan describes this as a classic BEC (Business Email Compromise) attack and notes it also happens in traditional banking with wire routing numbers.

**Circle's Freeze Policy and the Case for Proactive Action**

One dimension of the Drift hack draws extended commentary: Circle (issuer of USDC) refuses to freeze funds without a court order, whereas Tether (issuer of USDT) makes its own policy-based decisions to freeze known theft addresses. Monahan argues Circle's stance is practically useless in emergency scenarios. By the time a judge signs an emergency order on a crypto case — a domain where few judges have expertise — the funds have typically moved. "You've deliberately given up the sanctity of your protocol to the U.S. government," she says of Circle's approach.

More pointedly, she notes that emergency orders in crypto tracing cases are particularly vulnerable to being issued incorrectly because the technical evidence is hard for courts to evaluate quickly. Tether's model, where the company maintains its own policy and sets high thresholds before acting, is more practical: when a major hack is public, the theft address is visible, the funds haven't moved, and the risk of incorrectly freezing a legitimate user is minimal. "You can unfreeze things," she says. "We're not saying nuke it from space."

**SEAL 911 — Volunteer Crypto Emergency Response**

Monahan describes SEAL 911 as a loose but highly effective volunteer group covering the full stack of crypto security incidents: smart contract exploits, on-chain tracing, phishing drainers, malware analysis, and incident coordination. She is a core member. The group is donation-funded, with no membership fee. She emphasizes that the coordination problem used to be severe — in early DeFi war rooms, expertise was rare and hard to locate mid-crisis. SEAL 911 consolidates it into a single point of contact. "The odds that you have anyone better than SEAL 911 is zero," she says. Anyone who experiences a crypto security incident is encouraged to reach out.

**The Claude Code Source Leak — Slop at Speed**

The second major topic is the leak of Claude Code's source code, discovered to have been sitting on GitHub for approximately three months before anyone noticed. Warwick and Monahan speculate that an agent — possibly running on Sonnet when Opus should have been used — committed the entire codebase without human review. The code has since been ported to Rust by third parties before most people had finished reading what was in it.

Warwick describes the code as "shit thrown in a bucket" — clearly agent-generated at speed, slop-filled and cobbled together, but functional and arguably among the most valuable codebases in the world. He references Bar Levy's claim on the Y Combinator podcast that no single line of code in Claude Code is more than 6 months old, across a product that is now 14 months old. That means the entire codebase has been discarded and rewritten at least twice. "That is the most petrifying thing I've ever heard," Warwick says, though he acknowledges it also demonstrates extraordinary velocity.

**The Agentic Stack and What the Leak Means for Open Source**

Warwick introduces a layered framing for the agentic coding stack. At the base is what he calls the "math ball" — the model weights, training data, and fine-tuning that cost billions of dollars and represent the real proprietary asset of frontier AI labs. Above that is the system prompt and behavioral conditioning. Above that is the harness: the tooling, loop logic, context management, and prompting strategies that make a model actually useful for a specific task like coding.

The leak exposes the harness, not the math ball. The system prompt is visible and reportedly repeats safety instructions ("don't do illegal things") many times, which Monahan notes is genuinely the state of the art for behavioral alignment — brute repetition. The harness tricks — how tool use is structured, how token caching is optimized, how loops are managed — are idiosyncratic to Claude's model and represent empirically validated patterns developed through sustained interaction. Warwick's assessment is that this accelerates open-source model quality: developers can now apply these patterns to local models that previously lacked strong harness support.

The leak is also softened by ephemerality. Anthropic likely already runs Claude Code internally against a newer, unreleased model with a different harness; what was leaked may already be partially obsolete.

**Shifting Left in Engineering — From Code to Planning**

Warwick describes an internal shift at his company that he calls "shifting left": as agents write the code, the valuable human contribution moves upstream to planning. The old model required engineers to maintain a shared mental model of the codebase — its patterns, structure, and reasoning. That mental model is now the agents' job. What humans need to maintain instead is a clear model of intent: what the product should do, why, and for whom.

In practice, this means user stories and requirements documents drive the agents directly. Warwick gives an example of modifying an open-source tool (QMD, a local document search engine) by simply asking an agent to add a flag to select individual data collections rather than re-embedding everything — the agent read the code and made the change without Warwick understanding the underlying implementation. The role of a non-technical founder shifts from directing engineers to directing agents through clear articulation of desired behavior.
