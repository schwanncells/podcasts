---
podcast: Unchained
date: 2026-04-03
source_transcript: data/podcasts/transcripts/Unchained/2026-04-03_Quantum_Computing_Got_20x_Closer._It_Threatens_A_Third_of_All_Bitcoin.md
---

# Unchained — "Quantum Computing Got 20x Closer. It Threatens A Third of All Bitcoin"

**Host:** Laura Shin. **Guests:** Alex Pruden (co-founder and CEO, Project 11 — a firm focused on post-quantum migration and security for digital assets); Dolev Blustein (CEO, AuraTomic — quantum computing hardware company using neutral atoms trapped in optical tweezers; PhD research produced the world's first error-corrected quantum algorithms on atomic systems).

## TL;DR

- **Google published a white paper showing future quantum computers could break elliptic curve cryptography, with a timeline of 2029** — co-authored by Ethereum Foundation researcher Justin Drake and Stanford cryptographer Dan Boneh, the paper used a zero-knowledge proof to demonstrate the attack method without disclosing it publicly.
- **AuraTomic's paper shows Shor's algorithm could run on as few as 10,000 qubits** — a 50x reduction from Google's own estimate of 500,000 physical qubits, achieved by using atoms suspended in laser beams that can be physically repositioned during computation to make error correction far more efficient.
- **About a third of all Bitcoin is vulnerable** — Project 11 data (cited in the Google paper) tallies 6.7 million BTC (~$450 billion) across the top 100,000 addresses with exposed public keys, including Satoshi's wallets.
- **"Fast clock" quantum computers could execute an on-spend attack in roughly 9 minutes** — well within Bitcoin's ~1-hour confirmation window, meaning an adversary could intercept a transaction in the mempool, recover the private key, and redirect funds before the block confirms.
- **Once real-time attacks are possible, migration windows close permanently** — users who haven't moved funds to post-quantum addresses won't be able to do so safely, as attempting the migration would expose their public keys to the adversaries they're trying to escape.
- **Ethereum faces a larger attack surface but has faster block times as accidental protection** — 12-second block times make on-spend attacks impractical for now, but proof-of-stake consensus, smart contracts, L2s, and stablecoins all rely on elliptic curve cryptography and each require independent migration.
- **Bitcoin's decentralization creates a governance coordination problem** — handling Satoshi's coins or mandating wallet migration would require 51% miner consensus, making a hard technical problem also a hard political one.
- **Project 11 is shipping post-quantum wallet infrastructure for Bitcoin and Ethereum** and releasing a research report with specific metrics for tracking Q-Day; its public tool at project11.com lets users check whether their address's public key is already exposed.

---

**The Google Paper and Why This Time Is Different**

The episode was recorded on the day two major quantum computing papers dropped simultaneously. The Google paper — co-authored by Ethereum Foundation researcher Justin Drake and Stanford cryptographer Dan Boneh — provides a comprehensive analysis of how a future cryptographically relevant quantum computer could break elliptic curve cryptography, the foundation underlying virtually every major blockchain. Rather than publish the attack method directly, Google issued a zero-knowledge proof to establish the vulnerability without enabling replication, a practice Pruden compares to responsible disclosure in cybersecurity.

Pruden notes the paper's breadth as its most important feature. Beyond Bitcoin and Ethereum wallets, it explicitly maps the attack surface to stablecoins, zero-knowledge proof systems, and data availability layers for L2s. "Elliptic curve cryptography is the foundation of pretty much all digital assets," he says — and the paper's scope reflects how thoroughly it is embedded across the ecosystem. The involvement of Boneh, a prominent cryptographer, is also significant: Pruden observes that physicists building quantum hardware have long been more alarmed about the timeline than cryptographers, and the gap is slowly closing.

**AuraTomic's Breakthrough: 50x Fewer Qubits**

Blustein describes AuraTomic's paper, posted to Archive (not yet peer reviewed), as demonstrating that Shor's algorithm — the quantum algorithm that can factor the large numbers underlying public-key cryptography — could in principle run on as few as 10,000 physical qubits. Google's own paper estimated the requirement at roughly 500,000; estimates from a decade ago put it at a billion. The reduction comes from a novel hardware approach: atoms suspended in a vacuum and trapped in laser beams that can be physically moved around as the computation evolves, enabling far more efficient quantum error correction.

The current state of the art at Caltech, led by AuraTomic co-founder Manuel Andres, is a system of over 6,000 atomic qubits — already approaching the new threshold. Blustein stresses, however, that the distance between having a large qubit array and having a fault-tolerant computer capable of running Shor's algorithm remains significant. "It's not like you have a system of a lot of atomic qubits and then you just press a button and all of a sudden it becomes a fault-tolerant quantum computer running Shor's algorithm."

**How Quantum Error Correction Works**

Blustein explains that quantum states are inherently fragile — similar to analog computing. Classical analog computers are theoretically powerful but cannot correct errors; digital computers are robust because bits are binary and errors can be detected. Quantum error correction bridges these worlds: it allows analog-like superposition-based computation while applying digital-style error correction, exploiting wave-particle duality so that measurement projects errors away without destroying the computation. The theoretical possibility of quantum error correction was established in 1995, but demonstrating it experimentally — showing that adding more physical qubits can exponentially reduce error rates — only began happening in the last year, in Google's Willow result and AuraTomic's own work. This, Pruden says, is why people who have been skeptical of quantum timelines need to update: the bottleneck that blocked progress for three decades has just been crossed.

**The Q-Day Timeline and the Skeptics**

Blustein calls Q-Day by end of decade "quite plausible, although not guaranteed," and says AuraTomic currently holds what he believes is the world's lead in proximity to building a cryptographically relevant machine. Pruden, who has standing bets on Q-Day by 2035, says he would now feel comfortable betting on 2032, and thinks 2030 is a reasonable target for many observers. He flags a key finding from the Google paper: the assumption that Q-Day will approach slowly and visibly is probably wrong. Once a quantum computer can run Shor's algorithm on a 32-bit number, Google argues it is a trivially small engineering step to scale to 256-bit keys, meaning there may be no useful warning window. AI is already accelerating the timeline — "we use AI for everything," Blustein confirms.

Both guests push back on cryptographer Matthew Green's tweet that he "is not convinced we have anything to worry about in my lifetime." Pruden, who knows Green personally, says physicists and cryptographers continue to diverge on timeline and priority, but that Boneh's presence on the Google paper represents the gap narrowing. "This is actually slowly rippling out as a stone kind of thrown into a pond ripples out."

**What a Quantum Attack on Bitcoin Actually Looks Like**

Pruden breaks down two distinct threat categories. The first involves coins with permanently exposed public keys — Satoshi's wallets and other early addresses where the public key has been visible on-chain for years. A slow-clock quantum computer, easier to scale and apply error correction to, could recover those private keys at leisure. The Google paper describes this as the more likely near-term scenario.

The second category is the on-spend attack. When a user broadcasts a transaction, the public key is exposed in the mempool before any block confirms. Bitcoin addresses are hashed public keys, which provides one layer of obscurity, but signature verification requires broadcasting the public key directly, closing that protection at the moment of spending. Google's paper estimates a fast-clock quantum computer could recover a private key and re-sign a transaction redirecting the funds in roughly 9 minutes — Bitcoin's mempool window is roughly an hour, so this is well within range.

Pruden also addresses Grover's algorithm, a quantum attack on hash functions. The Google paper concludes the qubit resources required are "astronomical" compared to Shor's, placing it in the far-horizon category.

**The Satoshi Coins Problem**

What happens to coins that can't be safely migrated once Q-Day arrives has no easy answer. Proposed options include allowing "digital salvage" by whoever has the quantum computer, burning the coins to reduce supply, or some form of redistribution. Each would require different actions, and burning Satoshi's coins alone would require 51% of Bitcoin miners to agree to alter the ledger's effective supply cap. Pruden is skeptical of claims this would be simple: "Even if that was the end outcome, I think there would be a huge fight."

The deeper problem is that once real-time on-spend attacks are possible, the migration window closes permanently. Users trying to move funds to post-quantum addresses would broadcast their public keys into a mempool monitored by adversaries — a paradox with no clean exit that isn't resolved by private mempools or ZK proofs without compromising Bitcoin's typical guarantees.

**Bitcoin's Governance Coordination Problem**

Pruden acknowledges Bitcoin's decentralization as a genuine philosophical strength — it is why many holders view it as digital gold — but sees it in direct tension with the coordination required to respond to the quantum threat. Bitcoin Improvement Proposal 360, which proposes a new script type (pay to Merkle route, P2MR), is an early step: it disables the key-path spend for Taproot transactions, preventing public key exposure in that context. But Pruden calls it "one of many steps that have to happen" and notes it does not add post-quantum signatures to Bitcoin.

He urges the community to move from debate to engineering: build testnets, run performance evaluations, develop wallet migration infrastructure. Project 11 has already built "Yellow Pages," a tool letting users create a post-quantum key and sign it with their existing Bitcoin key to establish a migration claim before the on-spend window closes. "I don't think there's a bigger technical challenge to Bitcoin today."

**Ethereum's Different Risk Profile**

Ethereum has faster block times — 12 seconds — making on-spend attacks impractical for the near term and giving it a structural advantage over Bitcoin. But its attack surface is far wider. Proof-of-stake consensus requires validators to digitally sign votes on blocks; those signatures would be forgeable by a quantum computer, enabling consensus-layer attacks that Bitcoin's proof-of-work design does not face. Smart contracts need to be redeployed with post-quantum admin keys. L2 systems anchored to Ethereum's base layer carry their own vulnerabilities. Stablecoin users, many of whom have never interacted directly with a blockchain, somehow need to migrate keys they may not understand they hold.

On the positive side, the Ethereum Foundation — with Justin Drake now a co-author on the Google paper — is ahead of Bitcoin in formally acknowledging the problem. Project 11 has done testnet work with the EF, and the Foundation has divided its post-quantum effort between securing consensus and securing the wallet layer.

**Other Chains, Fast Block Times, and Quantum-Native L1s**

Blockchains with faster block times have inadvertently defended themselves against the on-spend attack class, at least for now. Bitcoin Cash, Dogecoin, and other Bitcoin forks share Bitcoin's slow block times and comparable vulnerability. The Google paper highlights Algorand as an example of a chain that has added a post-quantum address type using the NIST-standardized Falcon signature scheme, though Pruden notes it is unclear how widely used the new address type is or whether Algorand's DeFi ecosystem is compatible with it.

Several quantum-native L1s — built from inception with post-quantum cryptography — are also cited. Pruden views their long-term role as primarily serving as test beds: their survival as major chains depends on convincing the market that Bitcoin and Ethereum will fail to migrate in time, a premise he thinks "people are not ready to accept yet." He credits them with pioneering the post-quantum algorithms that existing chains will eventually have to adopt, and notes that in a meaningful sense all chains will become post-quantum L1s once migration happens — the underlying cryptographic primitive is the same.

**Project 11's Roadmap**

Project 11's public tool at project11.com lets any user check whether their wallet's public key is currently exposed — the same dataset cited in the Google paper. Pruden says the company will shortly release a limited post-quantum wallet for Bitcoin and Ethereum, acknowledging that its functionality will be constrained by the absence of post-quantum signature support in either protocol's base layer. A research report is also in progress, aimed at institutions, that will detail exactly what milestones to watch for as Q-Day approaches and provide charts and metrics for tracking progress.

Pruden closes with measured optimism, pointing to the ETH1-to-ETH2 transition as proof that decentralized systems can coordinate around hard technical changes that many initially thought impossible: "I think there is absolutely no reason why blockchains and the communities that surround them can't set the example for the rest of the world for how decentralized governance can actually lead and not lag in post-quantum security."
