---
podcast: Unchained
date: 2026-10-07
source_transcript: data/podcasts/transcripts/Unchained/2026-10-07_THORChain_Says_It_Can't_Block_North_Korean_Laundering._Is_That_True.md
---

# Unchained — "THORChain Says It Can't Block North Korean Laundering. Is That True?"

**Host:** Laura Shin. **Guests:** Taylor Monaghan (security expert), Chad Bareford (co-founder of THORChain).

## TL;DR

- **THORChain claims it cannot censor transactions—Chad Bareford cites lack of code, slow consensus (3 days to 2 weeks for 2/3 majority), and design trade-off (speed vs. decentralization)**
- **Taylor Monaghan counters: THORChain has used admin keys before and could implement Halt ETH/BTC trading functions to block specific routes from laundering stolen funds, as it did pause lending in the Thorify incident**
- **Only 4 operators control 39 of ~115 nodes (over the 1/3 threshold to block consensus), and only ~50 distinct operator addresses exist—enabling coordination that would be "incredibly easy"**
- **THORChain's closed-source TSS library, only ~3-4 code reviewers, and centralized front-end (swap.thorchain.org, which did screen BitGet hack addresses) contradict claims of true decentralization**
- **Node operators who opposed the Bybit hack response left the protocol; Taylor reports they feared financial penalty despite Chad denying any threat—but in May 2026, THORChain did slash the first operator ever, validating fears and raising coercion concerns**
- **The industry consensus: truly decentralized systems (Bitcoin, Ethereum) cannot and should not censor, but partially centralized systems (like NearIntense) should act to block stolen funds**
- **Chad equates THORChain to Bitcoin and Ethereum's decentralization by Nakamoto coefficient (4 vs. Bitcoin 3 and Ethereum ~2), but Taylor questions whether that standard applies when nearly 100% of certain routes are stolen funds**

---

**THORChain's Censorship Architecture: Technical Barriers or Design Choice?**

Chad Bareford begins by explaining THORChain's technical constraints. The protocol has no code to censor individual transactions or wallets, and any configuration changes require a two-thirds majority of validators to agree, a process that takes on average three days to two weeks. Even if the code existed, Bareford argues, this delay renders it useless for stopping fast-moving laundering flows—responding in real time would require the protocol to become far more centralized. He positions this as a fundamental design trade-off: THORChain optimized for decentralization from day one, much like Bitcoin and Ethereum, and those protocols are not under pressure to censor either.

Taylor Monaghan challenges this framing. She points out that THORChain has made the "we can't do anything" argument for three to four years since streaming swaps began attracting illicit actors—yet in multiple situations, the project has proven it could act. Most notably, for two to three years, co-founders JP and Chad held admin keys that could pause protocol features. When the Thorify incident occurred, Chad used the admin key to pause the lending feature. Taylor argues this precedent demonstrates capability: if THORChain could pause lending via admin key, why couldn't it pause all trading on specific routes or halt ETH and BTC trading altogether when nearly 100% of assets flowing through those routes were known to be stolen funds?

Chad responds that the admin key, while real, is overstated. He calls it a "provisional or interim key" rather than an admin key in the traditional sense, and clarifies it cannot reallocate funds—only make configuration changes that nodes can override. The Thorify pause was a temporary stop before the protocol voted to upgrade. Any broader action, such as turning off an entire route, would still require a two-thirds majority consensus and would halt all trading on that route for one to two weeks during the migration process. He argues this is impractical: shutting down the entire protocol to stop one hack just invites attackers to use Bitcoin or Ethereum instead.

---

**The Decentralization Question: Numbers vs. Reality**

Laura Shin raises a critical point: if THORChain is truly as decentralized as Bitcoin or Ethereum, why is the number of node operators so small? There are roughly 115 validators, but only 50-54 distinct operator addresses. More strikingly, four operators control 39 nodes—well over the one-third threshold needed to block consensus. Taylor observes that coordination among four parties would be "incredibly easy."

Chad counters by citing THORChain's Nakamoto coefficient: 4. Bitcoin's is 3, and Ethereum's is roughly 2. By this metric, THORChain is actually more decentralized than Bitcoin or Ethereum. He notes that Bitcoin could achieve 51% computing power with just three mining pools; Ethereum faces similar concentration among staking entities, many of which are corporate (Coinbase, Binance). So by Chad's logic, holding THORChain to a higher standard of decentralization than Bitcoin or Ethereum is unfair.

Taylor pushes back on this comparison. She cites a blog post Chad himself wrote: "A chain may claim to have hundreds of validators, but that number means very little if most are operated by the same entities, hosted in the same data centers, or selected through a closed process." By this standard, she questions whether THORChain passes its own test. Additionally, the threshold for blocking consensus is only one-third, not a majority. If four operators representing one-third of the network could theoretically halt the entire protocol, the practical decentralization is far lower than the Nakamoto coefficient suggests.

Chad further explains that THORChain uses a threshold signature scheme (TSS), where validators collectively control the underlying assets in custody. This architecture makes THORChain an intermediary, not a true base-layer protocol like Bitcoin or Ethereum. One crypto analyst, Sarshu of OKEx, noted that once the TSS signing threshold is reached, validators can move the funds—meaning THORChain is effectively a multi-party custodian, not a permissionless protocol.

---

**Closed Source, Code Review, and Transparency Gaps**

Taylor raises another decentralization concern: the TSS library is now closed source. Chad explains that a security exploit forced the team to close it temporarily so the security team could conduct a deeper code review before reopening it. The rest of the protocol—Thornode, Bifrost—remains open source. But this closed-source window, combined with the fact that only roughly three to four developers can approve code changes, creates an audit and transparency problem. How can node operators verify they're running safe, uncompromised software?

The centralization becomes more apparent when Laura points out that the front-end user interface, swap.thorchain.org, is fully centralized and does screen addresses (it blocked the BitGet hack addresses from the API). If THORChain's centralized UI can perform this screening, why can't the decentralized protocol layer do something similar? Chad acknowledges the UI is centralized and subject to laws, whereas the protocol itself is supposed to be censorship-resistant. But this distinction highlights the role of centralized points of control in the THORChain ecosystem.

---

**Node Operator Fear, Coercion, and the Bybit Precedent**

When the 1.4 billion dollar Bybit hack occurred, some node operators attempted to pause trading. They lost by an overwhelming majority, and afterward, about 20 validators left the protocol. Taylor interviewed some of these departing operators and reports they cited fear of financial penalty: they believed that if they remained in the minority on a contentious decision, the two-thirds majority could vote to slash their stake entirely. Chad denies this was ever discussed or threatened. He argues that slashing only happened once, when an attacker stole $10 million from the protocol itself—an objective mathematical proof of malfeasance, not a policy disagreement.

However, Taylor points out that THORChain *did* enact the first-ever slashing in May 2026. This validates the fear, even if it was for a theft rather than a disagreement. The mere fact that the mechanism exists and was used creates a chilling effect: node operators now know that a two-thirds majority *can* seize their stake. Chad maintains this is not a threat but a feature of consensus-based systems—Bitcoin and Ethereum also have this theoretical power. Yet Taylor argues that the existence of this mechanism, combined with evidence of its use, makes it harder for operators to dissent without risk.

Laura also notes that some developers publicly quit THORChain during the North Korea laundering controversy, citing moral concerns about the protocol facilitating theft. Chad acknowledges this happened but frames it as individuals leaving voluntarily, not being expelled.

---

**The Moral and Industry Consensus Argument**

Taylor frames the debate in moral terms: THORChain is part of the crypto ecosystem and has a responsibility to that ecosystem when stolen funds flow through it. Even if blocking all laundering is impossible, making it harder through partial measures (like pausing specific routes) has real value. She draws a parallel to the DAO hack in 2014, when Shapeshift engaged in a cat-and-mouse game with the attacker. The attacker eventually gave up rather than continue automating address changes in response to Shapeshift's blocks—suggesting that even imperfect defense works.

Chad argues that expecting THORChain to take on responsibility for hacks on other platforms (like Bybit or BitGet) is unfair. Validators are responsible for the security of *their own* protocol. Bitcoin miners don't police which UTXOs they include in blocks; Ethereum validators don't screen transactions. THORChain shouldn't be held to a different standard.

Laura Shin frames the broader industry consensus: truly decentralized systems (Bitcoin, Ethereum) are understood to be censorship-resistant and cannot be asked to discriminate. However, projects like NearIntense that retain more centralized control are expected to use that control to protect victims. The industry views projects like THORChain—which claim decentralization but retain some centralized control points (admin keys, small validator set, centralized UI)—with the most scorn when they refuse to act on stolen funds.

---

**Closing Tensions**

The debate ends without resolution, highlighting a fundamental tension: THORChain claims the decentralization of Bitcoin while retaining operational capabilities that Ethereum or Bitcoin do not have. Chad offers to put the question to the community: whether to remove the technical capability to pause trading altogether, eliminating any future temptation to censor. Taylor remains skeptical that this would address the underlying issue—that THORChain's architecture sits in a gray zone between decentralized protocol and financial intermediary, and the industry expects intermediaries to police stolen funds, even if imperfectly.
