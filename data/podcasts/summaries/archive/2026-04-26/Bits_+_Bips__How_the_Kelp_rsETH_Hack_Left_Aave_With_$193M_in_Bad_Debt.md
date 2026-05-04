---
podcast: Bits + Bips
date: 2026-04-26
source_transcript: data/podcasts/transcripts/Bits_+_Bips/2026-04-26_How_the_Kelp_rsETH_Hack_Left_Aave_With_$193M_in_Bad_Debt.md
---

# Bits + Bips — "How the Kelp rsETH Hack Left Aave With $193M in Bad Debt"

**Host:** Steve Erlic (head of research, Sharplink). **Guests:** Luke Laser (head of research, Blockworks), Shandra Deans (research analyst, Blockworks), Carlos Gonzalez Compo (researcher, Blockworks).

## TL;DR

- **116,000 rsETH minted on Arbitrum, borrowed $193M on Aave mainet** — Attacker exploited Layer Zero's DVN network using a 1-of-1 signature to mint unbacked rsETH, deposited it as collateral, and borrowed ~$193M at 93% LTV, leaving Aave short roughly the entire amount.
- **Aave froze rsETH market in 85 minutes** — The protocol's response was fast, but crystallization happened within minutes of the loan origination; freezing prevented new exposure but couldn't undo the $193M loss already taken.
- **98% of borrowed ETH collateral is leverage-looping via Liquid Staking Tokens** — Traders use active-yield staked ETH (like Etherfy vaults) to borrow passive wrapped ETH, convert it back to the active asset, and loop. This generates 95%+ of demand for borrowed ETH, disguising concentrated risk as diversified activity.
- **Looping trades flip from +1% carry to -7% after freeze** — Interest rates on ETH borrows spiked from ~0% to 10% due to 100% utilization, wiping out looper equity and threatening cascading liquidations across $8B+ in total affected deposits.
- **Unified-pool design forces all ETH lenders to accept looping risk** — Aave's single pool means lenders cannot opt out of who borrows their collateral; Morpho's modular design lets lenders whitelist borrower collateral types. Spark's supply and borrow caps further limited exposure.
- **$250M umbrella safety module inadequate for tail risk** — Historical Aave bad debt was <$5M; the 250M reserve seemed safe until $193M loss scenario arrived. Only ~$50M sits in the ETH umbrella; even with payouts, it covers only ~0.6% of impairment, leaving lenders exposed.
- **Socialization vs. isolation creates 17% haircut trade-off** — If Kelp spreads rsETH losses across all holders globally, mainet lenders face ~17% markdown but equity cushions absorb most losses; isolating to L2 hits that market much harder, potentially zeroing looper equity and forcing lender impairment.
- **Decentralization questioned: crisis governance centralizes to trusted intermediaries** — Both Aave's 5-of-9 Security Council freeze and Arbitrum's decision to freeze Lazarus funds raise questions about what "decentralized" means when core crisis response demands speed and accountability.

---

**The Attack Mechanics and Layer Zero's Vulnerability**

Shandra Deans explains the exploit sequence. The attacker signed a malicious cross-chain transaction exploiting Layer Zero's DVN (Decentralized Validator Network) infrastructure. The transaction falsely claimed 116,000 rsETH was burned on Arbitrum (Layer 2), which triggered the bridge to mint an equivalent amount of rsETH on Ethereum mainnet—entirely unbacked. The attacker immediately split the minted rsETH across multiple wallets, deposited them into Aave v3 as collateral, and borrowed 93% LTV against that position in a matter of minutes. Aave's bad debt crystallized at roughly $193 million.

Kelp faced a choice in its signature scheme: it could use a 1-of-1 signature (the default Layer Zero template) or a more sophisticated multi-signature setup. Kelp chose the simpler 1-of-1. Luke Laser notes that about 40% of unique OFT (Omnichain Fungible Token) deployments on Layer Zero still rely on the 1-of-1 configuration, and Layer Zero should push harder toward multi-sig adoption for new deployers. Aave, for its part, could have flagged the 1-of-1 signer as a collateral risk when listing rsETH and adjusted LTV parameters accordingly.

**Aave's Unified Pool and the Looping Problem**

The core architectural question: why did Aave list rsETH when it had known high risk? Shandra points out that Aave uses a unified pool model—all assets sit in one reserve, and anyone with sufficient health factor can borrow any asset. This is powerful for liquidity but conceals concentrated risk. A potential ETH borrower has only one real use case: going short the asset. But Aave sees almost no organic short demand; instead, 98% of ETH borrowing is leverage looping.

Looping works as follows: a trader deposits an active-yield LST (like staked ETH generating yield), borrows passive wrapped ETH from Aave, converts it back to the active asset, and deposits it to borrow more wrapped ETH—repeating the cycle. So long as the yield spread exceeds the borrow rate, it is profitable. Vault products like Etherfy abstract this looping into a simple high-yield ETH product for retail users. The top ten borrowed-ETH wallets are almost all such vaults.

This design means Aave's ETH lenders believe they are lending into a diverse set of use cases but are actually funding a single, leveraged trade. Shandra contrasts this with Morpho, which lets each lender choose what collateral types can borrow against their assets. Aave's unified pool forces opt-in to this looping risk. Spark, meanwhile, uses supply and borrow caps to rate-limit exposure—a safeguard Aave lacked.

**Crisis Response and Market Dynamics**

Luke Laser confirms that Aave froze the rsETH market 85 minutes after the exploit. The coordination required a 5-of-9 multi-signature, and the attacker's exploit path (minting through the Layer Zero bridge rather than manipulating an on-chain oracle) made it harder to catch at the mint event. By the time the market froze, the $193M loss was already crystallized in the ledger.

What happened next: ETH lenders panicked and rushed for exits. Wrapped ETH utilization hit 100%; liquidity evaporated. Borrowers could not withdraw collateral. As an alternative exit, traders borrowed stablecoins against their wrapped ETH, pushing stable markets to 100% utilization as well. Aave lowered the ETH borrow rate ceiling from ~10% to ~3% in an attempt to clear the market, but uncertainty about bad-debt resolution killed incentive for new supply. The market stayed stuck at 100% utilization with no available liquidity.

**The Looping Unwind and Leverage Implosion**

Before the freeze, leverage looping was positive-carry—yield spread of 50–100 basis points over borrow costs, levered 5–10x. After the freeze, when borrow rates spiked to 10%, the trade flipped to -7% napkin math on levered positions. Looper equity evaporated. Health factors tanked. The risk of cascading liquidations loomed, threatening to flood the ETH market with more selling pressure, even from positions unrelated to rsETH.

**Resolution Scenarios and the Umbrella Module Shortfall**

Kelp faces a critical decision on loss allocation. Llama Risk laid out two scenarios:

1. **Socialize globally** — Spread rsETH losses across all holders on all chains. This results in roughly a 17% markdown to rsETH. Mainet Aave lenders would absorb ~1.5% impairment, but looper equity cushions can absorb most of it. The Aave umbrella safety module (a junior-capital reserve that receives a 2–4% risk premium to take first losses) was sitting at $250 million, and the ETH umbrella has ~$50M. Even burning the entire umbrella would reduce the lender impairment from 1.5% to 0.6%—insufficient but less catastrophic.

2. **Isolate to L2** — Keep losses on Arbitrum, where rsETH is native. L2 lenders face much steeper haircuts; the equity cushion is exhausted faster, and lenders themselves absorb impairment. The aETH deposit token (which functions as a demand deposit earning yield) would face material markdown with no clear recovery timeline, leaving liquidity-locked lenders in illiquid markets.

Luke stresses that the umbrella module was historically adequate—Aave had realized less than $5M in bad debt across its history, making $250M seem like a comfortable cushion. The $193M loss was a left-tail event that exposed how undercapitalized tail risk insurance actually was.

**Systemic Risk and Future Exploits**

Carlos notes that two major attacks in quick succession—the Drift hack and the Kelp/Aave exploit—total over $500M in losses. North Korean threat actors (Lazarus) appear responsible, with armies of people testing every smart contract for vulnerability. The industry's response is critical.

Luke addresses whether this heralds more attacks. The attack surface has expanded as DeFi becomes more composable; however, the same attack vectors persist (bridges, RPC infrastructure, risky collateral wrappers). What matters is whether protocols learn from past mistakes. He highlights that Aave itself was not exploited—this was contagion from collateral impairment, not a smart contract flaw. That distinction matters for risk management assessment.

Spark avoided heavy losses partly by delisting rsETH in January and partly by deploying supply caps and borrow caps. These limits can prevent exposure from reaching Aave-scale magnitudes. The most competent teams continue to be security-first and avoid these issues.

**Decentralization, Crisis Governance, and Accountability**

A larger question emerges: what does decentralization mean when crisis response requires a handful of trusted intermediaries to act fast and make unilateral decisions?

Aave's 5-of-9 Security Council froze rsETH reserves. Arbitrum's Security Council froze ~$30–70M in stolen funds. Circle faced criticism for declining to freeze USDC taken by Lazarus in the Drift incident. Each decision was made by a select group, not by full governance votes.

Luke argues that certain functions—particularly risk management and crisis response—must be "gatekept to a select few highly competent and responsible parties that are easily identifiable and liable." This leans more toward centralization with trusted intermediaries rather than broad decentralized governance. The industry is inching toward a "CDI approach with trusted intermediaries" that have clear accountability.

The tension is real: regulators like the SEC (under Paul Atkins) want to exempt true DeFi from broker registration, but instances like this—where unilateral decisions freeze assets and socialize losses—complicate the argument that these are truly decentralized platforms.

**Recommendations for Users**

When interest rates on DeFi platforms don't outcompete Treasury yields yet carry tail-risk exposure, the risk-reward calculation breaks. Several paths forward emerge:

- **Vertically integrated platforms** — Maple Finance exemplifies a model where a single entity distributes the product, underwrites the risk, and provides legal enforcement. There is clear accountability and recourse.
- **Battle-tested protocols** — Sky (formerly Maker) has been live longer than any major DeFi protocol and has never experienced a bad-debt event. Concentration of flows toward historically proven platforms is likely.
- **Modular architecture with caps** — Spark's supply and borrow caps, combined with conservative collateral selection, prevent tail-risk scenarios from metastasizing.

For users prioritizing permissionless access, the safest path is the longest-tested protocols with the strongest risk discipline. For those comfortable with intermediaries, vertically integrated platforms offer clearer accountability.

