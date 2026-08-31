---
podcast: Unchained
date: 2026-06-18
source_transcript: data/podcasts/transcripts/Unchained/2026-06-18_Why_AI_Censorship_and_Reg_NMS_Repeal_Matter_for_Crypto_Markets_DEX_in_the_City.md
---

# Unchained — "Why AI Censorship and Reg NMS Repeal Matter for Crypto Markets: DEX in the City"

**Host:** Katherine KK (StarkWare). **Guests:** Jessi Brooks (web3 prosecutor turned web3 protector, Ribbit Capital; expert on AI regulation and crypto policy), V (former SEC enforcement division lawyer, author of "Fairness by Design: Verifiable Execution in On-Chain Markets").

## TL;DR

- **Federal government forced Anthropic to take Fable 5 and Mythos 5 offline globally** — ostensibly over cybersecurity bypasses, but without transparent process, notice-and-comment, or technical justification, raising concerns about government control over frontier AI models via "secret processes."
- **The real issue is KYC/AML for AI without due process** — government ordered foreign nationals (including Anthropic employees) blocked from accessing Fable 5, forcing a global shutdown because no AI system has Know Your Customer compliance. This mirrors Gensler-era SEC tactics: unclear rules, shifting standards, no due process.
- **Amazon allegedly pressured White House to shut down Fable 5** — claiming guardrails could be bypassed, but Anthropic and cybersecurity experts dispute the bypass exists and note that similar bypasses exist in open-source models outside the U.S., disadvantaging domestic AI innovation.
- **Jay Clayton to lead national intelligence, bringing crypto prosecution legacy** — Clayton (former SEC chair 2017–2020, interim SDNY U.S. Attorney) will focus on AI regulation and policy, notably while SDNY continues pursuing the Tornado Cash case.
- **CFTC proposed major amendments to Reg. 401-611 on prediction markets** — 300-page notice of proposed rulemaking clears political election contracts and redefines "gaming" to allow sports final-score betting, but requires platforms to self-certify and enforces based on a vague "public interest" standard with no full commission oversight.
- **SEC proposes repealing Reg NMS rules 611 and 610E** — after 20 years, these rules that enforce the NBBO (best publicly displayed price) would be eliminated, removing barriers to crypto-native securities markets like AMMs executing without routing to all exchanges.
- **Repealing Reg NMS could enable on-chain securities and better execution through market design** — instead of brokers deciding trade-offs behind closed doors, crypto offers transparent tools (solver auctions, private transaction channels, cryptographic attestations) to achieve best execution through design rather than regulation.
- **Citigroup rolling out tokenized depository receipts, not shares; Coinbase launching on-chain shares** — legal infrastructure hasn't caught up with tokenization speed, raising questions about issuer involvement, transfer agents, and whether the paused SEC innovation exemption will address these gaps.

---

**AI Censorship and Government Overreach**

Jessi Brooks frames the Anthropic situation as part of a larger pattern of government control over frontier technology. The White House forced Anthropic to disable Fable 5 and Mythos 5 globally after reports (allegedly from Amazon, an Anthropic investor and AI competitor) claimed guardrails could be bypassed. However, Anthropic and cybersecurity experts argue the bypass claim is unsubstantiated and note that similar vulnerabilities exist in open-source models already available to hackers outside the U.S. Brooks characterizes the government's process as opaque: no transparency, notice-and-comment period, or technical justification. She draws parallels to Operation Choke Point 2.0, arguing this represents a dangerous choke point on AI access itself—a precursor to how government might regulate crypto if given the chance.

The deeper issue, Brooks argues, is an implicit KYC (Know Your Customer) requirement imposed retroactively on AI. The government ordered foreign nationals blocked from accessing Fable 5, including Anthropic employees. Since no AI system has KYC compliance, Anthropic shut down the model globally. Brooks finds this especially concerning because it mirrors Gensler-era SEC tactics: unclear rules, shifting standards, no due process. KK adds that the lack of transparency is particularly troubling because the consumer is speaking a "third language" while the government and companies speak two different ones, leaving ordinary users in the dark about what's actually dangerous.

Brooks notes a troubling additional layer: the administration's narratives are contradictory and shifting. Pete Hegseth tweeted that this is what happens when companies don't cooperate with "war efforts." David Sacks blamed Anthropic directly. There's also an unconfirmed rumor that the White House couldn't reach Dario Amodei (Anthropic CEO) because he was at a wellness retreat, later debunked. The lack of clarity reinforces Brooks's concern that nobody—not even regulators—knows what actually happened, and the policy may never be explained.

**AI Governance and Trust**

V raises the stakes by framing AI as a civilization-level concern more serious than past debates over food, cars, or furniture. Unlike past consumer trust issues, even highly sophisticated people can't assess AI risks because the technology isn't transparent. V advocates for public-private collaboration similar to the Manhattan Project rather than leaving AI governance entirely to the private sector. KK counters that this is not anti-capitalist but rather an acknowledgment that business can never be fully trusted on existential-level technology.

Brooks and KK discuss the contradiction in Anthropic's messaging: the company warned that Mythos is "terrifying" and demanded regulation, yet released Fable as a "safer" version. This leaves users unsure whom to trust and what the actual risk is. The hosts note that international efforts matter because government policy is fractured—some parts say AI is too dangerous to release while others say states shouldn't regulate it because it would hurt U.S. competitiveness with China. Brooks concludes that no one knows what's going on and that the underlying reason for the shutdown may never be public.

**CFTC Prediction Markets Rule: Clarity, Loopholes, and Accountability**

KK worked through the CFTC's 300-page notice of proposed rulemaking on prediction markets, made possible by the agency's unusual circumstance of having only one chair (who has unusual power to act unilaterally under the Commodities Exchange Act, unlike the SEC's quorum requirement). The rule proposes amending Rule 401 to remove the flat prohibition on "gaming" contracts and instead allow the CFTC to make "public interest" determinations on a case-by-case basis, with a structured review framework.

Most significantly, the rule clears political election contracts—KK supports this, noting hundreds of years of U.S. history of betting on elections and the transparency benefits. For sporting and gaming contracts, the new definition of "gaming" is narrow enough to allow final-score betting while presumably banning injury betting. Contracts can trade while under review, and if the CFTC doesn't trigger review, they're automatically cleared.

V notes the rule provides important clarity and is "workable," but emphasizes that the public comment period is critical—stakeholders must weigh in. The hosts discuss tensions: the CFTC's ability to move fast with just one chair is impressive, but also raises governance concerns about whether one person can set rules affecting entire markets. KK's balancing point is that while defining vague terms like "gaming" is valuable, the rule puts much burden on industry self-certification and self-policing, with the CFTC having limited resources to audit after the fact. This could create problems that only emerge when consumers get hurt.

All three hosts note that "public interest" is meaningfully vague—different stakeholders (including the three of them) likely have different definitions. V stresses the importance of industry and public input so that the final rule reflects diverse perspectives and has credibility across constituencies.

**Reg NMS Repeal and Crypto-Native Securities Markets**

V presents the SEC's proposal to repeal Reg NMS rules 611 and 610E as potentially transformative for on-chain securities markets. These rules, in place for 20 years, enforce the NBBO (National Best Bid and Offer)—the best publicly displayed price to buy or sell a stock across all U.S. exchanges. Rule 611 forbids trading at worse prices when better ones exist elsewhere; Rule 610E prevents situations where compatible orders on different exchanges never match.

The problem, V explains, is that these rules assume traditional exchange architecture with order books, displayed bids, and brokers routing orders. Crypto AMMs (like Uniswap) don't check every other exchange before trading—they price against their own liquidity pool and execute automatically. Forcing AMMs to plug into traditional market data infrastructure would just rebuild the old system on a blockchain, defeating the purpose.

Repealing Reg NMS could unlock a different way to achieve best execution: instead of routing through traditional exchanges and brokers deciding trade-offs behind the scenes (and regulators investigating afterward), crypto markets offer tools like solver auctions (where multiple parties compete to give the best outcome), private transaction channels (reducing front-running), cryptographic attestations (showing investors and regulators how transactions are handled in real time), and programmable sequencing. These allow best execution through transparent design rather than regulation.

V emphasizes this is not a "YOLO deregulation" but rather an opportunity to build investor protections and market integrity into the system itself. She plans to submit comment and urges the industry to do the same during the 60-day comment period.

**Tokenized Securities and the Innovation Exemption Gap**

KK draws attention to recent announcements by Citigroup and Coinbase on tokenized securities. Citigroup is rolling out "tokenized depository receipts"—not actual shares but receipts representing claims on shares, a distinction reflected in Citigroup's official press release but misreported by the Wall Street Journal. Coinbase is launching on-chain shares with dividend payments.

KK's concern is that tokenization has moved faster than the legal infrastructure. The critical unknown is how transfer agents, issuers, and the regulatory framework will interact. She notes that the SEC's paused innovation exemption was supposed to address tokenized securities but remains in limbo, leaving uncertainty about what specific activities (tokenization itself, holding on-chain, dividend distribution, etc.) will be permitted. KK also flags that issuer buy-in is critical—referencing botched X Stocks and the SpaceX IPO problems where issuers were not aligned with what platforms promised customers.

V notes that the innovation exemption is precisely the tool meant to address these gaps, and the hosts agree to keep watching the tokenized securities space closely.

**Jurassic Finance and Dinosaur Tokenization**

In lighter closing news, KK highlights a new project called Jurassic Finance that is tokenizing dinosaur bones and fossils. The token is called RAWR. Investors would own fractional pieces of rare dinosaur bones sourced globally, which would be loaned to museums. KK emphasizes she cannot vouch for the legitimacy of the project and notes it looks potentially scammy, but she loves the blend of blockchain and dinosaurs. V quips that the project looks like "a black market for dinosaur bones." KK wraps by joking that at least it's not as risky as Nicholas Cage's real dinosaur bone purchases and toasts to summer, dinosaurs, and the Knicks.
