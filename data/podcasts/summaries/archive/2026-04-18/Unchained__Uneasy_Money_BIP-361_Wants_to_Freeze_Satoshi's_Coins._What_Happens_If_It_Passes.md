---
podcast: Unchained
date: 2026-04-18
source_transcript: data/podcasts/transcripts/Unchained/2026-04-18_Uneasy_Money_BIP-361_Wants_to_Freeze_Satoshi's_Coins._What_Happens_If_It_Passes.md
---

# Unchained — "Uneasy Money: BIP-361 Wants to Freeze Satoshi's Coins. What Happens If It Passes?"

**Host:** (co-hosts Taylor Monaghan, security expert). **Guest:** (none; discussion between two Unchained hosts).

## TL;DR

- **BIP-361 proposes freezing Bitcoin addresses that don't upgrade to quantum-resistant cryptography within a defined timeline** — specifically targeting early wallets most vulnerable to quantum attacks, with a freeze date around 8–10 years out; implementation requires network consensus but represents an unprecedented intervention in Bitcoin's immutability principle.
- **Early Bitcoin addresses face disproportionate quantum risk** — the original wallet generation schemes used less secure cryptography than modern addresses, and quantum computers strong enough to break ECDSA could derive private keys from publicly visible transaction signatures on addresses that have been reused.
- **Satoshi's ~1 million coins are the primary motivation** — held in early, quantum-vulnerable addresses; BIP-361 would eliminate the "Satoshi dump" existential risk that has haunted Bitcoin since inception, while also creating forced movement of coins that could trigger massive market volatility.
- **Bitcoin's governance schism prevents collaborative problem-solving** — post-2018 ossification and dominant "no changes" religious faction reject new ideas reflexively; quantum response was eventually forced onto the agenda only by genuine existential threat, illustrating how Bitcoin's coordination mechanisms have atrophied.
- **Satoshi's identity likely involves multiple people, including Adam Back, Hal Finney, and possibly David Kleiman** — Phil Dian's analysis linked all three to Epstein-connected individuals and documents; Hal Finney and Kleiman are deceased; this theory explains code/philosophy/administrative split across team.
- **Token holder rights remain unprotected in crypto** — World Liberty Financial ICO participants bought coins with indefinite lockup; now facing new unlock terms or permanent loss; token issuers have zero incentive to accommodate early holders and no legal remedy exists, unlike traditional equity where later funding rounds can water down bad early decisions.
- **Platform risk pervades crypto infrastructure** — Scroll chain cranked fees to 50K/day to punish Etherfyi's departure; CoW Swap's DNS hijacking succeeded via social engineering; X/Twitter censors crypto reach while taking control of cash tag resolution; blockchains and protocols cannot insulate users from centralized layer exploits.

---

**Bitcoin's Transition from Code to Religion**

The hosts trace Bitcoin's ideological evolution from pragmatic software project (2009–2011) through religious movement to fundamentalist institution. Early Bitcoin, despite being called "code is law," remained malleable: the infinite-coin bug was squashed, the chain rolled back, developers collaborated. By 2011–2014, evangelism and ideology began replacing pragmatism. The fork wars (2015–2017) hardened the divide between changeability and immutability; everyone except the most religious Bitcoiners migrated to Ethereum or alt-coins. Those who remained became a self-selected cohort ideologically opposed to modification. Post-2018, Bitcoin "ossified so hard"—BIP rate dropped sharply, and a new wave of hardcore fundamentalists rejected ideas reflexively, framing Bitcoin not as payment network (per Satoshi's white paper) but as sacred object beyond alteration. This creates an "immune system" that rejects any proposed change indiscriminately, chilling innovation and preventing collaborative problem-solving even in response to existential threats.

**The Quantum Threat and Bitcoin's Cryptographic Vulnerability**

Bitcoin's security rests entirely on ECDSA (elliptic curve digital signature algorithm) and SHA-256 hashing. Quantum computers with sufficient qubits could derive private keys from public keys—not through brute force, but by reversing the mathematical relationship Shor's algorithm exploits. Today's quantum computers would still take eons; a sufficiently advanced one could break ECDSA in roughly 30 seconds. The early Bitcoin wallets created before modern standards (pre-BIP39 seed phrases) are especially vulnerable because the public key was often broadcast in transactions, making it directly observable. Early addresses hold the worst cryptography; newer addresses are marginally more resistant. However, once a quantum computer reaches a critical power threshold, the distinction becomes irrelevant—all non-quantum-resistant addresses are compromised equally. The hosts emphasize this is not theoretical FUD: quantum advancement is linear, and doing nothing guarantees that eventually, anyone with a sufficiently powerful quantum computer can steal coins from any address that has signed a transaction, because the public key becomes the weak link.

**BIP-361: Freezing Coins as a Forcing Function**

Jameson Lopp, respected Bitcoin developer, proposed BIP-361—a protocol change to freeze addresses that don't upgrade to quantum-resistant cryptography within a set window. The proposal would freeze Satoshi's ~1 million coins (worth tens of billions) automatically if they remain in non-upgraded addresses, removing them from circulation permanently. The freeze date is set approximately 8–10 years out, creating a hard deadline. This is wildly controversial because it violates the core Bitcoin principle that "no one can freeze your coins"—immutability and uncensorability are religious tenets. Yet the hosts argue it's genius as a forcing function: it solves the Satoshi dump risk, eliminates existential FUD, and locks value permanently off the market, creating a "god candle" on that date. However, they note the timeline is problematic; eight years is long enough that people procrastinate, and the interim period—between freeze date and actual quantum threat emergence—creates a window where selective unfreezing requests could arise (e.g., people claiming to be in prison).

**Satoshi's Identity and the Multi-Person Theory**

The hosts discuss Phil Dian's recent theory that Satoshi was a small team: Adam Back wrote the white paper and philosophy; Hal Finney provided visionary ideas and ideological coherence; and David Kleiman wrote the code. Evidence includes stylometric analysis matching Back's writing, Kleiman's presence in Epstein files discussing seized hard drives (an apparent connection to Bitcoin), and Finney's earlier e-cash research. The theory is compelling because it explains the code/philosophy split (different authorial voices) and why no single person has ever claimed the mantle. Both Finney and Kleiman are deceased, eliminating any conspiracy-of-silence objection. The hosts note this is not a conspiracy theory but rather a reasonable deduction—someone created Bitcoin, and the question of one versus multiple people is factual, not speculative. The team theory resolves several mysteries about Bitcoin's origin while remaining unprovable.

**Satoshi's Coins as the Ultimate Market Catalyst**

If BIP-361 passes, the hosts project that when the freeze deadline arrives (roughly 2033–2034), the market will experience unprecedented volatility. Satoshi's coins, worth potentially trillions if Bitcoin reaches $1M+ per coin, will be locked forever. This removes perpetual tail risk: the question "what if Satoshi wakes up and dumps?" finally has an answer. One host argues an 8–10 year timeline is unnecessarily long; a 1–2 year deadline would close the issue cleanly during the bear market when disruptive changes are more tolerable. The alternate risk is forcing Satoshi (if alive) to move coins now or lose them forever, which would unmask whoever controls them—another outcome Satoshi presumably wanted to avoid for 15 years.

**Token Holder Rights and the Governance Void**

The World Liberty Financial ICO (late 2024) sold tokens with indefinite lockup "until we figure out the terms later." Now the project proposes a 2–3 year unlock structure with cliffs. Token holders, including Justin Sun's wallet (which is blocklisted and frozen selectively), have no legal recourse because token purchases are uncontracted gifts of digital assets with zero statutory rights. This contrasts with equity financing: in traditional startups, early funding mistakes are diluted away through later rounds without disrupting founder-investor relations. Tokens are immutable and fixed-supply, so bad terms stay bad. The hosts cite the Curve example: investors sent Michael Egorov $80K in USDT five years ago for CRV tokens that never materialized; lawsuits across three jurisdictions failed because no contract existed and no legal framework governs magic beans. Michael eventually returned the money—not because he had to, but because he no longer needed it and goodwill mattered. Token structures eliminate the relief valve that equity provides, leaving issuers with unlimited ability to change terms and holders with zero protection.

**Platform Risk in Ethereum Layer-2s and DNS**

Scroll chain increased network fees from ~$250/day to $50K/day after Etherfyi announced departure, intentionally making migration expensive for a major user. This exemplifies platform risk: a blockchain is immutable at the application layer, but validators and sequencers remain centralized authorities who can change fees, exclude transactions, or effectively freeze activity. The hosts extend this to DNS: CoW Swap's DNS was hijacked not through technical compromise but by social engineering support staff at their domain registrar. One attacker contacted a registrar agent claiming infrastructure problems, and when denied, contacted another agent with the same story and succeeded. DNS is critical infrastructure for every crypto company and entirely dependent on human-operated registrars vulnerable to social engineering.

**X/Twitter's Creeping Centralization of Crypto Infrastructure**

Elon Musk's X platform has progressively de-amplified crypto content while claiming the space is experiencing "a bad year." Simultaneously, X is redesigning its cash tag system ($TICKER) to centralize ticker ownership and visibility on X's platform, making X the de facto arbiter of which projects get promoted. This is platform risk compounded: X once hosted crypto discussion freely; now it controls content reach and is consolidating control over ticker resolution. Crypto projects cannot escape X's reach because network effects concentrate users there, yet remain subject to arbitrary rule changes and algorithmic suppression.

---

**Notes on Narrative:** The episode progresses thematically from Bitcoin's governance crisis (ossification and inability to adapt) through the quantum threat (forcing adaptation) to token governance and platform risk across Layer-2s, registrars, and centralized services. The Satoshi identity discussion is secondary flavor but clarifies stakes. The through-line is perverse incentives and misaligned governance whenever one party (Scroll validators, registrars, token issuers, X executives) holds unilateral power and no accountability mechanism exists.
