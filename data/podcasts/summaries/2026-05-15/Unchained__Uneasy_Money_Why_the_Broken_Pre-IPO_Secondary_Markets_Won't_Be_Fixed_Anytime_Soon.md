---
podcast: Unchained
date: 2026-05-15
source_transcript: data/podcasts/transcripts/Unchained/2026-05-15_Uneasy_Money_Why_the_Broken_Pre-IPO_Secondary_Markets_Won't_Be_Fixed_Anytime_Soon.md
---

# Unchained — "Uneasy Money: Why the Broken Pre-IPO Secondary Markets Won't Be Fixed Anytime Soon"

**Host:** Laura Shin. **Guests:** Kane Wark (co-host, Uneasy Money); Taylor Monahan (co-host, Uneasy Money, CEO of Pudgy Penguins; security expert at Lucanet).

## TL;DR

- **Anthropic and OpenAI announced they're voiding pre-IPO share trades** — companies created special purpose vehicles (SPVs) that slice up shares and resell them, creating a nested chain of transactions, but the companies are now backing away because fraud has proliferated and everyone's grandmother is buying "rocks with Anthropic written on it."
- **Operating agreements are the legal firewall** — if a company's operating agreement doesn't require board approval for share sales, insiders can sell without permission; Pudgy Penguins CEO now requires explicit approval for any equity sales, preventing the predatory secondary market problem they faced early on.
- **PreTocks hit 1.4 trillion implied valuation on 800 billion company** — a Solana-based synthetic market traded pre-IPO stock at 3x the actual company valuation, showing how frothy and detached-from-reality secondary markets have become; the price corrected when the void was announced.
- **Two types of on-chain markets exist with different risks** — PreTocks wraps real SPVs with actual share backing (settlement risk if suit voids the trades); Venuels and other purely synthetic markets are bets unmoored from any underlying asset, similar to bucket shops from the 1900s where you place bets against the house rather than trading real securities.
- **Continuous pricing will eventually settle on pre-IPO companies** — perpetual markets on platforms like Hyperliquid will create canonical prices whether or not companies want them; employees will see their wealth fluctuate daily instead of every fund-raise, creating chaos during controversies (e.g., if Anthropic's price crashes after a political dispute).
- **Going public may actually be worse than staying private** — unlimited liquidity, retail investors, and daily price volatility create more pressure than staying private with hand-picked institutional shareholders who receive periodic (not continuous) pricing updates; the economic incentive to IPO has inverted.
- **April 2026 was the worst hacking month in crypto history** — 625 million stolen across 30+ incidents (an incident per day), including DeFi hacks, smart contract exploits, exchange breaches, and unverified token drains; LLM-powered exploits are now being used to bypass 2FA and help construct malware.
- **Open-source supply chain is the next major vulnerability** — open-source maintainers lack formal security practices; a recent Tanstack exploit showed how an implant can worm through GitHub actions, grab all developer API keys, and exfiltrate across their networks and personal devices.

---

**Pre-IPO Secondary Markets and the SPV Explosion**

Kane Wark explains the mechanics: investors buying pre-IPO shares (like Anthropic or OpenAI) wrap them in special purpose vehicles, slice them into smaller pieces, and sell those shares, with each buyer wrapping their portion in another SPV and selling further down the chain. This creates an opaque market where it's easy to sell "rocks with Anthropic written on it"—i.e., securities backed by nothing or backed by previous SPV layers that have no legal standing.

The frothiness has reached a breaking point. Wark notes that the demand for these shares is real (people want Anthropic exposure), but it's far easier and more profitable to satisfy demand by selling fraudulent securities than by actually creating valid ones. WhatsApp group chats, unverified intermediaries, and outright scams proliferated, forcing Anthropic and OpenAI to announce they're voiding the trades.

**Operating Agreements as the Legal Mechanism**

Taylor Monahan (Pudgy Penguins CEO) shares an incident from his company's early days: a co-founder sold equity to a known predatory investor without Monahan's knowledge. The flaw was in the operating agreement, which didn't require approval. Now, Monahan requires his explicit sign-off for any equity sale. He frames the question back at Anthropic: did their operating agreement allow these sales, or is Anthropic trying to backtrack on trades that were technically permitted?

Monahan argues that even if the secondary market is permitted or encouraged, Anthropic still faces liability if they try to void trades retroactively. However, he acknowledges that a legitimate secondary marketplace would benefit everyone: companies get to satisfy demand for liquidity (some investors or employees need cash) without losing control over who owns their cap table. The current chaos is because there's no way to do proper KYC (know-your-customer) verification in the gray market.

**On-Chain Synthetic Markets: PreTocks and Venuels**

The distinction between two types of on-chain markets is crucial. PreTocks, built on Solana, wraps real SPVs with actual shares somewhere—the bet will eventually settle when Anthropic IPOs (or doesn't). However, PreTocks traded at a 1.4 trillion implied valuation when Anthropic's last raise was at 800 billion, creating a 3x multiple that was completely detached from reality.

Venuels and other purely synthetic markets are different: they're unmoored from any underlying asset. Wark explains this as equivalent to the bucket shop model from the 1900s—you're not trading real Mississippi Railroad shares, you're placing synthetic bets against the house (or other traders) about whether the price will go up or down. The oracle price anchors these markets loosely, but the market itself is pure speculation. When the void was announced, PreTocks crashed back to Anthropic's actual valuation.

**Perpetual Markets and Continuous Pricing Risk**

The episode explores a crucial long-term risk: once platforms like Hyperliquid create perpetual (leveraged, continuous) markets for pre-IPO stocks, those markets will likely become the canonical price whether companies like it or not. Funding mechanisms in perpetuals mean the market can stay open indefinitely without settlement.

This creates a cascade of problems for Anthropic and other pre-IPO companies. Currently, employees see price updates only when a new fund-raise happens (once every year or two), which keeps morale stable. If a continuous market exists, employees will see their wealth fluctuate daily. Worse, during a controversy—e.g., if Anthropic gets into a public fight with Trump and the perpetual market prices the company at 50% of its last raise—employees will panic. The company has zero control over the perpetual market and cannot stop the price discovery process.

**The Incentive to Stay Private**

The conversation highlights an inversion in market incentives. Historically, companies IPO'd because public markets were the only place with enough liquidity to raise capital. Now, private equity, venture funds, and secondary market investors have so much capital that large private companies (Anthropic at 800 billion valuation) can raise unlimited sums while staying private.

Once you IPO, you inherit continuous public pricing, mandatory reporting, retail investors, and all the attendant volatility. Staying private with a fixed shareholder base and periodic (not continuous) pricing updates keeps employees happier and gives the company far more autonomy. Monahan notes the paradox: "It is genuinely better to be illiquid" than to IPO, which is why so many mega-cap companies stay private now. This is returning the market structure to the pre-stock-market era of the 1800s, when large wealth was entirely private.

**April 2026 Hacking Spree: 625 Million and Counting**

Taylor Monahan reports that April was the worst month for crypto hacking on record: 625 million stolen, at least 30 incidents (though the real number is likely higher). The incidents ranged across every category—centralized exchange hacks, DeFi exploits, smart contract drains on random Arbitrum tokens, and supply chain attacks. Notably, Drift Protocol's $285 million hack happened so long ago that it's already faded from collective memory despite being one of the biggest heists ever.

**LLM-Powered Malware and 2FA Bypass**

Google announced (via Cloud Blog) that they discovered an LLM-built Python exploit that bypassed 2FA on an open-source admin tool, disrupting a planned mass exploitation campaign before launch. Monahan hypothesizes the attack worked by using local Gemini APIs (increasingly built into Android, Chrome, and OS-level systems) to help construct the exploit on the fly, discovering attack surfaces, locating private keys, or exfiltrating data in real time. This represents a new threat vector: as AI agents become more prevalent in systems, compromising an agent could insert malware that humans would never detect until it activates.

**Supply Chain Attacks and Open-Source Maintainers**

The real danger Monahan highlights is the slow-motion worm through open-source software. The recent Tanstack exploit showed how an implant gains access (via GitHub Actions, in this case), then spreads: grabbing all developer environment files and API keys, worming through all of their repos, and exfiltrating secrets to a command-and-control server. The attack then spreads to individual developer machines, harvesting more secrets and spreading further.

Monahan emphasizes that open-source maintainers operate like crypto people—largely on personal devices without formal security practices. Most crypto and open-source security incidents follow the same pattern: "someone gets woken up because his friend called him in the middle of the night and said 'your shit's gone.'" The decentralized nature of open-source (unlike an organization with Crowdstrike or formal processes) makes it uniquely vulnerable.

**Continuous Monitoring with Agents**

On the defense side, Monahan reports a successful experiment at Pudgy Penguins using an AI agent for anomaly detection. They had slow-drainer attacks (thousands of dollars per day over 12 hours) getting lost in normal activity. An agent analyzed their transaction data and discovered a simple metric: price discrepancies in input/output volumes were the early warning signal. When asked to backtest this signal against the four most recent incidents, the agent confirmed it would have caught all four—but with a 90-second detection lag. For one incident that went unnoticed for 12 hours, 90 seconds would have been a huge improvement, but it's still too slow for flash-loan attacks (which happen in a single transaction). The defense will require rearchitecting systems to prevent single-transaction bundle attacks.

**Circle's ARC Token and Pre-IPO Company Tokenization**

Circle announced a $220 million raise of ARC tokens, an interesting signal of tokenomics leaking into public company behavior. Circle is a publicly traded company that created a stable coin (USDC), then launched an L1 blockchain, and now is issuing a token that will presumably govern the chain. Monahan notes that the Circle equity buyer and the ARC token buyer are two different cohorts, and if Circle can pull the lever to issue new tokens and boost its balance sheet, why wouldn't they? He frames it as bullish for Circle's stock but doesn't necessarily believe the ARC token will be valuable.

The broader concern: Circle is now competing with Ethereum and Solana (established chains with their own tokenomics), and repeating the "corpo chains" lesson from the pre-Bitcoin era where consortium databases posed as blockchains. Monahan remains bullish on Ethereum and Solana for their clear scaling plans, but Circle's strategy looks like building a stablecoin transport layer dressed up as a chain.

**Arbitrum Hack and Court Proceedings**

A U.S. court ruled that Arbitrum DAO can vote to release the $120 million recovered from the Hacks (North Korean attackers allegedly stole ~$626 million; Arbitrum recovered roughly $120 million). The court's decision removes Arbitrum DAO as a party—they no longer have to pause governance while fighting the suit. Now Arbitrum's lawyers and the Hack Recovery (A) and their lawyers will continue the fight in court over whether North Korea has any legal claim to stolen funds.

A key argument emerged in oral hearings: Hack's lawyers claimed that every individual owner must come to court in person to prove their claim, but on-chain recovery distributions can be perfectly fair without that—the same ownership that caused the hack in the first place can be used to distribute recovery fairly, and it's "cryptographically verifiable" rather than requiring passports and sworn testimony. Monahan expects this argument will eventually convince judges that on-chain recovery is more fair than forcing individual claimants to litigate.
