---
podcast: Unchained
date: 2026-10-23
source_transcript: data/podcasts/transcripts/Unchained/2026-10-23_PaperTrade_Attracted_$140M,_Then_Changed_the_Rules._Was_It_a_Bait_and_Switch.md
---

# Unchained — "PaperTrade Attracted $140M, Then Changed the Rules. Was It a Bait and Switch?"

**Host:** Laura Shin. **Guest:** Jason Pagalatis (head of markets, Delphi Research).

## TL;DR

- **$140 million USDC pre-deposited on launch** — PaperTrade went live on October 10th as an on-chain, fully-leveraged exchange allowing up to 1,000x leverage trades on Bitcoin and Ethereum, and quickly attracted a week of heavy activity and trader losses.
- **Houses the trades, not an order book** — Unlike traditional perpetual futures, PaperTrade trades are taken against a Martingale (house) pool rather than matched against other traders, eliminating slippage and fees but creating a casino-like "house vs. player" dynamic.
- **Losing money mints reward tokens** — Traders who lose positions mint "Paper" tokens as rebates; at launch, each dollar lost minted ~100 Paper. The Martingale pool grows from trader losses and pays winners, creating a DAO-like model where losers own a piece of the house.
- **Price manipulation attack on day one** — A trader placed $5–20 million orders on HyperLiquid to push Bitcoin/Ethereum prices, which PaperTrade uses as its oracle, and exploited the high leverage to profit; the team manually locked positions and prevented the closure, forcing the attacker to stop.
- **Team announced token will not be made transferable** — After initially promising transferability in the roadmap, the team reversed course, citing an existential risk: if Paper becomes tradeable and a perp market launches, attackers could take massive short positions and then manipulate prices, potentially bankrupting the house pool.
- **The security risk was documented but the secondary implication wasn't communicated** — The team warned in docs of oracle risk but appeared not to communicate that adding a perp market creates a compound attack vector requiring either capping leverage or sacrificing the protocol's core value proposition.
- **Activity collapsed after the announcement** — Staking revenue fell from $2.1 million on Sunday to $84,500 in two hours after the announcement, as the farming incentive evaporated and user calculus changed.
- **Tokenomics changed retroactively** — The mint curve shifted from fixed Paper per dollar lost to a fixed share of total supply, making rewards unpredictable and adding to user frustration about post-launch changes.

---

**What PaperTrade Is and How It Works**

PaperTrade is an on-chain, fully-leveraged trading venue launched on the Hyper EVM network (the on-chain portion of HyperLiquid) that allows traders to take massive leveraged positions on Bitcoin and Ethereum with minimal friction. Unlike traditional order-book exchanges, trades are taken against a Martingale (house) pool rather than matched between opposing traders. This eliminates slippage and funding rates, allowing PaperTrade to offer 1,000x leverage with no transaction fees.

When a trader loses money, they mint Paper tokens proportional to their losses. These Paper tokens can be staked to generate yield from trading activity on the platform. The Martingale pool grows from trader losses and is distributed to winning traders. Pagalatis describes the model as similar to Rollbit, the gambling/casino ecosystem—it is, fundamentally, a house-vs.-player betting mechanism dressed in on-chain infrastructure. When traders win, they receive only 88–90% of their gains (a fee asymmetry). When they lose, the losses go into the pool that pays winners.

**The Initial Launch and Early Momentum**

PaperTrade launched on October 10th with $140 million in USDC pre-deposited by crypto traders eager to participate. The timing was symbolic—October 10th, 2023 was the date of a major liquidation cascade that wiped out many traders; relaunching on the same date with a protocol that reimburses losers in token form carried a narrative appeal.

For the first week, the platform functioned as intended. Heavy trading generated approximately $57 million in cumulative payouts to Paper holders through staking. Volume was robust; PaperTrade even briefly flipped NASDAQ's daily notional traded volume. The early cohort of traders believed they understood the deal: deposit money, trade with 1,000x leverage, and if they lost, receive Paper tokens that would eventually become transferable, valuable assets they could trade or sell.

**The Day-One Price Manipulation Attack**

On the same day PaperTrade launched, a trader exploited a subtle vulnerability. PaperTrade derives prices from HyperLiquid's order book rather than maintaining its own. A trader placed successive large market orders ($5–20 million) on HyperLiquid to push Bitcoin and Ethereum prices. Because traders on PaperTrade use extreme leverage, even small price moves wipe out positions. The attacker opened large short positions on PaperTrade, pushed the price down on HyperLiquid (causing a cascade of liquidations in that direction), and profited.

The PaperTrade team had documented this oracle-risk in their documentation but most users did not read it. Once the team identified the attack, they manually locked the attacker's positions, preventing them from being closed on PaperTrade. This forced the attacker to abandon the strategy on HyperLiquid. Pagalatis notes that this is not technically an "exploit" but rather a use of stated market mechanics; however, the team deemed it unacceptable and intervened with manual controls. The incident revealed that PaperTrade, despite being described as "fully on-chain," still had multisig control and central authority.

**The Bait and Switch: Reversing the Transferability Roadmap**

On Monday, roughly a week after launch, PaperTrade announced it would not make the Paper token transferable—contradicting an explicit roadmap item. The team's justification was mathematical: if Paper becomes transferable and a perpetual futures market launches for it, an attacker could execute a two-step exploit. First, the attacker takes a massive short position in Paper futures elsewhere (e.g., on a third-party perp exchange). Second, the attacker spends capital to manipulate PaperTrade's oracle, liquidating longs and enriching the Martingale pool (which is now worth more). Third, the attacker exits their short and profits from the pool manipulation.

The team quantified the risk: "If our bankroll is 10 million, an attack costing 15 million, manipulating the price of Bitcoin or Ether is not viable. You simply lose money. If however, you are able to put on 10 million of paper short side exposure, suddenly an attack costing $50 million is very viable indeed."

**The Dilemma: No Clear Technical Solution**

Pagalatis acknowledges the team's analysis is correct—the attack would almost certainly happen if Paper became transferable. However, he questions whether the team knew this when they promised transferability. The team could mitigate the risk by capping leverage, capping the pool size, or reducing leverage to 3x or 5x, but doing so strips away the only reason anyone uses PaperTrade in the first place: extreme leverage and high payoffs. The protocol is trapped: making the token transferable creates an existential risk; restricting it breaks the value proposition. Pagalatis calls it "a bad look" because users were promised one rule set and got a different one after depositing $140 million.

**The Collapse in Activity and Retroactive Tokenomics Changes**

After the announcement, activity on PaperTrade collapsed. Staking revenue fell from $2.1 million on Sunday to $84,500 within two hours. Users realized they had no reason to farm Paper if it would never be tradeable and their losses would only yield modest USDC yield from the Martingale pool, with no path to profitability. The opportunity cost of deploying capital on PaperTrade became obviously negative.

To compound the issue, the team also changed the tokenomics curve retroactively. Instead of a fixed amount of Paper minted per dollar lost, losses now mint a fixed share of the total circulating supply. This means participants no longer know how many tokens they will receive until the moment of loss, destroying a key assumption underlying their decision to participate.

**The Broader Philosophy: Tokens as Products vs. Tokens as Incentives**

Pagalatis reflects on a recurring problem in crypto: the confusion between a token *as the product* and a token *as an incentive*. Many projects mistake the token for the actual value driver, when in reality tokens should be secondary to a real, profitable business. He contrasts PaperTrade with HyperLiquid, which succeeded as a product first (before the token launched) and whose token now has real value because the underlying exchange works. He notes that successful incentive structures (like equity RSOs in traditional companies) are only valuable when tied to a durable business that produces cash flow and has product-market fit. Paper's problem is that it was structured as if the token *were* the product, with the house's profitability as a secondary concern.

Pagalatis points to MetaDAO as an example of more ethical token deployment: when a portfolio company failed, it returned capital to investors. He argues that most business ventures fail, but that failure should be managed honestly—not with endless treasury milking and founder salaries while users are held hostage by non-transferable tokens.
