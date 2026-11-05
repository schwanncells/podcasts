---
podcast: Unchained
date: 2026-11-05
source_transcript: data/podcasts/transcripts/Unchained/2026-11-05_Uneasy Money_What_the_$6B_Binance_Hack_Revealed_About_Who_Can_Freeze_Stolen_Funds.md
---

# Unchained — "Uneasy Money: What the $6B Binance Hack Revealed About Who Can Freeze Stolen Funds"

**Host:** Laura Shin. **Guests:** Adam Sadowski (CEO, Llama Risk; risk provider for Aave protocol); Taylor Monaghan (security expert and Unchained co-host).

## TL;DR

- **$6B stolen from Binance, attributed to North Korea** — hackers moved $3B onto Ethereum, primarily in stablecoins (Tether and USDC), with immediate liquidation into ETH. The attack exploited EIP-7702 sweeping mechanisms and targeted the brief window between theft and stablecoin freeze orders.
- **Tether froze $1B within minutes** — Circle froze USDC in roughly 3 minutes, citing law enforcement involvement. Both companies' rapid response prevented most stolen funds from being converted to unrecoverable assets.
- **Aave markets temporarily frozen to prevent stolen funds from sitting on the books** — $60M USDT collateral was supplied to borrow $45M worth of ETH. Aave implemented a "market freeze" (one-way valve where users could withdraw/repay but not borrow) rather than locking user funds, preserving protocol solvency while removing exposure to stolen assets.
- **Synthetics recovered ~$9M in stolen SNX through token authority controls** — rather than changing token state, the team used the token authority to create an approval and transfer stolen tokens to the DAO, demonstrating a novel approach to fund recovery.
- **DeFi teams asked "what can we do?" instead of accepting the constraint** — the common wisdom was "there's nothing we can do," but the Binance incident shifted cultural expectations; teams are now willing to take action against sanctioned threat actors.
- **Aave implements risk oracles and ratcheting mechanisms to limit large sudden borrowing** — rather than a hard cap that would invite Sybil attacks or halt the market, time-based ratcheting will limit borrowing over specific periods to prevent future exploits.
- **Price feeds remain a critical, underestimated dependency** — Oracle systems determine collateral value and protocol solvency; tokenized stocks add complexity due to multiple trading sessions and exchanges with varying liquidity.
- **Automating crisis response creates a trilemma:** speed (instant response vs. manual multi-sig delays), verifiability (transparent on-chain logic vs. off-chain opacity), and rich risk signals (off-chain data quality vs. on-chain-only constraints).

---

**The Binance Hack and Immediate Stablecoin Response**

On November 5th, North Korean-attributed attackers stole approximately $6B from Binance and moved $3B to Ethereum, with the bulk denominated in stablecoins (Tether and USDC). The attackers used sophisticated mechanics including EIP-7702 transaction sweeping to continuously extract funds while Binance's security systems were still operating. The critical vulnerability was timing: there was a brief window between the theft and when stablecoin issuers could freeze the addresses.

Tether and Circle responded with remarkable speed. Tether froze $1B in USDT within the first minutes; Circle followed with a USDC freeze roughly three minutes later. Circle attributed the rapid action to law enforcement contact, though hosts skeptically questioned whether such coordination was truly possible in that timeframe. Regardless of the mechanism, the stablecoin freezes prevented the attackers from converting the stolen funds into ETH or other untrackable assets, preserving the possibility of fund recovery.

**Aave's Market Freeze and Risk Management Response**

Sadowski's team at Llama Risk coordinated with Aave's Guardian multi-sig to freeze Aave's markets overnight. The key action was a "market freeze"—described as a one-way valve—that prevented new borrowing and deposits but allowed existing users to repay debt and withdraw collateral. This preserved protocol solvency and kept users from being locked into the system while preventing stolen funds from accumulating on Aave's balance sheet.

The stolen funds had reached Aave after about 35 minutes of the exploit, when the attackers ran low on immediately accessible DEX liquidity. They supplied $60M USDT as collateral and borrowed approximately $45M in WETH. The position immediately became vulnerable to liquidation due to the maximum loan-to-value ratio chosen; subsequent market movement has triggered the liquidation cascade.

**Why Aave Cannot Arbitrarily Limit Large Borrowing**

The conversation touched on a core design tension: why did Aave allow someone to borrow a billion dollars of ETH against stablecoin collateral? Sadowski explained that Aave's markets are configured based on asset liquidity and intended use cases. USDT and WETH are core assets used for legitimate purposes like shorting ETH. However, he acknowledged that there is a genuine trade-off between market access and exposure limits.

The challenge is implementation. If Aave imposed a hard cap—for example, "maximum 1M USDC per minute"—attackers could sybil it by spawning multiple addresses or transactions, or the ratcheting mechanism itself could halt the entire market and frustrate legitimate users during high-demand periods. Instead, Aave is implementing a more sophisticated solution: time-based ratcheting that limits borrowing over configured periods while preserving market function and avoiding adversarial loopholes.

**Synthetics' Creative Token Recovery**

Synthetix responded to the theft of approximately $9M in SNX by recovering the tokens through the token authority contract, a power the team had historically avoided using. Rather than changing token state, they used the token authority to create an approval and transfer the stolen tokens directly to the DAO. This represented a shift in cultural thinking: the attack forced the team to reconsider what intervention was acceptable when the alternative was allowing a sanctioned threat actor (North Korea) to retain stolen user funds.

Taylor noted that the decision threshold is not arbitrary. While the team has ultimate power to modify any protocol parameter, exercising it carries reputational and political risk. However, the cumulative circumstance of a record-breaking hack, attribution to North Korea, and the involvement of Binance—a major exchange with institutional relationships—created sufficient moral and pragmatic urgency to act.

**The Shift in Crisis Response Culture**

A recurring theme was that teams historically assumed "there's nothing we can do" in the face of large hacks. The Binance incident shifted expectations. Taylor emphasized that the question is not whether to act, but what constraints apply. The question should be "what can we do?" rather than "can we do anything?" Several teams rose to answer that question, including Arbitrum, which Monaghan noted has now established itself on a hook to defend against large-scale theft—a position he described as privileged and morally defensible.

**Price Feeds as Critical Infrastructure**

Sadowski raised an often-overlooked vulnerability: price feeds. Oracle systems like Chainlink determine collateral valuations and protocol solvency. For crypto assets, this is relatively straightforward through exchange aggregation and volume-weighted pricing. However, the arrival of tokenized stocks (now deployed on Aave Base instance) creates new complexity: multiple trading sessions (overnight, morning, regular market hours), varying liquidity across exchanges, and the need to construct coherent pricing across discontinuous sessions.

Sadowski noted that determining even crude oil pricing took six months of iteration due to the complexity of stitching together Brent and other benchmarks. Tokenized stocks are an order of magnitude more complex. This creates a gap in the current stack: robust off-chain data infrastructure (like Chainlink) provides high-quality data feeds, but the judgment layer—deciding what methodology, aggregation, and parameters should define an asset's price—is often baked into the Oracle or left to the protocol to interpret.

**Risk Oracles and Automated Crisis Response**

To address these gaps, Llama Risk is building risk oracles using Chainlink's Runtime Environment (CRE). This allows risk managers to implement custom logic for pricing, monitoring, and crisis detection without relying on either the infrastructure provider's built-in methodology or manual multi-sig governance. The benefit is that crisis response can be partially automated while remaining transparent and under protocol control.

However, this creates a trilemma. Manual multi-sigs (like Aave's Guardians) provide transparency and control but are slow—they require convening signers across time zones, which took hours even in the Binance incident. Fully on-chain controllers offer speed and verifiability but cannot access off-chain data or nuanced risk signals. Off-chain systems with custom logic can be fast and data-rich but sacrifice immediate verifiability. The goal is to balance all three: speed, transparent logic, and rich risk signals, though that balance remains elusive.

**Systemic Risks from Large Stolen Fund Movements**

Beyond the direct theft, large stolen-fund movements create secondary risks. When billions of dollars suddenly enter a protocol, liquidations and forced exits can cascade through markets. Aave's market freeze prevented this from happening while Binance and law enforcement addressed the primary breach. However, this highlighted the broader vulnerability: DeFi protocols are exposed to the consequences of exchange hacks even when no funds are directly stolen from the protocols themselves. The Binance incident revealed both the effectiveness and limitations of current safeguards.

