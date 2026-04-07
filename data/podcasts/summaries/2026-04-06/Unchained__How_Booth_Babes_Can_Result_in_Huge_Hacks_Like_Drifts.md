---
podcast: Unchained
date: 2026-04-06
source_transcript: data/podcasts/transcripts/Unchained/2026-04-06_How_'Booth_Babes'_Can_Result_in_Huge_Hacks_Like_Drift's.md
---

# Unchained — "How 'Booth Babes' Can Result in Huge Hacks Like Drift's"

**Host:** Laura Shin. **Guests:** Amanda Wick (Head of Americas at Verify VASP; former federal prosecutor; co-author of 2024 paper on digitally enabled sanctions evasion); Michael Llewellyn (Head of Solutions Engineering at Turnkey; former smart contract auditor at OpenZeppelin; served on multiple DeFi security councils).

## TL;DR

- **The Drift hack was a 6-month intelligence operation** — attackers met Drift team members in person at multiple crypto conferences, built trust over months, deposited $1 million of their own capital, and onboarded a vault onto the protocol before compromising developer machines.
- **Operatives used "fully constructed identities"** — Drift's postmortem described attackers with fabricated employment histories, public-facing credentials, and professional networks; the individuals who appeared at conferences "were not North Korean nationals," indicating DPRK used proxies.
- **The technical exploit combined social engineering with a VS Code vulnerability and Solana's durable nonce** — attackers convinced engineers to clone repositories, compromised machines, then obtained pre-signed transactions on the 2-of-5 admin multisig weeks before the attack launched; on-chain analytics showed they rehearsed the exploit.
- **The DPRK group is UNC 4736, also called Apple Juice or Citrine Sleet** — TRM and Elliptic attributed the hack based on digital fingerprints; DPRK operates multiple competing hacking franchises, each bringing in revenue for the North Korean state, particularly the nuclear program.
- **Circle let $232 million in USDC be bridged out over six hours without freezing** — attackers specifically chose USDC over USDT because they knew Circle's policy requires a court order or law enforcement action before freezing; TRM noted the "confidence of the hackers was staggering," moving faster and more aggressively than even the Bybit DPRK laundering of 2025.
- **Tether is meaningfully faster than Circle on hack response** — Tether participates in the T3 Financial Crime Unit with Tron and TRM Labs, froze $9 million in the Bybit hack, and will act on security professional reports when more than 50% of funds in an address are confirmed dirty; Circle requires formal legal cover before acting.
- **Security professionals say most crypto teams are likely being targeted right now** — once a project exceeds $50–100 million in TVL, it likely appears on DPRK's list; key mitigations include separate signing devices, endpoint protection, credential rotation, rolling operational security audits, and treating any persistent new contact as a potential threat vector.

---

**The Six-Month Setup**

Michael Llewellyn was having dinner with security professionals at EthCC in Cannes when the Drift hack unfolded, and was tracking it in real time. He describes the postmortem revelation as the most important part: this was not a smash-and-grab but a sustained intelligence operation. Operatives met Drift contributors at multiple crypto conferences, showed technical fluency, discussed protocol integrations, deposited $1 million in capital, and onboarded a vault — requiring them to submit a strategy document — to establish credibility. Drift's own postmortem described the attackers as having "fully constructed identities, including employment histories, public facing credentials and professional networks," potentially assembled over one or two years.

Once trust was established, attackers were able to convince engineers to clone certain repositories. They exploited known vulnerabilities in VS Code extensions, compromised the machines of developers who held admin keys, and obtained signatures on the protocol's 2-of-5 admin multisig weeks in advance. Solana's durable nonce feature allowed them to hold a valid pre-signed transaction ready to execute at any moment, without it expiring. On-chain analytics suggested they also ran rehearsals before launching. The attack itself, Llewellyn notes, came one month to the day after the Bybit hack.

**DPRK Proxies and the Booth Babes Problem**

Laura Shin points out that Drift explicitly stated the in-person operatives were not North Korean nationals, which raises the question of who they were. Amanda Wick, drawing on her background as a federal prosecutor, dismisses the notion that you can visually identify a North Korean at a conference. "If I was going to hire somebody," she says, "it would be white Brad Tad or Chad Crypto Bro to run around these conferences." Malign actors hire whoever makes their targets most comfortable and looks most innocuous — including, she says, attractive women, the so-called "booth babes" phenomenon she first observed at a Bitcoin Miami conference, where hired individuals draw conference attendees into booths to collect contact information and conversation data.

Llewellyn adds that DPRK has long used "laptop mules" — US nationals or non-Korean individuals who front job interviews for North Korean hackers, receive a shipped laptop, and then follow instructions that give access to the actual attackers. The broader pattern of DPRK infiltrating open-source crypto projects through contributor accounts is also well-documented: they are skilled developers who do not introduce backdoors early, preferring to gather operational intelligence patiently and identify the weakest link over time.

**Who Is UNC 4736?**

TRM Labs and Elliptic published attribution pointing to a DPRK state-affiliated group designated UNC 4736, also known as Apple Juice or Citrine Sleet. Llewellyn explains that North Korea does not operate a single hacking unit — Lazarus is just the best-known name. Instead, the country runs multiple groups operating somewhat like franchises under central state direction, competing against one another to bring in the most revenue for the regime. Wick adds that crypto theft appears to be a significant funding source for the North Korean state, particularly the nuclear program, and that nation-state actors like DPRK bring resources, time, and long-term planning that most crypto teams never prepare for.

**Circle's Inaction — and the USDC Playbook**

The second major controversy was Circle's decision not to freeze USDC during a six-hour window while the $232 million hack was actively being bridged across Circle's own cross-chain transfer protocol, CCTP, from Solana to Ethereum. Llewellyn says Circle's slow-freeze posture is well-known among security professionals: the company has historically required a court order or formal law enforcement involvement before acting. As a result, attackers specifically stocked USDC rather than USDT for the Drift hack, knowing they had a wide operational window. Security professionals — including Seal 911, Zero Shadow, and ZachXBT — flagged the theft in near-real time and, based on past experience, were not surprised by Circle's non-response.

Wick goes further. Circle is a registered US money services business with AML/CFT obligations. In her view, their compliance professionals should have been able to identify an active laundering in progress and act under their existing terms of service, which explicitly permit blacklisting. She frames it as "performative compliance" — doing the minimum legally required rather than exercising the powers they hold. The analogy she uses: "it's like saying that if your bank was being robbed, and you were watching people move the money out, and they were unarmed, and there was very little risk of doing anything, that you would say we just decided to let the funds walk out." She adds that law enforcement globally, not just security researchers, has been frustrated with Circle for similar reasons — including foreign law enforcement who arrive with evidence and are told to get an MLAT, which can take years.

A particular irony cited by ZachXBT: days before the Drift hack, Circle froze 16-plus legitimate business hot wallets in response to what appears to have been a poorly traced court order. Wick offers some fairness here — when a court order arrives under seal, the company receiving it often has no factual basis to challenge it, and may not even have the underlying affidavit. That is a different situation from six hours of on-chain bridging activity while the industry screams.

**Tether vs. Circle**

Tether, by contrast, participates in the T3 Financial Crime Unit alongside Tron and TRM Labs, moves faster on security professional reports, and froze $9 million in DPRK-linked Bybit funds. Llewellyn says Tether has invested in the infrastructure — formal relationships with groups like Zero Shadow and Seal 911 — to be ready to act before a full law enforcement process plays out. Their documented threshold: more than 50% of funds in an address confirmed dirty before freezing. Wick notes that Tether operates more on a risk-based, common-sense model than a purely legalistic one, and acknowledges the irony that the US-based "compliant" issuer has a significantly worse track record on hack response than the offshore issuer. She qualifies this: Tether's compliance on sanctions facilitation is a murkier picture, and the comparison is not a simple one-to-one.

**What the Law Doesn't Cover — and What It Should**

Wick argues that the existing legal framework has not kept up with blockchain-speed financial crime. Her proposed fix: a safe harbor for protocols and stablecoin issuers analogous to the BSA safe harbor for suspicious activity reports — giving companies legal cover to freeze funds based on actionable intelligence from credentialed security professionals, without waiting for a court order. She envisions some form of credentialing process for security professionals who submit freeze requests, so the bar is higher than "trust me, it's dirty." She also points to the asymmetry on the back end: even if issuers freeze funds quickly, many jurisdictions outside the US and UK lack the asset seizure and recovery infrastructure to actually retrieve them. Both sides of the pipeline need work.

**Security Recommendations**

Llewellyn's recommendations for crypto teams, framed as lessons from Drift:

Separate signing from development entirely. Any device used to sign admin transactions should be isolated — no random repository cloning, no VS Code extensions, no external email. Hardware wallets or API-based key management with fine-grained policies (Llewellyn mentions Turnkey) are preferable to keys stored on developer laptops. Multi-sig thresholds alone are insufficient if any one signer's machine can be compromised; time locks and additional safeguards are worth the operational friction for high-value protocols.

Treat social persistence as a threat signal. Wick notes that the pattern of meeting someone at a conference, and then having them systematically stay in touch over six months, is a behavioral marker worth training employees to notice. The overlap between aggressive business development and adversarial relationship-building is real, and DeFi protocols that want to grow their communities are structurally more exposed. The answer is not paranoia, but basic awareness that sustained, systematic outreach from new contacts is worth scrutiny.

Get independent operational security audits. Wick emphasizes that internal security teams, however skilled, are not sufficient — outside adversarial testing and rolling audits are necessary, especially as a protocol grows. Llewellyn adds that most of the large hacks in the past year have not come from smart contract exploits but from operational security failures, and SOC 2 is a floor, not a ceiling.

Rotate credentials now if you may have been targeted. Teams that have had sustained outside contact, hired new contributors, or cloned external repositories in the past year should treat their systems as potentially compromised: full device wipe, credential rotation, and wallet key rotation where possible. Seal 911 operates a Telegram hotline for teams actively concerned they are compromised. Llewellyn closes with the broader point: "Drift is not the only one" — it is very likely that other teams are being targeted with similar long-horizon operations at this moment.
